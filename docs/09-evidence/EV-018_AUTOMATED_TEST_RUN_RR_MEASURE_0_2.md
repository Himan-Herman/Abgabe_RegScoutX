# EV-018 — Validator- und Testlauf nach RR_MEASURE 0.2 (Thesis-Endstand)

Version 1.0 · Status: aktiv · Datum: 29.09.2026

Durchführung: alle Validatoren und die unittest-Suiten `tools/` und `tests/` auf Basis von Commit `43c7b13` (Maßnahmenkatalog `RR_MEASURE_CATALOG.yaml` 0.2, Methode [RR_MEASURE_METHOD.md](../03-regulatory/RR_MEASURE_METHOD.md)). Alle Tests arbeiten ausschließlich lokal mit synthetischen Daten in temporären Verzeichnissen. Umgebung: macOS 27.0, Python 3.13.15. Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.6 |
| rr_applicability | 0.4 |
| data_model | 0.8 |
| rr_measure | 0.2 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `.venv/bin/python -m unittest discover -s tools -p test_*.py` | 142 | 0 | OK |
| `.venv/bin/python -m unittest discover -s tests -t .` | 208 | 0 | OK |
| alle Validatoren unter `tools/` einschließlich `validate_rr_measures.py`, `validate_reference_assessment.py`, `derive_case_reference.py --check` und `tools/traceability.py` | — | 0 | PASS, ohne Befund |

Kennzahlen: `RR_MEASURE` 0.2 mit 959 `MAPPED` (378 `SOURCE_EXPLICIT`, 581 `PROJECT_DERIVED`; 455 regelbasiert, 504 adjudiziert), 17 Maßnahmen, 17 Nachweisarten, keine verwaiste Maßnahme; `tools/traceability.py`: 959 von 959 `RR` mit Quelle, Lebenszyklusphase, Maßnahme und Nachweisart. Gegenüber EV-017 neu: 7 Tests des Maßnahmen-Validators (Mapping-Basis, Regel, Anker, Begründung, verwaiste Maßnahmen); TC-061 läuft gegen die eingefrorene Fassung `RR_MEASURE` 0.1 (SHA-256 geprüft) und bestätigt die berichteten Evaluationskennzahlen unverändert; der Pfad `REVIEW_REQUIRED` wird über eine Testfixture geprüft.

Geprüfte Testfälle: 60 automatisierte TC (TC-001 bis TC-061 ohne den Validatorlauf TC-029). Für TC-055 bis TC-060 belegt dieser Lauf die API- und Serverebene; Frontend-Build, Vitest und Playwright wurden nicht erneut ausgeführt, weil kein Frontend-Code geändert wurde (letzter vollständiger Browserlauf: EV-017).

Grenzen: kein Browserlauf; die fachliche Angemessenheit der Maßnahmenzuordnung ist durch Validatoren nicht geprüft.

Bewertung: **PASS**.
