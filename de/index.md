# Hilfsmittel Tierverkehrsdaten

19. Oktober 2026

- [Hinweis](#sec-note)
- [<span class="toc-section-number">1</span>
  Einleitung](#sec-introduction)
  - [<span class="toc-section-number">1.1</span> Status](#sec-status)
  - [<span class="toc-section-number">1.2</span>
    Anwendungsgebiet](#sec-scope-of-application)
  - [<span class="toc-section-number">1.3</span> Das Tiermeldewesen in
    der Schweiz](#sec-animal-movement-reporting)
  - [<span class="toc-section-number">1.4</span>
    Verweise](#sec-references)
- [<span class="toc-section-number">2</span>
  Namespaces](#sec-namespaces)
- [<span class="toc-section-number">3</span>
  Datenmodell](#sec-data-model)
  - [<span class="toc-section-number">3.1</span>
    Einzeltier](#sec-nodeshape-animalshape)
  - [<span class="toc-section-number">3.2</span>
    Equide](#sec-nodeshape-equidshape)
  - [<span class="toc-section-number">3.3</span> Gesundheitsstatus
    Einzeltier](#sec-nodeshape-animalhealthstatusshape)
  - [<span class="toc-section-number">3.4</span> Gesundheitsstatus
    Standort](#sec-nodeshape-localunithealthstatusshape)
  - [<span class="toc-section-number">3.5</span>
    Gruppenmeldung](#sec-nodeshape-groupnotificationshape)
  - [<span class="toc-section-number">3.6</span> Meldung
    Einzeltier](#sec-nodeshape-animalnotificationshape)
  - [<span class="toc-section-number">3.7</span> Rechtliche
    Einheit](#sec-nodeshape-legalunitshape)
  - [<span class="toc-section-number">3.8</span>
    Tierhaltender](#sec-nodeshape-animalkeepershape)
  - [<span class="toc-section-number">3.9</span> Örtliche
    Einheit](#sec-nodeshape-localunitshape)
- [<span class="toc-section-number">4</span>
  Wertebereiche](#sec-code-lists)
  - [<span class="toc-section-number">4.1</span> Seuchenstatus
    Einzeltier](#sec-codelist-animalhealthstatus)
  - [<span class="toc-section-number">4.2</span>
    Tiergeschichtestatus](#sec-codelist-animalhistorystate)
  - [<span class="toc-section-number">4.3</span> Zweck (Rinder, Schafe,
    Ziegen)](#sec-codelist-animaltypeofuse)
  - [<span class="toc-section-number">4.4</span> Meldestatus
    Equide](#sec-codelist-equidnotificationstate)
  - [<span class="toc-section-number">4.5</span> Zweck
    (Equiden)](#sec-codelist-equidtypeofusage)
  - [<span class="toc-section-number">4.6</span>
    Grössenkategorie](#sec-codelist-equidwithersclass)
  - [<span class="toc-section-number">4.7</span>
    Geschlecht](#sec-codelist-gender)
  - [<span class="toc-section-number">4.8</span>
    Nutztierart](#sec-codelist-genus)
  - [<span class="toc-section-number">4.9</span> Typ
    Gesundheitsstatus](#sec-codelist-healthstatustype)
  - [<span class="toc-section-number">4.10</span> Seuchenstatus örtliche
    Einheit](#sec-codelist-localunithealthstatus)
  - [<span class="toc-section-number">4.11</span>
    Bewegungstyp](#sec-codelist-notificationtype)
- [<span class="toc-section-number">5</span>
  Sicherheitsaspekte](#sec-safety-consideration)
- [<span class="toc-section-number">6</span>
  Haftungsausschluss](#sec-disclaimer)
- [<span class="toc-section-number">7</span>
  Urheberrechte](#sec-copyrights)
- [<span class="toc-section-number">8</span> Anhang A -
  Referenzen](#sec-appendix-a)
- [<span class="toc-section-number">9</span> Anhang B - Mitwirkung und
  Prüfung](#sec-appendix-b)
- [<span class="toc-section-number">10</span> Anhang C - Abkürzungen und
  Glossar](#sec-appendix-c)
- [<span class="toc-section-number">11</span> Anhang D - Änderungen
  gegenüber der Vorversion](#sec-appendix-d)
- [<span class="toc-section-number">12</span> Anhang E -
  Abbildungsverzeichnis](#sec-appendix-e)
- [<span class="toc-section-number">13</span> Anhang F -
  Tabellenverzeichnis](#sec-appendix-f)

# Hinweis

Im vorliegenden Dokument wird bei der Bezeichnung von Personen eine
geschlechtsneutrale Formulierung verwendet. Basis bildet der Leitfaden
der Bundeskanzlei. Je nach Situation kommen Paarformen (Bürgerinnen und
Bürger), geschlechtsabstrakte Formen (versicherte Person),
geschlechtsneutrale Formen (Versicherte) oder Umschreibungen ohne
Personenbezug zum Einsatz. Das generische Maskulin (Bürger) ist nicht
zulässig. Vollformen werden in fortlaufenden Texten verwendet, also in
Texten, die aus ausformulierten Sätzen bestehen. In verknappten
Textpassagen, namentlich in Tabellen, können Kurzformen verwendet
werden. Dabei wird die Kurzform mit Schrägstrich, aber ohne
Auslassungsstrich verwendet (Referent/in). Genderstern und ähnliche
Schreibweisen werden nicht verwendet.

# Einleitung

## Status

In Arbeit: Der Gebrauch ist nur innerhalb der Fachgruppe, bzw. im
Expertenausschuss zugelassen.

## Anwendungsgebiet

Das vorliegende Dokument beschreibt die Daten der Tierverkehrsdatenbank
(TVD) semantisch, um auch Fachpersonen ohne vertiefte IT-Kenntnisse ein
besseres Verständnis der Daten zu ermöglichen.

## Das Tiermeldewesen in der Schweiz

Die Land- und Ernährungswirtschaft in der Schweiz wurde in den 1990er
Jahren stark durch die Tierseuche «BSE» herausgefordert. Als sich 1996
die Erkenntnis der Übertragbarkeit der Krankheit vom Tier auf den
Menschen erhärtete, führte dies zu grosser Verunsicherung. In der Folge
stiegen die Erwartungen an die Sicherheit von tierischen Lebensmitteln
und das Bewusstsein für die Bedeutung der Lebensmittelkontrolle. Der
Ansatz «vom Stall bis auf den Teller» etablierte sich. Die
risikobasierte Überwachung, die lückenlose Rückverfolgbarkeit der
Nutztiere, die Kontrolle des Tierverkehrs, die Pflicht zur
Herkunftsdeklaration sowie Qualitätskontrollen in der gesamten
Produktions- und Verarbeitungskette bilden seither die Basis für einen
hohen Standard in der Lebensmittelsicherheit[^1].

Die Erfahrung BSE führte 1999 zum Aufbau einer nationalen
Tierverkehrsdatenbank (TVD). In Artikel 7a sowie 13–15 des
Tierseuchengesetzes[^2] und in Titel 2, Abschnitt 1, 1a und 2a der
Tierseuchenverordnung[^3] sind die grundlegenden gesetzlichen
Ausführungen zur Identifizierung/Kennzeichnung und der Registrierung von
Nutztieren sowie die zugehörigen Meldepflichten formuliert. Diese
orientieren sich an der europäischen Gesetzgebung zur selben
Thematik[^4] (Verordnung (EU) 2016/429 zu Tierseuchen; Delegierte
Verordnung (EU) 2019/2035 über Betriebe, in denen Landtiere gehalten
werden, und für Brütereien sowie zur Rückverfolgbarkeit).

Waren ab 1999 vorerst Rinder meldepflichtig, folgten ab 2011 die
Schweine und Equiden, wenn auch die Schweine bis heute nicht in Form von
Einzeltiermeldungen. Ab 2014, respektive 2020 galt die Meldepflicht in
die TVD dann auch für Kleinwiederkäuer (Schafe und Ziegen). Zu Beginn,
2014, betraf diese nur die Schlachtbetriebe. Seit 2014 besteht auch die
Meldepflicht für Geflügel[^5]. Seit dem Januar 2020 sind auch die
Tierhaltenden von Kleinwiederkäuern in das Meldewesen der Einzeltiere
eingebunden.[^6] Die Identifizierung und Kennzeichnung der Klauentiere
mit Ohrmarken, die Einzeltierregistrierung von Rindern, Schafen und
Ziegen in der TVD, sowie die Meldung von Tierzugängen, Tierabgängen
(Tier verlässt eine Tierhaltung lebend), Geburten, Einfuhr, Ausfuhr,
Schlachtung, Hofschlachtung und Verendung (Tier wird als nicht mehr
lebend abgemeldet), sind für alle Tierhaltenden in der Schweiz
obligatorisch[^7]. Die Meldungen unterliegen zudem gesetzlichen
Meldefristen[^8].

Die TVD ist Teil einer Systemlandschaft der Bereiche Landwirtschaft,
Veterinärwesen und Lebensmittelsicherheit. Die zentrale Eingangspforte
bildet dabei das Portal Agate[^9], mit dem Agrarpolitischen
Informationssystem AGIS[^10] im Zentrum.

<!-- Abbildung «Systemlandschaft und Datenflüsse» wird nachgeliefert. -->

In der Verordnung über die Identitas AG und die
Tierverkehrsdatenbank[^11] (IdTVD-V) werden Inhalte zum Tierverkehr und
Aufgaben der Identitas AG sowie die Zugriffsrechte auf die Daten weiter
ausgeführt. Die Bedeutung der Identifizierung/Kennzeichnung von
Nutztieren geht weit über die Seuchenthematik hinaus und fand deshalb
auch Eingang in die landwirtschaftliche Gesetzgebung[^12]
(Landwirtschaftsgesetz LwG Artikel 165g, 177 und 185) und diverse
zugehörige Verordnungen. Die Daten aus dem Tierverkehr entwickelten sich
zu einem unverzichtbaren Bestandteil in der Umsetzung agrarpolitischer
Massnahmen, beispielsweise der tierbezogenen Direktzahlungen[^13], der
Bestimmung der Nährstoffflüsse oder des Agrarumweltmonitorings[^14].
Weiter dienen die Daten auch als Grundlage für die Strukturerhebung der
Landwirtschaft in der Schweiz[^15] und generell der landwirtschaftlichen
Statistik[^16].

Rasch etablierte sich das Tiermeldewesen auch entlang der gesamten
Lebensmittelwertschöpfungskette. Programme mit Tierwohl-,
Rückverfolgbarkeits- und Herkunftsversprechen stützen sich darauf
ab[^17]. Die Vielfalt der Tierinformation aus dem Meldewesen des
Tierverkehrs spiegelt sich auch in den öffentlich verfügbaren
Datensätzen der Open Data Plattform Tierstatistik[^18].

Die technische Schnittstellenbeschreibung in diesem Dokument basiert auf
der technischen Servicebeschreibung AnimalTracing v1.32, sowie der
openAPI-Spezifikation v. x.xx.

## Verweise

Schnittstellen: AnimalTracing API, Technische Servicebeschreibung
AnimalTracing

# Namespaces

<a href="#tbl-namespaces" class="quarto-xref">Tabelle 1</a> listet die
Präfixe und Namespaces, die in diesem Dokument verwendet werden. Ein
Präfix steht stellvertretend für eine Namespace-IRI, den gemeinsamen
Anfang der IRIs eines Vokabulars. Die Turtle-Spezifikation beschreibt,
wie solche [*Prefixed
Names*](https://www.w3.org/TR/turtle/#prefixed-name) aufgelöst werden
\[Turtle\].

<div id="tbl-namespaces">

Tabelle 1: In eCH-0309 – Hilfsmittel Tierverkehrsdaten verwendete
Namespaces.

| Präfix | Namespace                                   |
|:-------|:--------------------------------------------|
| :      | https://agriculture.ld.admin.ch/eCH-0309/1/ |
| xsd:   | http://www.w3.org/2001/XMLSchema#           |

</div>

# Datenmodell

<div id="fig-uml">

<img src="../assets/img/uml.png" class="lightbox"
style="width:100.0%" />

Abbildung 1: UML-Diagramm des Datenmodells von eCH-0309.

</div>

<a href="#fig-uml" class="quarto-xref">Abbildung 1</a> zeigt die Klassen
des Datenmodells und ihre Beziehungen. Jedes Rechteck ist eine Klasse,
die Zeilen darin sind ihre Attribute; die eckigen Klammern geben an, wie
viele Werte zulässig sind, von der Mindest- bis zur Höchstzahl —
`[1..1]` bedeutet genau einen Wert, `[0..1]` höchstens einen. Ein Pfeil
führt zu der Klasse, auf die verwiesen wird, und trägt den Namen der
Beziehung; mehrere Beziehungen zwischen denselben Klassen teilen sich
einen Pfeil. Die Linie mit dem Dreieck verbindet eine Klasse mit ihrer
Oberklasse, auf die das Dreieck zeigt: Ein Equide ist ein Einzeltier und
hat zusätzlich zu den gezeigten alle Attribute des Einzeltiers, die im
Diagramm nicht wiederholt werden. Attribute mit einem Wertebereich sind
wie alle übrigen dargestellt; die zulässigen Werte stehen in
<a href="#sec-code-lists" class="quarto-xref">Kapitel 4</a>. Datentypen
und Beschreibungen führt das Diagramm nicht auf, sie folgen in den
Abschnitten zu den einzelnen Klassen.

## Einzeltier

Ein einzeln identifiziertes Nutztier. In der Tierverkehrsdatenbank
werden Tiere der Kategorien Rinder, Schafe, Ziegen und Equiden als
Einzeltiere erfasst; sie werden über die Ohrmarkennummer, bei Equiden
über die UELN, eindeutig identifiziert. Für Schweine und Geflügel werden
keine Einzeltiere geführt, sondern ausschliesslich Gruppenmeldungen.

### Übersicht

<div class="ech-facts">

Shape  
[:AnimalShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalShape)

Zielklasse  
[:Animal](https://agriculture.ld.admin.ch/eCH-0309/1/Animal)

</div>

### Eigenschaften

<table style="width:99%;">
<colgroup>
<col style="width: 43%" />
<col style="width: 48%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Identifikation Mutter</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/mother">:mother</a>):
Ein Einzeltier hat höchstens ein Muttertier.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-animalshape">Einzeltier</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Identifikation Vater</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/father">:father</a>):
Ein Einzeltier hat höchstens ein Vatertier.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-animalshape">Einzeltier</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Identifikator</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/identifier">:identifier</a>):
Ohrmarkennummer, bei Equiden UELN</td>
<td style="text-align: left;"><ul>
<li>Typ: Zeichenkette (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
<li>Länge: ≤ 15 Zeichen</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nutztierart</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/genus">:genus</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/Genus">:Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Geschlecht</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/gender">:gender</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/Gender">:Gender</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Geburtsdatum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/dateOfBirth">:dateOfBirth</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Todesdatum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/dateOfDeath">:dateOfDeath</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>TiergeschichteStatus</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/historyState">:historyState</a>):
Status der Tiergeschichte zum Abfragedatum. Nicht relevant für Equiden;
der Objektkatalog führt das Attribut deshalb mit Kardinalität 1, die
Pflicht gilt aber nur für die übrigen Einzeltiere.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalHistoryState">:AnimalHistoryState</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Zweck</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalTypeOfUse">:AnimalTypeOfUse</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kastriert</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/castrated">:castrated</a>):
Der Objektkatalog bezeichnet das Attribut als für Equiden nicht
vorhanden, die openAPI führt es aber auch auf den Equiden-Antworten; die
Abweichung ist mit Issue #45 bei Identitas angefragt.</td>
<td style="text-align: left;"><ul>
<li>Typ: Wahrheitswert (<a
href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

### Regeln

Der Objektkatalog führt den TiergeschichteStatus mit Kardinalität 1,
bezeichnet ihn für Equiden aber als nicht relevant. Die Pflicht gilt
deshalb für jedes Einzeltier ausser den Equiden.

## Equide

Subklasse der Klasse Einzeltier für Tiere der Gattung Equiden (Pferd,
Maultier, Maulesel, Esel). Alle Attribute der Klasse Einzeltier gelten
auch für Equiden; diese Klasse beschreibt ausschliesslich die
zusätzlichen, equidenspezifischen Angaben. Die Verantwortung für das
Meldewesen liegt bei Equiden nicht beim Tierhaltenden, sondern bei der
Eigentümerin oder beim Eigentümer. Ein Eigentümer ist die rechtliche
Einheit, in deren Eigentum Equiden sind; der Begriff wird nur für
Equideneigentümer geführt (Kapitel 3.1.1 des Hilfsmittels).

### Übersicht

<div class="ech-facts">

Shape  
[:EquidShape](https://agriculture.ld.admin.ch/eCH-0309/1/EquidShape)

Zielklasse  
[:Equid](https://agriculture.ld.admin.ch/eCH-0309/1/Equid)

</div>

### Eigenschaften

<table style="width:99%;">
<colgroup>
<col style="width: 44%" />
<col style="width: 47%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Eigentümer oder
Eigentümerin</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/owner">:owner</a>): Die
rechtliche Einheit, in deren Eigentum der Equide steht. Bei Equiden
liegt die Verantwortung für das Meldewesen beim Eigentümer und nicht
beim Tierhaltenden (Kapitel 3.1.1 des Hilfsmittels).</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-legalunitshape">Rechtliche
Einheit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Grössenkategorie</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/withersClass">:withersClass</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/EquidWithersClass">:EquidWithersClass</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldestatus</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationState">:notificationState</a>):
Equiden führen anstelle des TiergeschichteStatus einen eigenen
Meldestatus.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/EquidNotificationState">:EquidNotificationState</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Zweck</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfEquidUsage">:typeOfEquidUsage</a>):
Equiden verwenden einen eigenen Wertebereich: Heimtier oder
Nutztier.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/EquidTypeOfUsage">:EquidTypeOfUsage</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Identifikation Vater</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/father">:father</a>):
Equiden führen keinen Vater: die openAPI kennt für sie nur die Mutter
und die genetische Mutter. Der Objektkatalog nennt im Attribut dagegen
die UELN des Vatertiers; die Abweichung ist mit Issue #45 bei Identitas
angefragt.</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">0..0</td>
</tr>
<tr>
<td style="text-align: left;"><strong>TiergeschichteStatus</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/historyState">:historyState</a>):
Im Objektkatalog als «nicht relevant für Equiden» bezeichnet; an seine
Stelle tritt der Meldestatus.</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">0..0</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Zweck (Nutztiere)</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>):
Gilt nicht für Equiden; an seine Stelle tritt der equidenspezifische
Zweck.</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">0..0</td>
</tr>
</tbody>
</table>

## Gesundheitsstatus Einzeltier

Eine Seucheninformation, die auf einem Einzeltier erfasst ist.
Zusätzlich zum individuellen Seuchenstatus werden damit auch relevante
Impfungen erfasst.

### Übersicht

<div class="ech-facts">

Shape  
[:AnimalHealthStatusShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalHealthStatusShape)

Zielklasse  
[:AnimalHealthStatus](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalHealthStatus)

</div>

### Eigenschaften

<table style="width:99%;">
<colgroup>
<col style="width: 44%" />
<col style="width: 47%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Tier-ID</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/animal">:animal</a>):
Ein Gesundheitsstatus Einzeltier bezieht sich auf genau ein
Einzeltier.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-animalshape">Einzeltier</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Typ</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/healthStatusType">:healthStatusType</a>):
z. B. Seuchenstatus, Impfstatus, Risikostatus</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/HealthStatusType">:HealthStatusType</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/epizooticStatus">:epizooticStatus</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalEpizooticStatus">:AnimalEpizooticStatus</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Datum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/validFrom">:validFrom</a>):
Datum, ab dem der Seuchenstatus gültig ist oder das Impfdatum</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

## Gesundheitsstatus Standort

Bei Seuchengeschehen von nationaler Bedeutung ist es entscheidend, dass
Tierhaltende über Sperren und Seuchenstatus informiert sind; so kann ein
Ausbreitungsrisiko durch den Tierverkehr minimiert werden. Eine
Seucheninformation, die auf einer örtlichen Einheit erfasst ist. Neben
dem Seuchenstatus einer örtlichen Einheit können auch Impf-, Risiko- und
Laborergebnisse abgebildet werden. In der openAPI-Spezifikation von
AnimalTracing besteht dafür keine eigene Klasse; die entsprechenden
Angaben sind dort Attribute der örtlichen Einheit.

### Übersicht

<div class="ech-facts">

Shape  
[:LocalUnitHealthStatusShape](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitHealthStatusShape)

Zielklasse  
[:LocalUnitHealthStatus](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitHealthStatus)

</div>

### Eigenschaften

<table style="width:100%;">
<colgroup>
<col style="width: 42%" />
<col style="width: 49%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Örtliche Einheit</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localUnit">:localUnit</a>):
BUR-Nummer der örtlichen Einheit</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-localunitshape">Örtliche
Einheit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Typ</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/healthStatusType">:healthStatusType</a>):
z. B. Seuchenstatus, Impfstatus, Risikostatus</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/HealthStatusType">:HealthStatusType</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/epizooticStatus">:epizooticStatus</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitEpizooticStatus">:LocalUnitEpizooticStatus</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Datum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/validFrom">:validFrom</a>):
Datum, ab dem der Seuchenstatus gültig ist</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

## Gruppenmeldung

Ein Ereignis für eine nicht eindeutig identifizierbare Tiergruppe.
Gruppenmeldungen werden für Tiere der Kategorien Schweine und Geflügel
erfasst; die Individuen einer Tiergruppe sind deshalb nicht bekannt. Die
Ereignisse werden durch die natürlichen Personen der verantwortlichen
rechtlichen Einheit Tierhaltender gemeldet. Sie umfassen
Einstallungsmeldungen bei Geflügel, Bewegungsmeldungen bei Schweinen
sowie Schlachtungsmeldungen von Schweinen (in Stück) und Geflügelgruppen
(in kg). Für diese Klasse besteht in der openAPI-Spezifikation von
AnimalTracing kein Gegenstück, da Schweine und Geflügel dort nicht
abgebildet sind.

### Übersicht

<div class="ech-facts">

Shape  
[:GroupNotificationShape](https://agriculture.ld.admin.ch/eCH-0309/1/GroupNotificationShape)

Zielklasse  
[:GroupNotification](https://agriculture.ld.admin.ch/eCH-0309/1/GroupNotification)

</div>

### Eigenschaften

<table style="width:99%;">
<colgroup>
<col style="width: 46%" />
<col style="width: 44%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Örtliche Einheit</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localUnit">:localUnit</a>):
BUR-Nummer der örtlichen Einheit</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-localunitshape">Örtliche
Einheit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Herkunft</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/originLocalUnit">:originLocalUnit</a>):
BUR-Nummer der örtlichen Einheit von der das Tier kommt</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-localunitshape">Örtliche
Einheit</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ID</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/id">:id</a>):
Eindeutiger Identifikator der Bewegung, der durch das System vergeben
wird.</td>
<td style="text-align: left;"><ul>
<li>Typ: Zeichenkette (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nutztierart</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/genus">:genus</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/Genus">:Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Gruppeninformation</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/groupInformation">:groupInformation</a>):
Bei Einstallungsmeldungen von Geflügel ist eine Gruppeninformation
anzugeben</td>
<td style="text-align: left;"><ul>
<li>Typ: Zeichenkette (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldungstyp</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationType">:notificationType</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/NotificationType">:NotificationType</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Ereignisdatum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/eventDate">:eventDate</a>):
Datum, an dem das Ereignis stattgefunden hat</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldedatum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationDate">:notificationDate</a>):
Datum, an dem das Ereignis gemeldet wurde</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Anzahl</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/count">:count</a>):
Anzahl Tiere, die in einer Bewegung verstellt wurden
(Schweine/Geflügel)</td>
<td style="text-align: left;"><ul>
<li>Typ: Ganzzahl (<a
href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Gewicht</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/weight">:weight</a>):
Gesamtgewicht in kg der Tiergruppe bei Schlachtungsmeldungen von
Geflügel</td>
<td style="text-align: left;"><ul>
<li>Typ: Ganzzahl (<a
href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Zweck</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>):
Nutzungsart der Tiergruppe (bei Einzeltieren wird die Nutzungsart auf
der Klasse «Einzeltier» geführt)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalTypeOfUse">:AnimalTypeOfUse</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Alter</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/age">:age</a>): Bei
Einstallungsmeldungen von Geflügel ist das Alter in Wochen
anzugeben</td>
<td style="text-align: left;"><ul>
<li>Typ: Ganzzahl (<a
href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

## Meldung Einzeltier

Ein Ereignis, das ein Einzeltier betrifft. Als Ereignisse gelten
Bewegungsmeldungen, Meldungen von Grunddaten, Änderungen einzelner
Attribute der Grunddaten sowie finale Meldungen. Eine Meldung bezieht
sich immer auf die örtliche Einheit, auf welcher das Ereignis
stattgefunden hat, und kann zusätzlich die örtliche Einheit der Herkunft
angeben. Die Ereignisse werden durch die berechtigten Personen gemeldet
mit Angabe der Tierhaltung, auf die sich die Meldung bezieht; bei
Equiden werden sie durch die berechtigten Personen des verantwortlichen
Equideneigentümers gemeldet.

### Übersicht

<div class="ech-facts">

Shape  
[:AnimalNotificationShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalNotificationShape)

Zielklasse  
[:AnimalNotification](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalNotification)

</div>

### Eigenschaften

<table style="width:99%;">
<colgroup>
<col style="width: 46%" />
<col style="width: 44%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Identifikator</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/animal">:animal</a>):
Eine Meldung Einzeltier bezieht sich auf genau ein Einzeltier.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-animalshape">Einzeltier</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Örtliche Einheit</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localUnit">:localUnit</a>):
BUR-Nummer der örtlichen Einheit, auf die sich die Meldung bezieht</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-localunitshape">Örtliche
Einheit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Herkunft</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/originLocalUnit">:originLocalUnit</a>):
BUR-Nummer der örtlichen Einheit von der das Tier kommt</td>
<td style="text-align: left;"><ul>
<li>Typ: <a href="#sec-nodeshape-localunitshape">Örtliche
Einheit</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ID</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/id">:id</a>):
Eindeutiger Identifikator der Bewegung, der durch das System vergeben
wird.</td>
<td style="text-align: left;"><ul>
<li>Typ: Zeichenkette (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nutztierart</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/genus">:genus</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/Genus">:Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldungstyp</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationType">:notificationType</a>)</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/NotificationType">:NotificationType</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Ereignisdatum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/eventDate">:eventDate</a>):
Datum, an dem das Ereignis stattgefunden hat</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldedatum</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationDate">:notificationDate</a>):
Datum, an dem das Ereignis gemeldet wurde</td>
<td style="text-align: left;"><ul>
<li>Typ: Datum (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
</tbody>
</table>

## Rechtliche Einheit

Die rechtliche Einheit nach eCH-0108 ist eine juristische Person (z.B.
Aktiengesellschaft, GmbH), eine Personengesellschaft (z.B.
Kollektivgesellschaft) oder eine selbstständigerwerbende natürliche
Person, die dem Bundesgesetz über die Unternehmens-Identifikationsnummer
(UIDG) unterstellt ist und einen Eintrag im UID-Register aufweist. Sie
identifiziert z.B. das Steuersubjekt für Steuerbehörden oder die
beitragspflichtige Person für Sozialversicherungsbeiträge. Die
rechtliche Einheit wird mit der UID identifiziert. Nur wenn das
Unternehmen ein «Einzelunternehmen» ist, ist der Bewirtschafter zugleich
eine natürliche Person. Das Mastersystem für diese Daten ist das
UID-Register des BFS; das landwirtschaftliche Informationssystem bezieht
die Daten aus diesem Register über eine Schnittstelle. Der Tierhaltende
und der Equideneigentümer sind die beiden Ausprägungen der rechtlichen
Einheit, die in diesem Hilfsmittel vorkommen (Kapitel 3.1.1 des
Hilfsmittels). Die Attribute sind in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
Kapitel 3.1 und 3.2, sowie in
[eCH-0108](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2023-12-21_eCH-0108_V6.0.0_Unternehmensstammdaten%20Unternehmensregister.pdf),
Kapitel 3.1, beschrieben.

### Übersicht

<div class="ech-facts">

Shape  
[:LegalUnitShape](https://agriculture.ld.admin.ch/eCH-0309/1/LegalUnitShape)

Zielklasse  
[:LegalUnit](https://agriculture.ld.admin.ch/eCH-0309/1/LegalUnit)

</div>

## Tierhaltender

Ein Bewirtschafter ist eine rechtliche Einheit nach eCH-0108, die das
Geschäftsrisiko für einen Betrieb trägt (LBV Art. 2). Der Tierhaltende
ist eine Form des Bewirtschafters, der Tiere hält (LBV Art. 11a); er
braucht somit eine örtliche Einheit (Tierhaltung). Die Verantwortung für
das Meldewesen obliegt dem Tierhaltenden für alle Tierkategorien mit
Ausnahme der Equiden; bei Equiden liegt sie beim Eigentümer oder bei der
Eigentümerin (Kapitel 3.1.1 des Hilfsmittels). Die Attribute sind in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
Kapitel 3.1 und 3.2, beschrieben.

### Übersicht

<div class="ech-facts">

Shape  
[:AnimalKeeperShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalKeeperShape)

Zielklasse  
[:AnimalKeeper](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalKeeper)

</div>

### Regeln

Ein Tierhaltender braucht mindestens eine örtliche Einheit (Kapitel
3.1.1 des Hilfsmittels). Diese Regel ist der Semantikbeschreibung
entnommen, nicht dem Objektkatalog.

## Örtliche Einheit

Eine örtliche Einheit nach eCH-0108 ist eine Einrichtung an einem
bestimmten Ort, an welcher eine wirtschaftliche Tätigkeit ausgeübt wird.
Eine örtliche Einheit hat eine BUR-Nummer und ist immer einer
rechtlichen Einheit (bzw. einem Unternehmen) zugeordnet. Die örtliche
Einheit wird über die BUR-Nummer identifiziert. Die örtliche Einheit
kann aus einem oder mehreren Gebäuden bestehen. Die der BUR-Nummer
zugewiesene EGID bezieht sich auf «das Zentrum» der örtlichen Einheit,
resp. das Hauptgebäude. In der TVD werden die örtlichen Einheiten
«Tierhaltungen» genannt und sind zusätzlich über die TVD-Nummer
identifiziert. Diese Definition stammt aus
[eCH-0108](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2023-12-21_eCH-0108_V6.0.0_Unternehmensstammdaten%20Unternehmensregister.pdf),
Kapitel 1.5; die agrarspezifischen Ergänzungen sind in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
Kapitel 3.3 und 3.4, beschrieben.

### Übersicht

<div class="ech-facts">

Shape  
[:LocalUnitShape](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitShape)

Zielklasse  
[:LocalUnit](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnit)

</div>

### Eigenschaften

<table style="width:99%;">
<colgroup>
<col style="width: 53%" />
<col style="width: 35%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Beschreibung</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Kardinalität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Tierhaltender</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/animalKeeper">:animalKeeper</a>):
Zuordnung der örtlichen Einheit zum Tierhaltenden. Nach eCH-0108,
Kapitel 1.5, ist eine örtliche Einheit immer einer rechtlichen Einheit
(bzw. einem Unternehmen) zugeordnet; die Stammdaten der örtlichen
Einheit führen dafür das optionale Merkmal «mainUid» mit der UID der
rechtlichen Haupteinheit. Da der Tierhaltende nach dem Objektkatalog nur
eine Sonderform der rechtlichen Einheit ist, ist diese Zuordnung nicht
zwingend.</td>
<td style="text-align: left;"><ul>
<li>Typ: <a
href="#sec-nodeshape-animalkeepershape">Tierhaltender</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

# Wertebereiche

Für einen Teil der Wertebereiche liegen noch keine französischen und
italienischen Bezeichnungen vor; die Bezeichnungen sind in Deutsch und
Englisch aufgeführt, so wie sie die Quellen liefern.
(<https://test-03-tvd-api-at.identitas.ch/open-api/v1.0>, 2026-09-24)

## Seuchenstatus Einzeltier

<div id="tbl-codelist-animalhealthstatus">

Tabelle 2: Werte des Wertebereichs Seuchenstatus Einzeltier

| Wert         | Bezeichnung    | Beschreibung       |
|:-------------|:---------------|:-------------------|
| `Blocked`    | gesperrt       | Typ: Seuchenstatus |
| `Free`       | frei           | Typ: Seuchenstatus |
| `NotTested`  | Nicht getestet | Typ: Seuchenstatus |
| `Vaccinated` | geimpft        | Typ: Impfstatus    |

</div>

## Tiergeschichtestatus

<div id="tbl-codelist-animalhistorystate">

Tabelle 3: Werte des Wertebereichs Tiergeschichtestatus

| Wert          | Bezeichnung     | Beschreibung |
|:--------------|:----------------|:-------------|
| `Lost`        | Verschollen     |              |
| `NotDefined`  | Nicht definiert |              |
| `NotOk`       | Fehlerhaft      |              |
| `Ok`          | OK              |              |
| `TemporaryOk` | Temporär OK     |              |

</div>

## Zweck (Rinder, Schafe, Ziegen)

<div id="tbl-codelist-animaltypeofuse">

Tabelle 4: Werte des Wertebereichs Zweck (Rinder, Schafe, Ziegen)

| Wert    | Bezeichnung | Beschreibung                   |
|:--------|:------------|:-------------------------------|
| `Milk`  | Milch       | Milchkühe, -schafe und -ziegen |
| `Other` | Andere      |                                |

</div>

## Meldestatus Equide

<div id="tbl-codelist-equidnotificationstate">

Tabelle 5: Werte des Wertebereichs Meldestatus Equide

| Wert | Bezeichnung | Beschreibung |
|:---|:---|:---|
| `LocationChangeAndAcquisitionPending` | Standortwechsel und Eigentumsübernahme hängig |  |
| `LocationChangePending` | Standortwechsel hängig |  |
| `Ok` | OK |  |
| `OwnershipAcquisitionPending` | Eigentumsübernahme hängig |  |

</div>

## Zweck (Equiden)

<div id="tbl-codelist-equidtypeofusage">

Tabelle 6: Werte des Wertebereichs Zweck (Equiden)

| Wert              | Bezeichnung | Beschreibung |
|:------------------|:------------|:-------------|
| `CompanionAnimal` | Heimtier    |              |
| `FarmAnimal`      | Nutztier    |              |

</div>

## Grössenkategorie

<div id="tbl-codelist-equidwithersclass">

Tabelle 7: Werte des Wertebereichs Grössenkategorie

| Wert                   | Bezeichnung               | Beschreibung |
|:-----------------------|:--------------------------|:-------------|
| `GreaterThan148cm`     | Widerristhöhe über 148 cm |              |
| `LessOrEqualThan148cm` | Widerristhöhe bis 148 cm  |              |

</div>

## Geschlecht

<div id="tbl-codelist-gender">

Tabelle 8: Werte des Wertebereichs Geschlecht

| Wert     | Bezeichnung | Beschreibung |
|:---------|:------------|:-------------|
| `Female` | Weiblich    |              |
| `Male`   | Männlich    |              |

</div>

## Nutztierart

<div id="tbl-codelist-genus">

Tabelle 9: Werte des Wertebereichs Nutztierart

| Wert | Bezeichnung | Beschreibung |
|:---|:---|:---|
| `Camelid` | Kameliden | Neuweltkameliden |
| `Cattle` | Rindvieh | Tiere der Rindergattung (*Bos*) und Wasserbüffel (*Bubalus bubalis*) |
| `Equid` | Equiden | Tiere der Pferdegattung (Pferd, Maultier, Maulesel, Esel) |
| `Game` | Wild | Wild in Gehegen |
| `Goat` | Ziegen |  |
| `Pig` | Schweine |  |
| `Poultry` | Geflügel |  |
| `Sheep` | Schafe |  |

</div>

## Typ Gesundheitsstatus

<div id="tbl-codelist-healthstatustype">

Tabelle 10: Werte des Wertebereichs Typ Gesundheitsstatus

| Wert                | Bezeichnung   | Beschreibung |
|:--------------------|:--------------|:-------------|
| `EpizooticStatus`   | Seuchenstatus |              |
| `LaboratoryResult`  | Laborergebnis |              |
| `RiskStatus`        | Risikostatus  |              |
| `VaccinationStatus` | Impfstatus    |              |

</div>

## Seuchenstatus örtliche Einheit

<div id="tbl-codelist-localunithealthstatus">

Tabelle 11: Werte des Wertebereichs Seuchenstatus örtliche Einheit

| Wert        | Bezeichnung    | Beschreibung       |
|:------------|:---------------|:-------------------|
| `Blocked`   | gesperrt       | Typ: Seuchenstatus |
| `Free`      | frei           | Typ: Seuchenstatus |
| `High`      | Hoch           | Typ: Risikostatus  |
| `Low`       | Tief           | Typ: Risikostatus  |
| `Medium`    | Mittel         | Typ: Risikostatus  |
| `Negative`  | negativ        | Typ: Laborergebnis |
| `NotTested` | Nicht getestet | Typ: Seuchenstatus |
| `Positive`  | positiv        | Typ: Laborergebnis |

</div>

## Bewegungstyp

<div id="tbl-codelist-notificationtype">

Tabelle 12: Werte des Wertebereichs Bewegungstyp

| Wert | Bezeichnung | Beschreibung |
|:---|:---|:---|
| `Arrival` | Zugang | Nicht für Equiden |
| `Birth` | Geburt |  |
| `DayStay` | Tagesaufenthalt | Nicht für Equiden |
| `DeathBirth` | Totgeburt | Nicht für Equiden |
| `Deceased` | Verendung | Bei Equiden: Euthanasierung |
| `Export` | Ausfuhr | Bei Equiden: Eigentumsabgabe ins Ausland |
| `FirstRegistration` | Erstregistrierung |  |
| `Import` | Einfuhr |  |
| `ImportAfterExport` | Einfuhr nach Ausfuhr | Nicht für Equiden |
| `Leaving` | Abgang | Nicht für Equiden |
| `LocationChange` | Standortwechsel | Nur für Equiden |
| `OnFarmSlaughter` | Hofschlachtung | Nicht für Equiden |
| `Slaughter` | Schlachtung |  |

</div>

# Sicherheitsaspekte

Informationen zu den ausdrücklich massgeblichen rechtlichen Grundlagen
oder ein Hinweis darauf, dass bei der Umsetzung die entsprechenden
rechtlichen Grundlagen zu beachten sind.

# Haftungsausschluss

eCH-Standards, die der Verein eCH dem Anwender kostenlos zur Verfügung
stellt oder die auf eCH verweisen, haben nur den Status von
Empfehlungen. Der Verein eCH haftet in keinem Fall für Entscheidungen
oder Massnahmen, die der Anwender auf der Grundlage dieser Dokumente
trifft bzw. ergreift. Der Anwender ist dafür verantwortlich, die
Dokumente vor ihrer Verwendung selbst zu überprüfen und gegebenenfalls
fachlichen Rat einzuholen. eCH-Standards können und sollen die
technische, organisatorische oder rechtliche Beratung im Einzelfall
nicht ersetzen.

Dokumente, Verfahren, Methoden, Produkte und Standards, auf die in
eCH-Standards verwiesen wird, sind möglicherweise durch Marken-,
Urheber- oder Patentrechte geschützt. Es liegt in der ausschliesslichen
Verantwortung des Anwenders, die erforderlichen Lizenzen von den
berechtigten Personen und/oder Organisationen einzuholen.

Obwohl der Verein eCH bei der Erstellung der eCH-Standards mit
angemessener Sorgfalt vorgegangen ist, kann er keine Gewährleistung oder
Garantie dafür übernehmen, dass die bereitgestellten Informationen und
Dokumente aktuell, vollständig, richtig oder fehlerfrei sind. eCH behält
sich das Recht vor, die Inhalte der eCH-Standards jederzeit und ohne
vorherige Ankündigung zu ändern.

Jede Haftung für Schäden, die durch die Nutzung der eCH-Standards durch
den Anwender entstehen, wird im gesetzlich zulässigen Rahmen
ausgeschlossen.

# Urheberrechte

Personen, die eCH-Standards erarbeiten, bleiben Inhaber ihrer geistigen
Eigentumsrechte. Diese Personen verpflichten sich jedoch, ihre geistigen
Eigentumsrechte oder andere Rechte an geistigen Eigentumsrechten
Dritter, soweit möglich, den jeweiligen Fachgruppen und dem Verein eCH
kostenlos und zur uneingeschränkten Nutzung und Weiterentwicklung im
Rahmen des Vereinszwecks zur Verfügung zu stellen.

Die von den Fachgruppen erarbeiteten Standards dürfen unter Nennung des
jeweiligen Autors von eCH kostenlos und in uneingeschränktem Umfang
genutzt, verbreitet und weiterentwickelt werden.

eCH-Standards sind vollständig dokumentiert und frei von lizenz-
und/oder patentrechtlichen Einschränkungen. Die dazugehörige
Dokumentation kann kostenlos angefordert werden. Diese Bestimmungen
gelten jedoch nur für die von eCH erarbeiteten Standards, nicht aber für
Standards oder Produkte Dritter, die auf eCH-Standards verweisen. Die
Standards enthalten die entsprechenden Hinweise auf Rechte Dritter.

# Anhang A - Referenzen

<div id="refs" class="references csl-bib-body">

<div id="ref-Turtle" class="csl-entry">

<span class="csl-left-margin">\[Turtle\]
</span><span class="csl-right-inline">Beckett, David ; Berners-Lee,
Tim ; Prud’hommeaux, Eric ; Carothers, Gavin: *[RDF 1.1 Turtle – Terse
RDF Triple Language](https://www.w3.org/TR/turtle/)* (W3C
Recommendation) : World Wide Web Consortium (W3C), 2014</span>

</div>

</div>

# Anhang B - Mitwirkung und Prüfung

# Anhang C - Abkürzungen und Glossar

<div id="tbl-glossary">

Tabelle 13: Glossar des Hilfsmittels eCH-0309

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Begriff</th>
<th style="text-align: left;">Beschreibung</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Bewirtschafter</strong></td>
<td style="text-align: left;">Eine rechtliche Einheit, die das
Geschäftsrisiko für einen Betrieb trägt (LBV Art. 2). Der Tierhaltende
ist eine Form des Bewirtschafters, der Tiere hält (LBV Art. 11a).</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Linked Data Service</strong>
(LINDAS)</td>
<td style="text-align: left;">Der offizielle Linked-Data-Dienst der
Schweizer Bundesverwaltung, der als Triple Store fungiert.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldende Person</strong></td>
<td style="text-align: left;">Die Person oder die Personen, die für eine
Tierhaltung oder für einen Equideneigentümer Meldungen machen.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Resource Description
Framework</strong> (RDF)</td>
<td style="text-align: left;">Ein zentraler Standard des World Wide Web
Consortiums (W3C) zur Modellierung von Datenstrukturen im Web.
Informationen werden nicht in klassischen Tabellen, sondern als
vernetzte Graphen abgebildet.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Stammbetrieb</strong></td>
<td style="text-align: left;">Bei Rindern kann ein Stammbetrieb
hinterlegt werden, um die Zugehörigkeit der Tiere zu einer Tierhaltung
abzubilden, wenn sich ein Tier auf einer anderen örtlichen Einheit
befindet.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Tierhaltung</strong></td>
<td style="text-align: left;">In der Tierverkehrsdatenbank werden
örtliche Einheiten «Tierhaltungen» genannt; sie sind zusätzlich über die
TVD-Nummer identifiziert.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Tripel</strong></td>
<td style="text-align: left;"><p>Die Grundstruktur einer Aussage in RDF,
bestehend aus Subjekt, Prädikat und Objekt.</p>
<p><em>Oberbegriff</em>: Resource Description Framework</p></td>
</tr>
</tbody>
</table>

</div>

# Anhang D - Änderungen gegenüber der Vorversion

# Anhang E - Abbildungsverzeichnis

# Anhang F - Tabellenverzeichnis

[^1]: <https://www.news.admin.ch/de/nsb?id=57438>

[^2]: <https://www.fedlex.admin.ch/eli/cc/1966/1565_1621_1604/de>

[^3]: <https://www.fedlex.admin.ch/eli/cc/1995/3716_3716_3716/de>

[^4]: <https://eur-lex.europa.eu/DE/legal-content/summary/the-eu-animal-health-law.html>

[^5]: <https://fedlex.data.admin.ch/eli/cc/2011/775>, Version 1.1.2014,
    Seite 20

[^6]: <https://www.fedlex.admin.ch/eli/cc/2021/751/de#annex_1/lvl_u1/lvl_2>

[^7]: <https://www.fedlex.admin.ch/eli/cc/1966/1565_1621_1604/de#art_14>,
    <https://www.fedlex.admin.ch/eli/cc/1966/1565_1621_1604/de#art_15_a>

[^8]: <https://www.fedlex.admin.ch/eli/cc/1995/3716_3716_3716/de#art_14>

[^9]: <https://www.blw.admin.ch/blw/de/home/politik/datenmanagement/agate.html>

[^10]: <https://www.blw.admin.ch/blw/de/home/politik/datenmanagement/agate/agis.html>

[^11]: <https://www.fedlex.admin.ch/eli/cc/2021/751/de>

[^12]: <https://www.fedlex.admin.ch/eli/cc/1998/3033_3033_3033/de>

[^13]: <https://www.fedlex.admin.ch/eli/cc/2013/765/de#tit_2/chap_5/sec_7>,
    <https://www.fedlex.admin.ch/eli/cc/2013/765/de#tit_2/chap_5/sec_8>,
    <https://www.fedlex.admin.ch/eli/cc/2013/765/de#tit_2/chap_5/sec_9>

[^14]: <https://www.blw.admin.ch/de/agrarumweltmonitoring>

[^15]: <https://www.bfs.admin.ch/bfs/de/home/statistiken/land-forstwirtschaft/erhebungen/stru.html>

[^16]: <https://www.sbv-usp.ch/de/services/agristat-statistik-der-schweizer-landwirtschaft>

[^17]: <https://www.proviande.ch/de/herkunft>,
    <https://www.identitas.ch/produkte/labelbase>

[^18]: <https://tierstatistik.identitas.ch>
