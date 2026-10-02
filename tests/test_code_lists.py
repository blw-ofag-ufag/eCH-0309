"""Compares the code lists against the TVD AnimalTracing openAPI.

src/rdf/data/code_lists.skos.ttl is maintained by hand: the Wertebereiche are
part of the Hilfsmittel, and describing a value or adding a translation has to
survive. This module is what keeps it honest, by reporting drift in both
directions:

- a concept whose :animalTracingTerm no longer resolves, because the interface
  renamed or dropped something;
- a value the interface carries that the file neither holds nor lists below as
  deliberately absent.

The second direction only applies to the schemes that derive from an enum, which
say so by naming it on the scheme itself. The other four take their values from
the Wertebereich tables of the Hilfsmittel and reference the interface only where
a counterpart happens to exist, so they are not meant to exhaust any enum.

That direction is the one a generator cannot give you. A new value in the
openAPI is a decision for the Fachgruppe, not something to import silently.
"""

import json
import urllib.error
import urllib.request
from pathlib import Path

import pytest
from rdflib import RDF, Graph, URIRef
from rdflib.namespace import SKOS

OPENAPI_URL = "https://test-03-tvd-api-at.identitas.ch/open-api/v1.0"
NS = "https://agriculture.ld.admin.ch/eCH-0309/1/"
ANIMAL_TRACING_TERM = URIRef(NS + "animalTracingTerm")
CODE_LISTS = Path("src/rdf/data/code_lists.skos.ttl")

# Values the interface offers and the Hilfsmittel does not take, with the reason.
# Adding one here is a decision; leaving one out makes the test fail.
NOT_ADOPTED = {
    "EnumGenus": {
        "Bee": "in Tabelle 2 durchgestrichen",
        "Fish": "in Tabelle 2 durchgestrichen",
        "Unknow": "nicht in Tabelle 2 aufgeführt (Tippfehler der Schnittstelle)",
        "Others": "nicht in Tabelle 2 aufgeführt",
    },
    "EnumAnimalTypeOfUse": {"NotDefined": "nicht in Tabelle 3 aufgeführt"},
    "EquidTypeOfUsage": {"Undefined": "nicht in Tabelle 3 aufgeführt"},
}

# :animalTracingTerm names AnimalTracing, which is the openAPI wherever it
# carries a counterpart and the technical service description otherwise.
SERVICE_DESCRIPTION_ONLY = {"BvdRisk"}


@pytest.fixture(scope="module")
def openapi():
    try:
        with urllib.request.urlopen(OPENAPI_URL, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        pytest.skip(f"openAPI nicht erreichbar: {error}")


@pytest.fixture(scope="module")
def members(openapi):
    """Property names and enum values per schema, following allOf composition."""
    schemas = openapi["components"]["schemas"]

    def collect(body, seen=()):
        found = set((body.get("properties") or {}).keys()) | set(body.get("enum", []))
        for part in body.get("allOf", []):
            ref = part.get("$ref")
            if ref and ref not in seen:
                found |= collect(schemas.get(ref.rsplit("/", 1)[-1], {}), seen + (ref,))
            elif not ref:
                found |= collect(part, seen)
        return found

    by_name = {}
    for name, body in schemas.items():
        by_name.setdefault(name.rsplit(".", 1)[-1], set()).update(collect(body))
    return by_name


@pytest.fixture(scope="module")
def graph():
    if not CODE_LISTS.exists():
        pytest.skip(f"Datei nicht gefunden: {CODE_LISTS}")
    return Graph().parse(CODE_LISTS, format="turtle")


def terms(graph):
    return sorted({str(o) for o in graph.objects(None, ANIMAL_TRACING_TERM)})


def test_every_mapping_resolves(graph, members):
    """Each :animalTracingTerm names a schema that exists, and a value it holds."""
    unresolved = []
    for term in terms(graph):
        schema, _, value = term.partition(".")
        if schema in SERVICE_DESCRIPTION_ONLY:
            continue
        if schema not in members:
            unresolved.append(f"{term}: Schema «{schema}» gibt es nicht mehr")
        elif value and value not in members[schema]:
            unresolved.append(f"{term}: «{value}» gibt es in {schema} nicht mehr")
    assert not unresolved, "Die Schnittstelle hat sich geändert:\n  " + "\n  ".join(unresolved)


def derived_schemes(graph):
    """Enums a scheme declares itself derived from, by naming one on the scheme."""
    return {str(term)
            for scheme in graph.subjects(RDF.type, SKOS.ConceptScheme)
            for term in graph.objects(scheme, ANIMAL_TRACING_TERM)}


def test_no_value_of_a_derived_enum_is_unaccounted_for(graph, members):
    """Every value of an enum a scheme derives from is adopted or declared absent."""
    adopted = {}
    for term in terms(graph):
        schema, _, value = term.partition(".")
        if value:
            adopted.setdefault(schema, set()).add(value)

    unaccounted = []
    for schema in sorted(derived_schemes(graph) & set(members)):
        known = adopted.get(schema, set()) | set(NOT_ADOPTED.get(schema, {}))
        for value in sorted(members[schema] - known):
            unaccounted.append(
                f"{schema}.{value} ist neu in der Schnittstelle und weder übernommen "
                f"noch in NOT_ADOPTED begründet")
    assert not unaccounted, "\n  ".join([""] + unaccounted)


def test_values_declared_as_not_adopted_are_absent(graph):
    """What NOT_ADOPTED lists must really be absent, or the reason is stale."""
    present = set(terms(graph))
    stale = [f"{schema}.{value} ({reason})"
             for schema, values in NOT_ADOPTED.items()
             for value, reason in values.items()
             if f"{schema}.{value}" in present]
    assert not stale, "In NOT_ADOPTED begründet, aber trotzdem vorhanden:\n  " + "\n  ".join(stale)


def test_the_service_description_exceptions_are_really_absent(members):
    """BvdRisk is listed as service-description-only; fail if the openAPI gains it."""
    gained = sorted(SERVICE_DESCRIPTION_ONLY & set(members))
    assert not gained, (
        "Die openAPI führt jetzt " + ", ".join(gained)
        + " -- SERVICE_DESCRIPTION_ONLY kann entfallen.")
