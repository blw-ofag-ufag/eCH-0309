# Hilfsmittel Tierverkehrsdaten

2. Oktober 2026

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
  Datenmodell](#sec-data-model)
  - [<span class="toc-section-number">2.1</span>
    Einzeltier](#sec-nodeshape-animalshape)
  - [<span class="toc-section-number">2.2</span>
    Equide](#sec-nodeshape-equidshape)
  - [<span class="toc-section-number">2.3</span> Gesundheitsstatus
    Einzeltier](#sec-nodeshape-animalhealthstatusshape)
  - [<span class="toc-section-number">2.4</span> Gesundheitsstatus
    Standort](#sec-nodeshape-localunithealthstatusshape)
  - [<span class="toc-section-number">2.5</span>
    Gruppenmeldung](#sec-nodeshape-groupnotificationshape)
  - [<span class="toc-section-number">2.6</span> Meldung
    Einzeltier](#sec-nodeshape-animalnotificationshape)
  - [<span class="toc-section-number">2.7</span> Rechtliche
    Einheit](#sec-nodeshape-legalunitshape)
  - [<span class="toc-section-number">2.8</span>
    Tierhaltender](#sec-nodeshape-animalkeepershape)
  - [<span class="toc-section-number">2.9</span> Örtliche
    Einheit](#sec-nodeshape-localunitshape)
- [<span class="toc-section-number">3</span>
  Wertebereiche](#sec-code-lists)
  - [<span class="toc-section-number">3.1</span> Seuchenstatus
    Einzeltier](#sec-codelist-animalhealthstatus)
  - [<span class="toc-section-number">3.2</span>
    Tiergeschichtestatus](#sec-codelist-animalhistorystate)
  - [<span class="toc-section-number">3.3</span> Zweck (Rinder, Schafe,
    Ziegen)](#sec-codelist-animaltypeofuse)
  - [<span class="toc-section-number">3.4</span> Zweck
    (Equiden)](#sec-codelist-equidtypeofusage)
  - [<span class="toc-section-number">3.5</span>
    Grössenkategorie](#sec-codelist-equidwithersclass)
  - [<span class="toc-section-number">3.6</span>
    Geschlecht](#sec-codelist-gender)
  - [<span class="toc-section-number">3.7</span>
    Nutztierart](#sec-codelist-genus)
  - [<span class="toc-section-number">3.8</span> Typ
    Gesundheitsstatus](#sec-codelist-healthstatustype)
  - [<span class="toc-section-number">3.9</span> Seuchenstatus örtliche
    Einheit](#sec-codelist-localunithealthstatus)
  - [<span class="toc-section-number">3.10</span>
    Bewegungstyp](#sec-codelist-notificationtype)
- [<span class="toc-section-number">4</span>
  Sicherheitsaspekte](#sec-safety-consideration)
- [<span class="toc-section-number">5</span>
  Haftungsausschluss](#sec-disclaimer)
- [<span class="toc-section-number">6</span>
  Urheberrechte](#sec-copyrights)
- [<span class="toc-section-number">7</span> Anhang A -
  Referenzen](#sec-appendix-a)
- [<span class="toc-section-number">8</span> Anhang B - Mitwirkung und
  Prüfung](#sec-appendix-b)
- [<span class="toc-section-number">9</span> Anhang C - Abkürzungen und
  Glossar](#sec-appendix-c)
- [<span class="toc-section-number">10</span> Anhang D - Änderungen
  gegenüber der Vorversion](#sec-appendix-d)
- [<span class="toc-section-number">11</span> Anhang E -
  Abbildungsverzeichnis](#sec-appendix-e)
- [<span class="toc-section-number">12</span> Anhang F -
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
hohen Standard in der Lebensmittelsicherheit.

Die Erfahrung BSE führte 1999 zum Aufbau einer nationalen
Tierverkehrsdatenbank (TVD). In Artikel 7a sowie 13–15 des
Tierseuchengesetzes und in Titel 2, Abschnitt 1, 1a und 2a der
Tierseuchenverordnung sind die grundlegenden gesetzlichen Ausführungen
zur Identifizierung/Kennzeichnung und der Registrierung von Nutztieren
sowie die zugehörigen Meldepflichten formuliert. Diese orientieren sich
an der europäischen Gesetzgebung zur selben Thematik (Verordnung (EU)
2016/429 zu Tierseuchen; Delegierte Verordnung (EU) 2019/2035 über
Betriebe, in denen Landtiere gehalten werden, und für Brütereien sowie
zur Rückverfolgbarkeit).

Waren ab 1999 vorerst Rinder meldepflichtig, folgten ab 2011 die
Schweine und Equiden, wenn auch die Schweine bis heute nicht in Form von
Einzeltiermeldungen. Ab 2014, respektive 2020 galt die Meldepflicht in
die TVD dann auch für Kleinwiederkäuer (Schafe und Ziegen). Zu Beginn,
2014, betraf diese nur die Schlachtbetriebe. Seit 2014 besteht auch die
Meldepflicht für Geflügel. Seit dem Januar 2020 sind auch die
Tierhaltenden von Kleinwiederkäuern in das Meldewesen der Einzeltiere
eingebunden. Die Identifizierung und Kennzeichnung der Klauentiere mit
Ohrmarken, die Einzeltierregistrierung von Rindern, Schafen und Ziegen
in der TVD, sowie die Meldung von Tierzugängen, Tierabgängen (Tier
verlässt eine Tierhaltung lebend), Geburten, Einfuhr, Ausfuhr,
Schlachtung, Hofschlachtung und Verendung (Tier wird als nicht mehr
lebend abgemeldet), sind für alle Tierhaltenden in der Schweiz
obligatorisch.

Die TVD ist Teil einer Systemlandschaft der Bereiche Landwirtschaft,
Veterinärwesen und Lebensmittelsicherheit. Die zentrale Eingangspforte
bildet dabei das Portal Agate, mit dem Agrarpolitischen
Informationssystem AGIS im Zentrum.

<!-- Abbildung «Systemlandschaft und Datenflüsse» wird nachgeliefert. -->

In der Verordnung über die Identitas AG und die Tierverkehrsdatenbank
(IdTVD-V) werden Inhalte zum Tierverkehr und Aufgaben der Identitas AG
sowie die Zugriffsrechte auf die Daten weiter ausgeführt. Die Bedeutung
der Identifizierung/Kennzeichnung von Nutztieren geht weit über die
Seuchenthematik hinaus und fand deshalb auch Eingang in die
landwirtschaftliche Gesetzgebung (Landwirtschaftsgesetz LwG Artikel
165g, 177 und 185) und diverse zugehörige Verordnungen. Die Daten aus
dem Tierverkehr entwickelten sich zu einem unverzichtbaren Bestandteil
in der Umsetzung agrarpolitischer Massnahmen, beispielsweise der
tierbezogenen Direktzahlungen, der Bestimmung der Nährstoffflüsse oder
des Agrarumweltmonitorings. Weiter dienen die Daten auch als Grundlage
für die Strukturerhebung der Landwirtschaft in der Schweiz und generell
der landwirtschaftlichen Statistik.

Rasch etablierte sich das Tiermeldewesen auch entlang der gesamten
Lebensmittelwertschöpfungskette. Programme mit Tierwohl-,
Rückverfolgbarkeits- und Herkunftsversprechen stützen sich darauf ab.
Die Vielfalt der Tierinformation aus dem Meldewesen des Tierverkehrs
spiegelt sich auch in den öffentlich verfügbaren Datensätzen der Open
Data Plattform Tierstatistik.

Die technische Schnittstellenbeschreibung in diesem Dokument basiert auf
der technischen Servicebeschreibung AnimalTracing v1.32, sowie der
openAPI-Spezifikation v. x.xx.

## Verweise

Schnittstellen: AnimalTracing API, Technische Servicebeschreibung
AnimalTracing

NB: die Namen der im Kapitel 3 beschriebenen Klassen stimmen nicht mit
den ServiceOperations in AnimalTracing überein, da die semantische
Beschreibung einen Überblick über die Dateninhalte verschaffen soll und
gegenüber der Servicebeschreibung einen tieferen Detaillierungsgrad
aufweist.

# Datenmodell

<div id="fig-uml">

<img src="../assets/img/uml.png" class="lightbox"
style="width:100.0%" />

Abbildung 1: UML-Diagramm des Datenmodells von eCH-0309.

</div>

## Einzeltier

Ein einzeln identifiziertes Nutztier. In der Tierverkehrsdatenbank
werden Tiere der Kategorien Rinder, Schafe, Ziegen und Equiden als
Einzeltiere erfasst; sie werden über die Ohrmarkennummer, bei Equiden
über die UELN, eindeutig identifiziert. Für Schweine und Geflügel werden
keine Einzeltiere geführt, sondern ausschliesslich Gruppenmeldungen.

**Zielklasse:** `:Animal`

<div id="tbl-nodeshape-animalshape">

Tabelle 1: Eigenschaften Einzeltier

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Identifikation Mutter**: Ein Einzeltier hat höchstens ein Muttertier. | `:mother` | [`:Animal`](#sec-nodeshape-animalshape) | 0..1 |
| **Identifikation Vater**: Ein Einzeltier hat höchstens ein Vatertier. | `:father` | [`:Animal`](#sec-nodeshape-animalshape) | 0..1 |
| **Identifikator**: Ohrmarkennummer, bei Equiden UELN | `:identifier` | `xsd:string` | 1..1 |
| **Nutztierart** | `:genus` | `:Genus` | 1..1 |
| **Geschlecht** | `:gender` | `:Gender` | 0..1 |
| **Geburtsdatum** | `:dateOfBirth` | `xsd:date` | 0..1 |
| **Todesdatum** | `:dateOfDeath` | `xsd:date` | 0..1 |
| **TiergeschichteStatus** | `:animalHistoryState` | `:AnimalHistoryState` | 1..1 |
| **Zweck** | `:typeOfUse` | `:AnimalTypeOfUse` | 0..1 |
| **Kastriert** | `:castrated` | `xsd:boolean` | 0..1 |

</div>

## Equide

Subklasse der Klasse Einzeltier für Tiere der Gattung Equiden (Pferd,
Maultier, Maulesel, Esel). Alle Attribute der Klasse Einzeltier gelten
auch für Equiden; diese Klasse beschreibt ausschliesslich die
zusätzlichen, equidenspezifischen Angaben. Die Verantwortung für das
Meldewesen liegt bei Equiden nicht beim Tierhaltenden, sondern bei der
Eigentümerin oder beim Eigentümer. Ein Eigentümer ist die rechtliche
Einheit, in deren Eigentum Equiden sind; der Begriff wird nur für
Equideneigentümer geführt (Kapitel 3.1.1 des Hilfsmittels).

**Zielklasse:** `:Equid`

<div id="tbl-nodeshape-equidshape">

Tabelle 2: Eigenschaften Equide

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Eigentümer oder Eigentümerin**: Die rechtliche Einheit, in deren Eigentum der Equide steht. Bei Equiden liegt die Verantwortung für das Meldewesen beim Eigentümer und nicht beim Tierhaltenden (Kapitel 3.1.1 des Hilfsmittels). | `:owner` | [`:LegalUnit`](#sec-nodeshape-legalunitshape) | 1..1 |
| **Grössenkategorie** | `:withersClass` | `:EquidWithersClass` | 1..1 |

</div>

## Gesundheitsstatus Einzeltier

Eine Seucheninformation, die auf einem Einzeltier erfasst ist.
Zusätzlich zum individuellen Seuchenstatus werden damit auch relevante
Impfungen erfasst.

**Zielklasse:** `:AnimalHealthStatus`

<div id="tbl-nodeshape-animalhealthstatusshape">

Tabelle 3: Eigenschaften Gesundheitsstatus Einzeltier

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Tier-ID**: Ein Gesundheitsstatus Einzeltier bezieht sich auf genau ein Einzeltier. | `:animal` | [`:Animal`](#sec-nodeshape-animalshape) | 1..1 |
| **Typ**: z. B. Seuchenstatus, Impfstatus, Risikostatus | `:healthStatusType` | `:HealthStatusType` | 0..1 |
| **Status** | `:epizooticStatus` | `:AnimalEpizooticStatus` | 0..1 |
| **Datum**: Datum, ab dem der Seuchenstatus gültig ist oder das Impfdatum | `:validFrom` | `xsd:date` | 0..1 |

</div>

## Gesundheitsstatus Standort

Bei Seuchengeschehen von nationaler Bedeutung ist es entscheidend, dass
Tierhaltende über Sperren und Seuchenstatus informiert sind; so kann ein
Ausbreitungsrisiko durch den Tierverkehr minimiert werden. Eine
Seucheninformation, die auf einer örtlichen Einheit erfasst ist. Neben
dem Seuchenstatus einer örtlichen Einheit können auch Impf-, Risiko- und
Laborergebnisse abgebildet werden. In der openAPI-Spezifikation von
AnimalTracing besteht dafür keine eigene Klasse; die entsprechenden
Angaben sind dort Attribute der örtlichen Einheit.

**Zielklasse:** `:LocalUnitHealthStatus`

<div id="tbl-nodeshape-localunithealthstatusshape">

Tabelle 4: Eigenschaften Gesundheitsstatus Standort

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Örtliche Einheit**: BUR-Nummer der örtlichen Einheit | `:localUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 1..1 |
| **Typ**: z. B. Seuchenstatus, Impfstatus, Risikostatus | `:healthStatusType` | `:HealthStatusType` | 0..1 |
| **Status** | `:epizooticStatus` | `:LocalUnitEpizooticStatus` | 0..1 |
| **Datum**: Datum, ab dem der Seuchenstatus gültig ist | `:validFrom` | `xsd:date` | 0..1 |

</div>

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

**Zielklasse:** `:GroupNotification`

<div id="tbl-nodeshape-groupnotificationshape">

Tabelle 5: Eigenschaften Gruppenmeldung

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Örtliche Einheit**: BUR-Nummer der örtlichen Einheit | `:localUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 1..1 |
| **Herkunft**: BUR-Nummer der örtlichen Einheit von der das Tier kommt | `:originLocalUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 0..1 |
| **ID**: Eindeutiger Identifikator der Bewegung, der durch das System vergeben wird. | `:eventIdentifier` | `xsd:string` | 1..1 |
| **Nutztierart** | `:genus` | `:Genus` | 1..1 |
| **Gruppeninformation**: Bei Einstallungsmeldungen von Geflügel ist eine Gruppeninformation anzugeben | `:groupInformation` | `xsd:string` | 0..1 |
| **Meldungstyp** | `:notificationType` | `:NotificationType` | 1..1 |
| **Ereignisdatum**: Datum, an dem das Ereignis stattgefunden hat | `:eventDate` | `xsd:date` | 1..1 |
| **Meldedatum**: Datum, an dem das Ereignis gemeldet wurde | `:notificationDate` | `xsd:date` | 1..1 |
| **Anzahl**: Anzahl Tiere, die in einer Bewegung verstellt wurden (Schweine/Geflügel) | `:count` | `xsd:integer` | 0..1 |
| **Gewicht**: Gesamtgewicht in kg der Tiergruppe bei Schlachtungsmeldungen von Geflügel | `:weight` | `xsd:integer` | 0..1 |
| **Zweck**: Nutzungsart der Tiergruppe (bei Einzeltieren wird die Nutzungsart auf der Klasse «Einzeltier» geführt) | `:typeOfUse` | `:AnimalTypeOfUse` | 0..1 |
| **Alter**: Bei Einstallungsmeldungen von Geflügel ist das Alter in Wochen anzugeben | `:age` | `xsd:integer` | 0..1 |

</div>

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

**Zielklasse:** `:AnimalNotification`

<div id="tbl-nodeshape-animalnotificationshape">

Tabelle 6: Eigenschaften Meldung Einzeltier

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Identifikator**: Eine Meldung Einzeltier bezieht sich auf genau ein Einzeltier. | `:animal` | [`:Animal`](#sec-nodeshape-animalshape) | 1..1 |
| **Örtliche Einheit**: BUR-Nummer der örtlichen Einheit, auf die sich die Meldung bezieht | `:localUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 1..1 |
| **Herkunft**: BUR-Nummer der örtlichen Einheit von der das Tier kommt | `:originLocalUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 0..1 |
| **ID**: Eindeutiger Identifikator der Bewegung, der durch das System vergeben wird. | `:eventIdentifier` | `xsd:string` | 1..1 |
| **Nutztierart** | `:genus` | `:Genus` | 1..1 |
| **Meldungstyp** | `:notificationType` | `:NotificationType` | 1..1 |
| **Ereignisdatum**: Datum, an dem das Ereignis stattgefunden hat | `:eventDate` | `xsd:date` | 1..1 |
| **Meldedatum**: Datum, an dem das Ereignis gemeldet wurde | `:notificationDate` | `xsd:date` | 1..1 |

</div>

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

**Zielklasse:** `:LegalUnit`

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

**Zielklasse:** `:AnimalKeeper`

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

**Zielklasse:** `:LocalUnit`

<div id="tbl-nodeshape-localunitshape">

Tabelle 7: Eigenschaften Örtliche Einheit

| Beschreibung | Pfad | Typ | Kard. |
|:---|:---|:---|---:|
| **Tierhaltender**: Zuordnung der örtlichen Einheit zum Tierhaltenden. Nach eCH-0108, Kapitel 1.5, ist eine örtliche Einheit immer einer rechtlichen Einheit (bzw. einem Unternehmen) zugeordnet; die Stammdaten der örtlichen Einheit führen dafür das optionale Merkmal «mainUid» mit der UID der rechtlichen Haupteinheit. Da der Tierhaltende nach dem Objektkatalog nur eine Sonderform der rechtlichen Einheit ist, ist diese Zuordnung nicht zwingend. | `:animalKeeper` | [`:AnimalKeeper`](#sec-nodeshape-animalkeepershape) | 0..1 |

</div>

# Wertebereiche

Für einen Teil der Wertebereiche liegen noch keine französischen und
italienischen Bezeichnungen vor; die Bezeichnungen sind in Deutsch und
Englisch aufgeführt, so wie sie die Quellen liefern.
(<https://test-03-tvd-api-at.identitas.ch/open-api/v1.0>, 2026-09-24)

## Seuchenstatus Einzeltier

<div id="tbl-codelist-animalhealthstatus">

Tabelle 8: Werte des Wertebereichs Seuchenstatus Einzeltier

| Wert         | Bezeichnung    | Beschreibung       |
|:-------------|:---------------|:-------------------|
| `Blocked`    | gesperrt       | Typ: Seuchenstatus |
| `Free`       | frei           | Typ: Seuchenstatus |
| `NotTested`  | Nicht getestet | Typ: Seuchenstatus |
| `Vaccinated` | geimpft        | Typ: Impfstatus    |

</div>

## Tiergeschichtestatus

<div id="tbl-codelist-animalhistorystate">

Tabelle 9: Werte des Wertebereichs Tiergeschichtestatus

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

Tabelle 10: Werte des Wertebereichs Zweck (Rinder, Schafe, Ziegen)

| Wert    | Bezeichnung | Beschreibung                   |
|:--------|:------------|:-------------------------------|
| `Milk`  | Milch       | Milchkühe, -schafe und -ziegen |
| `Other` | Andere      |                                |

</div>

## Zweck (Equiden)

<div id="tbl-codelist-equidtypeofusage">

Tabelle 11: Werte des Wertebereichs Zweck (Equiden)

| Wert              | Bezeichnung | Beschreibung |
|:------------------|:------------|:-------------|
| `CompanionAnimal` | Heimtier    |              |
| `FarmAnimal`      | Nutztier    |              |

</div>

## Grössenkategorie

<div id="tbl-codelist-equidwithersclass">

Tabelle 12: Werte des Wertebereichs Grössenkategorie

| Wert                   | Bezeichnung               | Beschreibung |
|:-----------------------|:--------------------------|:-------------|
| `GreaterThan148cm`     | Widerristhöhe über 148 cm |              |
| `LessOrEqualThan148cm` | Widerristhöhe bis 148 cm  |              |

</div>

## Geschlecht

<div id="tbl-codelist-gender">

Tabelle 13: Werte des Wertebereichs Geschlecht

| Wert     | Bezeichnung | Beschreibung |
|:---------|:------------|:-------------|
| `Female` | Weiblich    |              |
| `Male`   | Männlich    |              |

</div>

## Nutztierart

<div id="tbl-codelist-genus">

Tabelle 14: Werte des Wertebereichs Nutztierart

| Wert | Bezeichnung | Beschreibung |
|:---|:---|:---|
| `Camelid` | Kameliden | Neuweltkameliden |
| `Cattle` | Rindvieh | Tiere der Rindergattung (Bos) und Wasserbüffel (Bubalus bubalis) |
| `Equid` | Equiden | Tiere der Pferdegattung (Pferd, Maultier, Maulesel, Esel) |
| `Game` | Wild | Wild in Gehegen |
| `Goat` | Ziegen |  |
| `Pig` | Schweine |  |
| `Poultry` | Geflügel |  |
| `Sheep` | Schafe |  |

</div>

## Typ Gesundheitsstatus

<div id="tbl-codelist-healthstatustype">

Tabelle 15: Werte des Wertebereichs Typ Gesundheitsstatus

| Wert                | Bezeichnung   | Beschreibung |
|:--------------------|:--------------|:-------------|
| `EpizooticStatus`   | Seuchenstatus |              |
| `LaboratoryResult`  | Laborergebnis |              |
| `RiskStatus`        | Risikostatus  |              |
| `VaccinationStatus` | Impfstatus    |              |

</div>

## Seuchenstatus örtliche Einheit

<div id="tbl-codelist-localunithealthstatus">

Tabelle 16: Werte des Wertebereichs Seuchenstatus örtliche Einheit

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

Tabelle 17: Werte des Wertebereichs Bewegungstyp

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

<div id="refs">

</div>

# Anhang B - Mitwirkung und Prüfung

# Anhang C - Abkürzungen und Glossar

<div id="tbl-glossary">

Tabelle 18: Glossar des Hilfsmittels eCH-0309

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">IRI</th>
<th style="text-align: left;">Begriff</th>
<th style="text-align: left;">Beschreibung</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/animalHolding"><code>term:animalHolding</code></a></td>
<td style="text-align: left;"><strong>Tierhaltung</strong></td>
<td style="text-align: left;">In der Tierverkehrsdatenbank werden
örtliche Einheiten «Tierhaltungen» genannt; sie sind zusätzlich über die
TVD-Nummer identifiziert.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/farmManager"><code>term:farmManager</code></a></td>
<td style="text-align: left;"><strong>Bewirtschafter</strong></td>
<td style="text-align: left;">Eine rechtliche Einheit, die das
Geschäftsrisiko für einen Betrieb trägt (LBV Art. 2). Der Tierhaltende
ist eine Form des Bewirtschafters, der Tiere hält (LBV Art. 11a).</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/homeHolding"><code>term:homeHolding</code></a></td>
<td style="text-align: left;"><strong>Stammbetrieb</strong></td>
<td style="text-align: left;">Bei Rindern kann ein Stammbetrieb
hinterlegt werden, um die Zugehörigkeit der Tiere zu einer Tierhaltung
abzubilden, wenn sich ein Tier auf einer anderen örtlichen Einheit
befindet.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/lindas"><code>term:lindas</code></a></td>
<td style="text-align: left;"><strong>Linked Data Service</strong>
(LINDAS)</td>
<td style="text-align: left;">Der offizielle Linked-Data-Dienst der
Schweizer Bundesverwaltung, der als Triple Store fungiert.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/rdf"><code>term:rdf</code></a></td>
<td style="text-align: left;"><strong>Resource Description
Framework</strong> (RDF)</td>
<td style="text-align: left;">Ein zentraler Standard des World Wide Web
Consortiums (W3C) zur Modellierung von Datenstrukturen im Web.
Informationen werden nicht in klassischen Tabellen, sondern als
vernetzte Graphen abgebildet.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/reportingPerson"><code>term:reportingPerson</code></a></td>
<td style="text-align: left;"><strong>Meldende Person</strong></td>
<td style="text-align: left;">Die Person oder die Personen, die für eine
Tierhaltung oder für einen Equideneigentümer Meldungen machen.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/triple"><code>term:triple</code></a></td>
<td style="text-align: left;"><strong>Tripel</strong></td>
<td style="text-align: left;"><p>Die Grundstruktur einer Aussage in RDF,
bestehend aus Subjekt, Prädikat und Objekt.</p>
<p><em>Oberbegriff</em>: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/rdf"><code>term:rdf</code></a></p></td>
</tr>
</tbody>
</table>

</div>

# Anhang D - Änderungen gegenüber der Vorversion

# Anhang E - Abbildungsverzeichnis

# Anhang F - Tabellenverzeichnis
