# EV-008 — Automatisierter Testlauf Demonstrator D4 (Anwendungs-API)

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: vollständige unittest-Suiten auf Basis von Commit `ec2218b` mit den D4-Änderungen am fachlichen Kern: adaptiver Fragebogen (`regscoutx/questionnaire.py`), Sichten (`regscoutx/assessment_views.py`), Anwendungs-API (`regscoutx/web_api.py`) und lokaler Server (`regscoutx/web_server.py`). Alle Tests schreiben nur in temporäre Verzeichnisse mit synthetischen Daten; der Servertest bindet an einen freien Port auf 127.0.0.1. Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.6 |
| rr_applicability | 0.4 |
| data_model | 0.8 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `-m unittest discover -s tools -p test_*.py` | 129 | 0 | OK |
| `-m unittest discover -s tests -t .` | 198 | 0 | OK |

Neu in diesem Lauf: `tests/test_web_application.py` (21 Tests: `QuestionnaireTest`, `ViewsTest`, `ApiTest`, `ServerTest`) sowie die erweiterte Architekturprüfung (Modul `APPLICATION_API`, Composition Root, Netzwerkmodule nur im lokalen Server). Begleitend liefen alle Validatoren und `tools/traceability.py` ohne Befund (42 von 43 `SR`, 43 von 43 `RUL` durch TC verifiziert).

Geprüfte Testfälle: alle 58 automatisierten TC (TC-001 bis TC-059 ohne den Validatorlauf TC-029). Für die Web-Abnahmeszenarien TC-055 bis TC-059 belegt dieser Lauf ausschließlich die API- und Serverebene; die Browser-Ende-zu-Ende-Ebene ist Gegenstand von EV-009.

Bewertung: **PASS**.
