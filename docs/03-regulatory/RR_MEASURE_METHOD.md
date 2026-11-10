# Methode der Maßnahmen- und Nachweiszuordnung (RR_MEASURE)

Version 1.0 · Status: aktiv · Stand: 29.09.2026 · gilt für [RR_MEASURE_CATALOG.yaml](RR_MEASURE_CATALOG.yaml) ab Version 0.2

Dieses Dokument legt fest, wie jeder regulatorischen Anforderung (`RR`) eine vorgesehene Umsetzungsmaßnahme und eine vorgesehene Nachweisart zugeordnet wird. Es schließt die Kette **Anforderung → Quelle → Lebenszyklusphase → Maßnahme → Nachweisdokument** der Traceability-Matrix nach [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 4 (Befund B-1 des Thesis-Audits, FINAL_THESIS_AUDIT.md (Entwicklungsarchiv; nicht im Abgabepaket)). Es erzeugt **keine** neue regulatorische Anforderung und ändert weder `RR`, `RUL`, `SR`, Anwendbarkeit noch Evaluationsergebnisse. Die Systemanforderung ist SR-043; die Datenstruktur `RR_MEASURE` steht in [DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml).

---

## 1. Begriffe und Abgrenzung

| Begriff | Bedeutung | nicht zu verwechseln mit |
| --- | --- | --- |
| vorgesehene Maßnahme (`measure_key`) | generische, wiederverwendbare Umsetzungsmaßnahme, z. B. „In der Risikomanagementakte dokumentieren“ | einer rechtlichen Pflicht zu genau dieser Maßnahme |
| vorgesehene Nachweisart (`evidence_type`) | Art des Nachweisartefakts, mit dem die Umsetzung typischerweise belegt wird (intended evidence artifact) | einem konkreten Dokument des Herstellers |
| Nachweisreferenz (`EvidenceReference`) | nutzerseitige Angabe eines tatsächlichen Dokuments in einer Bewertung, optional mit `measure_key` | vorgesehener Nachweisart |
| Projektevidenz (`EV-NNN`) | Nachweis dieses Projekts (Test-, Validator-, Evaluationslauf) | beidem oben |

Vorgesehene Maßnahmen und Nachweisarten sind **Traceability-Daten des Demonstrators**. Sie dienen als Arbeitsgrundlage einer Gap-Analyse und behaupten nicht, dass MDR, AI Act oder eine Norm ein bestimmtes Dokument verlangen, sofern der Anforderungstext dies nicht ausdrücklich tut (Mapping-Basis, Abschnitt 2).

## 2. Mapping-Basis

Jede Zuordnung trägt genau eine Mapping-Basis. Sie wird **ausschließlich aus dem deutschen Anforderungstext der `RR`** bestimmt; Normvolltexte liegen nicht im Repository und werden nicht herangezogen.

| Mapping-Basis | Kriterium | Bedeutung für die Aussage |
| --- | --- | --- |
| `SOURCE_EXPLICIT` | Der Anforderungstext benennt das Nachweisartefakt selbst: ein Dokument, eine Aufzeichnung, einen Plan, einen Bericht, eine Spezifikation, ein Verfahren in dokumentierter Form, eine Akte oder vom Hersteller bereitzustellende Informationen (Kennzeichnung, Gebrauchsanweisung, Angaben, Hinweise), bzw. verlangt ausdrücklich Dokumentieren, Aufzeichnen, Aufbewahren oder Archivieren. | Die Nachweisform ist quellenseitig benannt. |
| `PROJECT_DERIVED` | Der Anforderungstext verlangt einen Zustand, eine Eigenschaft, einen Prozess oder eine Tätigkeit (z. B. Risiken bewerten, prüfen, validieren, ein Verfahren vorsehen, Daten sammeln), schreibt aber kein bestimmtes Nachweisdokument vor. | RegScoutX sieht eine geeignete Maßnahme und Nachweisform vor (project-derived evidence mapping); **keine** rechtlich oder normativ vorgeschriebene Dokumentpflicht. |

Die Unterscheidung wird maschinell geprüft: Der Wortlautanker (`basis`) einer `SOURCE_EXPLICIT`-Zuordnung muss ein Artefaktbegriff aus `explicit_evidence_terms` im Katalog sein. Die Regel ist bewusst konservativ: Nennt ein Text nur eine Tätigkeit („Audits durchführen“, „Änderungsanforderung bewerten“), gilt `PROJECT_DERIVED`, auch wenn eine Aufzeichnung naheliegt. Eine dritte Zwischenkategorie („Tätigkeit benannt, Aufzeichnung naheliegend“) wurde erwogen und verworfen, weil sie die für die Aussage entscheidende Grenze – Dokument quellenseitig benannt oder nicht – nicht schärfer macht.

## 3. Ablauf

1. **Regelbasierte Zuordnung (`mapping_rule: TRIGGER`, seit 0.1):** Jede Maßnahme mit `trigger_pattern` wird in Katalogreihenfolge gegen den Anforderungstext geprüft; die erste Übereinstimmung wird zugeordnet, der gefundene Wortlaut ist `basis`. Die Mapping-Basis folgt aus diesem Wortlaut (Abschnitt 2). Der Validator leitet jede TRIGGER-Zuordnung neu ab.
2. **Vorgruppierung der offenen `RR`:** Die 502 in Version 0.1 offenen `RR` (`REVIEW_REQUIRED`, kein expliziter Artefaktbezug) wurden nach Anforderungstext, Themencluster, Lebenszyklusphase, Primärquelle und vorhandenen Artefakt- bzw. Tätigkeitsbegriffen gruppiert.
3. **Fachliche Adjudikation (`mapping_rule: ADJ-…`, seit 0.2):** Jede der 502 `RR` wurde einzeln gelesen und einer der 16 Zuordnungsregeln (Abschnitt 4) zugewiesen; semantisch gleichartige Anforderungen werden über dieselbe dokumentierte Regel behandelt. Jede `RR` erhält einen individuellen Eintrag: Maßnahme, Mapping-Basis, Wortlautanker aus ihrem Text und eine Begründung mit Bezug auf ihren Titel.
4. **Vorrang und Korrektur:** Eine Adjudikation hat Vorrang vor der regelbasierten Zuordnung. Das wird nur genutzt, wo eine Stichprobe eine unpassende TRIGGER-Zuordnung aufgedeckt hat (Abschnitt 6).
5. **Konsistenz- und Stichprobenprüfung:** Abschnitt 6.

Es gibt keine `RR` ohne sinnvolle Zuordnung; eine Platzhaltermaßnahme wurde nicht verwendet.

## 4. Zuordnungsregeln (Adjudikation)

| Regel | Maßnahme | Anwendungsbereich | `RR` |
| --- | --- | --- | --- |
| `ADJ-RM` | `MEAS_RISK_MANAGEMENT_FILE` | Tätigkeit oder Ergebnis des Risikomanagements (Ermittlung, Analyse, Einschätzung, Bewertung, Beherrschung, Restrisiko, Aktualisierung, Einrichtung des Systems) | 105 |
| `ADJ-UE` | `MEAS_USABILITY_ENGINEERING_FILE` | Usability-Engineering-Prozess und gebrauchstauglichkeitsbezogene Auslegung | 73 |
| `ADJ-QMS` | `MEAS_DOCUMENTED_PROCEDURE` | Prozess, Verfahren oder Bestandteil des Qualitätsmanagementsystems | 63 |
| `ADJ-DESIGN` | `MEAS_TECHNICAL_DOCUMENTATION` | Auslegungs- bzw. Entwicklungsergebnis oder Produktmerkmal (Softwareanforderungen, Architektur, Sicherheitsklasse, technische Schutzmaßnahme) | 49 |
| `ADJ-RECORD` | `MEAS_RECORD` | Ergebnis, Festlegung, Mitteilung oder Behandlung mit Aufzeichnung als Nachweis (Lieferantenbewertung, Nichtkonformität, Korrekturmaßnahme, Benachrichtigung) | 47 |
| `ADJ-PMS` | `MEAS_PMS_VIGILANCE` | Überwachung nach dem Inverkehrbringen, Rückmeldungen, Meldungen | 35 |
| `ADJ-INFO` | `MEAS_LABELLING_AND_INSTRUCTIONS` | vom Hersteller bereitzustellende Informationen, Information der Anwender | 22 |
| `ADJ-DATA` | `MEAS_DATA_GOVERNANCE` (neu) | Daten-Governance, Datenverwaltungsverfahren, Eigenschaften von Trainings-, Validierungs- und Testdatensätzen | 21 |
| `ADJ-CHANGE` | `MEAS_CHANGE_CONTROL` | Lenkung, Bewertung, Genehmigung und Umsetzung von Änderungen, Konfigurationskontrolle | 20 |
| `ADJ-PLAN` | `MEAS_PLAN` | Planung bzw. geplante Ausgestaltung eines Prozesses | 17 |
| `ADJ-VERIF` | `MEAS_VERIFICATION` | nachzuweisende Produkteigenschaft (Genauigkeit, Robustheit, Zuverlässigkeit) oder Prüf-/Verifizierungstätigkeit | 17 |
| `ADJ-REVIEW` | `MEAS_REVIEW` | Überprüfung, Angemessenheitsbewertung, Genehmigung, Freigabe | 12 |
| `ADJ-HO` | `MEAS_HUMAN_OVERSIGHT` (neu) | Gestaltung und Bereitstellung der menschlichen Aufsicht | 9 |
| `ADJ-VALID` | `MEAS_VALIDATION` | Validierung bzw. deren Festlegung | 6 |
| `ADJ-REPORT` | `MEAS_REPORT` | Bericht bzw. berichtsförmiges Ergebnis (klinische Bewertung, Problembericht) | 4 |
| `ADJ-COMP` | `MEAS_COMPETENCE` | Kompetenz, Wissen und deren Aufzeichnung | 4 |
| **gesamt** | | 502 offene `RR` aus 0.1 und 2 korrigierte TRIGGER-Zuordnungen | **504** |

**Taxonomie:** Die 15 Maßnahmen aus Version 0.1 wurden zuerst geprüft und wiederverwendet. Zwei Anforderungsarten ließen sich nicht sinnvoll abbilden und erhielten je eine eigene Maßnahme mit Nachweisart (DE/EN): Daten-Governance (`MEAS_DATA_GOVERNANCE`, `EVT_DATA_GOVERNANCE_RECORD`) für Art. 10 AI Act, weil keine bestehende Nachweisart Datensatzeigenschaften und Datenverwaltungsverfahren beschreibt, und menschliche Aufsicht (`MEAS_HUMAN_OVERSIGHT`, `EVT_HUMAN_OVERSIGHT_SPECIFICATION`) für Art. 14 AI Act, weil die vom Anbieter bestimmten Aufsichtsmaßnahmen ein eigener Nachweisgegenstand sind. Robustheitsanforderungen werden über Verifizierung (Eigenschaften), technische Dokumentation (Schutzmaßnahmen) und Risikomanagement (Rückkopplungsschleifen) abgebildet; eine eigene Robustheitsmaßnahme war nicht erforderlich. Präzisiert wurden die Beschreibungen von `EVT_LABELLING_AND_INSTRUCTIONS` (einschließlich Website und Zugangsinformation) und `EVT_REVIEW_RECORD` (einschließlich Genehmigung und Freigabe) sowie die Bezeichnung von `MEAS_REVIEW`. Ergebnis: 17 Maßnahmen, 17 Nachweisarten, keine verwaiste Maßnahme.

## 5. Ergebnis (Version 0.2)

| Kennzahl | Wert |
| --- | --- |
| `RR` mit Maßnahme und Nachweisart | **959 / 959** (0 `REVIEW_REQUIRED`) |
| Zuordnungsart | 455 `TRIGGER` (unverändert aus 0.1), 504 `ADJ` (502 adjudiziert, 2 korrigiert) |
| Mapping-Basis | 378 `SOURCE_EXPLICIT`, 581 `PROJECT_DERIVED` |
| davon adjudiziert | 44 `SOURCE_EXPLICIT`, 460 `PROJECT_DERIVED` |

Nach Themencluster (`SOURCE_EXPLICIT` / `PROJECT_DERIVED`; in 0.1 zugeordnet): Qualitäts- und Risikomanagement 115 / 248 (147 von 363), Software-Lebenszyklus 66 / 141 (111 von 207), Post-Market-Monitoring 69 / 69 (94 von 138), Gebrauchstauglichkeit 37 / 69 (28 von 106), Transparenz 90 / 8 (75 von 98), Data Governance 0 / 21 (0 von 21), Robustheit 1 / 15 (1 von 16), Menschliche Aufsicht 0 / 10 (1 von 10). Verteilungen nach Primärquelle und Lebenszyklusphase gibt `tools/validate_rr_measures.py` aus.

**Lesart:** Die epistemisch zu unterscheidenden Klassen sind (1) quellenseitig explizite Artefaktanforderungen und (2) projektseitig abgeleitete Umsetzungs- und Nachweisvorschläge. Insbesondere die AI-Act-spezifischen Cluster (Data Governance, Menschliche Aufsicht, Robustheit) sind vollständig bzw. fast vollständig projektseitig abgeleitet: Der Katalog enthält für sie vorgesehene Nachweisformen, nicht aber quellenseitig benannte Dokumente.

## 6. Prüfung

- **Validator** (`tools/validate_rr_measures.py`): Schema; Mapping-Status, Mapping-Basis, Zuordnungsregel und Begründung je `RR`; Wortlautanker im Anforderungstext; `SOURCE_EXPLICIT` nur mit Artefaktbegriff; TRIGGER-Zuordnungen und ihre Mapping-Basis reproduzierbar aus den `trigger_pattern`; ADJ-Zuordnungen tragen die Maßnahme ihrer Regel; gültige `measure_key`, Nachweisarten mit DE/EN-Bezeichnungen, keine verwaisten Maßnahmen, Nachweisarten oder Regeln. Ausgabe der Kennzahlen nach Mapping-Basis, Themencluster, Primärquelle und Lebenszyklusphase.
- **Traceability** (`tools/traceability.py`): 959 von 959 `RR` mit Quelle, Lebenszyklusphase, Maßnahme und Nachweisart; die abgeleitete Matrix weist die Mapping-Basis je `RR` aus.
- **Konsistenz:** Die Zuordnung aller 502 offenen `RR` wurde vollständig mit Regel, Anker und Titel gegengelesen; Wortlautanker, die die geforderte Tätigkeit nicht trafen, wurden präzisiert.
- **Stichprobe der TRIGGER-Zuordnungen:** 40 von 457 (deterministisch gezogen, Seed 20260929). 38 passend; 2 unpassend und durch Adjudikation korrigiert: RR-220 („Die Risikobewertung muss zeigen …“, vorher Kennzeichnung über „eIFU“, jetzt Risikomanagement) und RR-457 („Entwicklungsplanung … dokumentieren“, vorher Review über „Reviews“, jetzt Plan). In zwei weiteren Fällen (RR-470, RR-513) ist die Mapping-Basis konservativ `PROJECT_DERIVED`, obwohl der Text zusätzlich eine Aufzeichnung verlangt. Die übrigen 417 TRIGGER-Zuordnungen sind nicht einzeln fachlich bestätigt; nach der Stichprobe ist mit einem kleinen Anteil unpassender Zuordnungen zu rechnen.

## 7. Versionierung und Bindung der Evaluation

- `RR_MEASURE_CATALOG.yaml` 0.1 bleibt unverändert erhalten: in der Versionsgeschichte (bis Commit `950a7a5`) und byte-genau als eingefrorene Evaluationseingabe [../08-evaluation/frozen/RR_MEASURE_CATALOG_0.1.yaml](../08-evaluation/frozen/RR_MEASURE_CATALOG_0.1.yaml).
- **Evaluation R1/R2 verwendete Version 0.1.** Ihre Ergebnisse werden nicht rückwirkend neu berechnet; es gibt keine Evaluationsrevision R3. Begründung: Die Fortschreibung betrifft die Vollständigkeit der Traceability des Thesis-Endstands, nicht die eingefrorene regulatorische Entscheidungs-, Anwendbarkeits- oder Gap-Logik; keine Anwendbarkeit, kein Gap-Status und keine `RR` ändert sich. Betroffen wären ausschließlich Maßnahmenangaben (Maßnahmenstatus und Maßnahmen in Anforderungsdetail und Bericht, Kriterium T10, vollständiger Datensatz, Zahl offener Maßnahmenzuordnungen – 284 im Fall) und die davon abhängigen Berichtsinhalte und Inhaltshashes.
- **Thesis-Endstand der Traceability verwendet Version 0.2.** Die Referenzableitung (`tools/derive_case_reference.py`) und der Regressionstest TC-061 lesen die eingefrorene Fassung 0.1 (SHA-256 geprüft), damit die berichteten Evaluationskennzahlen reproduzierbar bleiben.
- Laufzeitfolge: Das `CatalogVersionSet` enthält `rr_measure_version` 0.2. Mit 0.1 gespeicherte Bewertungen öffnen als `MISMATCH` und lassen sich bewusst neu bewerten (SR-037). Die Evaluationswerkzeuge unter `evaluation/` und die Browser-Spezifikationen der Fallstudie reproduzieren R2 vollständig nur auf dem Evaluationsstand (`8b0ec2f`).

## 8. Grenzen

- Die Zuordnung ist eine projektseitige Modellierung durch den Projektbearbeiter, kein unabhängiges fachliches Review.
- Genau eine primäre Maßnahme je `RR`; mehrere geeignete Nachweisformen (z. B. Spezifikation und Verifizierung) werden nicht gemeinsam ausgewiesen.
- Die Mapping-Basis bewertet den Anforderungstext des Katalogs, nicht den vollständigen Quelltext (etwa den einleitenden Satz eines Artikels oder eine Normklausel); eine quellenseitig an anderer Stelle geforderte Dokumentation kann daher als `PROJECT_DERIVED` erscheinen.
- Oberfläche und Bericht zeigen Maßnahme und Nachweisart als „vorgesehen“, die Mapping-Basis jedoch nicht; sie ist im Katalog und in der abgeleiteten Traceability-Matrix ausgewiesen.
- Die Statusbezeichnung von `MAPPED` („Maßnahme regelbasiert zugeordnet“, `DATA_MODEL.yaml` 0.8) bezeichnet seit 0.2 eine Zuordnung nach einer dokumentierten Zuordnungsregel (`TRIGGER` oder `ADJ-…`), nicht ausschließlich eine automatische Zuordnung. Sie wurde nicht geändert, weil eine Änderung das an die Evaluation gebundene Datenmodell 0.8 berühren würde.

## 9. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung mit `RR_MEASURE_CATALOG.yaml` 0.2: Mapping-Basis, Ablauf, 16 Zuordnungsregeln, zwei neue Maßnahmen, Ergebnis, Prüfung einschließlich Stichprobe, Bindung der Evaluation an 0.1, Grenzen. |
