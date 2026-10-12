# Auxiliary document: animal movement data

October 12, 2026

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
  - [<span class="toc-section-number">4.1</span> Health status of an
    individual animal](#sec-codelist-animalhealthstatus)
  - [<span class="toc-section-number">4.2</span> Animal history
    state](#sec-codelist-animalhistorystate)
  - [<span class="toc-section-number">4.3</span> Type of use (cattle,
    sheep, goats)](#sec-codelist-animaltypeofuse)
  - [<span class="toc-section-number">4.4</span> Type of use
    (equids)](#sec-codelist-equidtypeofusage)
  - [<span class="toc-section-number">4.5</span> Withers
    class](#sec-codelist-equidwithersclass)
  - [<span class="toc-section-number">4.6</span>
    Gender](#sec-codelist-gender)
  - [<span class="toc-section-number">4.7</span>
    Genus](#sec-codelist-genus)
  - [<span class="toc-section-number">4.8</span> Health status
    type](#sec-codelist-healthstatustype)
  - [<span class="toc-section-number">4.9</span> Health status of a
    local unit](#sec-codelist-localunithealthstatus)
  - [<span class="toc-section-number">4.10</span> Notification
    type](#sec-codelist-notificationtype)
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
- [<span class="toc-section-number">11</span> Annex D - Changes in
  comparison to previous version](#sec-appendix-d)
- [<span class="toc-section-number">12</span> Annex E - Table of
  figures](#sec-appendix-e)
- [<span class="toc-section-number">13</span> Annex F - Table of
  tables](#sec-appendix-f)

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
formed the basis for a high standard of food safety ever since.

The BSE experience led to the establishment of a national animal
movement database (TVD) in 1999. Article 7a and Articles 13–15 of the
Animal Diseases Act and Title 2, Sections 1, 1a and 2a of the Animal
Diseases Ordinance set out the basic legal provisions on the
identification/marking and the registration of farm animals as well as
the associated reporting obligations. They follow European legislation
on the same subject (Regulation (EU) 2016/429 on transmissible animal
diseases; Delegated Regulation (EU) 2019/2035 on establishments keeping
terrestrial animals and hatcheries, and on traceability).

While only cattle were subject to reporting from 1999, pigs and equids
followed from 2011, although pigs are to this day not reported as
individual animals. From 2014 and 2020 respectively, the obligation to
report to the TVD also applied to small ruminants (sheep and goats). At
the beginning, in 2014, this concerned only the slaughterhouses. Since
2014 there has also been an obligation to report poultry. Since January
2020, keepers of small ruminants have been included in individual animal
reporting as well. The identification and marking of cloven-hoofed
animals with ear tags, the individual registration of cattle, sheep and
goats in the TVD, and the reporting of animal arrivals, animal
departures (an animal leaves a holding alive), births, imports, exports,
slaughter, on-farm slaughter and death (an animal is deregistered as no
longer living) are mandatory for all animal keepers in Switzerland.

The TVD is part of a system landscape spanning agriculture, veterinary
affairs and food safety. The central entry point is the Agate portal,
with the agricultural policy information system AGIS at its centre.

<!-- Abbildung «Systemlandschaft und Datenflüsse» wird nachgeliefert. -->

The Ordinance on Identitas AG and the animal movement database (IdTVD-V)
further sets out the content relating to animal movements, the tasks of
Identitas AG and the rights of access to the data. The importance of
identifying/marking farm animals goes far beyond the subject of animal
disease and therefore also found its way into agricultural legislation
(Agriculture Act LwG, Articles 165g, 177 and 185) and various associated
ordinances. The animal movement data have become an indispensable
component in implementing agricultural policy measures, for example
animal-related direct payments, the determination of nutrient flows or
agri-environmental monitoring. The data also serve as a basis for the
structural survey of Swiss agriculture and for agricultural statistics
in general.

Animal movement reporting quickly became established along the entire
food value chain as well. Programmes with animal welfare, traceability
and origin commitments rely on it. The variety of animal information
from animal movement reporting is also reflected in the publicly
available datasets of the Tierstatistik open data platform.

The technical interface description in this document is based on the
technical service description AnimalTracing v1.32 and on the openAPI
specification v. x.xx.

## References

Interfaces: AnimalTracing API, technical service description
AnimalTracing

NB: the names of the classes described in chapter 3 do not match the
ServiceOperations in AnimalTracing, because the semantic description is
intended to provide an overview of the data content and is more detailed
than the service description.

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

| Prefix | Namespace                                   |
|:-------|:--------------------------------------------|
| :      | https://agriculture.ld.admin.ch/eCH-0309/1/ |
| xsd:   | http://www.w3.org/2001/XMLSchema#           |

</div>

# Data Model

<div id="fig-uml">

<img src="../assets/img/uml.png" class="lightbox"
style="width:100.0%" />

Figure 1: UML diagram of the eCH-0309 data model.

</div>

## Animal keeper

A farm manager (Bewirtschafter) is a legal unit as defined in eCH-0108
that bears the business risk for a farm (LBV Art. 2). The animal keeper
is a form of farm manager that keeps animals (LBV Art. 11a) and
therefore requires a local unit (animal holding). Responsibility for
reporting lies with the animal keeper for all animal categories except
equids; for equids it lies with the owner (chapter 3.1.1 of the tool).
The attributes are described in
[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapters 3.1 and 3.2.

### Overview

<div class="ech-facts">

Shape  
[:AnimalKeeperShape](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalKeeperShape)

Target class  
[:AnimalKeeper](https://agriculture.ld.admin.ch/eCH-0309/1/AnimalKeeper)

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Rules (SPARQL)

#### An animal keeper requires at least one local unit (chapter 3.1.1 of the tool). This rule is taken from the semantic description, not from the object catalogue.

``` sparql
SELECT $this
WHERE {
    FILTER NOT EXISTS { ?localUnit :animalKeeper $this . }
}
```

## Equid

Subclass of the class individual animal for animals of the equid genus
(horse, mule, hinny, donkey). All attributes of the class individual
animal also apply to equids; this class describes only the additional,
equid-specific information. For equids, responsibility for reporting
lies with the owner rather than with the animal keeper. An owner is the
legal unit that owns equids; the term is used for equid owners only
(chapter 3.1.1 of the tool).

### Overview

<div class="ech-facts">

Shape  
[:EquidShape](https://agriculture.ld.admin.ch/eCH-0309/1/EquidShape)

Target class  
[:Equid](https://agriculture.ld.admin.ch/eCH-0309/1/Equid)

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 43%" />
<col style="width: 47%" />
<col style="width: 8%" />
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
lies with the owner rather than with the animal keeper (chapter 3.1.1 of
the tool).</td>
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/EquidWithersClass">:EquidWithersClass</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
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
This class has no counterpart in the AnimalTracing openAPI
specification, because pigs and poultry are not covered there.

### Overview

<div class="ech-facts">

Shape  
[:GroupNotificationShape](https://agriculture.ld.admin.ch/eCH-0309/1/GroupNotificationShape)

Target class  
[:GroupNotification](https://agriculture.ld.admin.ch/eCH-0309/1/GroupNotification)

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 46%" />
<col style="width: 44%" />
<col style="width: 8%" />
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/eventIdentifier">:eventIdentifier</a>):
Unique identifier of the movement, assigned by the system.</td>
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/Genus">:Genus</a></li>
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/NotificationType">:NotificationType</a></li>
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalTypeOfUse">:AnimalTypeOfUse</a></li>
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
laboratory results can also be represented. The AnimalTracing openAPI
specification has no dedicated class for this; there the corresponding
information is held as attributes of the local unit.

### Overview

<div class="ech-facts">

Shape  
[:LocalUnitHealthStatusShape](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitHealthStatusShape)

Target class  
[:LocalUnitHealthStatus](https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitHealthStatus)

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:100%;">
<colgroup>
<col style="width: 42%" />
<col style="width: 49%" />
<col style="width: 7%" />
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/HealthStatusType">:HealthStatusType</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/epizooticStatus">:epizooticStatus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/LocalUnitEpizooticStatus">:LocalUnitEpizooticStatus</a></li>
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

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 44%" />
<col style="width: 47%" />
<col style="width: 7%" />
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/HealthStatusType">:HealthStatusType</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/epizooticStatus">:epizooticStatus</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalEpizooticStatus">:AnimalEpizooticStatus</a></li>
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

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 46%" />
<col style="width: 45%" />
<col style="width: 7%" />
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/Genus">:Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Gender</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/gender">:gender</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/Gender">:Gender</a></li>
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/animalHistoryState">:animalHistoryState</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalHistoryState">:AnimalHistoryState</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Type of use</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/typeOfUse">:typeOfUse</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/AnimalTypeOfUse">:AnimalTypeOfUse</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Castrated</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/castrated">:castrated</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: Boolean (<a
href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a>)</li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

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

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 46%" />
<col style="width: 44%" />
<col style="width: 8%" />
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/eventIdentifier">:eventIdentifier</a>):
Unique identifier of the movement, assigned by the system.</td>
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
href="https://agriculture.ld.admin.ch/eCH-0309/1/Genus">:Genus</a></li>
</ul></td>
<td style="text-align: right;">1..1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Notification type</strong> (<a
href="https://agriculture.ld.admin.ch/eCH-0309/1/notificationType">:notificationType</a>)</td>
<td style="text-align: left;"><ul>
<li>Type: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/NotificationType">:NotificationType</a></li>
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
the two forms of legal unit that occur in this Hilfsmittel (chapter
3.1.1 of the tool). The attributes are described in
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

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

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

Closed  
No (further properties are allowed)

Data access  
None (transactional data, not part of the published graph)

</div>

### Properties

<table style="width:99%;">
<colgroup>
<col style="width: 56%" />
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
object catalogue treats the animal keeper only as a special form of the
legal unit, this assignment is not mandatory.</td>
<td style="text-align: left;"><ul>
<li>Type: <a href="#sec-nodeshape-animalkeepershape">Animal
keeper</a></li>
</ul></td>
<td style="text-align: right;">0..1</td>
</tr>
</tbody>
</table>

# Code lists

For some of these code lists no French or Italian designations are
available yet; the designations below are given in German and English,
as provided by the sources.
(<https://test-03-tvd-api-at.identitas.ch/open-api/v1.0>, 2026-09-24)

## Health status of an individual animal

<div id="tbl-codelist-animalhealthstatus">

Table 2: Values of the code list Health status of an individual animal

| Value        | Designation | Description              |
|:-------------|:------------|:-------------------------|
| `Blocked`    | Blocked     | Type: epizootic status   |
| `Free`       | Free        | Type: epizootic status   |
| `NotTested`  | Not tested  | Type: epizootic status   |
| `Vaccinated` | Vaccinated  | Type: vaccination status |

</div>

## Animal history state

<div id="tbl-codelist-animalhistorystate">

Table 3: Values of the code list Animal history state

| Value         | Designation  | Description |
|:--------------|:-------------|:------------|
| `Lost`        | Lost         |             |
| `NotDefined`  | Not defined  |             |
| `NotOk`       | Not ok       |             |
| `Ok`          | Ok           |             |
| `TemporaryOk` | Temporary ok |             |

</div>

## Type of use (cattle, sheep, goats)

<div id="tbl-codelist-animaltypeofuse">

Table 4: Values of the code list Type of use (cattle, sheep, goats)

| Value   | Designation | Description                    |
|:--------|:------------|:-------------------------------|
| `Milk`  | Milk        | Milchkühe, -schafe und -ziegen |
| `Other` | Other       |                                |

</div>

## Type of use (equids)

<div id="tbl-codelist-equidtypeofusage">

Table 5: Values of the code list Type of use (equids)

| Value             | Designation      | Description |
|:------------------|:-----------------|:------------|
| `CompanionAnimal` | Companion animal |             |
| `FarmAnimal`      | Farm animal      |             |

</div>

## Withers class

<div id="tbl-codelist-equidwithersclass">

Table 6: Values of the code list Withers class

| Value                  | Designation                 | Description |
|:-----------------------|:----------------------------|:------------|
| `GreaterThan148cm`     | Withers height above 148 cm |             |
| `LessOrEqualThan148cm` | Withers height up to 148 cm |             |

</div>

## Gender

<div id="tbl-codelist-gender">

Table 7: Values of the code list Gender

| Value    | Designation | Description |
|:---------|:------------|:------------|
| `Female` | Female      |             |
| `Male`   | Male        |             |

</div>

## Genus

<div id="tbl-codelist-genus">

Table 8: Values of the code list Genus

| Value | Designation | Description |
|:---|:---|:---|
| `Camelid` | Camelid | Neuweltkameliden |
| `Cattle` | Cattle | Tiere der Rindergattung (Bos) und Wasserbüffel (Bubalus bubalis) |
| `Equid` | Equid | Tiere der Pferdegattung (Pferd, Maultier, Maulesel, Esel) |
| `Game` | Game | Wild in Gehegen |
| `Goat` | Goat |  |
| `Pig` | Pig |  |
| `Poultry` | Poultry |  |
| `Sheep` | Sheep |  |

</div>

## Health status type

<div id="tbl-codelist-healthstatustype">

Table 9: Values of the code list Health status type

| Value               | Designation        | Description |
|:--------------------|:-------------------|:------------|
| `EpizooticStatus`   | Epizootic status   |             |
| `LaboratoryResult`  | Laboratory result  |             |
| `RiskStatus`        | Risk status        |             |
| `VaccinationStatus` | Vaccination status |             |

</div>

## Health status of a local unit

<div id="tbl-codelist-localunithealthstatus">

Table 10: Values of the code list Health status of a local unit

| Value       | Designation | Description             |
|:------------|:------------|:------------------------|
| `Blocked`   | Blocked     | Type: epizootic status  |
| `Free`      | Free        | Type: epizootic status  |
| `High`      | High        | Type: risk status       |
| `Low`       | Low         | Type: risk status       |
| `Medium`    | Medium      | Type: risk status       |
| `Negative`  | Negative    | Type: laboratory result |
| `NotTested` | Not tested  | Type: epizootic status  |
| `Positive`  | Positive    | Type: laboratory result |

</div>

## Notification type

<div id="tbl-codelist-notificationtype">

Table 11: Values of the code list Notification type

| Value | Designation | Description |
|:---|:---|:---|
| `Arrival` | Arrival | Not for equids |
| `Birth` | Birth |  |
| `DayStay` | Day stay | Not for equids |
| `DeathBirth` | Stillbirth | Not for equids |
| `Deceased` | Death | For equids: euthanasia |
| `Export` | Export | For equids: transfer of ownership abroad |
| `FirstRegistration` | First registration |  |
| `Import` | Import |  |
| `ImportAfterExport` | Import after export | Not for equids |
| `Leaving` | Departure | Not for equids |
| `LocationChange` | Change of location | For equids only |
| `OnFarmSlaughter` | On-farm slaughter | Not for equids |
| `Slaughter` | Slaughter |  |

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

Table 12: Glossary of eCH-0309

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

# Annex D - Changes in comparison to previous version

# Annex E - Table of figures

# Annex F - Table of tables
