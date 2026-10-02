# eCH-0309 – Animal movement data

The Hilfsmittel "eCH-0309 – Tierverkehrsdaten" describes the data of the Swiss
animal movement database (TVD) at a semantic level. Births, changes of location,
deaths and slaughters of defined livestock species have to be reported, among
other reasons for the traceability of animal diseases and for calculating animal
populations.

This repository maintains the data model as SHACL and SKOS, and generates the
*Datenmodell* and *Wertebereiche* chapters of the document from it, in German,
French and English.

## Quick start

```bash
make setup    # virtualenv, Python dependencies, ROBOT
make test     # syntax, prefixes, translations, one test per shape and property
make docs     # renders docs/ into build/docs/ as HTML, PDF, Word and Markdown
```

On its first run `make docs` additionally downloads SHACL Play, PlantUML and a
portable Java 17 into `venv/`. The rendered document then sits at
`build/docs/de/index.pdf`.

## Where things are

| Path | Contents |
|---|---|
| `src/rdf/shapes/model.shacl.ttl` | The data model: classes, attributes, relationships, cardinalities, and every label in de/en/fr/it |
| `src/rdf/ontology/model.owl.ttl` | Declarations only — classes, properties, taxonomy. All constraints live in the shapes |
| `src/rdf/data/code_lists.skos.ttl` | The Wertebereiche as SKOS, maintained by hand |
| `src/rdf/data/glossary.skos.ttl` | The glossary for Anhang C |
| `src/rdf/prefixes.ttl` | The binding prefix list; `tests/test_prefixes.py` enforces it everywhere |
| `docs/de`, `docs/fr`, `docs/en` | One `index.qmd` each with the hand-written text; the other `.md` files are generated |
| `src/python/utils/` | The generators, see below |
| `tests/` | Pytest. `fixtures/example_model.ttl` is a non-normative example graph, so the shapes are validated against something rather than nothing |


## How the document is produced

`make docs` generates the derived chapters and then renders with Quarto:

| Generator | Produces |
|---|---|
| `generate_shacl_docs.py` | `docs/*/entities.md` — the entity tables, from the shapes |
| `generate_code_list_docs.py` | `docs/*/code-lists.md` — one table per code list |
| `generate_glossary_docs.py` | `docs/*/glossary.md` |
| SHACL Play → PlantUML → `patch_uml_diagram.py` | `docs/assets/img/uml.png` — the class diagram |

## Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the naming conventions and for
the files synchronised from the
[semantic-web-template](https://github.com/blw-ofag-ufag/semantic-web-template).

## Contact

Do you have questions? Please do not hesitate to contact us at [agridata.ch@blw.admin.ch](mailto:agridata.ch@blw.admin.ch), open an [issue in this repository](../../issues), or directly submit a [Request for Change (RFC) via the official eCH feedback form](https://ech.ch/de/ech-standards/standardisierungsprozess/request-change-rfc).