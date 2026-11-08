# Systematische RR-Extraktion — SRC-002 Art. 17

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` |
| Aktive Quellenbereiche | `SRC-002#Art.17/Abs.1` einschließlich der im Coverage-Plan freigegebenen Teilbereiche sowie `SRC-002#Art.17/Abs.2` |
| Kontextuell geprüft | `SRC-002#Art.17/Abs.1/Buchst.i` · `SRC-002#Art.17/Abs.3` · `SRC-002#Art.17/Abs.4` |
| Rechtsstand | konsolidierter Stand 27.07.2026 gemäß [SOURCES.md](SOURCES.md) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.9 |
| Bearbeitungsstatus der aktiven Bereiche | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Extraktionsstand. Sie vergibt **keine** permanenten `RR`-Identifikatoren; die Kandidaten tragen ausschließlich die temporären Kennungen `A17-A` bis `A17-X`. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Methodisches Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Finale neue Gap-`RR`-Kandidaten | **24** — `A17-A` bis `A17-X` |
| davon regulär | 23 |
| davon conditional | 1 — `A17-M` |
| Unresolved | 0 |
| Deferred | 0 |
| Cross-Source-dedupliziert | 0 |
| Operative aktive Fundstellen ohne Entscheidung | 0 |

| Einordnung | Fundstellen |
| --- | --- |
| Außerhalb aktiver Gap-Coverage | `SRC-002#Art.17/Abs.1/Buchst.i` · `SRC-002#Art.17/Abs.4` |
| Interplay ohne eigene `RR` | `SRC-002#Art.17/Abs.3` |
| Späterer Cross-Source-Deduplizierungs- und Traceability-Punkt gegen Art. 72 | A17-P · A17-Q · A17-R |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 24 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-002#Art.17/Abs.1` | 2 `RR` | A17-A, A17-B |
| `SRC-002#Art.17/Abs.1/Buchst.a` | 2 `RR` | A17-C, A17-D |
| `SRC-002#Art.17/Abs.1/Buchst.b` | 3 `RR` | A17-E, A17-F, A17-G |
| `SRC-002#Art.17/Abs.1/Buchst.c` | 3 `RR` | A17-H, A17-I, A17-J |
| `SRC-002#Art.17/Abs.1/Buchst.d` | 1 `RR` | A17-K |
| `SRC-002#Art.17/Abs.1/Buchst.e` | 2 `RR` | A17-L, A17-M |
| `SRC-002#Art.17/Abs.1/Buchst.f` | 1 `RR` | A17-N |
| `SRC-002#Art.17/Abs.1/Buchst.g` | 1 `RR` | A17-O |
| `SRC-002#Art.17/Abs.1/Buchst.h` | 3 `RR` | A17-P, A17-Q, A17-R |
| `SRC-002#Art.17/Abs.1/Buchst.i` | — | außerhalb aktiver Gap-Coverage (Abschnitt 7) |
| `SRC-002#Art.17/Abs.1/Buchst.j` | 1 `RR` | A17-S |
| `SRC-002#Art.17/Abs.1/Buchst.k` | 1 `RR` | A17-T |
| `SRC-002#Art.17/Abs.1/Buchst.l` | 1 `RR` | A17-U |
| `SRC-002#Art.17/Abs.1/Buchst.m` | 1 `RR` | A17-V |
| `SRC-002#Art.17/Abs.2/Satz.1` | 1 `RR` | A17-W |
| `SRC-002#Art.17/Abs.2/Satz.2` | 1 `RR` | A17-X |
| `SRC-002#Art.17/Abs.3` | 0 `RR` | Interplay (Abschnitt 7) |
| `SRC-002#Art.17/Abs.4` | — | außerhalb Scope (Abschnitt 7) |

Zu Abs. 1: Die Compliance-Eignung des Qualitätsmanagementsystems gehört zu A17-A, die Dokumentationsform zu A17-B. Eine aggregierende `RR` für „alle Buchst. a bis m" wird **nicht** gebildet; die Mindestinhalte werden über die Buchstaben-Kandidaten erfasst, der einleitende Teil des Absatzes über den Absatz-Lokator `SRC-002#Art.17/Abs.1`.

---

## 4. Kandidaten

### A17-A — Einrichtung eines compliance-geeigneten Qualitätsmanagementsystems

- **Title EN:** Establishment of a Compliance-Ensuring Quality Management System
- **DE:** Der Anbieter muss ein Qualitätsmanagementsystem einrichten, das die Einhaltung der Verordnung gewährleistet.
- **EN:** The provider shall put in place a quality management system that ensures compliance with the Regulation.
- **Primary:** `SRC-002#Art.17/Abs.1`
- **Supplementary:** — (leer)
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Einrichtung und Compliance-Eignung bilden denselben QMS-Sollzustand.

### A17-B — Systematische und geordnete QMS-Dokumentation

- **Title EN:** Systematic and Orderly QMS Documentation
- **DE:** Der Anbieter muss das Qualitätsmanagementsystem systematisch und ordnungsgemäß in Form schriftlicher Regeln, Verfahren und Anweisungen dokumentieren.
- **EN:** The provider shall document the quality management system in a systematic and orderly manner in the form of written policies, procedures and instructions.
- **Primary:** `SRC-002#Art.17/Abs.1`
- **Supplementary:** — (leer)
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Dokumentationsform und Qualitätsmerkmale konkretisieren dieselbe Dokumentationspflicht.

### A17-C — Strategie zur Einhaltung der Regulierungsvorschriften

- **Title EN:** Strategy for Regulatory Compliance
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem ein Konzept zur Einhaltung der Regulierungsvorschriften umfasst, einschließlich der Einhaltung der anwendbaren Konformitätsbewertungsverfahren.
- **EN:** The provider shall ensure that the quality management system includes a strategy for regulatory compliance, including compliance with the applicable conformity assessment procedures.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.a`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

### A17-D — Verfahren zum Management von Änderungen

- **Title EN:** Procedures for Management of Modifications
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Verfahren für das Management von Änderungen am Hochrisiko-KI-System umfasst.
- **EN:** The provider shall ensure that the quality management system includes procedures for the management of modifications to the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.a`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

### A17-E — Verfahren für den Systementwurf

- **Title EN:** Design Techniques, Procedures and Systematic Actions
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Techniken, Verfahren und systematische Maßnahmen für den Entwurf des Hochrisiko-KI-Systems umfasst.
- **EN:** The provider shall ensure that the quality management system includes techniques, procedures and systematic actions to be used for the design of the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.b`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** nein

### A17-F — Verfahren zur Entwurfskontrolle

- **Title EN:** Design Control Techniques, Procedures and Systematic Actions
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Techniken, Verfahren und systematische Maßnahmen für die Entwurfskontrolle des Hochrisiko-KI-Systems umfasst.
- **EN:** The provider shall ensure that the quality management system includes techniques, procedures and systematic actions to be used for design control of the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.b`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** nein

### A17-G — Verfahren zur Entwurfsprüfung

- **Title EN:** Design Verification Techniques, Procedures and Systematic Actions
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Techniken, Verfahren und systematische Maßnahmen für die Entwurfsprüfung des Hochrisiko-KI-Systems umfasst.
- **EN:** The provider shall ensure that the quality management system includes techniques, procedures and systematic actions to be used for design verification of the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.b`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Verifikation und Validierung
- **Uncertainty:** null
- **Conditional:** nein

**Nachadjudikation Buchst. b:** Der Split in A17-E, A17-F und A17-G ist bestätigt. Split-Bedingung 1 (unabhängig unterschiedlicher Erfüllungsstatus) ist erfüllt; Split-Bedingung 2 (je vollständige regulatorisch sinnvolle Compliance-Aussage) ist erfüllt.

### A17-H — Verfahren für die Entwicklung

- **Title EN:** Development Techniques, Procedures and Systematic Actions
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Techniken, Verfahren und systematische Maßnahmen für die Entwicklung des Hochrisiko-KI-Systems umfasst.
- **EN:** The provider shall ensure that the quality management system includes techniques, procedures and systematic actions to be used for the development of the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.c`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** nein

### A17-I — Verfahren zur Qualitätskontrolle

- **Title EN:** Quality Control Techniques, Procedures and Systematic Actions
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Techniken, Verfahren und systematische Maßnahmen für die Qualitätskontrolle des Hochrisiko-KI-Systems umfasst.
- **EN:** The provider shall ensure that the quality management system includes techniques, procedures and systematic actions to be used for quality control of the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.c`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** nein

### A17-J — Verfahren zur Qualitätssicherung

- **Title EN:** Quality Assurance Techniques, Procedures and Systematic Actions
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Techniken, Verfahren und systematische Maßnahmen für die Qualitätssicherung des Hochrisiko-KI-Systems umfasst.
- **EN:** The provider shall ensure that the quality management system includes techniques, procedures and systematic actions to be used for quality assurance of the high-risk AI system.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.c`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** nein

**Nachadjudikation Buchst. c:** Der Split in A17-H, A17-I und A17-J ist bestätigt; beide Split-Bedingungen sind erfüllt.

### A17-K — Untersuchungs-, Test- und Validierungsverfahren

- **Title EN:** Examination, Testing and Validation Procedures
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Untersuchungs-, Test- und Validierungsverfahren umfasst, die vor, während und nach der Entwicklung des Hochrisiko-KI-Systems durchzuführen sind, einschließlich der festgelegten Häufigkeit ihrer Durchführung.
- **EN:** The provider shall ensure that the quality management system includes examination, test and validation procedures to be carried out before, during and after the development of the high-risk AI system, including the frequency with which they are to be carried out.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.d`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung
- **Uncertainty:** null
- **Conditional:** nein

### A17-L — Festlegung anzuwendender technischer Spezifikationen und Normen

- **Title EN:** Applicable Technical Specifications and Standards
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem die anzuwendenden technischen Spezifikationen einschließlich Normen umfasst.
- **EN:** The provider shall ensure that the quality management system includes the technical specifications, including standards, to be applied.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.e`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

### A17-M — Alternative Mittel zur Sicherstellung der Section-2-Compliance

- **Title EN:** Alternative Means to Ensure Compliance with Section 2
- **DE:** Werden die einschlägigen harmonisierten Normen nicht vollständig angewandt oder decken sie nicht alle relevanten Anforderungen aus Abschnitt 2 ab, muss der Anbieter sicherstellen, dass das Qualitätsmanagementsystem die Mittel umfasst, mit denen die Einhaltung dieser Anforderungen durch das Hochrisiko-KI-System gewährleistet werden soll.
- **EN:** Where the relevant harmonised standards are not applied in full or do not cover all relevant requirements set out in Section 2, the provider shall ensure that the quality management system includes the means to be used to ensure that the high-risk AI system complies with those requirements.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.e`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** ja

**Trigger:** Einschlägige harmonisierte Normen werden nicht vollständig angewandt oder decken nicht alle relevanten Anforderungen nach Abschnitt 2 ab.

### A17-N — Systeme und Verfahren für Datenmanagement

- **Title EN:** Data Management Systems and Procedures
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Systeme und Verfahren für das Datenmanagement umfasst, einschließlich der einschlägigen Datenoperationen, die vor und zum Zweck des Inverkehrbringens oder der Inbetriebnahme des Hochrisiko-KI-Systems durchgeführt werden.
- **EN:** The provider shall ensure that the quality management system includes systems and procedures for data management, including the relevant data operations performed before and for the purpose of placing the high-risk AI system on the market or putting it into service.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.f`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Data Governance
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** nein

**Cross-Article:** Keine vollständige Deduplizierung gegen Art. 10; A17-N bildet einen eigenständigen QMS-Integrations- und Prozessstatus.

### A17-O — Einbindung des Risikomanagementsystems in das QMS

- **Title EN:** Inclusion of the Risk Management System in the QMS
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem das in Artikel 9 genannte Risikomanagementsystem umfasst.
- **EN:** The provider shall ensure that the quality management system includes the risk management system referred to in Article 9.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.g`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

**Cross-Article:** Keine vollständige Deduplizierung gegen Art. 9; A17-O bildet einen eigenständigen QMS-Integrationsstatus.

### A17-P — Einrichtung des Post-Market-Monitoring-Systems

- **Title EN:** Establishment of the Post-Market Monitoring System
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem die Einrichtung eines Systems zur Beobachtung nach dem Inverkehrbringen gemäß Artikel 72 umfasst.
- **EN:** The provider shall ensure that the quality management system includes the setting-up of a post-market monitoring system in accordance with Article 72.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.h`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** nein

### A17-Q — Umsetzung des Post-Market-Monitoring-Systems

- **Title EN:** Implementation of the Post-Market Monitoring System
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem die Umsetzung des Systems zur Beobachtung nach dem Inverkehrbringen gemäß Artikel 72 umfasst.
- **EN:** The provider shall ensure that the quality management system includes the implementation of the post-market monitoring system in accordance with Article 72.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.h`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** nein

### A17-R — Aufrechterhaltung des Post-Market-Monitoring-Systems

- **Title EN:** Maintenance of the Post-Market Monitoring System
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem die Aufrechterhaltung des Systems zur Beobachtung nach dem Inverkehrbringen gemäß Artikel 72 umfasst.
- **EN:** The provider shall ensure that the quality management system includes the maintenance of the post-market monitoring system in accordance with Article 72.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.h`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** nein

**Nachadjudikation Buchst. h:** Der Split in A17-P, A17-Q und A17-R ist bestätigt; Split-Bedingung 1 und Split-Bedingung 2 sind erfüllt. Die Kandidaten sind **nicht** bis zur Art.-72-Extraktion zurückgestellt, weil der Art.-17-QMS-Integrationsstatus bereits unabhängig bestimmbar ist. Eine spätere Cross-Source-Deduplizierung gegen Art. 72 ist erforderlich (Abschnitt 6).

### A17-S — Kommunikationsmanagement

- **Title EN:** Management of Communications
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem die Handhabung der Kommunikation mit zuständigen nationalen und sonstigen einschlägigen Behörden, einschließlich Stellen zur Gewährung oder Unterstützung des Datenzugangs, mit notifizierten Stellen, anderen Akteuren, Kunden und sonstigen interessierten Kreisen umfasst.
- **EN:** The provider shall ensure that the quality management system includes the handling of communication with national competent authorities, other relevant authorities, including those providing or supporting access to data, notified bodies, other operators, customers and other interested parties.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.j`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** nein

### A17-T — Systeme und Verfahren zur Aufzeichnung

- **Title EN:** Record-Keeping Systems and Procedures
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Systeme und Verfahren zur Aufzeichnung sämtlicher einschlägiger Dokumentation und Informationen umfasst.
- **EN:** The provider shall ensure that the quality management system includes systems and procedures for record-keeping of all relevant documentation and information.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.k`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

### A17-U — Ressourcenmanagement

- **Title EN:** Resource Management
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem Ressourcenmanagement einschließlich Maßnahmen im Hinblick auf die Versorgungssicherheit umfasst.
- **EN:** The provider shall ensure that the quality management system includes resource management, including security-of-supply related measures.
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.l`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null
- **Conditional:** nein

### A17-V — Rechenschaftsrahmen und Verantwortlichkeiten

- **Title EN:** Accountability Framework and Responsibilities
- **DE:** Der Anbieter muss sicherstellen, dass das Qualitätsmanagementsystem einen Rechenschaftsrahmen umfasst, der die Verantwortlichkeiten der Leitung und des sonstigen Personals für alle in Artikel 17 Absatz 1 aufgeführten Aspekte festlegt.
- **EN:** The provider shall ensure that the quality management system includes an accountability framework setting out the responsibilities of management and other staff with regard to all aspects listed in Article 17(1).
- **Primary:** `SRC-002#Art.17/Abs.1/Buchst.m`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

### A17-W — Proportionale QMS-Umsetzung nach Organisationsgröße

- **Title EN:** Proportionate QMS Implementation According to Organisational Size
- **DE:** Der Anbieter muss die in Artikel 17 Absatz 1 genannten Aspekte in einem angemessenen Verhältnis zur Größe seiner Organisation umsetzen, insbesondere wenn es sich um ein KMU einschließlich Start-up-Unternehmen oder um ein kleines Midcap-Unternehmen handelt.
- **EN:** The provider shall implement the aspects referred to in Article 17(1) proportionately to the size of its organisation, in particular where the provider is an SME, including a start-up, or an SMC.
- **Primary:** `SRC-002#Art.17/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.17/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

### A17-X — Erforderlicher Grad an Strenge und Schutzniveau

- **Title EN:** Required Degree of Rigour and Level of Protection
- **DE:** Der Anbieter muss unabhängig von der proportionalen Ausgestaltung des Qualitätsmanagementsystems stets den Grad an Strenge und das Schutzniveau einhalten, die erforderlich sind, um die Übereinstimmung seines Hochrisiko-KI-Systems mit der Verordnung sicherzustellen.
- **EN:** The provider shall in all cases respect the degree of rigour and the level of protection required to ensure the compliance of its high-risk AI system with the Regulation.
- **Primary:** `SRC-002#Art.17/Abs.2/Satz.2`
- **Supplementary:** — (leer)
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

---

## 5. Cross-Article-Entscheidungen

| Bezug | Entscheidung | Begründung |
| --- | --- | --- |
| Art. 17 Abs. 1 Buchst. f ↔ Art. 10 | keine vollständige Deduplizierung | Buchst. f betrifft QMS-Systeme und -Verfahren für das Datenmanagement; Art. 10 regelt die materiellen Data-Governance-Pflichten |
| Art. 17 Abs. 1 Buchst. g ↔ Art. 9 | keine vollständige Deduplizierung | A17-O betrifft den QMS-Integrationsstatus; Art. 9 regelt das materielle Risikomanagementsystem |
| Art. 17 Abs. 1 Buchst. h ↔ Art. 72 | noch keine finale Deduplizierung | siehe Abschnitt 6 |
| Art. 15 | keine echte Dublette zu Buchst. b, c und d | — |
| Art. 13 und Art. 14 | keine echte Dublette | — |

---

## 6. Späterer Abgleich A17-P, A17-Q, A17-R ↔ Art. 72

A17-P, A17-Q und A17-R sind jetzt aktivierbar und **nicht** zurückgestellt: Der Art.-17-QMS-Integrationsstatus ist bereits unabhängig bestimmbar. Der spätere Cross-Source-Deduplizierungs- und Traceability-Abgleich gegen `SRC-002#Art.72` ist zwingend durchzuführen, sobald Art. 72 systematisch extrahiert wird. Diese Frage wird hier **nicht** entschieden.

---

## 7. Scope-Entscheidungen

**`SRC-002#Art.17/Abs.1/Buchst.i` — außerhalb aktiver Gap-Coverage.** Der Buchstabe betrifft den Bereich schwerwiegender Vorfälle und der Vigilanz nach Art. 73. Es entsteht **keine** `RR`; der Gegenstand wird nicht in das Post-Market-Monitoring hineingezogen. Das entspricht der Einordnung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 9.5.

**`SRC-002#Art.17/Abs.3` — 0 `RR`, Interplay.** Die Integration in ein bestehendes sektorspezifisches unionsrechtliches Qualitätsmanagementsystem ist eine Option („may" bzw. „können") und keine zusätzliche Verpflichtung. Die Stelle ist besonders relevant für die spätere integrierte MDR- und AI-Act-Systemlogik.

**`SRC-002#Art.17/Abs.4` — außerhalb des aktuellen System- und Adressatenscope.** Es erfolgt keine Scope-Erweiterung.

---

## 8. Multilingualer Audit

DE/EN: **PASS**.

Geprüft wurden insbesondere: strategy / Konzept bzw. Strategie · design control / Entwurfskontrolle · design verification / Entwurfsprüfung · quality control / Qualitätskontrolle · quality assurance / Qualitätssicherung · means / Mittel · data management / Datenmanagement · setting-up, implementation und maintenance / Einrichtung, Umsetzung und Aufrechterhaltung · record-keeping / Aufzeichnung · security of supply / Versorgungssicherheit · accountability framework / Rechenschaftsrahmen · proportionate to the size / angemessenes Verhältnis zur Größe · degree of rigour / Grad an Strenge · level of protection / Schutzniveau.

| Merkmal | Befund |
| --- | --- |
| Materielle Divergenzen | 0 |
| Weitere Sprachfassungen erforderlich | nein |
| Unresolved | 0 |

---

## 9. Locator-Audit

Alle formalen Lokatoren entsprechen der Syntax aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4. Ein Lokatorelement `Chapeau` wird nicht verwendet; der einleitende Teil von Abs. 1 wird als `SRC-002#Art.17/Abs.1` referenziert. Externe URLs kommen nicht vor. Es wurden **keine** zusätzlichen Cross-Article-`supplementary`-Lokatoren aufgenommen.

---

## 10. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war für diesen Quellenbereich ausreichend. Eine Methodenänderung ist **nicht** erforderlich.

Abgedeckte Fallgestaltungen:

- Oberpflicht gegenüber Qualitätskriterium,
- einleitender QMS-Teil gegenüber Mindestinhalten,
- mehrere eigenständige Prozesskomponenten,
- Strukturen mit „einschließlich" bzw. „including",
- conditional Compliance-Mittel,
- QMS-Integration gegenüber materieller Fachpflicht,
- Cross-Source-Deduplizierung,
- spätere Deduplizierung gegen eine noch nicht extrahierte Quelle,
- Interplay ohne eigene `RR`,
- Proportionalität gegenüber Mindestschutzniveau.

Es wurde **keine** Art.-17-Sonderregel eingeführt.

---

## 11. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | angewandte Extraktions-, Atomizitäts- und Source-Fidelity-Methode (Version 1.2) |
| [COVERAGE_PLAN.md](COVERAGE_PLAN.md) | Freigabe der Quellenbereiche und Einordnung von Buchst. i, Abs. 3 und Abs. 4 (Version 1.9) |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | führende Vergabestelle; hier nicht verändert |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |
| [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | Identifikatoren und Lokator-Syntax |
| [RR_EXTRACTION_ART9.md](RR_EXTRACTION_ART9.md) | Abgleich zu Buchst. g |
| [RR_EXTRACTION_ART10.md](RR_EXTRACTION_ART10.md) | Abgleich zu Buchst. f |

---

## 12. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: vollständige systematische Extraktion der freigegebenen Bereiche von `SRC-002` Art. 17 Abs. 1 und Abs. 2; 24 Kandidaten A17-A bis A17-X, davon 23 regulär und A17-M conditional; 0 unresolved und 0 deferred; Buchst. b, c und h nach gezielter Atomizitäts-Nachadjudikation mit jeweils bestätigtem Split; Buchst. i außerhalb aktiver Gap-Coverage; Abs. 3 Interplay ohne eigene `RR`; Abs. 4 außerhalb Scope; A17-P, A17-Q und A17-R für den späteren Art.-72-Abgleich markiert. Keine Identifikatorvergabe. |
