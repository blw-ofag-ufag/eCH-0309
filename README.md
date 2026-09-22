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

