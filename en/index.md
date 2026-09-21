# eCH-1234 Template Quarto Document

September 21, 2026

- [Note](#sec-note)
- [<span class="toc-section-number">1</span>
  Introduction](#sec-introduction)
  - [<span class="toc-section-number">1.1</span> Status](#sec-status)
  - [<span class="toc-section-number">1.2</span> Scope of
    application](#sec-scope-of-application)
  - [<span class="toc-section-number">1.3</span> We can have
    sub-headings](#sec-example-subheading)
- [<span class="toc-section-number">2</span> Technical
  notes](#sec-technical-notes)
- [<span class="toc-section-number">3</span> Data
  Model](#sec-data-model)
- [<span class="toc-section-number">4</span> Data
  Retrieval](#sec-data-retrieval)
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

Approved: This document was approved by the Experts’ Committee. It has
normative power for the defined field of application in the determined
scope of application.

## Scope of application

The information in this chapter should provide the reader with a brief
overview of what this standard is intended for. Information about the
following matters may be helpful here.

## We can have sub-headings

And write some text.

### Also sub-sub-headings

And write some more text. Maybe even with a pretty image.

<div id="fig-example">

![](https://fastly.picsum.photos/id/653/536/354.jpg?hmac=3InR8I5KmwbdkPHehlM8BMPd_BDHG_RWZkxt_IkeQGY)

Figure 1: Always add some text to describe what the image shows.

</div>

When displaying diagrams, try to write them in Mermaid JS straight away;
this makes changes in the future or translations straightforward.

# Technical notes

We use the ROBOT CLI in our project (Jackson et al. 2019), especially
for it’s ability to run the HermiT reasoner (Glimm et al. 2014).

# Data Model

# Data Retrieval

The master and reference data underlying this document are available as
*Linked Data*.

The technological basis for this is the Resource Description Framework
(RDF, Cyganiak et al. 2014), a central standard of the World Wide Web
Consortium (W3C) for modeling data structures on the web. In RDF,
information is not represented in classic tables, but as interconnected
graphs. Each statement consists of a so-called triple (subject,
predicate, object). This structure enables a machine-readable,
interoperable, and cross-system unambiguous description of resources and
their relations to one another.

For the storage and publication of this RDF data,
[LINDAS](https://lindas.admin.ch/) (Linked Data Service) is used, the
official Linked Data service of the Swiss Federal Administration. LINDAS
functions as a so-called *triple store*, a specialized graph database
optimized for the efficient storage and querying of RDF triples, which
makes the data publicly available via a standardized interface.

The following chapter provides minimal instructions on how the data can
be queried and retrieved from LINDAS.

``` rq
BASE <https://agriculture.ld.admin.ch/eCH-1234/2/>
PREFIX schema: <http://schema.org/>
SELECT *
WHERE {
    ?genre a <Genre> ;
        schema:name ?name .
}
LIMIT 10
```

The underlying data itself is maintained on GitHub as Turtle files.

``` ttl
@base <https://agriculture.ld.admin.ch/eCH-1234/2/> .
@prefix genre: <https://agriculture.ld.admin.ch/eCH-1234/2/genre/> .
@prefix schema: <http://schema.org/> .

genre:1 a <Genre> ;
    schema:name "Rock" .

genre:2 a <Genre> ;
    schema:name "Jazz" .

genre:3 a <Genre> ;
    schema:name "Metal" ;
    schema:partOf genre:1 .
```

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

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-cyganiak2014rdf11" class="csl-entry">

Cyganiak, Richard, David Wood, and Markus Lanthaler. 2014. *RDF 1.1
Concepts and Abstract Syntax*. W3C Recommendation. World Wide Web
Consortium (W3C). <https://www.w3.org/TR/rdf11-concepts/>.

</div>

<div id="ref-glimm2014hermit" class="csl-entry">

Glimm, Birte, Ian Horrocks, Boris Motik, Giorgos Stoilos, and Zhe Wang.
2014. “HermiT: An OWL 2 Reasoner.” *Journal of Automated Reasoning* 53
(3): 245–69.

</div>

<div id="ref-jackson2019robot" class="csl-entry">

Jackson, Rebecca C, James P Balhoff, Eric Douglass, Nomi L Harris,
Christopher J Mungall, and James A Overton. 2019. “ROBOT: A Tool for
Automating Ontology Workflows.” *BMC Bioinformatics* 20 (1): 407.
<https://doi.org/10.1186/s12859-019-3002-3>.

</div>

</div>

# Annex B - Cooperation and Verification

# Annex C - Abbreviations and Glossary

<div id="tbl-glossary">

Table 1: Glossary of the eCH-0309 standard

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 25%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">IRI</th>
<th style="text-align: left;">Term</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/lindas"><code>term:lindas</code></a></td>
<td style="text-align: left;"><strong>Linked Data Service</strong>
(LINDAS)</td>
<td style="text-align: left;">The official Linked Data service of the
Swiss Federal Administration, acting as a triple store.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/rdf"><code>term:rdf</code></a></td>
<td style="text-align: left;"><strong>Resource Description
Framework</strong> (RDF)</td>
<td style="text-align: left;">A central standard of the World Wide Web
Consortium (W3C) for modeling data structures on the Web. Information is
represented as networked graphs rather than in traditional tables.</td>
</tr>
<tr>
<td style="text-align: left;"><a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/triple"><code>term:triple</code></a></td>
<td style="text-align: left;"><strong>Triple</strong></td>
<td style="text-align: left;"><p>The basic structure of a statement in
RDF, consisting of a subject, predicate, and object.</p>
<p><em>broader</em>: <a
href="https://agriculture.ld.admin.ch/eCH-0309/1/term/rdf"><code>term:rdf</code></a></p></td>
</tr>
</tbody>
</table>

</div>

# Annex D - Changes in comparison to previous version

# Annex E - Table of figures

# Annex F - Table of tables
