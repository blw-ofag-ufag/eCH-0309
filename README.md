# eCH-0309 - Tierverkehrsdaten

Das Hilfsmittel "eCH-0309 - Tierverkehrsdaten" beschreibt die Daten der Tierverkehrsdatenbank (TVD) auf semantischer Ebene. Geburten, Standortwechsel, Tod und Schlachtungen von definierten Nutztierarten müssen unter anderem zur Rückverfolgbarkeit von Tierseuchen sowie der Berechnung von Tierbeständen gemeldet werden.

## Technische Hinweise

Das Datenmodell wird als SHACL-Shapes in `src/rdf/shapes/model.shacl.ttl` gepflegt und
als RDF-Graph nach [LINDAS](https://lindas.admin.ch/) publiziert. Die Dokumentation in
`docs/` wird daraus generiert.

Für die Verarbeitung des Graphen verwenden wir die ROBOT CLI, insbesondere wegen ihrer
Fähigkeit, den HermiT Reasoner auszuführen. Das UML-Diagramm des Datenmodells wird mit
SHACL Play aus den Shapes gezeichnet und mit PlantUML gerendert; die Wertebereiche werden
aus der openAPI-Spezifikation der TVD generiert.

## Offene Fragen

Fragen, die mit der Fachgruppe zu klären sind, sind als Issues erfasst – je eine
Frage, mit dem zugehörigen Prüfkommentar aus dem Word-Dokument und dem Hinweis,
wo die Entscheidung im Repository kodiert ist. Sie tragen die Label
[`data model`](../../issues?q=is%3Aissue+is%3Aopen+label%3A%22data+model%22) und
[`documentation`](../../issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation).

