"""Unit tests for src/python/utils/patch_uml_diagram.py.

The script rewrites the PlantUML that SHACL Play draws, and its output ends up
in the published document. Nothing else checks it, so each of its three passes
is pinned here against a small diagram rather than against the real build.
"""

import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path("src/python/utils/patch_uml_diagram.py")


@pytest.fixture(scope="module")
def patch():
    if not MODULE_PATH.exists():
        pytest.skip(f"Script not found: {MODULE_PATH}")
    spec = importlib.util.spec_from_file_location("patch_uml_diagram", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ANIMAL = '":AnimalShape (:Animal)"'
EQUID = '":EquidShape (:Equid)"'
LOCAL_UNIT = '":LocalUnitShape (:LocalUnit)"'

DIAGRAM = [
    "@startuml",
    f"Class {ANIMAL} ",
    f"Class {EQUID} ",
    f"Class {LOCAL_UNIT} ",
    'Class ":Genus" ',
    f'{ANIMAL} : :identifier  : xsd:string  [1..1]  ',
    f'{ANIMAL} : +:gender : :Gender [0..1] ',
    f'{EQUID} : +:localUnit : :LocalUnit [1..1] ',
    f'{ANIMAL} --> ":Genus" : :genus<U+00A0>[1..1]  ',
    f'{LOCAL_UNIT} --> ":Genus" : :genus<U+00A0>[1..1]  \\l:otherGenus<U+00A0>[0..1]  ',
    "hide circle",
    "@enduml",
]

DOMAINS = {"Genus", "Gender"}


def test_drawn_classes_ignores_invented_value_domain_classes(patch):
    """A bare `Class ":Genus"` names no shape, so it is not a drawn class."""
    titles = patch.drawn_classes(DIAGRAM)
    assert set(titles) == {"Animal", "Equid", "LocalUnit"}


def test_promote_turns_an_object_attribute_into_an_association(patch):
    result = patch.promote_references(DIAGRAM, DOMAINS)
    assert f'{EQUID} --> "{LOCAL_UNIT[1:-1]}" : :localUnit [1..1] ' in result


def test_promote_leaves_literal_attributes_alone(patch):
    result = patch.promote_references(DIAGRAM, DOMAINS)
    assert f'{ANIMAL} : :identifier  : xsd:string  [1..1]  ' in result


def test_promote_leaves_value_domain_attributes_alone(patch):
    """:Gender is a value domain, so :gender must not become an association."""
    result = patch.promote_references(DIAGRAM, DOMAINS)
    assert f'{ANIMAL} : +:gender : :Gender [0..1] ' in result


def test_demote_drops_the_value_domain_class(patch):
    result = patch.demote_value_domains(DIAGRAM, DOMAINS)
    assert not any(line.startswith('Class ":Genus"') for line in result)


def test_demote_turns_an_association_into_an_attribute(patch):
    result = patch.demote_value_domains(DIAGRAM, DOMAINS)
    assert f'{ANIMAL} : :genus : :Genus [1..1] ' in result


def test_demote_expands_every_property_of_a_shared_label(patch):
    """One association may carry several properties, separated by PlantUML's \\l."""
    result = patch.demote_value_domains(DIAGRAM, DOMAINS)
    assert f'{LOCAL_UNIT} : :genus : :Genus [1..1] ' in result
    assert f'{LOCAL_UNIT} : :otherGenus : :Genus [0..1] ' in result


def test_demote_keeps_a_label_it_cannot_read(patch):
    unreadable = [f'{ANIMAL} --> ":Genus" : something unparseable']
    assert patch.demote_value_domains(unreadable, DOMAINS) == unreadable


def test_generalizations_are_added_for_drawn_classes(patch, tmp_path):
    from rdflib import Graph
    ontology = tmp_path / "ontology.ttl"
    ontology.write_text(
        "@prefix : <https://agriculture.ld.admin.ch/eCH-0309/1/> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        ":Equid rdfs:subClassOf :Animal .\n"
        ":Absent rdfs:subClassOf :Animal .\n", encoding="utf-8")
    graph = Graph().parse(ontology, format="turtle")

    result = patch.add_generalizations(DIAGRAM, graph)
    assert f'{ANIMAL} <|-- {EQUID} ' in result
    assert not any("Absent" in line for line in result)
    assert result.index(f'{ANIMAL} <|-- {EQUID} ') < result.index("hide circle")


def test_value_domains_reads_the_concept_types(patch, tmp_path):
    code_lists = tmp_path / "code_lists.ttl"
    code_lists.write_text(
        "@prefix : <https://agriculture.ld.admin.ch/eCH-0309/1/> .\n"
        "@prefix genus: <https://agriculture.ld.admin.ch/eCH-0309/1/genus/> .\n"
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
        "genus:Cattle a skos:Concept, :Genus .\n", encoding="utf-8")
    assert patch.value_domains(code_lists) == {"Genus"}


def test_the_passes_compose(patch, tmp_path):
    """The three passes in the order main() applies them leave no value domain."""
    from rdflib import Graph
    ontology = tmp_path / "ontology.ttl"
    ontology.write_text(
        "@prefix : <https://agriculture.ld.admin.ch/eCH-0309/1/> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        ":Equid rdfs:subClassOf :Animal .\n", encoding="utf-8")

    lines = patch.promote_references(DIAGRAM, DOMAINS)
    lines = patch.demote_value_domains(lines, DOMAINS)
    lines = patch.add_generalizations(lines, Graph().parse(ontology, format="turtle"))

    assert not any(line.startswith('Class ":Genus"') for line in lines)
    assert not any("-->" in line and ":Genus" in line for line in lines)
    assert f'{ANIMAL} <|-- {EQUID} ' in lines
    assert sum(1 for line in lines if line.startswith("Class ")) == 3


def test_attribute_types_are_dropped(patch):
    """The type belongs in the entity table; the diagram keeps name and cardinality."""
    result = patch.drop_attribute_types([
        f'{ANIMAL} : :identifier  : xsd:string  [1..1]  ',
        f'{ANIMAL} : +:gender : :Gender [0..1] ',
        f'{ANIMAL} --> "{EQUID[1:-1]}" : :mother [0..1] ',
    ])
    assert result[0] == f'{ANIMAL} : :identifier [1..1] '
    assert result[1] == f'{ANIMAL} : :gender [0..1] '
    assert result[2] == f'{ANIMAL} --> "{EQUID[1:-1]}" : :mother [0..1] ', "associations untouched"


def test_titles_are_shortened_to_the_target_class(patch):
    result = patch.shorten_titles([f"Class {ANIMAL} ", f'{ANIMAL} <|-- {EQUID} '])
    assert result == ['Class ":Animal" ', '":Animal" <|-- ":Equid" ']
