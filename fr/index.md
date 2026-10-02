# Document auxiliaire : données sur le trafic des animaux

2 octobre 2026

- [Remarque](#sec-note)
- [<span class="toc-section-number">1</span>
  Introduction](#sec-introduction)
  - [<span class="toc-section-number">1.1</span> Statut](#sec-status)
  - [<span class="toc-section-number">1.2</span> Domaine
    d’application](#sec-scope-of-application)
  - [<span class="toc-section-number">1.3</span> La notification du
    trafic des animaux en Suisse](#sec-animal-movement-reporting)
  - [<span class="toc-section-number">1.4</span>
    Renvois](#sec-references)
- [<span class="toc-section-number">2</span> Modèle de
  données](#sec-data-model)
  - [<span class="toc-section-number">2.1</span> Animal
    individuel](#sec-nodeshape-animalshape)
  - [<span class="toc-section-number">2.2</span> Détenteur
    d’animaux](#sec-nodeshape-animalkeepershape)
  - [<span class="toc-section-number">2.3</span> Notification d’animal
    individuel](#sec-nodeshape-animalnotificationshape)
  - [<span class="toc-section-number">2.4</span> Notification de
    groupe](#sec-nodeshape-groupnotificationshape)
  - [<span class="toc-section-number">2.5</span> Unité
    juridique](#sec-nodeshape-legalunitshape)
  - [<span class="toc-section-number">2.6</span> Unité
    locale](#sec-nodeshape-localunitshape)
  - [<span class="toc-section-number">2.7</span>
    Équidé](#sec-nodeshape-equidshape)
  - [<span class="toc-section-number">2.8</span> État sanitaire de
    l’animal individuel](#sec-nodeshape-animalhealthstatusshape)
  - [<span class="toc-section-number">2.9</span> État sanitaire de
    l’unité locale](#sec-nodeshape-localunithealthstatusshape)
- [<span class="toc-section-number">3</span> Domaines de
  valeurs](#sec-code-lists)
  - [<span class="toc-section-number">3.1</span> État sanitaire de
    l’animal individuel](#sec-codelist-animalhealthstatus)
  - [<span class="toc-section-number">3.2</span> Statut de l’historique
    de l’animal](#sec-codelist-animalhistorystate)
  - [<span class="toc-section-number">3.3</span> Type d’utilisation
    (bovins, ovins, caprins)](#sec-codelist-animaltypeofuse)
  - [<span class="toc-section-number">3.4</span> Type d’utilisation
    (équidés)](#sec-codelist-equidtypeofusage)
  - [<span class="toc-section-number">3.5</span> Catégorie de
    taille](#sec-codelist-equidwithersclass)
  - [<span class="toc-section-number">3.6</span>
    Sexe](#sec-codelist-gender)
  - [<span class="toc-section-number">3.7</span> Espèce d’animal de
    rente](#sec-codelist-genus)
  - [<span class="toc-section-number">3.8</span> Type d’état
    sanitaire](#sec-codelist-healthstatustype)
  - [<span class="toc-section-number">3.9</span> État sanitaire de
    l’unité locale](#sec-codelist-localunithealthstatus)
  - [<span class="toc-section-number">3.10</span> Type de
    mouvement](#sec-codelist-notificationtype)
- [<span class="toc-section-number">4</span> Considérations de
  sécurité](#sec-safety-consideration)
- [<span class="toc-section-number">5</span> Clause de
  non-responsabilité](#sec-disclaimer)
- [<span class="toc-section-number">6</span> Droits
  d’auteur](#sec-copyrights)
- [<span class="toc-section-number">7</span> Annexe A -
  Références](#sec-appendix-a)
- [<span class="toc-section-number">8</span> Annexe B - Collaboration et
  Vérification](#sec-appendix-b)
- [<span class="toc-section-number">9</span> Annexe C - Abréviations et
  glossaire](#sec-appendix-c)
- [<span class="toc-section-number">10</span> Annexe D - Modifications
  par rapport à la version précédente](#sec-appendix-d)
- [<span class="toc-section-number">11</span> Annexe E - Table des
  illustrations](#sec-appendix-e)
- [<span class="toc-section-number">12</span> Annexe F - Liste des
  tableaux](#sec-appendix-f)

# Remarque

Dans le présent document, les désignations de personnes sont formulées
de manière épicène (neutre du point de vue du genre). Le guide de la
Chancellerie fédérale sert de base. Selon la situation, on utilise des
formulations paires (citoyennes et citoyens), des formes abstraites
(personne assurée), des formes neutres ou des périphrases sans référence
à la personne. L’usage du masculin générique n’est pas autorisé. Les
formes complètes sont employées dans le texte continu, c’est-à-dire dans
les textes composés de phrases rédigées. Dans les passages de texte
raccourcis, notamment dans les tableaux, des formes abrégées peuvent
être utilisées. La forme abrégée s’utilise alors avec une barre oblique,
mais sans trait d’omission (rapporteur/euse). L’astérisque de genre et
les typographies similaires ne sont pas utilisés.

# Introduction

## Statut

En cours : L’utilisation n’est autorisée qu’au sein du groupe spécialisé
et du comité d’experts.

## Domaine d’application

Le présent document décrit sémantiquement les données de la banque de
données sur le trafic des animaux (BDTA), afin de permettre également
aux spécialistes sans connaissances informatiques approfondies de mieux
comprendre ces données.

## La notification du trafic des animaux en Suisse

Dans les années 1990, l’agriculture et l’industrie alimentaire suisses
ont été fortement mises à l’épreuve par l’épizootie «ESB». Lorsque la
transmissibilité de la maladie de l’animal à l’être humain s’est
confirmée en 1996, cela a provoqué une grande incertitude. Les attentes
en matière de sécurité des denrées alimentaires d’origine animale ont
augmenté en conséquence, de même que la conscience de l’importance du
contrôle des denrées alimentaires. L’approche «de l’étable à la table»
s’est imposée. La surveillance basée sur les risques, la traçabilité
sans faille des animaux de rente, le contrôle du trafic des animaux,
l’obligation de déclarer la provenance ainsi que les contrôles de
qualité tout au long de la chaîne de production et de transformation
constituent depuis lors la base d’un niveau élevé de sécurité
alimentaire.

L’expérience de l’ESB a conduit en 1999 à la création d’une banque de
données nationale sur le trafic des animaux (BDTA). L’article 7a ainsi
que les articles 13 à 15 de la loi sur les épizooties et le titre 2,
sections 1, 1a et 2a de l’ordonnance sur les épizooties énoncent les
dispositions légales fondamentales relatives à l’identification/au
marquage et à l’enregistrement des animaux de rente ainsi qu’aux
obligations d’annonce correspondantes. Elles s’alignent sur la
législation européenne en la matière (règlement (UE) 2016/429 sur les
maladies animales transmissibles; règlement délégué (UE) 2019/2035
concernant les établissements détenant des animaux terrestres et les
couvoirs ainsi que la traçabilité).

Si seuls les bovins étaient soumis à l’obligation d’annonce à partir de
1999, les porcs et les équidés ont suivi dès 2011, même si les porcs ne
font aujourd’hui encore pas l’objet d’annonces par animal individuel. À
partir de 2014, respectivement de 2020, l’obligation d’annonce à la BDTA
s’est également appliquée aux petits ruminants (moutons et chèvres). Au
début, en 2014, elle ne concernait que les abattoirs. Depuis 2014, il
existe également une obligation d’annonce pour la volaille. Depuis
janvier 2020, les détenteurs de petits ruminants sont eux aussi intégrés
dans le système d’annonce des animaux individuels. L’identification et
le marquage des animaux à onglons au moyen de marques auriculaires,
l’enregistrement individuel des bovins, des moutons et des chèvres dans
la BDTA, ainsi que l’annonce des entrées, des sorties (l’animal quitte
vivant une unité d’élevage), des naissances, des importations, des
exportations, des abattages, des abattages à la ferme et des morts
(l’animal est désannoncé comme n’étant plus vivant) sont obligatoires
pour tous les détenteurs d’animaux en Suisse.

La BDTA fait partie d’un paysage systémique regroupant l’agriculture,
les affaires vétérinaires et la sécurité alimentaire. Le portail Agate
en constitue la porte d’entrée centrale, avec au cœur le système
d’information sur la politique agricole AGIS.

<!-- Abbildung «Systemlandschaft und Datenflüsse» wird nachgeliefert. -->

L’ordonnance sur Identitas SA et la banque de données sur le trafic des
animaux (OId-BDTA) précise les contenus relatifs au trafic des animaux,
les tâches d’Identitas SA ainsi que les droits d’accès aux données.
L’importance de l’identification/du marquage des animaux de rente
dépasse largement la problématique des épizooties et a donc également
trouvé sa place dans la législation agricole (loi sur l’agriculture
LAgr, art. 165g, 177 et 185) et dans diverses ordonnances associées. Les
données issues du trafic des animaux sont devenues un élément
indispensable de la mise en œuvre des mesures de politique agricole, par
exemple les paiements directs liés aux animaux, la détermination des
flux d’éléments nutritifs ou le monitoring agroenvironnemental. Ces
données servent en outre de base au relevé des structures de
l’agriculture suisse et, plus généralement, à la statistique agricole.

Le système d’annonce du trafic des animaux s’est rapidement imposé tout
au long de la chaîne de valeur alimentaire. Les programmes assortis de
promesses en matière de bien-être animal, de traçabilité et de
provenance s’y appuient. La diversité des informations sur les animaux
issues du système d’annonce du trafic des animaux se reflète également
dans les jeux de données publiquement disponibles de la plateforme Open
Data Tierstatistik.

La description technique des interfaces figurant dans le présent
document se fonde sur la description technique de service AnimalTracing
v1.32 ainsi que sur la spécification openAPI v. x.xx.

## Renvois

Interfaces: AnimalTracing API, description technique de service
AnimalTracing

NB: les noms des classes décrites au chapitre 3 ne correspondent pas aux
ServiceOperations d’AnimalTracing, car la description sémantique doit
donner une vue d’ensemble du contenu des données et présente un degré de
détail plus fin que la description de service.

# Modèle de données

<div id="fig-uml">

<img src="../assets/img/uml.png" class="lightbox"
style="width:100.0%" />

Figure 1: Diagramme UML du modèle de données eCH-0309.

</div>

## Animal individuel

Un animal de rente identifié individuellement. Dans la banque de données
sur le trafic des animaux, les animaux des catégories bovins, ovins,
caprins et équidés sont enregistrés comme animaux individuels ; ils sont
identifiés de manière univoque par leur numéro de marque auriculaire, ou
par l’UELN pour les équidés. Aucun animal individuel n’est tenu pour les
porcs et la volaille, mais uniquement des notifications de groupe.

**Classe cible:** `:Animal`

<div id="tbl-nodeshape-animalshape">

Table 1: propriétés Animal individuel

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **Mère**: Un animal individuel a au plus une mère. | `:mother` | [`:Animal`](#sec-nodeshape-animalshape) | 0..1 |
| **Père**: Un animal individuel a au plus un père. | `:father` | [`:Animal`](#sec-nodeshape-animalshape) | 0..1 |
| **Identifiant**: Numéro de marque auriculaire, UELN pour les équidés | `:identifier` | `xsd:string` | 1..1 |
| **Espèce d’animal de rente** | `:genus` | `:Genus` | 1..1 |
| **Sexe** | `:gender` | `:Gender` | 0..1 |
| **Date de naissance** | `:dateOfBirth` | `xsd:date` | 0..1 |
| **Date de mort** | `:dateOfDeath` | `xsd:date` | 0..1 |
| **Statut de l’historique de l’animal** | `:animalHistoryState` | `:AnimalHistoryState` | 1..1 |
| **Type d’utilisation** | `:typeOfUse` | `:AnimalTypeOfUse` | 0..1 |
| **Castré** | `:castrated` | `xsd:boolean` | 0..1 |

</div>

## Détenteur d’animaux

Un exploitant est une unité juridique au sens de l’eCH-0108 qui assume
le risque économique d’une exploitation (OTerm art. 2). Le détenteur
d’animaux est une forme d’exploitant qui détient des animaux (OTerm art.
11a) ; il lui faut donc une unité locale (unité d’élevage). La
responsabilité des notifications incombe au détenteur d’animaux pour
toutes les catégories d’animaux à l’exception des équidés ; pour les
équidés, elle incombe au propriétaire ou à la propriétaire (chapitre
3.1.1 de l’outil). Les attributs sont décrits dans
l’[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapitres 3.1 et 3.2.

**Classe cible:** `:AnimalKeeper`

## Notification d’animal individuel

Un événement concernant un animal individuel. Sont considérées comme
événements les notifications de mouvement, les notifications de données
de base, les modifications d’attributs individuels des données de base
ainsi que les notifications finales. Une notification se rapporte
toujours à l’unité locale où l’événement a eu lieu et peut en outre
indiquer l’unité locale de provenance. Les événements sont annoncés par
les personnes autorisées, avec indication de l’unité d’élevage à
laquelle la notification se rapporte ; pour les équidés, ils sont
annoncés par les personnes autorisées du propriétaire d’équidés
responsable.

**Classe cible:** `:AnimalNotification`

<div id="tbl-nodeshape-animalnotificationshape">

Table 2: propriétés Notification d’animal individuel

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **Identifiant**: Une notification d’animal individuel se rapporte à exactement un animal individuel. | `:animal` | [`:Animal`](#sec-nodeshape-animalshape) | 1..1 |
| **Unité locale**: Numéro REE de l’unité locale à laquelle se rapporte la notification | `:localUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 1..1 |
| **Provenance**: Numéro REE de l’unité locale d’où provient l’animal | `:originLocalUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 0..1 |
| **ID**: Identifiant univoque du mouvement, attribué par le système. | `:eventIdentifier` | `xsd:string` | 1..1 |
| **Espèce d’animal de rente** | `:genus` | `:Genus` | 1..1 |
| **Type de mouvement** | `:notificationType` | `:NotificationType` | 1..1 |
| **Date de l’événement**: Date à laquelle l’événement a eu lieu | `:eventDate` | `xsd:date` | 1..1 |
| **Date d’annonce**: Date à laquelle l’événement a été annoncé | `:notificationDate` | `xsd:date` | 1..1 |

</div>

## Notification de groupe

Un événement concernant un groupe d’animaux qui ne peuvent pas être
identifiés individuellement. Les notifications de groupe sont
enregistrées pour les animaux des catégories porcs et volaille ; les
individus d’un tel groupe ne sont donc pas connus. Les événements sont
annoncés par les personnes physiques de l’unité juridique responsable,
le détenteur d’animaux. Ils comprennent les annonces de mise en place
pour la volaille, les annonces de mouvement pour les porcs ainsi que les
annonces d’abattage de porcs (en têtes) et de groupes de volaille (en
kg). Cette classe n’a pas d’équivalent dans la spécification openAPI
d’AnimalTracing, car les porcs et la volaille n’y sont pas représentés.

**Classe cible:** `:GroupNotification`

<div id="tbl-nodeshape-groupnotificationshape">

Table 3: propriétés Notification de groupe

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **Unité locale**: Numéro REE de l’unité locale | `:localUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 1..1 |
| **Provenance**: Numéro REE de l’unité locale d’où provient l’animal | `:originLocalUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 0..1 |
| **ID**: Identifiant univoque du mouvement, attribué par le système. | `:eventIdentifier` | `xsd:string` | 1..1 |
| **Espèce d’animal de rente** | `:genus` | `:Genus` | 1..1 |
| **Information de groupe**: Une information de groupe doit être indiquée pour les annonces de mise en place de volaille | `:groupInformation` | `xsd:string` | 0..1 |
| **Type de mouvement** | `:notificationType` | `:NotificationType` | 1..1 |
| **Date de l’événement**: Date à laquelle l’événement a eu lieu | `:eventDate` | `xsd:date` | 1..1 |
| **Date d’annonce**: Date à laquelle l’événement a été annoncé | `:notificationDate` | `xsd:date` | 1..1 |
| **Nombre**: Nombre d’animaux déplacés lors d’un mouvement (porcs/volaille) | `:count` | `xsd:integer` | 0..1 |
| **Poids**: Poids total en kg du groupe d’animaux pour les annonces d’abattage de volaille | `:weight` | `xsd:integer` | 0..1 |
| **Type d’utilisation**: Type d’utilisation du groupe d’animaux (pour les animaux individuels il figure sur la classe «Einzeltier») | `:typeOfUse` | `:AnimalTypeOfUse` | 0..1 |
| **Âge**: Pour les annonces de mise en place de volaille, l’âge doit être indiqué en semaines | `:age` | `xsd:integer` | 0..1 |

</div>

## Unité juridique

L’unité juridique au sens de l’eCH-0108 est une personne morale (p. ex.
société anonyme, Sàrl), une société de personnes (p. ex. société en nom
collectif) ou une personne physique exerçant une activité indépendante
qui est soumise à la loi fédérale sur le numéro d’identification des
entreprises (LIDE) et qui est inscrite au registre IDE. Elle identifie
par exemple le sujet fiscal pour les autorités fiscales ou la personne
assujettie aux cotisations d’assurances sociales. L’unité juridique est
identifiée par son IDE. Ce n’est que lorsque l’entreprise est une
«entreprise individuelle» que l’exploitant est en même temps une
personne physique. Le système maître de ces données est le registre IDE
de l’OFS ; le système d’information agricole obtient les données de ce
registre via une interface. Le détenteur d’animaux et le propriétaire
d’équidés sont les deux formes d’unité juridique qui apparaissent dans
le présent Hilfsmittel (chapitre 3.1.1 de l’outil). Les attributs sont
décrits dans
l’[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapitres 3.1 et 3.2, ainsi que dans
l’[eCH-0108](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2023-12-21_eCH-0108_V6.0.0_Unternehmensstammdaten%20Unternehmensregister.pdf),
chapitre 3.1.

**Classe cible:** `:LegalUnit`

## Unité locale

Une unité locale au sens de l’eCH-0108 est une installation située en un
lieu déterminé où s’exerce une activité économique. Une unité locale
possède un numéro REE et est toujours rattachée à une unité juridique
(ou entreprise). L’unité locale est identifiée par son numéro REE. Une
unité locale peut se composer d’un ou de plusieurs bâtiments. L’EGID
attribué au numéro REE se rapporte au «centre» de l’unité locale,
respectivement à son bâtiment principal. Dans la BDTA, les unités
locales sont appelées «unités d’élevage» et sont en outre identifiées
par leur numéro BDTA. Cette définition est tirée de
l’[eCH-0108](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2023-12-21_eCH-0108_V6.0.0_Unternehmensstammdaten%20Unternehmensregister.pdf),
chapitre 1.5 ; les compléments spécifiques à l’agriculture sont décrits
dans
l’[eCH-0261](https://ech.ch/sites/default/files/imce/eCH-Dossier/eCH-Dossier_PDF_Publikationen/Hauptdokument/STAN_d_DEF_2024-02_07_eCH-0261_V1.0.0_Datenstandard_Agrardaten_Stammdaten.pdf),
chapitres 3.3 et 3.4.

**Classe cible:** `:LocalUnit`

<div id="tbl-nodeshape-localunitshape">

Table 4: propriétés Unité locale

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **Détenteur d’animaux**: Rattachement de l’unité locale au détenteur d’animaux. Selon l’eCH-0108, chapitre 1.5, une unité locale est toujours rattachée à une unité juridique (ou entreprise) ; les données de base de l’unité locale comportent à cet effet l’attribut facultatif «mainUid» contenant l’IDE de l’unité juridique principale. Le détenteur d’animaux n’étant, selon le catalogue d’objets, qu’une forme particulière de l’unité juridique, ce rattachement n’est pas obligatoire. | `:animalKeeper` | [`:AnimalKeeper`](#sec-nodeshape-animalkeepershape) | 0..1 |

</div>

## Équidé

Sous-classe de la classe animal individuel pour les animaux du genre
équidé (cheval, mulet, bardot, âne). Tous les attributs de la classe
animal individuel s’appliquent également aux équidés ; cette classe ne
décrit que les informations supplémentaires propres aux équidés. Pour
les équidés, la responsabilité des notifications incombe au propriétaire
et non au détenteur d’animaux. Un propriétaire est l’unité juridique qui
détient des équidés en propriété ; le terme n’est utilisé que pour les
propriétaires d’équidés (chapitre 3.1.1 de l’outil).

**Classe cible:** `:Equid`

<div id="tbl-nodeshape-equidshape">

Table 5: propriétés Équidé

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **Propriétaire**: L’unité juridique qui détient l’équidé en propriété. Pour les équidés, la responsabilité des notifications incombe au propriétaire et non au détenteur d’animaux (chapitre 3.1.1 de l’outil). | `:owner` | [`:LegalUnit`](#sec-nodeshape-legalunitshape) | 1..1 |
| **Catégorie de taille** | `:withersClass` | `:EquidWithersClass` | 1..1 |

</div>

## État sanitaire de l’animal individuel

Une information épizootique enregistrée sur un animal individuel. Outre
le statut épizootique individuel, les vaccinations pertinentes sont
également enregistrées.

**Classe cible:** `:AnimalHealthStatus`

<div id="tbl-nodeshape-animalhealthstatusshape">

Table 6: propriétés État sanitaire de l’animal individuel

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **ID de l’animal**: Un état sanitaire de l’animal individuel se rapporte à exactement un animal individuel. | `:animal` | [`:Animal`](#sec-nodeshape-animalshape) | 1..1 |
| **Type**: p. ex. statut épizootique, vaccinal ou de risque | `:healthStatusType` | `:HealthStatusType` | 0..1 |
| **Statut** | `:epizooticStatus` | `:AnimalEpizooticStatus` | 0..1 |
| **Date**: Date à partir de laquelle le statut est valable, ou la date de vaccination | `:validFrom` | `xsd:date` | 0..1 |

</div>

## État sanitaire de l’unité locale

Lorsque des épizooties revêtent une importance nationale, il est
essentiel que les détenteurs d’animaux soient informés des interdictions
de déplacement et du statut épizootique, afin de minimiser le risque de
propagation par le trafic des animaux. Une information épizootique
enregistrée sur une unité locale. Outre le statut épizootique d’une
unité locale, les résultats de vaccination, de risque et de laboratoire
peuvent également être représentés. La spécification openAPI
d’AnimalTracing ne prévoit pas de classe distincte à cet effet ; les
informations correspondantes y sont des attributs de l’unité locale.

**Classe cible:** `:LocalUnitHealthStatus`

<div id="tbl-nodeshape-localunithealthstatusshape">

Table 7: propriétés État sanitaire de l’unité locale

| Description | Chemin | Type | Card. |
|:---|:---|:---|---:|
| **Unité locale**: Numéro REE de l’unité locale | `:localUnit` | [`:LocalUnit`](#sec-nodeshape-localunitshape) | 1..1 |
| **Type**: p. ex. statut épizootique, vaccinal ou de risque | `:healthStatusType` | `:HealthStatusType` | 0..1 |
| **Statut** | `:epizooticStatus` | `:LocalUnitEpizooticStatus` | 0..1 |
| **Date**: Date à partir de laquelle le statut est valable | `:validFrom` | `xsd:date` | 0..1 |

</div>

# Domaines de valeurs

Pour une partie de ces domaines de valeurs, aucune désignation française
ou italienne n’est encore disponible ; les désignations sont indiquées
en allemand et en anglais, telles que les sources les fournissent.
(<https://test-03-tvd-api-at.identitas.ch/open-api/v1.0>, 2026-09-24)

## État sanitaire de l’animal individuel

<div id="tbl-codelist-animalhealthstatus">

Table 8: Valeurs du domaine de valeurs État sanitaire de l’animal
individuel

| Valeur       | Désignation | Description               |
|:-------------|:------------|:--------------------------|
| `Blocked`    | Bloqué      | Type : statut épizootique |
| `Free`       | Libre       | Type : statut épizootique |
| `NotTested`  | Non testé   | Type : statut épizootique |
| `Vaccinated` | Vacciné     | Type : statut vaccinal    |

</div>

## Statut de l’historique de l’animal

<div id="tbl-codelist-animalhistorystate">

Table 9: Valeurs du domaine de valeurs Statut de l’historique de
l’animal

| Valeur        | Désignation     | Description |
|:--------------|:----------------|:------------|
| `Lost`        | Verschollen     |             |
| `NotDefined`  | Nicht definiert |             |
| `NotOk`       | Fehlerhaft      |             |
| `Ok`          | OK              |             |
| `TemporaryOk` | Temporär OK     |             |

</div>

## Type d’utilisation (bovins, ovins, caprins)

<div id="tbl-codelist-animaltypeofuse">

Table 10: Valeurs du domaine de valeurs Type d’utilisation (bovins,
ovins, caprins)

| Valeur  | Désignation | Description                    |
|:--------|:------------|:-------------------------------|
| `Milk`  | Milch       | Milchkühe, -schafe und -ziegen |
| `Other` | Andere      |                                |

</div>

## Type d’utilisation (équidés)

<div id="tbl-codelist-equidtypeofusage">

Table 11: Valeurs du domaine de valeurs Type d’utilisation (équidés)

| Valeur            | Désignation | Description |
|:------------------|:------------|:------------|
| `CompanionAnimal` | Heimtier    |             |
| `FarmAnimal`      | Nutztier    |             |

</div>

## Catégorie de taille

<div id="tbl-codelist-equidwithersclass">

Table 12: Valeurs du domaine de valeurs Catégorie de taille

| Valeur                 | Désignation                           | Description |
|:-----------------------|:--------------------------------------|:------------|
| `GreaterThan148cm`     | Hauteur au garrot supérieure à 148 cm |             |
| `LessOrEqualThan148cm` | Hauteur au garrot jusqu’à 148 cm      |             |

</div>

## Sexe

<div id="tbl-codelist-gender">

Table 13: Valeurs du domaine de valeurs Sexe

| Valeur   | Désignation | Description |
|:---------|:------------|:------------|
| `Female` | Weiblich    |             |
| `Male`   | Männlich    |             |

</div>

## Espèce d’animal de rente

<div id="tbl-codelist-genus">

Table 14: Valeurs du domaine de valeurs Espèce d’animal de rente

| Valeur | Désignation | Description |
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

## Type d’état sanitaire

<div id="tbl-codelist-healthstatustype">

Table 15: Valeurs du domaine de valeurs Type d’état sanitaire

| Valeur              | Désignation             | Description |
|:--------------------|:------------------------|:------------|
| `EpizooticStatus`   | Statut épizootique      |             |
| `LaboratoryResult`  | Résultat de laboratoire |             |
| `RiskStatus`        | Statut de risque        |             |
| `VaccinationStatus` | Statut vaccinal         |             |

</div>

## État sanitaire de l’unité locale

<div id="tbl-codelist-localunithealthstatus">

Table 16: Valeurs du domaine de valeurs État sanitaire de l’unité locale

| Valeur      | Désignation | Description                    |
|:------------|:------------|:-------------------------------|
| `Blocked`   | Bloqué      | Type : statut épizootique      |
| `Free`      | Libre       | Type : statut épizootique      |
| `High`      | Élevé       | Type : statut de risque        |
| `Low`       | Faible      | Type : statut de risque        |
| `Medium`    | Moyen       | Type : statut de risque        |
| `Negative`  | Négatif     | Type : résultat de laboratoire |
| `NotTested` | Non testé   | Type : statut épizootique      |
| `Positive`  | Positif     | Type : résultat de laboratoire |

</div>

## Type de mouvement

<div id="tbl-codelist-notificationtype">

Table 17: Valeurs du domaine de valeurs Type de mouvement

| Valeur | Désignation | Description |
|:---|:---|:---|
| `Arrival` | Entrée | Pas pour les équidés |
| `Birth` | Naissance |  |
| `DayStay` | Séjour à la journée | Pas pour les équidés |
| `DeathBirth` | Mortinaissance | Pas pour les équidés |
| `Deceased` | Mort | Pour les équidés : euthanasie |
| `Export` | Exportation | Pour les équidés : cession de propriété à l’étranger |
| `FirstRegistration` | Premier enregistrement |  |
| `Import` | Importation |  |
| `ImportAfterExport` | Importation après exportation | Pas pour les équidés |
| `Leaving` | Sortie | Pas pour les équidés |
| `LocationChange` | Changement de lieu | Uniquement pour les équidés |
| `OnFarmSlaughter` | Abattage à la ferme | Pas pour les équidés |
| `Slaughter` | Abattage |  |

</div>

# Considérations de sécurité

Informations sur les bases légales expressément déterminantes ou
remarque indiquant que les bases légales pertinentes doivent être
respectées lors de la mise en œuvre.

# Clause de non-responsabilité

Les standards eCH que l’association eCH met gratuitement à la
disposition de l’utilisateur ou qui font référence à eCH n’ont que le
statut de recommandations. L’association eCH décline toute
responsabilité pour les décisions ou mesures prises par l’utilisateur
sur la base de ces documents. Il incombe à l’utilisateur de vérifier
lui-même les documents avant de les utiliser et, si nécessaire, de
demander des conseils professionnels. Les standards eCH ne peuvent et ne
doivent pas remplacer les conseils techniques, organisationnels ou
juridiques dans un cas individuel.

Les documents, procédures, méthodes, produits et standards auxquels il
est fait référence dans les standards eCH sont potentiellement protégés
par des droits de marque, d’auteur ou de brevet. Il est de la
responsabilité exclusive de l’utilisateur d’obtenir les licences
nécessaires auprès des ayants droit et/ou des organisations.

Bien que l’association eCH ait apporté le soin nécessaire à
l’élaboration des standards eCH, elle ne peut garantir ni assurer que
les informations et documents fournis sont actuels, complets, exacts ou
exempts d’erreurs. eCH se réserve le droit de modifier le contenu de ses
standards à tout moment et sans préavis.

Toute responsabilité pour les dommages causés par l’utilisation des
standards eCH par l’utilisateur est exclue dans les limites autorisées
par la loi.

# Droits d’auteur

Les personnes qui élaborent les standards eCH restent propriétaires de
leurs droits de propriété intellectuelle. Ces personnes s’engagent
toutefois à mettre leurs droits de propriété intellectuelle ou d’autres
droits sur des droits de propriété intellectuelle de tiers, dans la
mesure du possible, à la disposition des groupes d’experts concernés et
de l’association eCH, et ce gratuitement et pour une utilisation ainsi
qu’un développement ultérieur illimités dans le cadre du but de
l’association.

Les standards élaborés par les groupes d’experts peuvent être utilisés,
diffusés et développés gratuitement et de manière illimitée en
mentionnant le nom de l’auteur respectif d’eCH.

Les standards eCH sont entièrement documentés et libres de toute
restriction de droit de licence et/ou de brevet. La documentation
correspondante peut être demandée gratuitement. Ces dispositions ne
s’appliquent toutefois qu’aux standards élaborés par eCH, et non aux
standards ou produits de tiers qui font référence aux standards eCH. Les
standards contiennent les références correspondantes aux droits de
tiers.

# Annexe A - Références

<div id="refs">

</div>

# Annexe B - Collaboration et Vérification

# Annexe C - Abréviations et glossaire

<div id="tbl-glossary">

Table 18: Glossaire de l’eCH-0309

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">IRI</th>
<th style="text-align: left;">Terme</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/animalHolding"><code>term:animalHolding</code></a></td>
<td style="text-align: left;"><strong>Unité d’élevage</strong></td>
<td style="text-align: left;">Dans la banque de données sur le trafic
des animaux, les unités locales sont appelées «unités d’élevage»; elles
sont en outre identifiées par leur numéro BDTA.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/farmManager"><code>term:farmManager</code></a></td>
<td style="text-align: left;"><strong>Exploitant</strong></td>
<td style="text-align: left;">Une unité juridique qui assume le risque
économique d’une exploitation (OTerm art. 2). Le détenteur d’animaux est
une forme d’exploitant qui détient des animaux (OTerm art. 11a).</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/homeHolding"><code>term:homeHolding</code></a></td>
<td style="text-align: left;"><strong>Exploitation de
référence</strong></td>
<td style="text-align: left;">Pour les bovins, une exploitation de
référence peut être enregistrée afin de représenter l’appartenance des
animaux à une unité d’élevage lorsqu’un animal se trouve sur une autre
unité locale.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/lindas"><code>term:lindas</code></a></td>
<td style="text-align: left;"><strong>Linked Data Service</strong>
(LINDAS)</td>
<td style="text-align: left;">Le service officiel de données liées de
l’administration fédérale suisse, fonctionnant comme un triple store
(magasin de triplets).</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/rdf"><code>term:rdf</code></a></td>
<td style="text-align: left;"><strong>Resource Description
Framework</strong> (RDF)</td>
<td style="text-align: left;">Une norme centrale du World Wide Web
Consortium (W3C) pour la modélisation des structures de données sur le
Web. Les informations ne sont pas représentées dans des tableaux
classiques, mais sous forme de graphes interconnectés.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/reportingPerson"><code>term:reportingPerson</code></a></td>
<td style="text-align: left;"><strong>Personne déclarante</strong></td>
<td style="text-align: left;">La personne ou les personnes qui
effectuent les annonces pour une unité d’élevage ou pour un propriétaire
d’équidés.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/triple"><code>term:triple</code></a></td>
<td style="text-align: left;"><strong>Triplet</strong></td>
<td style="text-align: left;"><p>La structure de base d’une déclaration
en RDF, composée d’un sujet, d’un prédicat et d’un objet.</p>
<p><em>plus générique</em>: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/rdf"><code>term:rdf</code></a></p></td>
</tr>
</tbody>
</table>

</div>

# Annexe D - Modifications par rapport à la version précédente

# Annexe E - Table des illustrations

# Annexe F - Liste des tableaux
