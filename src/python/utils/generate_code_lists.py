"""Generate SKOS code lists from the TVD AnimalTracing openAPI specification.

The Wertebereich tables of the Hilfsmittel carry German values and a good deal
of unresolved review comment; the TVD implementation carries the values that
are actually in use. This script takes the value *set* from the openAPI and the
German wording from the Hilfsmittel, and records on every concept where each
part came from, so that a later re-import shows up as a reviewable diff.

The openAPI is still in development: it is fetched fresh on every run, and the
generated file is committed, so `git diff` after a re-run is the changelog.

Concept values (skos:notation) are the openAPI's language-independent
identifiers. German labels and descriptions come from the Hilfsmittel tables
below; where it has no entry, the concept carries an English label only rather
than an invented translation. French and Italian await a source.
"""

import argparse
import json
import re
import urllib.request
from datetime import date
from pathlib import Path

DEFAULT_URL = "https://test-03-tvd-api-at.identitas.ch/open-api/v1.0"

# Scheme local name -> how to build it. "german" maps an openAPI value to the
# Hilfsmittel's wording; "descriptions" to that table's Definition column.
SCHEMES = [
    {
        "scheme": "genus", "enum": "EnumGenus",
        "name": {"de": "Nutztierart", "en": "Genus"},
        "table": "Tabelle 2: Definition Wertebereich Nutztierarten für die TVD",
        "german": {
            "Cattle": "Rindvieh", "Sheep": "Schafe", "Goat": "Ziegen", "Equid": "Equiden",
            "Camelid": "Kameliden", "Game": "Wild", "Pig": "Schweine", "Bee": "Biene",
            "Fish": "Fisch", "Poultry": "Geflügel",
        },
        "descriptions": {
            "Cattle": "Tiere der Rindergattung (Bos) und Wasserbüffel (Bubalus bubalis)",
            "Equid": "Tiere der Pferdegattung (Pferd, Maultier, Maulesel, Esel)",
            "Camelid": "Neuweltkameliden",
            "Game": "Wild in Gehegen",
        },
    },
    {
        "scheme": "gender", "enum": "EnumGender",
        "name": {"de": "Geschlecht", "en": "Gender"},
        "table": "Tabelle 6: Definition Wertebereich Geschlecht",
        "german": {"Male": "Männlich", "Female": "Weiblich"},
        "descriptions": {},
    },
    {
        "scheme": "animalTypeOfUse", "enum": "EnumAnimalTypeOfUse",
        "name": {"de": "Zweck (Rinder, Schafe, Ziegen)", "en": "Type of use (cattle, sheep, goats)"},
        "table": "Tabelle 3: Definition Wertebereich Zweck pro Nutztierart",
        "german": {"Milk": "Milch", "Other": "Andere"},
        "descriptions": {"Milk": "Milchkühe, -schafe und -ziegen"},
    },
    {
        "scheme": "equidTypeOfUsage", "enum": "EquidTypeOfUsage",
        "name": {"de": "Zweck (Equiden)", "en": "Type of use (equids)"},
        "table": "Tabelle 3: Definition Wertebereich Zweck pro Nutztierart",
        "german": {"CompanionAnimal": "Heimtier", "FarmAnimal": "Nutztier"},
        "descriptions": {},
    },
    {
        "scheme": "animalHistoryState", "enum": "EnumAnimalHistoryState",
        "name": {"de": "Tiergeschichtestatus", "en": "Animal history state"},
        "table": "Tabelle 7: Definition Wertebereich Tiergeschichtestatus",
        "german": {
            "NotDefined": "Nicht definiert", "NotOk": "Fehlerhaft",
            "TemporaryOk": "Temporär OK", "Ok": "OK", "Lost": "Verschollen",
        },
        "descriptions": {},
    },
    {
        # No Wertebereich table in the Hilfsmittel for «Grössenkategorie».
        "scheme": "equidWithersClass", "enum": "EnumEquidWithersClass",
        "name": {"de": "Grössenkategorie", "en": "Withers class"},
        "table": None,
        "german": {},
        "descriptions": {},
    },
]

HEADER = '''# ==============================================================================
# CODE LISTS (Wertebereiche)
#
# GENERATED FILE -- do not edit by hand. Regenerate with:
#     venv/bin/python src/python/utils/generate_code_lists.py \\
#         -o src/rdf/data/code_lists.skos.ttl
#
# Values are taken from the TVD AnimalTracing openAPI, German wording from the
# Wertebereich tables of the Hilfsmittel. Every concept records both with
# :animalTracingTerm and :sourceTerm.
#
# The openAPI is still in development, so these lists are provisional. French
# and Italian labels are missing: neither source provides them, and inventing
# them here would misrepresent the source. See :codeLists for the as-of date.
# ==============================================================================

@prefix :                <https://agriculture.ld.admin.ch/eCH-0309/1/> .
@prefix code:            <https://agriculture.ld.admin.ch/eCH-0309/1/code/> .

@prefix dcterms:         <http://purl.org/dc/terms/> .
@prefix schema:          <http://schema.org/> .
@prefix skos:            <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd:             <http://www.w3.org/2001/XMLSchema#> .
'''


def escape(text):
    return text.replace("\\", "\\\\").replace('"', '\\"')


def readable(value):
    """'CompanionAnimal' -> 'Companion animal'; used as the English label."""
    words = re.findall(r"[A-Z]+(?![a-z])|[A-Z][a-z]*|\d+[a-z]*", value) or [value]
    return " ".join([words[0]] + [w.lower() for w in words[1:]])


def slug(text):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", text).lower()


def load_spec(url, local):
    if local:
        return json.loads(Path(local).read_text(encoding="utf-8")), local
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8")), url


def enums_by_short_name(spec):
    found = {}
    for name, schema in spec["components"]["schemas"].items():
        if "enum" in schema:
            found.setdefault(name.rsplit(".", 1)[-1], schema["enum"])
    return found


def main():
    parser = argparse.ArgumentParser(description="Generate SKOS code lists from the TVD openAPI.")
    parser.add_argument("-u", "--url", default=DEFAULT_URL, help="openAPI URL (fetched fresh)")
    parser.add_argument("-i", "--input", help="Local openAPI file, used instead of --url")
    parser.add_argument("-o", "--output", required=True, help="Output Turtle file")
    args = parser.parse_args()

    spec, origin = load_spec(args.url, args.input)
    enums = enums_by_short_name(spec)

    info = spec.get("info", {})
    out = [HEADER]
    out.append(f'''
# ==============================================================================
# SCHEME METADATA
# ==============================================================================

:codeLists a skos:Collection ;
    schema:name "Wertebereiche der Tierverkehrsdaten"@de,
        "Code lists of the animal movement data"@en ;
    dcterms:source "{escape(str(origin))}" ;
    dcterms:hasVersion "{escape(str(info.get("title", "")))} {escape(str(info.get("version", "")))}" ;
    dcterms:modified "{date.today().isoformat()}"^^xsd:date .
''')

    missing = []
    for spec_entry in SCHEMES:
        values = enums.get(spec_entry["enum"])
        if values is None:
            missing.append(spec_entry["enum"])
            continue

        out.append(f'''
# ------------------------------------------------------------------------------
# {spec_entry["name"]["de"]} -- openAPI {spec_entry["enum"]}
# {"Hilfsmittel: " + spec_entry["table"] if spec_entry["table"] else "No Wertebereich table in the Hilfsmittel."}
# ------------------------------------------------------------------------------

:{spec_entry["scheme"]} a skos:ConceptScheme ;
    schema:name "{escape(spec_entry["name"]["de"])}"@de,
        "{escape(spec_entry["name"]["en"])}"@en ;
    :animalTracingTerm "{spec_entry["enum"]}" .
''')
        for value in values:
            iri = f'code:{slug(spec_entry["scheme"])}-{slug(value)}'
            german = spec_entry["german"].get(value)
            description = spec_entry["descriptions"].get(value)

            lines = [f"{iri} a skos:Concept ;",
                     f'    skos:inScheme :{spec_entry["scheme"]} ;',
                     f'    skos:topConceptOf :{spec_entry["scheme"]} ;',
                     f'    skos:notation "{escape(value)}" ;']
            names = []
            if german:
                names.append(f'"{escape(german)}"@de')
            names.append(f'"{escape(readable(value))}"@en')
            lines.append("    schema:name " + (",\n        ".join(names)) + " ;")
            if description:
                lines.append(f'    schema:description "{escape(description)}"@de ;')
            if german:
                lines.append(f'    :sourceTerm "{escape(german)}" ;')
            lines.append(f'    :animalTracingTerm "{spec_entry["enum"]}.{escape(value)}" .')
            out.append("\n".join(lines) + "\n")

    Path(args.output).write_text("\n".join(out), encoding="utf-8")
    if missing:
        raise SystemExit(f"ERROR: enum(s) not found in the openAPI: {', '.join(missing)}")


if __name__ == "__main__":
    main()
