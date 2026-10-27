"""Compares the code lists against the TVD AnimalTracing openAPI.

src/rdf/data/codelists.ttl is maintained by hand: the Wertebereiche are part of
the Hilfsmittel, and describing a value or adding a translation has to survive.
This module is what keeps it honest, by reporting drift in both directions:

- a code value the interface no longer carries, because it renamed or dropped
  something;
- a value the interface carries that the file neither holds nor lists below as
  deliberately absent.

Only the lists derived from an enum are compared. A list says so through the
data model: the property shape that restricts its values to the list names the
enum with :animalTracingTerm, and the schema:codeValue of each of its values is
the enum member. The other four lists take their values from the Wertebereich
tables of the Hilfsmittel, so they are not meant to exhaust any enum. Where one
of their values has a counterpart in the interface, under another name or in
several enums, HILFSMITTEL_COUNTERPARTS records it, and the interface is checked
to still carry it.

The second direction is the one a generator cannot give you. A new value in the
openAPI is a decision for the Fachgruppe, not something to import silently.
"""

import json
import urllib.error
import urllib.request
from pathlib import Path

import pytest
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import SH

OPENAPI_URL = "https://test-01-tvd-api-at.identitas.ch/open-api/v1.0"
NS = "https://agriculture.ld.admin.ch/eCH-0309/1/"
SCHEMA = Namespace("http://schema.org/")
ANIMAL_TRACING_TERM = URIRef(NS + "animalTracingTerm")
CODE_LISTS = Path("src/rdf/data/codelists.ttl")
SHAPES = Path("src/rdf/shapes/model.shacl.ttl")

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

# Values of the lists taken from the Hilfsmittel alone, with their counterparts
# in the interface: an enum member as Schema.Member, or a whole schema. A value
# without a counterpart, such as DayStay, is not listed.
HILFSMITTEL_COUNTERPARTS = {
    "notificationtype:Birth": ["EnumCattleNotificationType.Birth", "EnumSheepNotificationType.Birth",
                               "EnumGoatNotificationType.Birth"],
    "notificationtype:Arrival": ["EnumCattleNotificationType.Arrival", "EnumSheepNotificationType.Arrival",
                                 "EnumGoatNotificationType.Arrival"],
    "notificationtype:Leaving": ["EnumCattleNotificationType.Leaving", "EnumSheepNotificationType.Leaving",
                                 "EnumGoatNotificationType.Leaving"],
    "notificationtype:Slaughter": ["EnumCattleNotificationType.Slaughtering", "EnumSheepNotificationType.Slaughter",
                                   "EnumGoatNotificationType.Slaughter"],
    "notificationtype:Deceased": ["EnumCattleNotificationType.Deceased", "EnumSheepNotificationType.Deceased",
                                  "EnumGoatNotificationType.Deceased"],
    "notificationtype:Import": ["EnumCattleNotificationType.Import", "EnumSheepNotificationType.Import",
                                "EnumGoatNotificationType.Import"],
    "notificationtype:Export": ["EnumCattleNotificationType.Export", "EnumSheepNotificationType.Export",
                                "EnumGoatNotificationType.Export"],
    "notificationtype:OnFarmSlaughter": ["EnumCattleNotificationType.YardSlaughter",
                                         "EnumSheepNotificationType.OnFarmSlaughter",
                                         "EnumGoatNotificationType.OnFarmSlaughter"],
    "notificationtype:DeathBirth": ["EnumCattleNotificationType.DeathBirth", "EnumSheepNotificationType.DeathBirth",
                                    "EnumGoatNotificationType.DeathBirth"],
    "notificationtype:FirstRegistration": ["EnumSheepNotificationType.FirstRegistration",
                                           "EnumGoatNotificationType.FirstRegistration"],
    "healthstatustype:EpizooticStatus": ["BvdState", "FootRotState"],
    "localunithealthstatus:Blocked": ["FootRotState.Blocked", "BvdState.Blocked"],
    "localunithealthstatus:Free": ["FootRotState.Free"],
    "localunithealthstatus:NotTested": ["FootRotState.NotTested"],
    "animalhealthstatus:Vaccinated": ["EnumCattleLsdState.Vaccinated"],
}


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
def derived():
    """Maps each enum a list derives from to the code values of that list."""
    for path in (CODE_LISTS, SHAPES):
        if not path.exists():
            pytest.skip(f"Datei nicht gefunden: {path}")
    graph = Graph().parse(CODE_LISTS, format="turtle").parse(SHAPES, format="turtle")
    enums = {}
    for prop, enum in graph.subject_objects(ANIMAL_TRACING_TERM):
        for node in graph.objects(prop, SH.node):
            for nested in graph.objects(node, SH.property):
                if graph.value(nested, SH.path) != SCHEMA.inCodeSet:
                    continue
                code_list = graph.value(nested, SH.hasValue)
                enums.setdefault(str(enum), set()).update(
                    str(graph.value(code, SCHEMA.codeValue))
                    for code in graph.objects(code_list, SCHEMA.hasCategoryCode))
    return enums


def test_every_code_value_resolves(derived, members):
    """Each enum a list derives from exists, and holds every code value of the list."""
    unresolved = []
    for enum, values in sorted(derived.items()):
        if enum not in members:
            unresolved.append(f"Schema «{enum}» gibt es nicht mehr")
            continue
        for value in sorted(values - members[enum]):
            unresolved.append(f"{enum}.{value}: «{value}» gibt es in {enum} nicht mehr")
    assert not unresolved, "Die Schnittstelle hat sich geändert:\n  " + "\n  ".join(unresolved)


def test_no_value_of_a_derived_enum_is_unaccounted_for(derived, members):
    """Every value of an enum a list derives from is adopted or declared absent."""
    unaccounted = []
    for enum in sorted(set(derived) & set(members)):
        known = derived[enum] | set(NOT_ADOPTED.get(enum, {}))
        for value in sorted(members[enum] - known):
            unaccounted.append(
                f"{enum}.{value} ist neu in der Schnittstelle und weder übernommen "
                f"noch in NOT_ADOPTED begründet")
    assert not unaccounted, "\n  ".join([""] + unaccounted)


def test_values_declared_as_not_adopted_are_absent(derived):
    """What NOT_ADOPTED lists must really be absent, or the reason is stale."""
    stale = [f"{enum}.{value} ({reason})"
             for enum, values in NOT_ADOPTED.items()
             for value, reason in values.items()
             if value in derived.get(enum, set())]
    assert not stale, "In NOT_ADOPTED begründet, aber trotzdem vorhanden:\n  " + "\n  ".join(stale)


def test_every_enum_of_not_adopted_is_derived_from(derived):
    """A NOT_ADOPTED entry for an enum no list derives from would never be checked."""
    orphans = sorted(set(NOT_ADOPTED) - set(derived))
    assert not orphans, "Keine Liste leitet sich ab von: " + ", ".join(orphans)


def test_hilfsmittel_counterparts_resolve(members):
    """Each counterpart recorded for a Hilfsmittel value is still in the interface."""
    unresolved = []
    for value, counterparts in sorted(HILFSMITTEL_COUNTERPARTS.items()):
        for counterpart in counterparts:
            schema, _, member = counterpart.partition(".")
            if schema not in members:
                unresolved.append(f"{value}: Schema «{schema}» gibt es nicht mehr")
            elif member and member not in members[schema]:
                unresolved.append(f"{value}: «{member}» gibt es in {schema} nicht mehr")
    assert not unresolved, "Die Schnittstelle hat sich geändert:\n  " + "\n  ".join(unresolved)


def test_hilfsmittel_counterparts_name_existing_values():
    """A key of HILFSMITTEL_COUNTERPARTS that is no value of a list is stale."""
    if not CODE_LISTS.exists():
        pytest.skip(f"Datei nicht gefunden: {CODE_LISTS}")
    graph = Graph().parse(CODE_LISTS, format="turtle")
    codes = set(graph.subjects(SCHEMA.inCodeSet, None))
    stale = [value for value in sorted(HILFSMITTEL_COUNTERPARTS)
             if graph.namespace_manager.expand_curie(value) not in codes]
    assert not stale, "Kein Wert der Codelisten: " + ", ".join(stale)
