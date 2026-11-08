# EV-006 — Automatisierter Testlauf Demonstrator D2

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: vollständige unittest-Suiten auf Basis von Commit `3d36f9a` einschließlich Anwendungseinstieg, lokaler Persistenz, Versionsabgleich, Revisionen, Audit und Bestätigungspflicht wieder anwendbarer Bewertungen (Meilenstein D2). Vollständige Regression, weil `GAP_ENGINE` und `ASSESSMENT_SERVICE` erweitert wurden. Persistenztests schreiben ausschließlich in temporäre Verzeichnisse mit synthetischen Daten. Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.5 |
| rr_applicability | 0.4 |
| data_model | 0.7 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `-m unittest discover -s tools -p test_*.py` | 129 | 0 | OK |
| `-m unittest discover -s tests -t .` | 150 | 0 | OK |

Neu in diesem Lauf: `tests/test_assessment_application.py` (17 Tests: `PersistenceTest`, `VersionRevisionTest`, `AuditTest`, `EvidenceLifecycleTest`, `ReactivationTest`), angepasste Tests in `tests/test_assessment_service.py` (Bestätigungspflicht, Ableitungstabelle mit veralteten Bewertungen, zentrale Bezeichnungen) und ein Architekturtest (Persistenzimplementierung nur über die Schnittstelle). Begleitend liefen alle Validatoren und `tools/traceability.py` ohne Befund.

Geprüfte Testfälle: alle 49 automatisierten TC (TC-001 bis TC-050 ohne den Validatorlauf TC-029), darunter neu TC-047 bis TC-050, die erweiterten TC-043 und TC-044 sowie die Referenzfälle TC-036 bis TC-039.

Bewertung: **PASS**.
