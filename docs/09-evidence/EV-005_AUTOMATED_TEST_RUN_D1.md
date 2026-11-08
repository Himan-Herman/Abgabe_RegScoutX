# EV-005 — Automatisierter Testlauf Demonstrator D1

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: vollständige unittest-Suiten auf Basis von Commit `acf78d7` einschließlich des Assessment-/Gap-Kerns (Meilenstein D1). Vollständige Regression, weil Applicability-Domainobjekte in den gemeinsamen Kern verlegt wurden. Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.4 |
| rr_applicability | 0.4 |
| data_model | 0.6 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `-m unittest discover -s tools -p test_*.py` | 129 | 0 | OK |
| `-m unittest discover -s tests -t .` | 133 | 0 | OK |

Neu in diesem Lauf: `tests/test_assessment_service.py` (29 Tests: `GapStatusTest`, `EvidenceMeasureTest`, `RecalculationTest`, `AssessmentResultTest`, `AssessmentInputTest`, `GoldenCaseAssessmentTest`), zwei Architekturtests (Modulklassifikation, Zyklenfreiheit) und ein Validatortest (Kategorie K). Begleitend liefen alle Validatoren und `tools/traceability.py` ohne Befund (35 von 43 `SR` und 43 von 43 `RUL` durch TC verifiziert).

Geprüfte Testfälle: alle 45 automatisierten TC (TC-001 bis TC-046 ohne den Validatorlauf TC-029), darunter neu TC-042 bis TC-046 und die Referenzfälle TC-036 bis TC-039 zusätzlich über den Assessment-Kern.

Bewertung: **PASS**.
