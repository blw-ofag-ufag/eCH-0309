"""Complete a PlantUML class diagram drawn by SHACL Play.

SHACL Play reads the shapes graph alone, and decides how to render a reference
from the target shape's own constraints. Three consequences follow, one per pass
below:

1. `promote_references` -- a reference whose target shape declares no
   constraints of its own is emitted as a box attribute instead of an
   association, so the same kind of relation is drawn two different ways
   depending on how richly the *other* class happens to be described.
2. `demote_value_domains` -- a code list class is drawn as a class in its own
   right whenever some coded attribute is mandatory, and as an attribute
   otherwise. A Wertebereich is a value domain, not an entity, so it is drawn
   the way UML draws an enumeration-typed attribute: on the class that uses it.
   The lists themselves have their own chapter in the document.
3. `add_generalizations` -- rdfs:subClassOf axioms live in the ontology, which
   SHACL Play never reads, so a subclass with no property shapes of its own
   ends up as an isolated box.

The passes are applied in that order and do not commute: `promote_references`
has to see the box attributes before `demote_value_domains` rewrites references
back into that form, and `add_generalizations` has to see the final set of drawn
classes so that it does not link a class that is no longer there.

SHACL Play names a class `":EquidShape (:Equid)"` -- the shape, then its target
class in parentheses -- and that title is what every pass matches against.
"""

import argparse
import re
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import RDF, RDFS, SKOS

CLASS_RE = re.compile(r'^Class\s+"(?P<title>[^"]+)"')
TARGET_RE = re.compile(r"\(([^)]+)\)\s*$")
ASSOCIATION_RE = re.compile(
    r'^"(?P<source>[^"]+)"\s*-->\s*"(?P<target>[^"]+)"\s*:\s*(?P<label>.+?)\s*$')
ATTRIBUTE_RE = re.compile(
    r'^"(?P<source>[^"]+)"\s*:\s*\+?(?P<property>\S+)\s*:\s*(?P<type>\S+)\s*\[(?P<cardinality>[^\]]+)\]\s*$')
# An association label lists one property and its cardinality, and may list
# several separated by PlantUML's line break. SHACL Play writes the escape
# <U+00A0> between name and cardinality, which PlantUML renders as a
# non-breaking space.
LINE_BREAK = "\\l"
MEMBER_RE = re.compile(r'^\s*(?P<property>\S+?)(?:<U\+00A0>|\s)+\[(?P<cardinality>[^\]]+)\]')


def local_name(term):
    """The part of an IRI, QName or class title after the last '/', '#' or ':'."""
    return str(term).rsplit("#", 1)[-1].rsplit("/", 1)[-1].rsplit(":", 1)[-1]


def class_title(line):
    """The title of the class this line declares, or None if it declares none."""
    match = CLASS_RE.match(line)
    return match.group("title") if match else None


def drawn_classes(lines):
    """Maps the local name of every drawn target class to the title denoting it.

    Only titles naming a target class in parentheses count: a bare
    `Class ":Genus"` is a value domain SHACL Play invented, not a shape.
    """
    titles = {}
    for line in lines:
        title = class_title(line)
        if title:
            target = TARGET_RE.search(title)
            if target:
                titles[local_name(target.group(1))] = title
    return titles


def value_domains(path):
    """Local names of the classes that type a skos:Concept, i.e. the Wertebereiche."""
    if not path:
        return set()
    graph = Graph(bind_namespaces="none")
    graph.parse(path, format="turtle")
    return {
        local_name(concept_class)
        for concept in graph.subjects(RDF.type, SKOS.Concept)
        for concept_class in graph.objects(concept, RDF.type)
        if concept_class != SKOS.Concept
    }


def promote_references(lines, domains):
    """Draws an object-typed box attribute as an association where it points at a
    drawn class. Literal attributes and value domains are left as they are."""
    titles = drawn_classes(lines)
    promoted = []
    for line in lines:
        match = ATTRIBUTE_RE.match(line)
        target = titles.get(local_name(match.group("type"))) if match else None
        if (match is None
                or target is None
                or local_name(match.group("type")) in domains
                or match.group("source") not in titles.values()):
            promoted.append(line)
            continue
        promoted.append(
            f'"{match.group("source")}" --> "{target}" : '
            f'{match.group("property")} [{match.group("cardinality")}] ')
    return promoted


def demote_value_domains(lines, domains):
    """Draws every reference to a value domain as a box attribute, and drops the
    classes SHACL Play invented for those domains."""
    demoted = []
    for line in lines:
        title = class_title(line)
        if title and local_name(title) in domains:
            continue

        match = ASSOCIATION_RE.match(line)
        if match and local_name(match.group("target")) in domains:
            members = []
            for part in match.group("label").split(LINE_BREAK):
                member = MEMBER_RE.match(part)
                if member:
                    members.append(
                        f'"{match.group("source")}" : {member.group("property")} : '
                        f'{match.group("target")} [{member.group("cardinality")}] ')
            # A label this pass cannot read is kept as it was, rather than lost.
            demoted.extend(members or [line])
            continue

        demoted.append(line)
    return demoted


def add_generalizations(lines, ontology):
    """Adds a generalization for every rdfs:subClassOf between two drawn classes."""
    titles = drawn_classes(lines)
    generalizations = sorted({
        f'"{titles[local_name(parent)]}" <|-- "{titles[local_name(child)]}" '
        for child, parent in ontology.subject_objects(RDFS.subClassOf)
        if local_name(child) != local_name(parent)
        and local_name(child) in titles and local_name(parent) in titles
    })
    if not generalizations:
        return lines

    patched = list(lines)
    for index, line in enumerate(patched):
        if line.startswith("hide circle") or line.startswith("@enduml"):
            patched[index:index] = generalizations
            break
    return patched


def main():
    parser = argparse.ArgumentParser(description="Complete a SHACL Play PlantUML diagram.")
    parser.add_argument("-i", "--input", required=True, help="PlantUML file (.puml), edited in place")
    parser.add_argument("-o", "--ontology", required=True, help="Ontology file (.ttl) declaring rdfs:subClassOf")
    parser.add_argument("-c", "--code-lists", help="SKOS file (.ttl) whose concept types are value domains")
    args = parser.parse_args()

    ontology = Graph(bind_namespaces="none")
    ontology.parse(args.ontology, format="turtle")
    domains = value_domains(args.code_lists)

    puml = Path(args.input)
    lines = puml.read_text(encoding="utf-8").splitlines()

    lines = promote_references(lines, domains)
    lines = demote_value_domains(lines, domains)
    lines = add_generalizations(lines, ontology)

    puml.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
