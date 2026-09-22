"""Complete a PlantUML class diagram drawn by SHACL Play.

Two things the drawing misses, both because SHACL Play reads the shapes graph
alone and decides how to render a reference from the target shape's own
constraints:

1. rdfs:subClassOf axioms live in the ontology, so generalizations are never
   drawn at all and a subclass without property shapes ends up isolated.
2. A reference whose target shape declares no constraints is emitted as a box
   attribute rather than an association, so the same relation is drawn two
   different ways depending on how richly the *other* class happens to be
   described. Only references to a drawn class are rewritten here, which leaves
   literal attributes (sh:datatype) untouched.

The class titles SHACL Play emits carry the target class in parentheses, e.g.
`Class ":EquidShape (:Equid)"`, which is what both rewrites match against.
"""

import argparse
import re
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import RDFS

CLASS_RE = re.compile(r'^Class\s+"(?P<title>[^"]+)"')
TARGET_RE = re.compile(r"\(([^)]+)\)\s*$")
ATTRIBUTE_RE = re.compile(
    r'^"(?P<source>[^"]+)"\s*:\s*\+(?P<property>\S+)\s*:\s*(?P<type>\S+)\s*\[(?P<cardinality>[^\]]+)\]\s*$'
)


def local_name(term):
    """The part of an IRI or QName after the last '/', '#' or ':'."""
    return str(term).rsplit("#", 1)[-1].rsplit("/", 1)[-1].rsplit(":", 1)[-1]


def collect_titles(lines):
    """Maps a drawn class's local name to the PlantUML title that denotes it."""
    titles = {}
    for line in lines:
        match = CLASS_RE.match(line)
        if match:
            target = TARGET_RE.search(match.group("title"))
            if target:
                titles[local_name(target.group(1))] = match.group("title")
    return titles


def as_association(line, titles):
    """Rewrites an object-typed box attribute as an association, or returns None."""
    match = ATTRIBUTE_RE.match(line)
    if not match:
        return None
    target = titles.get(local_name(match.group("type")))
    if target is None or match.group("source") not in titles.values():
        return None
    return (
        f'"{match.group("source")}" --> "{target}" : '
        f'{match.group("property")} [{match.group("cardinality")}] '
    )


def generalizations(graph, titles):
    """PlantUML generalizations for rdfs:subClassOf axioms between drawn classes."""
    lines = set()
    for sub, sup in graph.subject_objects(RDFS.subClassOf):
        sub_name, sup_name = local_name(sub), local_name(sup)
        if sub_name != sup_name and sub_name in titles and sup_name in titles:
            lines.add(f'"{titles[sup_name]}" <|-- "{titles[sub_name]}" ')
    return sorted(lines)


def main():
    parser = argparse.ArgumentParser(description="Complete a SHACL Play PlantUML diagram.")
    parser.add_argument("-i", "--input", required=True, help="PlantUML file (.puml), edited in place")
    parser.add_argument("-o", "--ontology", required=True, help="Ontology file (.ttl) declaring rdfs:subClassOf")
    args = parser.parse_args()

    graph = Graph(bind_namespaces="none")
    graph.parse(args.ontology, format="turtle")

    puml = Path(args.input)
    lines = puml.read_text(encoding="utf-8").splitlines()
    titles = collect_titles(lines)

    lines = [as_association(line, titles) or line for line in lines]

    extra = generalizations(graph, titles)
    if extra:
        for index, line in enumerate(lines):
            if line.startswith("hide circle") or line.startswith("@enduml"):
                lines[index:index] = extra
                break

    puml.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
