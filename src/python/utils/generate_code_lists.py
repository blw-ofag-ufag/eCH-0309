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
NAMESPACE = "https://agriculture.ld.admin.ch/eCH-0309/1/"

# Scheme local name -> how to build it. "german" maps an openAPI value to the
# Hilfsmittel's wording; "descriptions" to that table's Definition column.
SCHEMES = [
    {
        "scheme": "genus", "enum": "EnumGenus",
        "name": {"de": "Nutztierart", "en": "Genus", "fr": "Espèce d'animal de rente", "it": "Specie di animale da reddito"},
        "table": "Tabelle 2: Definition Wertebereich Nutztierarten für die TVD",
        "german": {
            "Cattle": "Rindvieh", "Sheep": "Schafe", "Goat": "Ziegen", "Equid": "Equiden",
            "Camelid": "Kameliden", "Game": "Wild", "Pig": "Schweine", "Bee": "Biene",
            "Fish": "Fisch", "Poultry": "Geflügel",
        },
        "excluded": {
            "Bee": "in Tabelle 2 durchgestrichen",
            "Fish": "in Tabelle 2 durchgestrichen",
            "Unknow": "nicht in Tabelle 2 aufgeführt",
            "Others": "nicht in Tabelle 2 aufgeführt",
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
        "name": {"de": "Geschlecht", "en": "Gender", "fr": "Sexe", "it": "Sesso"},
        "table": "Tabelle 6: Definition Wertebereich Geschlecht",
        "german": {"Male": "Männlich", "Female": "Weiblich"},
        "descriptions": {},
    },
    {
        "scheme": "animalTypeOfUse", "enum": "EnumAnimalTypeOfUse",
        "name": {"de": "Zweck (Rinder, Schafe, Ziegen)", "en": "Type of use (cattle, sheep, goats)", "fr": "Type d'utilisation (bovins, ovins, caprins)", "it": "Tipo di utilizzo (bovini, ovini, caprini)"},
        "table": "Tabelle 3: Definition Wertebereich Zweck pro Nutztierart",
        "german": {"Milk": "Milch", "Other": "Andere"},
        "excluded": {"NotDefined": "nicht in Tabelle 3 aufgeführt"},
        "descriptions": {"Milk": "Milchkühe, -schafe und -ziegen"},
    },
    {
        "scheme": "equidTypeOfUsage", "enum": "EquidTypeOfUsage",
        "name": {"de": "Zweck (Equiden)", "en": "Type of use (equids)", "fr": "Type d'utilisation (équidés)", "it": "Tipo di utilizzo (equidi)"},
        "table": "Tabelle 3: Definition Wertebereich Zweck pro Nutztierart",
        "german": {"CompanionAnimal": "Heimtier", "FarmAnimal": "Nutztier"},
        "excluded": {"Undefined": "nicht in Tabelle 3 aufgeführt"},
        "descriptions": {},
    },
    {
        "scheme": "animalHistoryState", "enum": "EnumAnimalHistoryState",
        "name": {"de": "Tiergeschichtestatus", "en": "Animal history state", "fr": "Statut de l'historique de l'animal", "it": "Stato della storia dell'animale"},
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
        "name": {"de": "Grössenkategorie", "en": "Withers class", "fr": "Catégorie de taille", "it": "Categoria di grandezza"},
        # The enum is named WithersClass and chapter 3.1.4 lists «Widerristhöhe»
        # among the equid attributes, so the threshold is the height at the withers.
        "table": None,
        "german": {"LessOrEqualThan148cm": "Widerristhöhe bis 148 cm",
                   "GreaterThan148cm": "Widerristhöhe über 148 cm"},
        "english": {"LessOrEqualThan148cm": "Withers height up to 148 cm",
                    "GreaterThan148cm": "Withers height above 148 cm"},
        "french": {"LessOrEqualThan148cm": "Hauteur au garrot jusqu'à 148 cm",
                   "GreaterThan148cm": "Hauteur au garrot supérieure à 148 cm"},
        "italian": {"LessOrEqualThan148cm": "Altezza al garrese fino a 148 cm",
                    "GreaterThan148cm": "Altezza al garrese superiore a 148 cm"},
        "descriptions": {},
    },
]


# Code lists the Hilfsmittel defines itself. The openAPI has no matching list:
# notification types are split per species there and carry no equid variant, and
# the health statuses appear as separate fields (BvdState, BvdRisk, FootrotState)
# rather than as a Typ/Status pair. Values, wording and order therefore come from
# the Wertebereich tables; :animalTracingTerm records only the counterparts that
# are unambiguous. Deliberately unmapped: «Tagesaufenthalt», which resembles
# CommuteStart/CommuteStop, and «Einfuhr nach Ausfuhr», which resembles
# ImportSwissEarTag -- neither is certain enough to assert.
DOCUMENT_SCHEMES = [
    {
        "scheme": "notificationType",
        "name": {"de": "Bewegungstyp", "en": "Notification type",
                 "fr": "Type de mouvement", "it": "Tipo di movimento"},
        "table": "Tabelle 8: Definition Wertebereich Bewegungstyp",
        "values": [
            ("Birth", "Geburt", "Birth", "Naissance", "Nascita", None,
             ["EnumCattleNotificationType.Birth", "EnumSheepNotificationType.Birth", "EnumGoatNotificationType.Birth"]),
            ("Arrival", "Zugang", "Arrival", "Entrée", "Entrata", "nicht",
             ["EnumCattleNotificationType.Arrival", "EnumSheepNotificationType.Arrival", "EnumGoatNotificationType.Arrival"]),
            ("Leaving", "Abgang", "Departure", "Sortie", "Uscita", "nicht",
             ["EnumCattleNotificationType.Leaving", "EnumSheepNotificationType.Leaving", "EnumGoatNotificationType.Leaving"]),
            ("Slaughter", "Schlachtung", "Slaughter", "Abattage", "Macellazione", None,
             ["EnumCattleNotificationType.Slaughtering", "EnumSheepNotificationType.Slaughter", "EnumGoatNotificationType.Slaughter"]),
            ("Deceased", "Verendung", "Death", "Mort", "Morte", "euthanasie",
             ["EnumCattleNotificationType.Deceased", "EnumSheepNotificationType.Deceased", "EnumGoatNotificationType.Deceased"]),
            ("Import", "Einfuhr", "Import", "Importation", "Importazione", None,
             ["EnumCattleNotificationType.Import", "EnumSheepNotificationType.Import", "EnumGoatNotificationType.Import"]),
            ("Export", "Ausfuhr", "Export", "Exportation", "Esportazione", "eigentum",
             ["EnumCattleNotificationType.Export", "EnumSheepNotificationType.Export", "EnumGoatNotificationType.Export"]),
            ("DayStay", "Tagesaufenthalt", "Day stay", "Séjour à la journée", "Soggiorno giornaliero", "nicht", []),
            ("ImportAfterExport", "Einfuhr nach Ausfuhr", "Import after export",
             "Importation après exportation", "Importazione dopo esportazione", "nicht", []),
            ("OnFarmSlaughter", "Hofschlachtung", "On-farm slaughter", "Abattage à la ferme",
             "Macellazione in azienda", "nicht",
             ["EnumCattleNotificationType.YardSlaughter", "EnumSheepNotificationType.OnFarmSlaughter", "EnumGoatNotificationType.OnFarmSlaughter"]),
            ("DeathBirth", "Totgeburt", "Stillbirth", "Mortinaissance", "Nato morto", "nicht",
             ["EnumCattleNotificationType.DeathBirth", "EnumSheepNotificationType.DeathBirth", "EnumGoatNotificationType.DeathBirth"]),
            ("LocationChange", "Standortwechsel", "Change of location", "Changement de lieu",
             "Cambiamento di ubicazione", "nur", []),
            ("FirstRegistration", "Erstregistrierung", "First registration", "Premier enregistrement",
             "Prima registrazione", None,
             ["EnumSheepNotificationType.FirstRegistration", "EnumGoatNotificationType.FirstRegistration"]),
        ],
    },
    {
        "scheme": "healthStatusType",
        "name": {"de": "Typ Gesundheitsstatus", "en": "Health status type",
                 "fr": "Type d'état sanitaire", "it": "Tipo di stato sanitario"},
        "table": "Tabelle 9: Definition Wertebereich Typ Gesundheitsstatus",
        "values": [
            ("EpizooticStatus", "Seuchenstatus", "Epizootic status", "Statut épizootique", "Stato epizootico", None, ["BvdState", "FootrotState"]),
            ("VaccinationStatus", "Impfstatus", "Vaccination status", "Statut vaccinal", "Stato vaccinale", None, []),
            ("RiskStatus", "Risikostatus", "Risk status", "Statut de risque", "Stato di rischio", None, ["BvdRisk"]),
            ("LaboratoryResult", "Laborergebnis", "Laboratory result", "Résultat de laboratoire", "Risultato di laboratorio", None, []),
        ],
    },
    {
        "scheme": "localUnitHealthStatus",
        "name": {"de": "Seuchenstatus örtliche Einheit", "en": "Health status of a local unit",
                 "fr": "État sanitaire de l'unité locale", "it": "Stato sanitario dell'unità locale"},
        "table": "Tabelle 10: Definition Wertebereich Seuchenstatus örtliche Einheit",
        "values": [
            ("Blocked", "gesperrt", "Blocked", "Bloqué", "Bloccato", "Seuchenstatus", ["FootRotState.Blocked", "BvdState.Blocked"]),
            ("Free", "frei", "Free", "Libre", "Libero", "Seuchenstatus", ["FootRotState.Free"]),
            ("NotTested", "Nicht getestet", "Not tested", "Non testé", "Non testato", "Seuchenstatus", ["FootRotState.NotTested"]),
            ("High", "Hoch", "High", "Élevé", "Alto", "Risikostatus", []),
            ("Low", "Tief", "Low", "Faible", "Basso", "Risikostatus", []),
            ("Medium", "Mittel", "Medium", "Moyen", "Medio", "Risikostatus", []),
            ("Positive", "positiv", "Positive", "Positif", "Positivo", "Laborergebnis", []),
            ("Negative", "negativ", "Negative", "Négatif", "Negativo", "Laborergebnis", []),
        ],
    },
    {
        "scheme": "animalHealthStatus",
        "name": {"de": "Seuchenstatus Einzeltier", "en": "Health status of an individual animal",
                 "fr": "État sanitaire de l'animal individuel", "it": "Stato sanitario dell'animale singolo"},
        "table": "Tabelle 11: Definition Wertebereich Seuchenstatus Einzeltier",
        "values": [
            ("Blocked", "gesperrt", "Blocked", "Bloqué", "Bloccato", "Seuchenstatus", []),
            ("Free", "frei", "Free", "Libre", "Libero", "Seuchenstatus", []),
            ("NotTested", "Nicht getestet", "Not tested", "Non testé", "Non testato", "Seuchenstatus", []),
            ("Vaccinated", "geimpft", "Vaccinated", "Vacciné", "Vaccinato", "Impfstatus", ["EnumCattleLsdState.Vaccinated"]),
        ],
    },
]

# The Definition column of the tables, reused across rows.
NOTES = {
    "nicht": {"de": "Nicht für Equiden", "en": "Not for equids", "fr": "Pas pour les équidés", "it": "Non per gli equidi"},
    "nur": {"de": "Nur für Equiden", "en": "For equids only", "fr": "Uniquement pour les équidés", "it": "Solo per gli equidi"},
    "euthanasie": {"de": "Bei Equiden: Euthanasierung", "en": "For equids: euthanasia",
                   "fr": "Pour les équidés : euthanasie", "it": "Per gli equidi: eutanasia"},
    "eigentum": {"de": "Bei Equiden: Eigentumsabgabe ins Ausland", "en": "For equids: transfer of ownership abroad",
                 "fr": "Pour les équidés : cession de propriété à l'étranger",
                 "it": "Per gli equidi: cessione di proprietà all'estero"},
    "Seuchenstatus": {"de": "Typ: Seuchenstatus", "en": "Type: epizootic status",
                      "fr": "Type : statut épizootique", "it": "Tipo: stato epizootico"},
    "Risikostatus": {"de": "Typ: Risikostatus", "en": "Type: risk status",
                     "fr": "Type : statut de risque", "it": "Tipo: stato di rischio"},
    "Laborergebnis": {"de": "Typ: Laborergebnis", "en": "Type: laboratory result",
                      "fr": "Type : résultat de laboratoire", "it": "Tipo: risultato di laboratorio"},
    "Impfstatus": {"de": "Typ: Impfstatus", "en": "Type: vaccination status",
                   "fr": "Type : statut vaccinal", "it": "Tipo: stato vaccinale"},
}

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
# Each code list gets its own sub-namespace and each concept is named by the
# identifier the source system uses for it, as in eCH-0265, where the AGIS,
# NAEBI and PSM lists are keyed by their own numeric codes. The identifier is
# therefore not ours to case.
#
# Values that the Hilfsmittel strikes through or does not list are left out, and
# the omission is noted on the scheme: the two documents are meant to carry the
# same values.
#
# The openAPI is still in development, so these lists are provisional. French
# and Italian labels are missing: neither source provides them, and inventing
# them here would misrepresent the source. See :codeLists for the as-of date.
# ==============================================================================

@prefix :                <https://agriculture.ld.admin.ch/eCH-0309/1/> .
{prefixes}
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
    prefixes = "\n".join(
        f'@prefix {name + ":":24s}<{NAMESPACE}{name}/> .'
        for name in (entry["scheme"].lower() for entry in SCHEMES + DOCUMENT_SCHEMES)
    ) + "\n"
    out = [HEADER.format(prefixes=prefixes)]
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

        excluded = spec_entry.get("excluded", {})
        dropped = "".join(
            f"\n# Nicht übernommen: {value} -- {reason}."
            for value, reason in excluded.items() if value in values
        )
        values = [value for value in values if value not in excluded]

        out.append(f'''
# ------------------------------------------------------------------------------
# {spec_entry["name"]["de"]} -- openAPI {spec_entry["enum"]}
# {"Hilfsmittel: " + spec_entry["table"] if spec_entry["table"] else "No Wertebereich table in the Hilfsmittel."}{dropped}
# ------------------------------------------------------------------------------

{spec_entry["scheme"].lower()}:ConceptScheme a skos:ConceptScheme ;
    schema:name {",".join(chr(10) + "        " + chr(34) + escape(text) + chr(34) + "@" + code if n else chr(34) + escape(text) + chr(34) + "@" + code for n, (code, text) in enumerate(spec_entry["name"].items()))} ;
    :animalTracingTerm "{spec_entry["enum"]}" .
''')
        for value in values:
            iri = f'{spec_entry["scheme"].lower()}:{value}'
            german = spec_entry["german"].get(value)
            description = spec_entry["descriptions"].get(value)

            lines = [f"{iri} a skos:Concept ;",
                     f'    skos:inScheme {spec_entry["scheme"].lower()}:ConceptScheme ;',
                     f'    skos:topConceptOf {spec_entry["scheme"].lower()}:ConceptScheme ;',
                     f'    skos:notation "{escape(value)}" ;']
            names = []
            for code in ("de", "en", "fr", "it"):
                key = {"de": "german", "en": "english", "fr": "french", "it": "italian"}[code]
                text = spec_entry.get(key, {}).get(value)
                if text is None and code == "en":
                    text = readable(value)
                if text:
                    names.append(f'"{escape(text)}"@{code}')
            lines.append("    schema:name " + (",\n        ".join(names)) + " ;")
            if description:
                lines.append(f'    schema:description "{escape(description)}"@de ;')
            # :sourceTerm is the Hilfsmittel's own wording, so only a scheme that
            # has a Wertebereich table can carry one.
            if german and spec_entry["table"]:
                lines.append(f'    :sourceTerm "{escape(german)}" ;')
            lines.append(f'    :animalTracingTerm "{spec_entry["enum"]}.{escape(value)}" .')
            out.append("\n".join(lines) + "\n")

    for entry in DOCUMENT_SCHEMES:
        prefix = entry["scheme"].lower()
        out.append(f'''
# ------------------------------------------------------------------------------
# {entry["name"]["de"]} -- aus dem Hilfsmittel, {entry["table"]}
# ------------------------------------------------------------------------------

{prefix}:ConceptScheme a skos:ConceptScheme ;
    schema:name {",".join(chr(10) + "        " + chr(34) + escape(text) + chr(34) + "@" + code if n else chr(34) + escape(text) + chr(34) + "@" + code for n, (code, text) in enumerate(entry["name"].items()))} .
''')
        for notation, de, en, fr, it, note, tracing in entry["values"]:
            lines = [f"{prefix}:{notation} a skos:Concept ;",
                     f"    skos:inScheme {prefix}:ConceptScheme ;",
                     f"    skos:topConceptOf {prefix}:ConceptScheme ;",
                     f'    skos:notation "{escape(notation)}" ;',
                     "    schema:name " + ",\n        ".join(
                         f'"{escape(text)}"@{code}' for code, text in
                         (("de", de), ("en", en), ("fr", fr), ("it", it))) + " ;"]
            if note:
                lines.append("    schema:description " + ",\n        ".join(
                    f'"{escape(NOTES[note][code])}"@{code}' for code in ("de", "en", "fr", "it")) + " ;")
            lines.append(f'    :sourceTerm "{escape(de)}" ;')
            if tracing:
                lines.append("    :animalTracingTerm " + ", ".join(f'"{escape(t)}"' for t in tracing) + " ;")
            lines[-1] = lines[-1][:-1] + "."
            out.append("\n".join(lines) + "\n")

    Path(args.output).write_text("\n".join(out), encoding="utf-8")
    if missing:
        raise SystemExit(f"ERROR: enum(s) not found in the openAPI: {', '.join(missing)}")


if __name__ == "__main__":
    main()
