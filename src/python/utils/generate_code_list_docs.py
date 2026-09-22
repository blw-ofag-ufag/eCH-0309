"""Render the SKOS code lists as a chapter of the Hilfsmittel.

Mirrors generate_glossary_docs.py: one section per skos:ConceptScheme, each
with a table of the values. The Hilfsmittel addresses readers without deep IT
knowledge, so the code lists belong in the document itself and not only in the
Turtle.

Labels currently exist in German and English only -- the openAPI carries no
translations and the Wertebereich tables of the Hilfsmittel are German. Where a
label is missing in the document's language, the section says so rather than
silently falling back.
"""

import argparse
import re
from pathlib import Path

from rdflib import Graph, Namespace
from rdflib.namespace import DCTERMS, RDF, SKOS

SCHEMA = Namespace("http://schema.org/")

TRANSLATIONS = {
    "en": {
        "value": "Value", "term": "Designation", "desc": "Description",
        "note": "No French or Italian designations are available for these code lists yet; the "
                "designations below are given in German and English, as provided by the sources.",
        "caption": "Values of the code list",
    },
    "de": {
        "value": "Wert", "term": "Bezeichnung", "desc": "Beschreibung",
        "note": "Für diese Wertebereiche liegen noch keine französischen und italienischen "
                "Bezeichnungen vor; die Bezeichnungen sind in Deutsch und Englisch aufgeführt, "
                "so wie sie die Quellen liefern.",
        "caption": "Werte des Wertebereichs",
    },
    "fr": {
        "value": "Valeur", "term": "Désignation", "desc": "Description",
        "note": "Aucune désignation française ou italienne n'est encore disponible pour ces "
                "domaines de valeurs ; les désignations sont indiquées en allemand et en anglais, "
                "telles que les sources les fournissent.",
        "caption": "Valeurs du domaine de valeurs",
    },
    "it": {
        "value": "Valore", "term": "Designazione", "desc": "Descrizione",
        "note": "Per questi domini di valori non sono ancora disponibili designazioni francesi e "
                "italiane; le designazioni sono riportate in tedesco e in inglese, così come le "
                "forniscono le fonti.",
        "caption": "Valori del dominio di valori",
    },
}


def get_localized_value(graph, subject, predicates, lang):
    for predicate in predicates:
        values = {}
        for obj in graph.objects(subject, predicate):
            values[(obj.language or "").lower()] = str(obj)
        if not values:
            continue
        for candidate in (lang, "de", "en", ""):
            if candidate in values:
                return values[candidate]
    return None


def anchor(uri):
    return re.sub(r"[^a-z0-9]+", "-", str(uri).rsplit("/", 1)[-1].lower()).strip("-")


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def main():
    parser = argparse.ArgumentParser(description="Generate Markdown documentation from SKOS code lists.")
    parser.add_argument("-i", "--input", required=True, help="Input SKOS file (.ttl)")
    parser.add_argument("-d", "--docs_dir", required=True, help="Docs directory containing language subdirectories")
    parser.add_argument("-p", "--prefixes", required=False, help="Prefix file (.ttl) to override QNames")
    args = parser.parse_args()

    graph = Graph(bind_namespaces="none")
    graph.parse(args.input, format="turtle")

    if args.prefixes:
        prefix_graph = Graph(bind_namespaces="none")
        prefix_graph.parse(args.prefixes, format="turtle")
        for prefix, uri in prefix_graph.namespaces():
            try:
                graph.bind(str(prefix), Namespace(str(uri)), override=True, replace=True)
            except TypeError:
                graph.bind(str(prefix), Namespace(str(uri)), override=True)

    docs_dir = Path(args.docs_dir)
    languages = [lang for lang in TRANSLATIONS if (docs_dir / lang).is_dir()]

    schemes = sorted(graph.subjects(RDF.type, SKOS.ConceptScheme), key=lambda s: anchor(s))
    source = next(graph.objects(None, DCTERMS.source), None)
    modified = next(graph.objects(None, DCTERMS.modified), None)

    for lang in languages:
        words = TRANSLATIONS[lang]
        lines = [words["note"], ""]
        if source and modified:
            lines[0] += f" ([{source}]({source}), {modified})"

        for scheme in schemes:
            name = get_localized_value(graph, scheme, [SCHEMA.name, SKOS.prefLabel], lang) or anchor(scheme)
            lines.append(f"## {name} {{#sec-codelist-{anchor(scheme)}}}")
            lines.append("")
            lines.append(f"| {words['value']} | {words['term']} | {words['desc']} |")
            lines.append("|:--|:--|:--|")

            concepts = sorted(
                graph.subjects(SKOS.inScheme, scheme),
                key=lambda c: str(next(graph.objects(c, SKOS.notation), "")),
            )
            for concept in concepts:
                notation = next(graph.objects(concept, SKOS.notation), "")
                term = get_localized_value(graph, concept, [SCHEMA.name, SKOS.prefLabel], lang) or ""
                description = get_localized_value(graph, concept, [SCHEMA.description, SKOS.definition], lang) or ""
                lines.append(f"| `{cell(notation)}` | {cell(term)} | {cell(description)} |")

            lines.append(f": {words['caption']} {name} {{#tbl-codelist-{anchor(scheme)} tbl-colwidths=\"[25,30,45]\"}}")
            lines.append("")

        (docs_dir / lang / "code-lists.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
