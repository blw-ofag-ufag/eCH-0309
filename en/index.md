# Auxiliary document: animal movement data

October 30, 2026

- [Note](#sec-note)
- [<span class="toc-section-number">1</span>
  Introduction](#sec-introduction)
  - [<span class="toc-section-number">1.1</span> Status](#sec-status)
  - [<span class="toc-section-number">1.2</span> Field of
    application](#sec-scope-of-application)
  - [<span class="toc-section-number">1.3</span> Animal movement
    reporting in Switzerland](#sec-animal-movement-reporting)
  - [<span class="toc-section-number">1.4</span>
    References](#sec-references)
- [<span class="toc-section-number">2</span>
  Namespaces](#sec-namespaces)
- [<span class="toc-section-number">3</span> Data
  Model](#sec-data-model)
  - [<span class="toc-section-number">3.1</span> Animal
    keeper](#sec-nodeshape-animalkeepershape)
  - [<span class="toc-section-number">3.2</span>
    Equid](#sec-nodeshape-equidshape)
  - [<span class="toc-section-number">3.3</span> Group
    notification](#sec-nodeshape-groupnotificationshape)
  - [<span class="toc-section-number">3.4</span> Health status of a
    local unit](#sec-nodeshape-localunithealthstatusshape)
  - [<span class="toc-section-number">3.5</span> Health status of an
    individual animal](#sec-nodeshape-animalhealthstatusshape)
  - [<span class="toc-section-number">3.6</span> Individual
    animal](#sec-nodeshape-animalshape)
  - [<span class="toc-section-number">3.7</span> Individual animal
    notification](#sec-nodeshape-animalnotificationshape)
  - [<span class="toc-section-number">3.8</span> Legal
    unit](#sec-nodeshape-legalunitshape)
  - [<span class="toc-section-number">3.9</span> Local
    unit](#sec-nodeshape-localunitshape)
- [<span class="toc-section-number">4</span> Code
  lists](#sec-code-lists)
  - [<span class="toc-section-number">4.1</span> Animal history
    state](#sec-codelist-animalhistorystate)
  - [<span class="toc-section-number">4.2</span> Equid notification
    state](#sec-codelist-equidnotificationstate)
  - [<span class="toc-section-number">4.3</span>
    Gender](#sec-codelist-gender)
  - [<span class="toc-section-number">4.4</span>
    Genus](#sec-codelist-genus)
  - [<span class="toc-section-number">4.5</span> Health status of a
    local unit](#sec-codelist-localunitepizooticstatus)
  - [<span class="toc-section-number">4.6</span> Health status of an
    individual animal](#sec-codelist-animalepizooticstatus)
  - [<span class="toc-section-number">4.7</span> Health status
    type](#sec-codelist-healthstatustype)
  - [<span class="toc-section-number">4.8</span> Notification
    type](#sec-codelist-notificationtype)
  - [<span class="toc-section-number">4.9</span> Type of use (cattle,
    sheep, goats)](#sec-codelist-animaltypeofuse)
  - [<span class="toc-section-number">4.10</span> Type of use
    (equids)](#sec-codelist-equidtypeofusage)
  - [<span class="toc-section-number">4.11</span> Withers
    class](#sec-codelist-equidwithersclass)
- [<span class="toc-section-number">5</span> Safety
  considerations](#sec-safety-consideration)
- [<span class="toc-section-number">6</span>
  Disclaimer](#sec-disclaimer)
- [<span class="toc-section-number">7</span>
  Copyrights](#sec-copyrights)
- [<span class="toc-section-number">8</span> Annex A -
  References](#sec-appendix-a)
- [<span class="toc-section-number">9</span> Annex B - Cooperation and
  Verification](#sec-appendix-b)
- [<span class="toc-section-number">10</span> Annex C - Abbreviations
  and Glossary](#sec-appendix-c)
- [<span class="toc-section-number">11</span> Annex D - Mapping to the
  TVD interface](#sec-appendix-d)
- [<span class="toc-section-number">12</span> Annex E - Changes in
  comparison to previous version](#sec-appendix-e)
- [<span class="toc-section-number">13</span> Annex F - Table of
  figures](#sec-appendix-f)
- [<span class="toc-section-number">14</span> Annex G - Table of
  tables](#sec-appendix-g)

# Note

This document uses a gender-neutral formulation when referring to
persons. This is based on the guidelines (German) of the Federal
Chancellery. Depending on the situation, paired forms (citizens),
gender-abstract forms (insured person), gender-neutral forms (insured
person) or paraphrases with-out personal reference are used. The generic
masculine (citizen) is not permitted. Full forms are used in continuous
texts, i.e. in texts consisting of formulated sentences. Short forms can
be used in ab-breviated text passages, namely in tables. The short form
is used with a slash but without an ellipsis (referent). Gender
asterisks and similar spellings are not used.

# Introduction

## Status

In progress: Use is permitted only within the technical group and the
Experts’ Committee.

## Field of application

This document describes the data of the animal movement database (TVD)
semantically, so that specialists without in-depth IT knowledge can also
gain a better understanding of the data.

## Animal movement reporting in Switzerland

In the 1990s, Swiss agriculture and the food industry were severely
challenged by the animal disease BSE. When the realisation that the
disease could be transmitted from animals to humans was confirmed in
1996, this caused great uncertainty. Expectations regarding the safety
of food of animal origin rose as a result, as did awareness of the
importance of food control. The approach «from stable to table» became
established. Risk-based surveillance, seamless traceability of farm
animals, control of animal movements, the obligation to declare origin
and quality controls throughout the production and processing chain have
formed the basis for a high standard of food safety ever since[^1].

The BSE experience led to the establishment of a national animal
movement database (TVD) in 1999. Article 7a and Articles 13–15 of the
Animal Diseases Act[^2] and Title 2, Sections 1, 1a and 2a of the Animal
Diseases Ordinance[^3] set out the basic legal provisions on the
identification/marking and the registration of farm animals as well as
the associated reporting obligations. They follow European legislation
on the same subject[^4] (Regulation (EU) 2016/429 on transmissible
animal diseases; Delegated Regulation (EU) 2019/2035 on establishments
keeping terrestrial animals and hatcheries, and on traceability).

While only cattle were subject to reporting from 1999, pigs and equids
followed from 2011, although pigs are to this day not reported as
individual animals. From 2014 and 2020 respectively, the obligation to
report to the TVD also applied to small ruminants (sheep and goats). At
the beginning, in 2014, this concerned only the slaughterhouses. Since
2014 there has also been an obligation to report poultry[^5]. Since
January 2020, keepers of small ruminants have been included in
individual animal reporting as well.[^6] The identification and marking
of cloven-hoofed animals with ear tags, the individual registration of
cattle, sheep and goats in the TVD, and the reporting of animal
arrivals, animal departures (an animal leaves a holding alive), births,
imports, exports, slaughter, on-farm slaughter and death (an animal is
deregistered as no longer living) are mandatory for all animal keepers
in Switzerland[^7]. Reports are also subject to statutory reporting
deadlines[^8].

The TVD is part of a system landscape spanning agriculture, veterinary
affairs and food safety. The central entry point is the Agate
portal[^9], with the agricultural policy information system AGIS[^10] at
its centre.

<!-- Abbildung «Systemlandschaft und Datenflüsse» wird nachgeliefert. -->

The Ordinance on Identitas AG and the animal movement database[^11]
(IdTVD-V) further sets out the content relating to animal movements, the
tasks of Identitas AG and the rights of access to the data. The
importance of identifying/marking farm animals goes far beyond the
subject of animal disease and therefore also found its way into
agricultural legislation[^12] (Agriculture Act LwG, Articles 165g, 177
and 185) and various associated ordinances. The animal movement data
have become an indispensable component in implementing agricultural
policy measures, for example animal-related direct payments[^13], the
determination of nutrient flows or agri-environmental monitoring[^14].
The data also serve as a basis for the structural survey of Swiss
agriculture[^15] and for agricultural statistics in general[^16].

Animal movement reporting quickly became established along the entire
food value chain as well. Programmes with animal welfare, traceability
and origin commitments rely on it[^17]. The variety of animal
information from animal movement reporting is also reflected in the
publicly available datasets of the Tierstatistik open data
platform[^18].

The technical interface description in this document is based on the
technical service description AnimalTracing v1.32 and on the openAPI
specification v. x.xx.

## References

Interfaces: AnimalTracing API, technical service description
AnimalTracing

# Namespaces

<a href="#tbl-namespaces" class="quarto-xref">Table 1</a> lists the
prefixes and namespaces used in this document. A prefix stands for a
namespace IRI, the common beginning of the IRIs of a vocabulary. The
Turtle specification describes how such [*prefixed
names*](https://www.w3.org/TR/turtle/#prefixed-name) are resolved
\[Turtle\].

<div id="tbl-namespaces">

Table 1: Namespaces used in eCH-0309 – Auxiliary document: animal
movement data.

| Prefix    | Namespace                                            |
|:----------|:-----------------------------------------------------|
| :         | https://agriculture.ld.admin.ch/eCH-0309/1/          |
| codelist: | https://agriculture.ld.admin.ch/eCH-0309/1/codelist/ |
| schema:   | http://schema.org/                                   |
| xsd:      | http://www.w3.org/2001/XMLSchema#                    |

</div>

# Data Model

<div id="fig-uml">

<img src="../assets/img/uml.png" class="lightbox"
style="width:100.0%" />

Figure 1: UML diagram of the eCH-0309 data model.

</div>

<a href="#fig-uml" class="quarto-xref">Figure 1</a> shows the classes of
the data model and their relationships. Each rectangle is a class and
the lines inside it are its attributes; the square brackets state how
many values are permitted, from the minimum to the maximum — `[1..1]`
means exactly one value, `[0..1]` at most one. An arrow leads to the
class being referred to and carries the name of the relationship;
several relationships between the same two classes share one arrow. The
line with the triangle connects a class to its superclass, at which the
triangle points: an equid is an individual animal and has, in addition
to the attributes shown, all attributes of the individual animal, which
are not repeated in the diagram. Attributes with a code list are drawn
like all the others; the permitted values are given in
<a href="#sec-code-lists" class="quarto-xref">Section 4</a>. The diagram
states neither datatypes nor descriptions; those follow in the sections
on the individual classes.

## Animal keeper

A farm manager (Bewirtschafter) is a legal unit as defined in eCH-0108
that bears the business risk for a farm (LBV Art. 2). The animal keeper
is a form of farm manager that keeps animals (LBV Art. 11a) and
therefore requires a local unit (animal holding). Responsibility for
reporting lies with the animal keeper for all animal categories except
equids; for equids it lies with the owner. The attributes are described
in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapters 3.1 and 3.2.

### Overview

<div class="ech-facts">

Shape  
[:AnimalKeeperShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalKeeperShape)

Target class  
[:AnimalKeeper](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalKeeper)

</div>

## Equid

Subclass of the class individual animal for animals of the equid genus
(horse, mule, hinny, donkey). All attributes of the class individual
animal also apply to equids; this class describes only the additional,
equid-specific information. For equids, responsibility for reporting
lies with the owner rather than with the animal keeper. An owner is the
legal unit that owns equids; the term is used for equid owners only.

### Overview

<div class="ech-facts">

Shape  
[:EquidShape](https://agriculture.ld.admin.ch/eCH-0309/1/EquidShape)

Target class  
[:Equid](https://agriculture.ld.admin.ch/eCH-0309/1/Equid)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 53%" />
<col style="width: 36%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Owner</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/owner">:owner</a>): The
legal unit that owns the equid. For equids, responsibility for reporting
lies with the owner rather than with the animal keeper.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-legalunitshape">Legal unit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Withers class</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/withersClass">:withersClass</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-equidwithersclass">Withers class</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Notification state</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationState">:notificationState</a>):
Equids carry a notification state of their own instead of the animal
history state.</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-equidnotificationstate">Equid notification
state</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type of use</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfEquidUsage">:typeOfEquidUsage</a>):
Equids use a code list of their own: companion animal or farm
animal.</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-equidtypeofusage">Type of use
(equids)</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Father</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/father">:father</a>):
Equids have no father; only the mother and the genetic mother are
recorded.</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">0..0</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Animal history state</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/historyState">:historyState</a>):
Not relevant for equids; the notification state takes its place.</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">0..0</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type of use (livestock)</strong>
(<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>):
Does not apply to equids; the equid-specific type of use takes its
place.</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">0..0</td>
</tr>
</tbody>
</table>

## Group notification

An event concerning a group of animals that cannot be identified
individually. Group notifications are recorded for animals of the
categories pigs and poultry; the individuals of such a group are
therefore not known. Events are reported by the natural persons of the
responsible legal unit, the animal keeper. They comprise housing
notifications for poultry, movement notifications for pigs, and
slaughter notifications for pigs (by head) and poultry groups (in kg).

### Overview

<div class="ech-facts">

Shape  
[:GroupNotificationShape](https://agriculture.ld.admin.ch/eCH-0309/1/GroupNotificationShape)

Target class  
[:GroupNotification](https://agriculture.ld.admin.ch/eCH-0309/1/GroupNotification)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 52%" />
<col style="width: 37%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Local unit</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localUnit">:localUnit</a>):
BUR number of the local unit</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-localunitshape">Local unit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Origin</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/originLocalUnit">:originLocalUnit</a>):
BUR number of the local unit the animal comes from</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-localunitshape">Local unit</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ID</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/id">:id</a>): Unique
identifier of the movement, assigned by the system.</td>
<td style="text-align: left;"><ul>
<li>Type: Text (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Genus</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/genus">:genus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-genus">Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Group information</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/groupInformation">:groupInformation</a>):
Group information must be given for housing notifications of
poultry</td>
<td style="text-align: left;"><ul>
<li>Type: Text (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Notification type</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationType">:notificationType</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-notificationtype">Notification type</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Event date</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/eventDate">:eventDate</a>):
Date on which the event took place</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Notification date</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationDate">:notificationDate</a>):
Date on which the event was reported</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Number</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/count">:count</a>):
Number of animals moved in one movement (pigs/poultry)</td>
<td style="text-align: left;"><ul>
<li>Type: Integer (<a
href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Weight</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/weight">:weight</a>):
Total weight in kg of the animal group for slaughter notifications of
poultry</td>
<td style="text-align: left;"><ul>
<li>Type: Integer (<a
href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type of use</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>):
Type of use of the animal group (for individual animals it is held on
the class «Einzeltier»)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-animaltypeofuse">Type of use (cattle, sheep,
goats)</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Age</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/age">:age</a>): For
housing notifications of poultry the age must be given in weeks</td>
<td style="text-align: left;"><ul>
<li>Type: Integer (<a
href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

## Health status of a local unit

Where animal disease events are of national significance, it is
essential that animal keepers are informed about movement bans and
disease status, so that the risk of spread through animal movements can
be minimised. Disease information recorded for a local unit. In addition
to the epizootic status of a local unit, vaccination, risk and
laboratory results can also be represented.

### Overview

<div class="ech-facts">

Shape  
[:LocalUnitHealthStatusShape](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitHealthStatusShape)

Target class  
[:LocalUnitHealthStatus](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitHealthStatus)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 53%" />
<col style="width: 36%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Local unit</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localUnit">:localUnit</a>):
BUR number of the local unit</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-localunitshape">Local unit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/healthStatusType">:healthStatusType</a>):
e.g. epizootic, vaccination or risk status</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-healthstatustype">Health status
type</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/epizooticStatus">:epizooticStatus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-localunitepizooticstatus">Health status of a
local unit</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Date</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/validFrom">:validFrom</a>):
Date from which the status is valid</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

## Health status of an individual animal

Disease information recorded for an individual animal. In addition to
the individual epizootic status, relevant vaccinations are recorded as
well.

### Overview

<div class="ech-facts">

Shape  
[:AnimalHealthStatusShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalHealthStatusShape)

Target class  
[:AnimalHealthStatus](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalHealthStatus)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 53%" />
<col style="width: 36%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Animal ID</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/animal">:animal</a>): A
health status of an individual animal refers to exactly one individual
animal.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-animalshape">Individual
animal</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/healthStatusType">:healthStatusType</a>):
e.g. epizootic, vaccination or risk status</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-healthstatustype">Health status
type</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/epizooticStatus">:epizooticStatus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-animalepizooticstatus">Health status of an
individual animal</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Date</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/validFrom">:validFrom</a>):
Date from which the status is valid, or the date of vaccination</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

## Individual animal

An individually identified farm animal. In the animal movement database,
animals of the categories cattle, sheep, goats and equids are recorded
as individual animals; they are uniquely identified by their ear tag
number, or by the UELN in the case of equids. No individual animals are
kept for pigs and poultry, only group notifications.

### Overview

<div class="ech-facts">

Shape  
[:AnimalShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalShape)

Target class  
[:Animal](https://agriculture.ld.admin.ch/eCH-0309/1/Animal)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 39%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Mother</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/mother">:mother</a>):
An individual animal has at most one mother animal.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-animalshape">Individual
animal</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Father</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/father">:father</a>):
An individual animal has at most one father animal.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-animalshape">Individual
animal</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Identifier</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/identifier">:identifier</a>):
Ear tag number, or UELN for equids</td>
<td style="text-align: left;"><ul>
<li>Type: Text (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
<li>Length: ≤ 15 characters</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Genus</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/genus">:genus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-genus">Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Gender</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/gender">:gender</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-gender">Gender</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Date of birth</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/dateOfBirth">:dateOfBirth</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Date of death</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/dateOfDeath">:dateOfDeath</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Animal history state</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/historyState">:historyState</a>):
State of the animal history at the date of the query. Not relevant for
equids; the obligation therefore applies only to the other individual
animals.</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-animalhistorystate">Animal history
state</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type of use</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-animaltypeofuse">Type of use (cattle, sheep,
goats)</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Castrated</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/castrated">:castrated</a>):
Whether the animal is castrated. Applies to equids as well.</td>
<td style="text-align: left;"><ul>
<li>Type: Boolean (<a
href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

### Rules

The animal history state is not relevant for equids. It is therefore
mandatory for every individual animal except equids.

## Individual animal notification

An event concerning an individual animal. Events comprise movement
notifications, notifications of basic data, changes to individual
attributes of the basic data as well as final notifications. A
notification always refers to the local unit at which the event took
place and may in addition state the local unit of origin. Events are
reported by the authorised persons, stating the animal holding to which
the notification refers; for equids they are reported by the authorised
persons of the responsible equid owner.

### Overview

<div class="ech-facts">

Shape  
[:AnimalNotificationShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalNotificationShape)

Target class  
[:AnimalNotification](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalNotification)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 53%" />
<col style="width: 37%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Identifier</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/animal">:animal</a>):
An individual animal notification refers to exactly one individual
animal.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-animalshape">Individual
animal</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Local unit</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localUnit">:localUnit</a>):
BUR number of the local unit to which the notification refers</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-localunitshape">Local unit</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Origin</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/originLocalUnit">:originLocalUnit</a>):
BUR number of the local unit the animal comes from</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-localunitshape">Local unit</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>ID</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/id">:id</a>): Unique
identifier of the movement, assigned by the system.</td>
<td style="text-align: left;"><ul>
<li>Type: Text (<a
href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Genus</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/genus">:genus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-genus">Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Notification type</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationType">:notificationType</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="http://schema.org/CategoryCode">schema:CategoryCode</a>, see code
list <a href="#sec-codelist-notificationtype">Notification type</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Event date</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/eventDate">:eventDate</a>):
Date on which the event took place</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Notification date</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationDate">:notificationDate</a>):
Date on which the event was reported</td>
<td style="text-align: left;"><ul>
<li>Type: Date (<a
href="http://www.w3.org/2001/XMLSchema#date">xsd:date</a>)</li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
</tbody>
</table>

## Legal unit

A legal unit as defined in eCH-0108 is a legal entity (e.g. a public
limited company or a limited liability company), a partnership (e.g. a
general partnership) or a self-employed natural person that is subject
to the federal act on the business identification number (UIDG) and has
an entry in the UID register. It identifies, for example, the taxable
entity for the tax authorities or the person liable for social insurance
contributions. The legal unit is identified by its UID. Only where the
enterprise is a «sole proprietorship» is the farm manager at the same
time a natural person. The master system for this data is the FSO’s UID
register; the agricultural information system obtains the data from that
register through an interface. The animal keeper and the equid owner are
the two forms of legal unit that occur in this document. The attributes
are described in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapters 3.1 and 3.2, and in
[eCH-0108](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2023-12-21_eCH-0108_V6.0.0_Unternehmensstammdaten%20Unternehmensregister.pdf),
chapter 3.1.

### Overview

<div class="ech-facts">

Shape  
[:LegalUnitShape](https://agriculture.ld.admin.ch/eCH-0309/1/LegalUnitShape)

Target class  
[:LegalUnit](https://agriculture.ld.admin.ch/eCH-0309/1/LegalUnit)

</div>

## Local unit

A local unit as defined in eCH-0108 is a facility at a given location
where an economic activity is carried out. A local unit has a BUR number
and is always assigned to a legal unit (or enterprise). The local unit
is identified by its BUR number. A local unit may consist of one or more
buildings. The EGID assigned to the BUR number refers to «the centre» of
the local unit, that is, its main building. In the TVD, local units are
called «animal holdings» and are additionally identified by their TVD
number. This definition is taken from
[eCH-0108](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2023-12-21_eCH-0108_V6.0.0_Unternehmensstammdaten%20Unternehmensregister.pdf),
chapter 1.5; the agriculture-specific additions are described in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapters 3.3 and 3.4.

### Overview

<div class="ech-facts">

Shape  
[:LocalUnitShape](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitShape)

Target class  
[:LocalUnit](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnit)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 55%" />
<col style="width: 32%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Details</th>
<th style="text-align: right;">Cardinality</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Animal keeper</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/animalKeeper">:animalKeeper</a>):
Assignment of the local unit to the animal keeper. According to
eCH-0108, chapter 1.5, a local unit is always assigned to a legal unit
(or enterprise); the master data of the local unit carries the optional
attribute «mainUid» holding the UID of the main legal unit. Because the
animal keeper is only a special form of the legal unit, this assignment
is not mandatory.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-animalkeepershape">Animal
keeper</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

# Code lists

The following code lists define the permitted values of the
corresponding attributes of the data model
(<a href="#sec-data-model" class="quarto-xref">Section 3</a>). Each code
list is modelled as a `schema:CategoryCodeSet` and each of its values as
a `schema:CategoryCode`. How the codes correspond to the enums of the
TVD interface is shown in [Annex D](#sec-appendix-d).

## Animal history state

State of the history of an individual animal on the query date. Not
relevant for equids.

<div id="tbl-codelist-animalhistorystate">

Table 2: Values of the code list Animal history state.

| Code | Name | Description |
|:---|:---|:---|
| [`Lost`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhistorystate/Lost) | Lost | The whereabouts of the animal are unknown |
| [`NotDefined`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhistorystate/NotDefined) | Not defined | No status has been set for the animal history |
| [`NotOk`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhistorystate/NotOk) | Not ok | The animal history contains errors or gaps |
| [`Ok`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhistorystate/Ok) | Ok | The animal history is complete and correct |
| [`TemporaryOk`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhistorystate/TemporaryOk) | Temporary ok | The animal history is provisionally considered correct |

</div>

## Equid notification state

State of the notifications about an equid: whether a change of location
or a transfer of ownership is still pending.

<div id="tbl-codelist-equidnotificationstate">

Table 3: Values of the code list Equid notification state.

| Code | Name | Description |
|:---|:---|:---|
| [`LocationChangeAndAcquisitionPending`](https://agriculture.ld.admin.ch/eCH-0309/1/equidnotificationstate/LocationChangeAndAcquisitionPending) | Change of location and transfer of ownership pending | Notifications of a change of location and of a transfer of ownership have not yet been completed |
| [`LocationChangePending`](https://agriculture.ld.admin.ch/eCH-0309/1/equidnotificationstate/LocationChangePending) | Change of location pending | A notification of a change of location has not yet been completed |
| [`Ok`](https://agriculture.ld.admin.ch/eCH-0309/1/equidnotificationstate/Ok) | OK | No notification is pending for the equid |
| [`OwnershipAcquisitionPending`](https://agriculture.ld.admin.ch/eCH-0309/1/equidnotificationstate/OwnershipAcquisitionPending) | Transfer of ownership pending | A notification of a transfer of ownership has not yet been completed |

</div>

## Gender

Sex of an individual animal.

<div id="tbl-codelist-gender">

Table 4: Values of the code list Gender.

| Code | Name | Description |
|:---|:---|:---|
| [`Female`](https://agriculture.ld.admin.ch/eCH-0309/1/gender/Female) | Female | Female animal |
| [`Male`](https://agriculture.ld.admin.ch/eCH-0309/1/gender/Male) | Male | Male animal |

</div>

## Genus

Livestock species whose animals are registered in the TVD and whose
movements are notified.

<div id="tbl-codelist-genus">

Table 5: Values of the code list Genus.

| Code | Name | Description |
|:---|:---|:---|
| [`Camelid`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Camelid) | Camelid | New World camelids |
| [`Cattle`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Cattle) | Cattle | Animals of the genus *Bos* and water buffalo (*Bubalus bubalis*) |
| [`Equid`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Equid) | Equid | Animals of the horse family (horse, mule, hinny, donkey) |
| [`Game`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Game) | Game | Farmed game in enclosures |
| [`Goat`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Goat) | Goat | Domestic goats |
| [`Pig`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Pig) | Pig | Domestic pigs |
| [`Poultry`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Poultry) | Poultry | Domestic poultry, e.g. chickens, turkeys, ducks and geese |
| [`Sheep`](https://agriculture.ld.admin.ch/eCH-0309/1/genus/Sheep) | Sheep | Domestic sheep |

</div>

## Health status of a local unit

Values of the health status of a local unit; their type is given in the
description.

<div id="tbl-codelist-localunitepizooticstatus">

Table 6: Values of the code list Health status of a local unit.

| Code | Name | Description |
|:---|:---|:---|
| [`Blocked`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Blocked) | Blocked | Type: epizootic status |
| [`Free`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Free) | Free | Type: epizootic status |
| [`High`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/High) | High | Type: risk status |
| [`Low`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Low) | Low | Type: risk status |
| [`Medium`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Medium) | Medium | Type: risk status |
| [`Negative`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Negative) | Negative | Type: laboratory result |
| [`NotTested`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/NotTested) | Not tested | Type: epizootic status |
| [`Positive`](https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Positive) | Positive | Type: laboratory result |

</div>

## Health status of an individual animal

Values of the health status of an individual animal; their type is given
in the description.

<div id="tbl-codelist-animalepizooticstatus">

Table 7: Values of the code list Health status of an individual animal.

| Code | Name | Description |
|:---|:---|:---|
| [`Blocked`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhealthstatus/Blocked) | Blocked | Type: epizootic status |
| [`Free`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhealthstatus/Free) | Free | Type: epizootic status |
| [`NotTested`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhealthstatus/NotTested) | Not tested | Type: epizootic status |
| [`Vaccinated`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhealthstatus/Vaccinated) | Vaccinated | Type: vaccination status |

</div>

## Health status type

Kind of health status of a local unit or an individual animal.

<div id="tbl-codelist-healthstatustype">

Table 8: Values of the code list Health status type.

| Code | Name | Description |
|:---|:---|:---|
| [`EpizooticStatus`](https://agriculture.ld.admin.ch/eCH-0309/1/healthstatustype/EpizooticStatus) | Epizootic status | Status regarding an animal disease, e.g. blocked or free |
| [`LaboratoryResult`](https://agriculture.ld.admin.ch/eCH-0309/1/healthstatustype/LaboratoryResult) | Laboratory result | Result of a laboratory test, e.g. positive or negative |
| [`RiskStatus`](https://agriculture.ld.admin.ch/eCH-0309/1/healthstatustype/RiskStatus) | Risk status | Rating of the disease risk, e.g. high, medium or low |
| [`VaccinationStatus`](https://agriculture.ld.admin.ch/eCH-0309/1/healthstatustype/VaccinationStatus) | Vaccination status | Whether vaccination against an animal disease has taken place |

</div>

## Notification type

Type of a notification about an individual animal, e.g. a movement, a
birth or a slaughter.

<div id="tbl-codelist-notificationtype">

Table 9: Values of the code list Notification type.

| Code | Name | Description |
|:---|:---|:---|
| [`Arrival`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Arrival) | Arrival | Not for equids |
| [`Birth`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Birth) | Birth | Live birth of an animal |
| [`DayStay`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/DayStay) | Day stay | Not for equids |
| [`DeathBirth`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/DeathBirth) | Stillbirth | Not for equids |
| [`Deceased`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Deceased) | Death | For equids: euthanasia |
| [`Export`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Export) | Export | For equids: transfer of ownership abroad |
| [`FirstRegistration`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/FirstRegistration) | First registration | For sheep and goats only |
| [`Import`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Import) | Import | Import of an animal from abroad |
| [`ImportAfterExport`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/ImportAfterExport) | Import after export | Not for equids |
| [`Leaving`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Leaving) | Departure | Not for equids |
| [`LocationChange`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/LocationChange) | Change of location | For equids only |
| [`OnFarmSlaughter`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/OnFarmSlaughter) | On-farm slaughter | Not for equids |
| [`Slaughter`](https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Slaughter) | Slaughter | Slaughter in a slaughterhouse |

</div>

## Type of use (cattle, sheep, goats)

Type of use of cattle, sheep and goats.

<div id="tbl-codelist-animaltypeofuse">

Table 10: Values of the code list Type of use (cattle, sheep, goats).

| Code | Name | Description |
|:---|:---|:---|
| [`Milk`](https://agriculture.ld.admin.ch/eCH-0309/1/animaltypeofuse/Milk) | Milk | Dairy cows, sheep and goats |
| [`Other`](https://agriculture.ld.admin.ch/eCH-0309/1/animaltypeofuse/Other) | Other | Any use other than milk production, e.g. meat production |

</div>

## Type of use (equids)

Type of use of an equid; it determines whether the equid may be
slaughtered for food production.

<div id="tbl-codelist-equidtypeofusage">

Table 11: Values of the code list Type of use (equids).

| Code | Name | Description |
|:---|:---|:---|
| [`CompanionAnimal`](https://agriculture.ld.admin.ch/eCH-0309/1/equidtypeofusage/CompanionAnimal) | Companion animal | Equid that must not be slaughtered for food production |
| [`FarmAnimal`](https://agriculture.ld.admin.ch/eCH-0309/1/equidtypeofusage/FarmAnimal) | Farm animal | Equid that may be slaughtered for food production |

</div>

## Withers class

Classification of equids into two categories by their height at the
withers.

<div id="tbl-codelist-equidwithersclass">

Table 12: Values of the code list Withers class.

| Code | Name | Description |
|:---|:---|:---|
| [`GreaterThan148cm`](https://agriculture.ld.admin.ch/eCH-0309/1/equidwithersclass/GreaterThan148cm) | Withers height above 148 cm | Equids with a height at the withers of more than 148 cm |
| [`LessOrEqualThan148cm`](https://agriculture.ld.admin.ch/eCH-0309/1/equidwithersclass/LessOrEqualThan148cm) | Withers height up to 148 cm | Equids with a height at the withers of at most 148 cm |

</div>

# Safety considerations

Information about the explicitly relevant legal bases or a note that
during the implementation the rele-vant legal bases must be observed.

# Disclaimer

eCH-standards which the registered association eCH provides the user
free of charge or which make reference to eCH shall only have the status
of recommendations. The registered association eCH will not be liable in
any event for any decisions made or measures taken by the user based on
these documents. The user will be responsible for verifying the
documents himself prior to their use and to seek advice if required.
eCH-standards can and shall not replace the technical, organizational or
legal advice in the individual case.

Documents, procedures, methods, products and standards that are made
reference to in eCH-standards are possibly protected by trademarks,
copyrights or patents. It is the exclusive responsibil-ity of the user
to obtain the necessary licences from the entitled persons and/or
organizations.

Although the registered association eCH has taken adequate care to
prepare the eCH-standards with due diligence, it cannot grant any
warranty or guarantee that the information and documents provided are
up-to-date, complete, true or without any errors. eCH reserves the right
to change the contents of the eCH-standards at any time and without
prior announcement.

Any liability for damage caused by the use of the eCH-standards by the
user shall be excluded to the extent legally admissible.

# Copyrights

Persons preparing eCH-standards shall remain the owners of their
intellectual property rights. These persons, however, obligate
themselves to provide their intellectual property rights or other rights
in third party intellectual property rights, to the extent possible, to
the relevant technical units and the registered association eCH for free
and for unlimited use and further development as part of the purpose of
the association.

The standards prepared by the technical units can be used, distributed
and developed further for free and to an unlimited extent by stating the
name of the respective author of eCH.

eCH-standards are fully documented and free of any restrictions of
licence and/or patent law. The associated documentation can be requested
for free. These provisions shall apply to the standards prepared by eCH
only, however, not to any standards or products of third parties which
include reference to eCH-standards. The standards include the relevant
references to third party rights.

# Annex A - References

<div id="refs" class="references csl-bib-body">

<div id="ref-Turtle" class="csl-entry">

<span class="csl-left-margin">\[Turtle\]
</span><span class="csl-right-inline">Beckett, David ; Berners-Lee,
Tim ; Prud’hommeaux, Eric ; Carothers, Gavin: *[RDF 1.1 Turtle – Terse
RDF Triple Language](https://www.w3.org/TR/turtle/)* (W3C
Recommendation) : World Wide Web Consortium (W3C), 2014</span>

</div>

</div>

# Annex B - Cooperation and Verification

# Annex C - Abbreviations and Glossary

<div id="tbl-glossary">

Table 13: Glossary of eCH-0309

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Term</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Animal holding</strong></td>
<td style="text-align: left;">In the animal movement database, local
units are called «animal holdings»; they are additionally identified by
their TVD number.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Farm manager</strong></td>
<td style="text-align: left;">A legal unit that bears the business risk
for a farm (LBV Art. 2). The animal keeper is a form of farm manager
that keeps animals (LBV Art. 11a).</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Home holding</strong></td>
<td style="text-align: left;">For cattle, a home holding can be recorded
in order to represent an animal’s affiliation to an animal holding while
the animal is located on another local unit.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Linked Data Service</strong>
(LINDAS)</td>
<td style="text-align: left;">The official Linked Data service of the
Swiss Federal Administration, acting as a triple store.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Reporting person</strong></td>
<td style="text-align: left;">The person or persons who make
notifications for an animal holding or for an equid owner.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Resource Description
Framework</strong> (RDF)</td>
<td style="text-align: left;">A central standard of the World Wide Web
Consortium (W3C) for modeling data structures on the Web. Information is
represented as networked graphs rather than in traditional tables.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Triple</strong></td>
<td style="text-align: left;"><p>The basic structure of a statement in
RDF, consisting of a subject, predicate, and object.</p>
<p><em>Broader</em>: Resource Description Framework</p></td>
</tr>
</tbody>
</table>

</div>

# Annex D - Mapping to the TVD interface

For the code lists in
<a href="#tbl-animaltracing-enums" class="quarto-xref">Table 14</a>, the
code of a value is the member of the same name of an enum of the TVD
interface AnimalTracing.

For notification type, health status type and the two epizootic status
code lists, the interface holds the notification types per livestock
species and the health statuses per disease in enums of their own,
partly under other names. The following tables show which members of the
interface correspond to a value; values without a corresponding value in
the interface are not listed.

<div id="tbl-animaltracing-enums">

Table 14: Enums of the TVD interface from which the code lists take
their codes.

| Code list | Enum of the interface |
|:---|:---|
| [Animal history state](#sec-codelist-animalhistorystate) | `EnumAnimalHistoryState` |
| [Equid notification state](#sec-codelist-equidnotificationstate) | `EnumEquidNotificationState` |
| [Gender](#sec-codelist-gender) | `EnumGender` |
| [Genus](#sec-codelist-genus) | `EnumGenus` |
| [Type of use (cattle, sheep, goats)](#sec-codelist-animaltypeofuse) | `EnumAnimalTypeOfUse` |
| [Type of use (equids)](#sec-codelist-equidtypeofusage) | `EquidTypeOfUsage` |
| [Withers class](#sec-codelist-equidwithersclass) | `EnumEquidWithersClass` |

</div>

<div id="tbl-animaltracing-codelist-localunitepizooticstatus">

Table 15: Corresponding values of the code list Health status of a local
unit in the TVD interface.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 41%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Code</th>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">TVD interface</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Blocked"><code>Blocked</code></a></td>
<td style="text-align: left;">Blocked</td>
<td style="text-align: left;"><code>BvdState.Blocked</code><br />
<code>FootRotState.Blocked</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/Free"><code>Free</code></a></td>
<td style="text-align: left;">Free</td>
<td style="text-align: left;"><code>FootRotState.Free</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/localunithealthstatus/NotTested"><code>NotTested</code></a></td>
<td style="text-align: left;">Not tested</td>
<td style="text-align: left;"><code>FootRotState.NotTested</code></td>
</tr>
</tbody>
</table>

</div>

<div id="tbl-animaltracing-codelist-animalepizooticstatus">

Table 16: Corresponding values of the code list Health status of an
individual animal in the TVD interface.

| Code | Name | TVD interface |
|:---|:---|:---|
| [`Vaccinated`](https://agriculture.ld.admin.ch/eCH-0309/1/animalhealthstatus/Vaccinated) | Vaccinated | `EnumCattleLsdState.Vaccinated` |

</div>

<div id="tbl-animaltracing-codelist-healthstatustype">

Table 17: Corresponding values of the code list Health status type in
the TVD interface.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 36%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Code</th>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">TVD interface</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/healthstatustype/EpizooticStatus"><code>EpizooticStatus</code></a></td>
<td style="text-align: left;">Epizootic status</td>
<td style="text-align: left;"><code>BvdState</code><br />
<code>FootRotState</code></td>
</tr>
</tbody>
</table>

</div>

<div id="tbl-animaltracing-codelist-notificationtype">

Table 18: Corresponding values of the code list Notification type in the
TVD interface.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 33%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Code</th>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">TVD interface</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Arrival"><code>Arrival</code></a></td>
<td style="text-align: left;">Arrival</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Arrival</code><br />
<code>EnumGoatNotificationType.Arrival</code><br />
<code>EnumSheepNotificationType.Arrival</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Birth"><code>Birth</code></a></td>
<td style="text-align: left;">Birth</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Birth</code><br />
<code>EnumGoatNotificationType.Birth</code><br />
<code>EnumSheepNotificationType.Birth</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/DeathBirth"><code>DeathBirth</code></a></td>
<td style="text-align: left;">Stillbirth</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.DeathBirth</code><br />
<code>EnumGoatNotificationType.DeathBirth</code><br />
<code>EnumSheepNotificationType.DeathBirth</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Deceased"><code>Deceased</code></a></td>
<td style="text-align: left;">Death</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Deceased</code><br />
<code>EnumGoatNotificationType.Deceased</code><br />
<code>EnumSheepNotificationType.Deceased</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Export"><code>Export</code></a></td>
<td style="text-align: left;">Export</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Export</code><br />
<code>EnumGoatNotificationType.Export</code><br />
<code>EnumSheepNotificationType.Export</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/FirstRegistration"><code>FirstRegistration</code></a></td>
<td style="text-align: left;">First registration</td>
<td
style="text-align: left;"><code>EnumGoatNotificationType.FirstRegistration</code><br />
<code>EnumSheepNotificationType.FirstRegistration</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Import"><code>Import</code></a></td>
<td style="text-align: left;">Import</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Import</code><br />
<code>EnumGoatNotificationType.Import</code><br />
<code>EnumSheepNotificationType.Import</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Leaving"><code>Leaving</code></a></td>
<td style="text-align: left;">Departure</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Leaving</code><br />
<code>EnumGoatNotificationType.Leaving</code><br />
<code>EnumSheepNotificationType.Leaving</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/OnFarmSlaughter"><code>OnFarmSlaughter</code></a></td>
<td style="text-align: left;">On-farm slaughter</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.YardSlaughter</code><br />
<code>EnumGoatNotificationType.OnFarmSlaughter</code><br />
<code>EnumSheepNotificationType.OnFarmSlaughter</code></td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationtype/Slaughter"><code>Slaughter</code></a></td>
<td style="text-align: left;">Slaughter</td>
<td
style="text-align: left;"><code>EnumCattleNotificationType.Slaughtering</code><br />
<code>EnumGoatNotificationType.Slaughter</code><br />
<code>EnumSheepNotificationType.Slaughter</code></td>
</tr>
</tbody>
</table>

</div>

# Annex E - Changes in comparison to previous version

# Annex F - Table of figures

# Annex G - Table of tables

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
