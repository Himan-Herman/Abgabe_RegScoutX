# EV-001 — Automatisierter Testlauf Block 5

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: unittest-Suiten gegen den Arbeitsstand auf Basis von Commit `04672b3` einschließlich der Block-5-Änderungen (dieses Artefakt selbst beeinflusst kein Testergebnis). Interpreter `.venv/bin/python`, `PYTHONDONTWRITEBYTECODE=1`.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.3 |
| rr_applicability | 0.4 |
| data_model | 0.4 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `-m unittest discover -s tools -p test_*.py` | 128 | 0 | OK |
| `-m unittest discover -s tests -t .` | 99 | 0 | OK |

Geprüfte Testfälle (39): TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011, TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-030, TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038, TC-039, TC-040.

Bewertung: **PASS**.
