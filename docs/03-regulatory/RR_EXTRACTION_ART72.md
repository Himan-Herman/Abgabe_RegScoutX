# Systematische RR-Extraktion — SRC-002 Art. 72

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` |
| Quellenbereich | `SRC-002#Art.72` |
| Rechtsstand | konsolidierter Stand 27.07.2026 gemäß [SOURCES.md](SOURCES.md) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.11 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Extraktionsstand. Sie vergibt **keine** permanenten `RR`-Identifikatoren; die Kandidaten tragen ausschließlich die temporären Kennungen `A72-A` bis `A72-K`. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finaler Gesamtstand

| Stufe | Anzahl |
| --- | --- |
| Finale neue Gap-`RR`-Kandidaten | **11** — `A72-A` bis `A72-K` |
| davon regulär | 8 |
| davon conditional | 3 — `A72-G`, `A72-J`, `A72-K` |
| Unresolved | 0 |
| Deferred | 0 |
| Cross-Source-dedupliziert | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

| Einordnung | Fundstelle |
| --- | --- |
| Institutionelle Pflicht ohne Anbieter-`RR` | `SRC-002#Art.72/Abs.3/Satz.3` |
| Scope-Ausnahme ohne `RR` | `SRC-002#Art.72/Abs.2/Satz.3` |
| Außerhalb Scope | `SRC-002#Art.72/Abs.4/UAbs.2` |
| Interplay ohne eigene `RR` | Wahl der Integrationsroute aus `SRC-002#Art.72/Abs.4/UAbs.1` |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 11 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Kennungs-Mapping nach der Nachadjudikation

Im früheren Arbeitsstand war `A72-G` als vermeintlich eigenständige `RR` zur Compliance-Bewertung geführt. Nach der Nachadjudikation entfällt dieser Kandidat als eigenständige `RR`; sein normativer Gehalt ist in A72-D, A72-E und A72-F integriert (Abschnitt 5, A72-F).

Die noch nicht permanent vergebenen temporären Kennungen wurden deshalb für den finalen Evidenzstand lückenlos neu geordnet:

| Früherer Arbeitsstand | Finale Kennung |
| --- | --- |
| A72-H | A72-G |
| A72-I | A72-H |
| A72-J | A72-I |
| neuer Kandidat zur Vorlage | A72-J |
| A72-K | A72-K |

Kein permanenter Identifikator war betroffen.

---

## 4. `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-002#Art.72/Abs.1` | 3 `RR` | A72-A, A72-B, A72-C |
| `SRC-002#Art.72/Abs.2/Satz.1` | 3 `RR` | A72-D, A72-E, A72-F |
| `SRC-002#Art.72/Abs.2/Satz.2` | 1 conditional `RR` | A72-G |
| `SRC-002#Art.72/Abs.2/Satz.3` | 0 `RR` | Scope-Ausnahme (Abschnitt 6) |
| `SRC-002#Art.72/Abs.3/Satz.1` | 1 `RR` | A72-H |
| `SRC-002#Art.72/Abs.3/Satz.2` | 1 `RR` | A72-I |
| `SRC-002#Art.72/Abs.3/Satz.3` | 0 Anbieter-`RR` | institutionelle Pflicht der Kommission (Abschnitt 7) |
| `SRC-002#Art.72/Abs.4/UAbs.1` | 2 conditional `RR` | A72-J, A72-K; die Integrationswahl selbst ist Interplay bzw. Option ohne eigene `RR`; für die notwendigen Elemente aus Abs. 1 bis 3 entsteht keine zusätzliche aggregierende `RR` (Abschnitt 9) |
| `SRC-002#Art.72/Abs.4/UAbs.2` | — | außerhalb Scope (Abschnitt 9) |

Zu Abs. 2 Satz 1: Es gibt **keinen** separaten vierten Kandidaten zur fortdauernden Compliance-Bewertung. Die Eignung der Daten zur fortdauernden Compliance-Bewertung ist verpflichtendes Qualitäts- und Funktionskriterium des Datengegenstands von A72-D, A72-E und A72-F.

---

## 5. Kandidaten

### A72-A — Einrichtung des Post-Market-Monitoring-Systems

- **Title EN:** Establishment of the Post-Market Monitoring System
- **DE:** Der Anbieter muss ein System zur Beobachtung nach dem Inverkehrbringen für das Hochrisiko-KI-System einrichten.
- **EN:** The provider shall establish a post-market monitoring system for the high-risk AI system.
- **Primary:** `SRC-002#Art.72/Abs.1`
- **Supplementary:** — (leer)
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

**Cross-Article:** Keine Deduplizierung mit `RR-096`. Die materielle Einrichtung des PMS und seine QMS-Integration sind unterschiedliche Sollzustände (Abschnitt 11).

### A72-B — Dokumentation des Post-Market-Monitoring-Systems

- **Title EN:** Documentation of the Post-Market Monitoring System
- **DE:** Der Anbieter muss das System zur Beobachtung nach dem Inverkehrbringen dokumentieren.
- **EN:** The provider shall document the post-market monitoring system.
- **Primary:** `SRC-002#Art.72/Abs.1`
- **Supplementary:** — (leer)
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

### A72-C — Proportionale Ausgestaltung des Post-Market-Monitoring-Systems

- **Title EN:** Proportionate Design of the Post-Market Monitoring System
- **DE:** Der Anbieter muss sicherstellen, dass die Art und Weise der Einrichtung und Dokumentation des Systems zur Beobachtung nach dem Inverkehrbringen im Verhältnis zur Art der KI-Technologien und zu den Risiken des Hochrisiko-KI-Systems steht.
- **EN:** The provider shall ensure that the manner in which the post-market monitoring system is established and documented is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Primary:** `SRC-002#Art.72/Abs.1`
- **Supplementary:** — (leer)
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** A72-A erfasst die Existenz bzw. Einrichtung, A72-B die Dokumentation und A72-C die Proportionalität der Art und Weise von Einrichtung und Dokumentation.

**Nachadjudikation:** Der frühere EN-Arbeitstext wurde korrigiert, weil die Formulierung „shall establish and document … in a manner proportionate" die bereits separat atomisierten Handlungen A72-A und A72-B erneut in den Erfüllungsstatus von A72-C einbezogen hätte.

### A72-D — Aktive und systematische Erhebung geeigneter PMS-Daten

- **Title EN:** Active and Systematic Collection of Suitable Post-Market Data
- **DE:** Der Anbieter muss sicherstellen, dass das System zur Beobachtung nach dem Inverkehrbringen über die gesamte Lebensdauer des Hochrisiko-KI-Systems aktiv und systematisch einschlägige Daten zu dessen Leistung erhebt, die es ihm ermöglichen, die fortdauernde Einhaltung der Anforderungen aus Kapitel III Abschnitt 2 durch das Hochrisiko-KI-System zu bewerten.
- **EN:** The provider shall ensure that the post-market monitoring system actively and systematically collects, throughout the lifetime of the high-risk AI system, relevant data on its performance which allow the provider to evaluate the continuous compliance of the high-risk AI system with the requirements set out in Chapter III, Section 2.
- **Primary:** `SRC-002#Art.72/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.72/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** nein

### A72-E — Aktive und systematische Dokumentation geeigneter PMS-Daten

- **Title EN:** Active and Systematic Documentation of Suitable Post-Market Data
- **DE:** Der Anbieter muss sicherstellen, dass das System zur Beobachtung nach dem Inverkehrbringen über die gesamte Lebensdauer des Hochrisiko-KI-Systems aktiv und systematisch einschlägige Daten zu dessen Leistung dokumentiert, die es ihm ermöglichen, die fortdauernde Einhaltung der Anforderungen aus Kapitel III Abschnitt 2 durch das Hochrisiko-KI-System zu bewerten.
- **EN:** The provider shall ensure that the post-market monitoring system actively and systematically documents, throughout the lifetime of the high-risk AI system, relevant data on its performance which allow the provider to evaluate the continuous compliance of the high-risk AI system with the requirements set out in Chapter III, Section 2.
- **Primary:** `SRC-002#Art.72/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.72/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** nein

### A72-F — Aktive und systematische Analyse geeigneter PMS-Daten

- **Title EN:** Active and Systematic Analysis of Suitable Post-Market Data
- **DE:** Der Anbieter muss sicherstellen, dass das System zur Beobachtung nach dem Inverkehrbringen über die gesamte Lebensdauer des Hochrisiko-KI-Systems aktiv und systematisch einschlägige Daten zu dessen Leistung analysiert, die es ihm ermöglichen, die fortdauernde Einhaltung der Anforderungen aus Kapitel III Abschnitt 2 durch das Hochrisiko-KI-System zu bewerten.
- **EN:** The provider shall ensure that the post-market monitoring system actively and systematically analyses, throughout the lifetime of the high-risk AI system, relevant data on its performance which allow the provider to evaluate the continuous compliance of the high-risk AI system with the requirements set out in Chapter III, Section 2.
- **Primary:** `SRC-002#Art.72/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.72/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** nein

**Nachadjudikation:** Die frühere Arbeitsfassung „Ermöglichung der fortdauernden Compliance-Bewertung" wird **nicht** als eigene `RR` geführt. Split-Bedingung 1 ist erfüllt, Split-Bedingung 2 **nicht**: Die Relativklausel bestimmt die erforderliche Eignung der Daten, die in A72-D, A72-E und A72-F erhoben, dokumentiert und analysiert werden, und bildet keine eigenständige vollständige Compliance-Aussage.

### A72-G — Analyse der Interaktion mit anderen KI-Systemen

- **Title EN:** Analysis of Interaction with Other AI Systems
- **DE:** Soweit dies relevant ist, muss der Anbieter sicherstellen, dass die Beobachtung nach dem Inverkehrbringen eine Analyse der Interaktion des Hochrisiko-KI-Systems mit anderen KI-Systemen umfasst.
- **EN:** Where relevant, the provider shall ensure that post-market monitoring includes an analysis of the interaction of the high-risk AI system with other AI systems.
- **Primary:** `SRC-002#Art.72/Abs.2/Satz.2`
- **Supplementary:** `SRC-002#Art.72/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** ja

**Trigger:** Die Interaktion mit anderen KI-Systemen ist für die Beobachtung nach dem Inverkehrbringen relevant.

### A72-H — PMS-System auf Grundlage eines PMS-Plans

- **Title EN:** Post-Market Monitoring System Based on a Post-Market Monitoring Plan
- **DE:** Der Anbieter muss sicherstellen, dass das System zur Beobachtung nach dem Inverkehrbringen auf einem Plan für die Beobachtung nach dem Inverkehrbringen beruht.
- **EN:** The provider shall ensure that the post-market monitoring system is based on a post-market monitoring plan.
- **Primary:** `SRC-002#Art.72/Abs.3/Satz.1`
- **Supplementary:** `SRC-002#Art.72/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

### A72-I — PMS-Plan als Bestandteil der technischen Dokumentation

- **Title EN:** Post-Market Monitoring Plan as Part of the Technical Documentation
- **DE:** Der Anbieter muss sicherstellen, dass der Plan für die Beobachtung nach dem Inverkehrbringen Bestandteil der in Anhang IV genannten technischen Dokumentation ist.
- **EN:** The provider shall ensure that the post-market monitoring plan forms part of the technical documentation referred to in Annex IV.
- **Primary:** `SRC-002#Art.72/Abs.3/Satz.2`
- **Supplementary:** `SRC-002#Art.72/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Konformitätsbewertung
- **Uncertainty:** null
- **Conditional:** nein

**Scope-Entscheidung:** Die Pflicht bleibt im Cluster Post-Market-Monitoring, weil ihr primärer Gegenstand der PMS-Plan und dessen regulatorische Einbettung ist. Eine allgemeine Coverage der technischen Dokumentation wird **nicht** eröffnet; das entspricht Exclusion Criterion E-7 in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 3.

### A72-J — Verwendung der PMS-Plan-Vorlage bei integrierter PMS-Struktur

- **Title EN:** Use of the Post-Market Monitoring Plan Template for an Integrated Arrangement
- **DE:** Entscheidet sich der Anbieter eines Hochrisiko-KI-Systems unter den Voraussetzungen des Artikels 72 Absatz 4 Unterabsatz 1 dafür, die erforderlichen Elemente aus Artikel 72 Absätze 1 bis 3 soweit angemessen in ein bereits nach dem einschlägigen Unionsharmonisierungsrecht bestehendes System und einen bestehenden Plan zur Beobachtung nach dem Inverkehrbringen zu integrieren, muss er für diese Integration die in Artikel 72 Absatz 3 genannte Vorlage für den Plan zur Beobachtung nach dem Inverkehrbringen verwenden.
- **EN:** Where, under the conditions set out in Article 72(4), first subparagraph, the provider of a high-risk AI system chooses, as appropriate, to integrate the necessary elements of Article 72(1) to (3) into an existing post-market monitoring system and plan established under the applicable Union harmonisation legislation, the provider shall use for that integration the template referred to in Article 72(3).
- **Primary:** `SRC-002#Art.72/Abs.4/UAbs.1`
- **Supplementary:** `SRC-002#Art.72/Abs.1` · `SRC-002#Art.72/Abs.2` · `SRC-002#Art.72/Abs.3/Satz.1` · `SRC-002#Art.72/Abs.3/Satz.2` · `SRC-002#Art.72/Abs.3/Satz.3`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** ja

**Trigger:**

- das Hochrisiko-KI-System fällt unter das Unionsharmonisierungsrecht aus Anhang I Abschnitt A;
- nach diesem Recht bestehen bereits ein System und ein Plan zur Beobachtung nach dem Inverkehrbringen;
- der Anbieter entscheidet sich für die Integrationsroute nach Art. 72 Abs. 4 UAbs. 1.

**Atomizität:** Die Integrationswahl selbst ist optional und erzeugt keine `RR`. Bei gewählter Route ist die Verwendung der Vorlage nach dem unverändert gebliebenen operativen Wortlaut eigenständig statusfähig: Die notwendigen Art.-72-Elemente können materiell integriert sein und ein gleichwertiges Schutzniveau erreichen, obwohl die vorgesehene Vorlage nicht verwendet wurde. Zur Adjudikation siehe Abschnitt 8.

**Lokatoren:** Art. 72 Abs. 4 UAbs. 1 definiert die Integrationsroute über die notwendigen Elemente aus Abs. 1 bis 3; diese Absätze werden deshalb als zwingend erforderlicher Kontext geführt. `SRC-002#Art.72/Abs.3/Satz.3` ist zusätzlich erforderlich, weil A72-J speziell die Verwendung der dort genannten Vorlage betrifft.

### A72-K — Gleichwertiges Schutzniveau bei integrierter PMS-Struktur

- **Title EN:** Equivalent Level of Protection for an Integrated Post-Market Monitoring Arrangement
- **DE:** Entscheidet sich der Anbieter eines Hochrisiko-KI-Systems unter den Voraussetzungen des Artikels 72 Absatz 4 Unterabsatz 1 dafür, die erforderlichen Elemente aus Artikel 72 Absätze 1 bis 3 in ein bereits nach dem einschlägigen Unionsharmonisierungsrecht bestehendes System und einen bestehenden Plan zur Beobachtung nach dem Inverkehrbringen zu integrieren, muss die integrierte Lösung ein gleichwertiges Schutzniveau erreichen.
- **EN:** Where, under the conditions set out in Article 72(4), first subparagraph, the provider of a high-risk AI system chooses to integrate the necessary elements of Article 72(1) to (3) into an existing post-market monitoring system and plan established under the applicable Union harmonisation legislation, the integrated arrangement shall achieve an equivalent level of protection.
- **Primary:** `SRC-002#Art.72/Abs.4/UAbs.1`
- **Supplementary:** `SRC-002#Art.72/Abs.1` · `SRC-002#Art.72/Abs.2` · `SRC-002#Art.72/Abs.3/Satz.1` · `SRC-002#Art.72/Abs.3/Satz.2`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption · Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** ja

**Trigger:**

- das Hochrisiko-KI-System fällt unter das Unionsharmonisierungsrecht aus Anhang I Abschnitt A;
- nach diesem Recht bestehen bereits ein System und ein Plan zur Beobachtung nach dem Inverkehrbringen;
- der Anbieter entscheidet sich für die Integrationsroute nach Art. 72 Abs. 4 UAbs. 1.

**Atomizität:** Die Schutzäquivalenz ist unabhängig von der Verwendung der Vorlage und von der formalen Integration statusfähig und bildet eine vollständige regulatorische Bedingung der optionalen Route.

**Lokatoren:** Die Absätze 1 bis 3 werden als Kontext der notwendigen Elemente geführt. `SRC-002#Art.72/Abs.3/Satz.3` wird **nicht** aufgenommen, weil die Leitlinie bzw. Vorlage der Kommission zur vollständigen normativen Bestimmung des gleichwertigen Schutzniveaus der integrierten materiellen PMS-Struktur nicht erforderlich ist.

---

## 6. `SRC-002#Art.72/Abs.2/Satz.3` — Scope-Ausnahme

0 `RR`. Die Stelle enthält eine Scope-Ausnahme hinsichtlich sensibler operativer Daten von Betreibern, die Strafverfolgungsbehörden sind. Sie begründet keine eigenständige positive Anbieterpflicht. Die Ausnahme ist bei der späteren `RUL`- bzw. Applicability-Logik zu berücksichtigen, soweit der Sachverhalt einschlägig ist.

---

## 7. `SRC-002#Art.72/Abs.3/Satz.3` — institutionelle Pflicht

0 Anbieter-`RR`. Die Stelle verpflichtet die Kommission, unter weitestgehender Berücksichtigung der Stellungnahme des Boards bis zum 2. September 2027 Leitlinien einschließlich einer Vorlage für den Plan zur Beobachtung nach dem Inverkehrbringen anzunehmen.

Diese Fassung beruht auf der Änderung von Art. 72 Abs. 3 durch die Verordnung (EU) 2026/1744, die im projektverbindlichen konsolidierten Rechtsstand nach [SOURCES.md](SOURCES.md) berücksichtigt ist. Die Änderung verändert A72-H und A72-I **nicht**.

---

## 8. Adjudikation der Vorlage bei der Integrationsroute

Art. 72 Abs. 3 wurde durch die Verordnung (EU) 2026/1744 geändert. Erwägungsgrund 41 der Verordnung (EU) 2026/1744 (CELEX `32026R1744`), die gemäß [SOURCES.md](SOURCES.md) zur Provenienz des konsolidierten Rechtsstands von `SRC-002` gehört, beschreibt die in den geänderten Art. 72 Abs. 3 aufzunehmende Vorlage allgemein als freiwillig. Es handelt sich **nicht** um einen Erwägungsgrund des konsolidierten `SRC-002`; er dient ausschließlich als systematischer Auslegungskontext und ist weder `primary`- noch `supplementary`-Lokator einer `RR`. Art. 72 Abs. 4 UAbs. 1 enthält im konsolidierten Rechtsstand vom 27.07.2026 weiterhin ausdrücklich den Verweis auf die Verwendung der Vorlage bei der besonderen Integrationsroute.

| Frage | Adjudikation |
| --- | --- |
| Allgemeine Verwendung der Vorlage | nicht obligatorisch |
| Wahl der Integrationsroute nach Abs. 4 | freiwillig |
| Verwendung der Vorlage bei gewählter Abs.-4-Integrationsroute | Bedingung dieser besonderen Route (A72-J) |

Es besteht **keine** unresolved Divergenz.

**Methodische Begründung:** Erwägungsgründe dienen der Auslegung, besitzen aber keine eigene bindende Rechtskraft und dürfen nicht dazu verwendet werden, eine operative Bestimmung entgegen ihrem Wortlaut zu beseitigen. Das entspricht der Regel aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8, wonach Erwägungsgründe die Interpretation unterstützen, aber keine normative Hauptfundstelle ersetzen. Methodische Stütze: EuGH, Urteil vom 19. Dezember 2019, C-418/18 P, *Puppinck u. a./Kommission*, Rn. 75–76 (CELEX `62018CJ0418`, ECLI:EU:C:2019:1113). Nach Rn. 75 sind Erwägungsgründe wichtige Auslegungselemente, die die Absicht des Unionsgesetzgebers verdeutlichen können; nach Rn. 76 besitzen sie keine bindende Rechtskraft und dürfen weder dazu herangezogen werden, von den tatsächlichen Bestimmungen des Rechtsakts abzuweichen, noch dazu, diese klar wortlautwidrig auszulegen. Das Urteil stützt die bereits bestehende Regel aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8 und führt keine neue Extraktionsmethode ein.

Inhalte der Vorlage werden **nicht** vorweggenommen. Dass die Vorlage derzeit noch nicht vorliegt, führt weder zu `deferred` noch zu `unresolved`; erfasst wird ausschließlich die normative Bedingung der Integrationsroute.

---

## 9. Abs. 4 — keine weiteren `RR`

| Gegenstand | Entscheidung | Begründung |
| --- | --- | --- |
| Integrationswahl | 0 `RR` / Interplay | Der Anbieter besitzt eine Wahlmöglichkeit. |
| Notwendige Elemente aus Abs. 1 bis 3 | keine zusätzliche aggregierende `RR` | Die materiellen Elemente werden durch A72-A bis A72-I abgedeckt; eine zusätzliche Gesamt-`RR` würde dieselben Gaps aggregieren. |
| `SRC-002#Art.72/Abs.4/UAbs.2` | außerhalb Scope | liegt außerhalb des aktuellen Medizinprodukte- und Anbieterscope |

---

## 10. MDR- und Produktrechts-Interplay

Die Verordnung (EU) 2017/745 ist in `SRC-002#Anh.I/Abschn.A/Nr.11` aufgeführt. Damit kann Art. 72 Abs. 4 UAbs. 1 für den betreffenden Medizinproduktepfad relevant sein.

`SRC-002#Anh.I/Abschn.A/Nr.11` wird gleichwohl **nicht** als `supplementary`-Lokator zu A72-J oder A72-K aufgenommen. A72-J und A72-K sind generische Anforderungen für alle einschlägigen Pfade nach Anhang I Abschnitt A; der konkrete MDR-Lokator ist späterer Applicability- und Traceability-Kontext. MDR-PMS-Pflichten werden in dieser Datei **nicht** extrahiert.

---

## 11. Cross-Source-Abgleich mit `RR-096` bis `RR-098`

| `RR` | Art.-17-Gegenstand | Art.-72-Gegenstand | Identischer Sollzustand | Identischer Erfüllungsstatus | Ergebnis |
| --- | --- | --- | --- | --- | --- |
| `RR-096` | QMS umfasst die Einrichtung des PMS | A72-A: PMS materiell eingerichtet | nein | nein | behalten, keine Deduplizierung |
| `RR-097` | QMS umfasst die Umsetzung des PMS | A72-D, A72-E, A72-F, A72-G: materielle operative PMS-Prozesse | nein | nein | behalten, keine Deduplizierung |
| `RR-098` | QMS umfasst die Aufrechterhaltung des PMS | materielle lebensdauerweite PMS-Anforderungen aus Art. 72 | nein | nein | behalten, keine Deduplizierung |

Ergebnis: `RR-096` bis `RR-098` bleiben unverändert. Der Katalog wird nicht geändert; es werden keine Art.-72-Lokatoren als `supplementary` ergänzt. Damit ist der in [RR_EXTRACTION_ART17.md](RR_EXTRACTION_ART17.md) vorgemerkte Abgleich durchgeführt.

---

## 12. Multilingualer Audit

DE und EN wurden geprüft; zusätzlich FR, ES und PT.

| Fundstelle | Befund | Status |
| --- | --- | --- |
| `SRC-002#Art.72/Abs.2/Satz.1` | DE nennt bei den möglichen Datenquellen ausdrücklich Daten von Anbietern oder Betreibern; EN sowie FR, ES und PT nennen Betreiber und sonstige Quellen | resolved |

**Adjudikation:** Die Aufzählung der möglichen Datenquellen ist offen und bestimmt keine exklusiven Datenlieferanten. Die atomaren Pflichten beziehen sich auf relevante Leistungsdaten, nicht auf eine bestimmte Quelle. Daraus folgt keine zusätzliche `RR`, und keine Datenquelle wird ausgeschlossen. Keine Sprachfassung wurde priorisiert; die Anzahl übereinstimmender Fassungen wurde nicht als Mehrheitsregel verwendet.

Unresolved: **0**.

Die Frage der Vorlage aus Abs. 4 ist **keine** Sprachdivergenz, sondern eine systematische Adjudikationsfrage infolge der Änderung von 2026 (Abschnitt 8).

---

## 13. Locator-Audit

Alle formalen Lokatoren entsprechen der Syntax aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4; ein Lokatorelement `Chapeau` wird nicht verwendet.

- A72-J: Primary `SRC-002#Art.72/Abs.4/UAbs.1`; Supplementary `SRC-002#Art.72/Abs.1`, `SRC-002#Art.72/Abs.2`, `SRC-002#Art.72/Abs.3/Satz.1`, `SRC-002#Art.72/Abs.3/Satz.2`, `SRC-002#Art.72/Abs.3/Satz.3`.
- A72-K: Primary `SRC-002#Art.72/Abs.4/UAbs.1`; Supplementary `SRC-002#Art.72/Abs.1`, `SRC-002#Art.72/Abs.2`, `SRC-002#Art.72/Abs.3/Satz.1`, `SRC-002#Art.72/Abs.3/Satz.2`; ohne `SRC-002#Art.72/Abs.3/Satz.3`.
- Erwägungsgrund 41 der Verordnung (EU) 2026/1744 wird nicht als Lokator geführt; ein Erwägungsgrund-Lokator auf `SRC-002` wird hierfür nicht verwendet.
- Es stehen keine MDR-Lokatoren in `Primary` oder `Supplementary`.

---

## 14. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. Eine Methodenänderung ist **nicht** erforderlich.

Abgedeckte Fallgestaltungen:

- kumulative Handlungen,
- unabhängiges Qualitätskriterium,
- gemeinsame Datenqualifikation,
- conditional Zusatzanalyse,
- Scope-Ausnahme,
- institutionelle Pflicht,
- Interplay- bzw. Integrationsoption,
- conditional Bedingung einer optionalen Route,
- Cross-Source-Trennung von QMS und materieller PMS-Pflicht,
- multilingualer Quellenvergleich,
- systematische Adjudikation nach einer Gesetzesänderung.

Es wurde **keine** Art.-72-Sonderregel eingeführt.

---

## 15. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | angewandte Extraktions-, Atomizitäts- und Source-Fidelity-Methode (Version 1.2) |
| [COVERAGE_PLAN.md](COVERAGE_PLAN.md) | Freigabe des Quellenbereichs und Bearbeitungsstatus (Version 1.11) |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | führende Vergabestelle; hier nicht verändert |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister, Fassungsstand von `SRC-002` und Provenienz der Verordnung (EU) 2026/1744 |
| [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | Identifikatoren und Lokator-Syntax |
| [RR_EXTRACTION_ART17.md](RR_EXTRACTION_ART17.md) | Herkunft von `RR-096` bis `RR-098` |

---

## 16. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: vollständige systematische Extraktion von `SRC-002` Art. 72; 11 finale Kandidaten A72-A bis A72-K, davon 8 regulär und 3 conditional; 0 unresolved und 0 deferred; nach gezielter Nachadjudikation Proportionalitätskandidat A72-C sprachlich atomar präzisiert, separate Compliance-Bewertungs-`RR` verworfen und als Datenqualifikation in A72-D, A72-E und A72-F integriert sowie die Vorlagen-Bedingung der optionalen Abs.-4-Integrationsroute als conditional Kandidat aufgenommen; `RR-096` bis `RR-098` nach Cross-Source-Prüfung unverändert beibehalten. Keine Identifikatorvergabe. |
