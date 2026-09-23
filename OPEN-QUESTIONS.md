# Offene Fragen für die Fachgruppe

Fragen, die beim Überführen des Hilfsmittels eCH-0309 nach SHACL/SKOS aufgetaucht
sind und die mit den Autorinnen und Autoren des Word-Dokuments geklärt werden
müssen. Jeder Eintrag nennt die Quelle, wo die Frage im Repository kodiert ist und
was sich je nach Antwort ändert.

Die Prüfkommentare sind mit ihrem Kürzel aus dem Word-Dokument zitiert
(z.B. `[SB14]`). Sie stammen aus `word/comments.xml` des Hilfsmittels und sind
dort alle noch offen.

---

## A. Modell und Klassen

### A1. Ist der Equideneigentümer zwingend eine rechtliche Einheit mit UID?

> `[SB14]` «Equideneigentümer sind nicht zwingend legalUnits nach UID-Register. Es
> ist nicht unbedingt korrekt, diese hier so zu nennen.»

Vier Quellen sagen das Gegenteil: der Objektkatalog (`Eigentümer oder Eigentümerin
| 1 | uid`), Kapitel 3.1.1, Kapitel 3.1.4 («…des verantwortlichen
Equideneigentümers (LegalUnit)») und die openAPI, in der `uid` in
`EquidDetailsOwnerResponse`, `EquidOwnershipListV1LegalUnitResponse` und
`LegalUnitBaseResponse` ein Pflichtfeld ist.

**Kodiert als** `:owner 1..1 :LegalUnit`; die vollständige Beweislage steht als
Kommentar über `:EquidShape` in `src/rdf/shapes/model.shacl.ttl`.

**Konsequenz** Wird `[SB14]` bestätigt, entfällt entweder `sh:minCount` auf
`:owner`, oder es braucht eine eigene Klasse `:EquidOwner` neben `:LegalUnit` –
letzteres ändert einen versionsgebundenen Namensraum und muss vor der
Publikation entschieden sein.

### A2. Sind alle örtlichen Einheiten Tierhaltungen?

> `[SB9]` «In der TVD werden auch ÖE geführt, die nicht Tierhaltungen sind – das
> müssen wir präzisieren. ÖE die eine TVD-Nummer haben, werden in der TVD
> Tierhaltungen genannt (auch wenn sie eine andere Betriebsform haben).»

**Kodiert als** der Kommentar auf `:LocalUnitShape`, der Kapitel 3.1.2 wörtlich
übernimmt und damit auch dessen Unschärfe.

**Konsequenz** Braucht `:LocalUnit` eine Unterklasse für Tierhaltungen, oder
genügt das Merkmal «hat eine TVD-Nummer»?

### A3. Wie hängen örtliche Einheit und Tierhaltender zusammen?

Der Objektkatalog führt für «örtliche Einheit» keine einzige Zeile – der ganze
Block verweist auf eCH-0261. Die Beziehung stammt deshalb aus Kapitel 3.1.2, das
von der **rechtlichen Einheit** spricht, nicht vom Tierhaltenden. eCH-0108 führt
die Verbindung als optionales Merkmal `mainUid` der Stammdaten der örtlichen
Einheit.

**Kodiert als** `:animalKeeper 0..1 :AnimalKeeper` ohne `:sourceTerm`.

**Konsequenz** Soll stattdessen `:LocalUnit → :LegalUnit [1..1]` modelliert
werden, was Kapitel 3.1.2 wörtlich entspricht?

### A4. Meldende Person: Begriff oder Klasse?

> `[DJ21]` «Meldende Person ist kein öffentlicher Bestandteil der Meldung.»

Kapitel 3.1.3 definiert den Begriff, im Objektkatalog ist das Attribut
«Meldender» in beiden Meldungsklassen durchgestrichen.

**Kodiert als** Glossarbegriff `term:reportingPerson`, keine Klasse.

### A5. Stammbetrieb: Begriff oder Beziehung?

Kapitel 3.1.1 beschreibt den Stammbetrieb für Rinder, der Objektkatalog führt ihn
nicht.

**Kodiert als** Glossarbegriff `term:homeHolding`.

**Konsequenz** Soll `:Animal` eine Beziehung `0..1` zu einer örtlichen Einheit
für den Stammbetrieb erhalten?

### A6. Fehlt bei den Equiden die Art?

> `[TS]` «Bei den Equiden gibt's ja noch die Art (Pferd, Esel, Pony, …)»

Die openAPI führt `EquidSpecies` mit `Horse`, `Donkey`, `Mule`, `Hinny`.

**Konsequenz** Ein zusätzliches Attribut auf `:Equid` und ein weiterer
Wertebereich.

---

## B. Wertebereiche

### B1. Doppelte Seuchenstatus-Werte

«gesperrt», «frei» und «Nicht getestet» stehen in Tabelle 10 und Tabelle 11 und
sind deshalb zweimal modelliert, einmal je Schema.

**Kodiert als** `localunithealthstatus:` und `animalhealthstatus:` mit je eigenen
Konzepten.

**Konsequenz** Ein gemeinsames Schema mit dem zusätzlichen Wert «geimpft» wäre
kompakter, weicht aber von der Darstellung im Dokument ab.

### B2. Typ und Status gegen die Schnittstelle

Die Schnittstelle kennt keine Typ/Status-Paare, sondern die Felder `BvdState`,
`BvdRisk` und `FootrotState`; deren Werte liefert `GetEnumeration`, nicht die
Spezifikation. «Seuche» hat überhaupt keinen Wertebereich im Dokument.

**Konsequenz** Bleibt das generische Modell (Typ, Seuche, Status), oder folgt das
Modell der Schnittstelle mit einem Status je Seuche?

### B3. Tagesaufenthalt

> `[JD26]` «Ist kein Bewegungstyp, sondern eine Kombination von Zugang und Abgang
> am selben Tag. Dieser Bewegungstyp kann jedoch über das UI und Schnittstelle
> gemeldet werden. Was wollen wir damit machen?»

**Kodiert als** `notificationtype:DayStay`, bewusst ohne `:animalTracingTerm`.

### B4. Ein Bewegungstyp, der nicht mehr gemeldet werden kann

> `[JD27]` «Kann nicht mehr gemeldet werden als Bewegungstyp. Ist aber in den
> Tiergeschichten vorhanden als Bewegungstyp. Was wollen wir damit?»

Auf welche Zeile von Tabelle 8 sich der Kommentar bezieht, ist aus der
Textkonversion nicht eindeutig – im Word-Dokument nachschauen.

### B5. «Diese Werte sind in dieser Form nicht existent»

> `[DJ25]` «Diese Werte sind in dieser Form nicht existent. Vorschlag: Verweis auf
> Agis-Register und englische Werte übernehmen.»

Das entspricht dem gewählten Vorgehen: die Werte stammen aus der openAPI, die
deutschen Bezeichnungen aus den Wertebereichstabellen. Zu klären ist, auf welche
Tabelle sich der Kommentar bezieht und ob das AGIS-Register die Quelle sein soll.

### B6. Durchgestrichene Werte

Im Word-Dokument sind durchgestrichen: «Biene» und «Fisch» in Tabelle 2, Tabelle 5
(Status, lebendig/tot) vollständig samt zugehörigem Attribut der Klasse
«Einzeltier», sowie «Meldender» in beiden Meldungsklassen.

> `[DJ19]` «Nicht mehr vorhanden in neuer Schnittstelle. Kann aus Geburts- und
> Todesdatum berechnet werden.»

**Kodiert als** weggelassen. **Konsequenz** Bestätigen, dass die Streichungen
endgültig sind.

### B7. Sentinel-Werte der Schnittstelle

`Unknow` und `Others` aus `EnumGenus`, `NotDefined` aus `EnumAnimalTypeOfUse` und
`Undefined` aus `EquidTypeOfUsage` stehen in keiner Tabelle des Hilfsmittels und
sind weggelassen, damit beide Dokumente dieselben Werte führen.

**Konsequenz** Für ein beschreibendes Hilfsmittel richtig; sollen die Listen je
zur Validierung von Echtdaten dienen, müssen die Sentinel-Werte zurück.

### B8. Mängel in der Schnittstelle selbst

`EnumGenus` enthält den Tippfehler `Unknow`. `CattleBreed` (67 Werte, englisch)
und `EnumCattleRace` (68 Werte, deutsch) sind dieselbe Liste zweimal, mit
unterschiedlicher Anzahl.

### B9. Fehlende französische und italienische Bezeichnungen

Für die sechs aus der openAPI erzeugten Wertebereiche gibt es keine
Übersetzungen: die openAPI führt nur englische Bezeichner, die Tabellen des
Hilfsmittels nur deutsche. Die vier aus dem Dokument stammenden Listen sind
vollständig viersprachig.

**Konsequenz** Entweder über `GetEnumeration` der AnimalTracing-Schnittstelle
beziehen – deren `EnumerationValue` liefert `TranslatedText` je Sprache – oder
übersetzen lassen. Für die Schnittstelle fehlt derzeit der Zugang.

### B11. Rasse: eine Liste oder vier?

Der Objektkatalog führt «Rasse» auf der Klasse «Einzeltier» als Wertebereich,
eine Wertebereichstabelle dazu gibt es nicht. Die openAPI führt vier Listen:
`CattleBreed` (67), `SheepBreed` (48), `GoatBreed` (20) und `EquidBreed` (198) –
dazu `EnumCattleRace` (68), dieselbe Rinderliste auf Deutsch, siehe B8.

**Kodiert als** noch nicht modelliert; das Attribut fehlt auf `:Animal`.

**Konsequenz** Ein gemeinsames Schema über alle Gattungen oder eines je Gattung?
Und welche der beiden Rinderlisten gilt?

### B12. Tierkategorie

Der Objektkatalog führt «Tierkategorie» auf «Gruppenmeldung» (Kardinalität 1)
und auf «Gesundheitsstatus Standort» als Wertebereich. Eine Wertebereichstabelle
fehlt, und in der openAPI ist kein eindeutiges Gegenstück erkennbar.

**Kodiert als** noch nicht modelliert.

**Konsequenz** Worin unterscheidet sich die Tierkategorie von der Nutztierart?

### B13. Seuche

«Seuche» ist auf beiden Gesundheitsstatus-Klassen als Wertebereich geführt, ohne
Tabelle. Die Schnittstelle kennt stattdessen Felder je Seuche – `BvdState`,
`BvdRisk`, `FootrotState` – siehe B2.

**Kodiert als** noch nicht modelliert.

**Konsequenz** Braucht es eine Seuchenliste, und wenn ja, aus welcher Quelle?

### B10. Grössenkategorie ohne Wertebereichstabelle

Der Begriff kommt im Hilfsmittel genau einmal vor, als Attributzeile der
Subklasse «Equiden». Die beiden Werte stammen allein aus `EnumEquidWithersClass`;
die Bezeichnungen nennen die Widerristhöhe, weil das Enum `WithersClass` heisst
und Kapitel 3.1.4 «Widerristhöhe» unter den Equidenattributen führt.

---

## C. Quellen, Versionen und Mapping

### C1. Welche Fassung ist massgebend?

> `[SB]` «stimmt diese Version? oder ist die openAPI aktueller?»
> `[DJ]` «Sinnvollerweise verwenden wir die Versionen, die ab dem Oktober 2026
> gültig sein werden.» `[SB]` «fände ich auch sehr sinnvoll»

Kapitel 1.3 nennt «AnimalTracing v1.32, sowie der openAPI-Spezifikation v. x.xx» –
die Versionsnummer ist im Dokument selbst ein Platzhalter.

**Kodiert als** Die Wertebereiche tragen auf der Sammlung `:codeLists` die
Quell-URL, Titel und Version der abgerufenen Spezifikation und das Abrufdatum.

### C2. Das Mapping ist noch nicht gemacht

> `[LS7]` «Mapping muss noch gemacht werden»

**Kodiert als** `:sourceTerm`, `:animalTracingTerm` und `:echTerm` auf jeder
Klasse, jeder Eigenschaft und jedem Wertebereichskonzept.

### C3. openAPI oder technische Servicebeschreibung?

`:animalTracingTerm` nennt heute Schemanamen der openAPI, die noch in Entwicklung
ist. Aktueller Release ist die technische Servicebeschreibung v1.32.1, die ihre
Wertelisten über `GetCodes` und `GetEnumeration` ausliefert statt sie abzudrucken.

**Konsequenz** Sollen die Verweise auf ServiceOperations und Datentypen der
Servicebeschreibung umgestellt werden? Sinnvoll erst nach dem openAPI-Release.

### C4. Namensraum der Wertebereiche

Die Wertebereiche liegen unter `https://agriculture.ld.admin.ch/eCH-0309/1/`.
eCH-0265 legt seine Kulturlisten dagegen unter `…/crops/` ab, ausserhalb des
Namensraums des Standards, weil sie geteilte Referenzdaten der Fachdomäne sind.

**Konsequenz** Gehören die TVD-Wertebereiche in einen geteilten TVD-Namensraum?
Nachträglich ist das ein Bruch.

### C5. Zustand ab Oktober 2026 und Januar 2027

> `[JD16]` «Änderungen für 2027. Hier einfliessen lassen.»
> `[JD28]` «Aktualisieren für den Zustand ab 2027»
> `[DJ29]` «Das ändert per Oktober 2026 und Januar 2027 seitens blv. Stimmt nicht
> mit dem zukünftigen IST überein.»
> `[YB12]` «Ab 2027 dann auch für Schafe und Ziegen möglich»

Das Hilfsmittel bildet das IST ab. Zu klären, welcher Stichtag gilt.

---

## D. Text und Abbildungen

### D1. Bezug des landwirtschaftlichen Informationssystems zum UID-Register

> `[SB10]` «das ist so nicht korrekt, die KLIS sind BUR angebunden und übernehmen
> heute (ausser der BUR-Nr und der UID) keine Daten.»

Der beanstandete Satz steht heute in der Beschreibung von `:LegalUnitShape`, weil
er aus Kapitel 3.1.1 übernommen wurde. **Muss korrigiert oder entfernt werden.**

### D2. Abbildung Systemlandschaft

> `[SB]` «streichen (inkl. Abbildung, diese ist veraltet)» `[LS]` «Wird ersetzt
> (Systemlandkarte)»

**Kodiert als** Der Text ist übernommen, der Verweis auf «Abbildung 1» entfernt;
ein Kommentar in den drei `index.qmd` markiert die Stelle für die neue Abbildung.

### D3. Gattung oder Nutztierart?

> `[SB8]` «in der TVD Verordnung wird Gattung verwendet»

**Kodiert als** Schema `genus:` mit der Bezeichnung «Nutztierart».

### D4. Redaktionelles

> `[YB11]` «Unten wird Eigentümer oder Eigentümerin ausgeschrieben hier nicht – im
> gesamten Dokument einheitlich machen»
> `[SB13]` «was sind TVD-Tiere?»
> `[YB15]` «Eher Einstallungsmeldung»
> `[YB24]` «Ist hier der HKB gemeint?»
> `[DJ20]`, `[DJ23]` «Benötigt, oder aus dem Kontext gegeben?» (Nutztierart auf
> den Meldungsklassen)
> `[DJ22]` «Funktioniert nicht mit den Equidenmeldungen.» (Herkunft)
> `[SB1]` «entweder nach vorne oder streichen»

### D5. Die Zusammenfassung fehlt

Die Zusammenfassung des Word-Dokuments ist noch der Platzhalter
`<Kurze Zusammenfassung des Zwecks des Dokuments>`. Im Hilfsmittel steht derzeit
ersatzweise der Satz aus Kapitel 1.2.

---

## Bereits umgesetzt

| Kommentar | Umsetzung |
|---|---|
| `[JD18]` Einzeltiermeldung 1..\* : 1, Aquakulturen entfernen | `:animal 1..1` auf `:AnimalNotificationShape`; keine Aquakulturklasse |
| `[DJ21]` Meldende Person nicht öffentlich | Kein Attribut, Glossarbegriff |
| `[DJ19]` Status aus Geburts- und Todesdatum berechenbar | Attribut und Wertebereich weggelassen |
