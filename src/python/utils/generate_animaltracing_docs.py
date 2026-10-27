"""Generates docs/<lang>/animaltracing.md, the tables of the annex on the TVD
interface: which enum of the AnimalTracing openAPI each code list derives from
(from the :animalTracingTerm of the property shapes), and, for the lists taken
from the Hilfsmittel, the counterparts of their values in the interface (from
src/rdf/mappings/animaltracing.ttl).

The helpers come from generate_shacl_docs.py, so the tables look and link like
those of the chapter on code lists.
"""

import argparse
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import SH

from generate_shacl_docs import (build_grid_table, code, code_list_label, code_list_slug,
                                 get_localized_value, natural_key, sanitize_cell)

SCHEMA = Namespace("http://schema.org/")
ANIMAL_TRACING_TERM = URIRef("https://agriculture.ld.admin.ch/eCH-0309/1/animalTracingTerm")

TRANSLATIONS = {
    "en": {
        "code_list": "Code list", "enum": "Enum of the interface",
        "enums_caption": "Enums of the TVD interface from which the code lists take their codes.",
        "code": "Code", "name": "Name", "counterparts": "TVD interface",
        "caption": "Corresponding values of the code list {name} in the TVD interface.",
    },
    "de": {
        "code_list": "Wertebereich", "enum": "Enumeration der Schnittstelle",
        "enums_caption": "Enumerationen der TVD-Schnittstelle, aus denen die Wertebereiche ihre Codes beziehen.",
        "code": "Code", "name": "Name", "counterparts": "TVD-Schnittstelle",
        "caption": "Entsprechungen der Werte des Wertebereichs {name} in der TVD-Schnittstelle.",
    },
    "fr": {
        "code_list": "Domaine de valeurs", "enum": "Énumération de l'interface",
        "enums_caption": "Énumérations de l'interface de la BDTA dont les domaines de valeurs tirent leurs codes.",
        "code": "Code", "name": "Nom", "counterparts": "Interface de la BDTA",
        "caption": "Équivalents des valeurs du domaine de valeurs {name} dans l'interface de la BDTA.",
    },
    "it": {
        "code_list": "Elenco di codici", "enum": "Enumerazione dell'interfaccia",
        "enums_caption": "Enumerazioni dell'interfaccia della BDTA da cui gli elenchi di codici traggono i loro codici.",
        "code": "Codice", "name": "Nome", "counterparts": "Interfaccia della BDTA",
        "caption": "Equivalenti dei valori dell'elenco di codici {name} nell'interfaccia della BDTA.",
    },
}


def derived_enums(shapes):
    """(code list, enum) for every property shape that restricts its values to a
    code list and names the enum of the interface the list derives from."""
    pairs = set()
    for prop, enum in shapes.subject_objects(ANIMAL_TRACING_TERM):
        for node in shapes.objects(prop, SH.node):
            for nested in shapes.objects(node, SH.property):
                if shapes.value(nested, SH.path) == SCHEMA.inCodeSet:
                    pairs.add((shapes.value(nested, SH.hasValue), str(enum)))
    return pairs


def annex(data, shapes, mappings, lang, trans):
    lines = []
    list_link = lambda cl: f"[{sanitize_cell(code_list_label(data, data, cl, lang))}](#sec-{code_list_slug(cl)})"

    rows = [[list_link(cl), code(enum)]
            for cl, enum in sorted(derived_enums(shapes),
                                   key=lambda p: code_list_label(data, data, p[0], lang).lower())]
    lines.extend(build_grid_table([trans["code_list"], trans["enum"]], rows, [40, 40]))
    lines.append("")
    lines.append(f": {trans['enums_caption']} {{#tbl-animaltracing-enums tbl-colwidths=\"[45,55]\"}}")
    lines.append("")

    by_list = {}
    for value in set(mappings.subjects(ANIMAL_TRACING_TERM, None)):
        for code_list in data.objects(value, SCHEMA.inCodeSet):
            by_list.setdefault(code_list, []).append(value)

    for code_list in sorted(by_list, key=lambda cl: code_list_label(data, data, cl, lang).lower()):
        rows = []
        longest = 0
        for value in sorted(by_list[code_list], key=lambda v: natural_key(data.value(v, SCHEMA.codeValue) or "")):
            code_value = str(data.value(value, SCHEMA.codeValue))
            longest = max(longest, len(code_value))
            terms = sorted(str(t) for t in mappings.objects(value, ANIMAL_TRACING_TERM))
            rows.append([f"[{code(code_value)}]({value})",
                         sanitize_cell(get_localized_value(data, value, [SCHEMA.name], lang) or ""),
                         # one counterpart per line: a Markdown hard line break
                         "\\\n".join(code(t) for t in terms)])
        lines.extend(build_grid_table([trans["code"], trans["name"], trans["counterparts"]], rows, [20, 30, 45]))
        lines.append("")
        # A code cannot wrap, so the code column is as wide as the longest code;
        # the interface column holds names like EnumCattleNotificationType.Slaughtering.
        code_width = min(30, max(14, round(longest * 1.15) + 2))
        widths = f"[{code_width},{55 - code_width},45]"
        label = sanitize_cell(code_list_label(data, data, code_list, lang))
        lines.append(f": {trans['caption'].format(name=label)} "
                     f"{{#tbl-animaltracing-{code_list_slug(code_list)} tbl-colwidths=\"{widths}\"}}")
        lines.append("")
    return lines


def main():
    parser = argparse.ArgumentParser(description="Generate the annex on the TVD interface.")
    parser.add_argument("-c", "--codelists", required=True, help="Code lists (.ttl)")
    parser.add_argument("-s", "--shapes", required=True, help="SHACL shapes of the data model (.ttl)")
    parser.add_argument("-m", "--mappings", required=True, help="Counterparts in the interface (.ttl)")
    parser.add_argument("-d", "--docs_dir", required=True, help="Docs directory containing language subdirectories")
    args = parser.parse_args()

    data = Graph().parse(args.codelists, format="turtle")
    shapes = Graph().parse(args.shapes, format="turtle")
    mappings = Graph().parse(args.mappings, format="turtle")

    docs_dir = Path(args.docs_dir)
    for lang, trans in TRANSLATIONS.items():
        if not (docs_dir / lang).is_dir():
            continue
        with open(docs_dir / lang / "animaltracing.md", "w", encoding="utf-8") as f:
            f.write("\n".join(annex(data, shapes, mappings, lang, trans)))


if __name__ == "__main__":
    main()
