import pytest
from pathlib import Path
from rdflib import Graph
from pyshacl import validate

def test_model_shacl():
    """
    Checks if the non-normative example graph tests/fixtures/example_model.ttl
    conforms to src/rdf/shapes/model.shacl.ttl.

    The example graph is kept outside src/rdf/data/ on purpose, so that it is
    never merged into build/rdf/03-processed.ttl and never published to LINDAS.
    Without it, the shapes would be validated against an empty graph and every
    generated test in tests/test_shacl.py would pass vacuously.

    src/rdf/ontology/model.owl.ttl must be passed as the ontology graph: it
    carries :Equid rdfs:subClassOf :Animal, which sh:class traverses when it
    checks whether an :Equid is an acceptable value for :animal. RDFS inference
    is switched on in addition, mirroring the `robot reason` stage of the build.
    """
    data_path = Path("tests/fixtures/example_model.ttl")
    shapes_path = Path("src/rdf/shapes/model.shacl.ttl")
    ontology_path = Path("src/rdf/ontology/model.owl.ttl")

    if not data_path.exists():
        pytest.skip(f"Data file not found: {data_path}")
    if not shapes_path.exists():
        pytest.skip(f"Shapes file not found: {shapes_path}")

    data_graph = Graph().parse(data_path, format="turtle")
    shapes_graph = Graph().parse(shapes_path, format="turtle")
    ont_graph = Graph().parse(ontology_path, format="turtle")

    conforms, report_graph, report_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        ont_graph=ont_graph,
        inference="rdfs",
        meta_shacl=False,
        advanced=True,
        debug=False
    )

    if not conforms:
        pytest.fail(f"Example graph does not conform to SHACL shapes:\n\n{report_text}", pytrace=False)
