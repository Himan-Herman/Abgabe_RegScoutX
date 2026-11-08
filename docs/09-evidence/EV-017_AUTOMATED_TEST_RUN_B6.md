# EV-017 — Automatisierter Testlauf Block 6 (vollständig, einschließlich Browser)

Version 1.0 · Status: aktiv · Datum: 29.09.2026

Durchführung: vollständige Test- und Prüfläufe auf Basis von Commit `219134c` mit den Evaluationsartefakten von Block 6 (Evaluationswerkzeug `evaluation/`, Regressionstest TC-061, Browser-Spezifikationen der Fallstudie, Dokumentation). Alle Läufe arbeiten ausschließlich lokal mit synthetischen Daten in temporären Verzeichnissen bzw. in `web/e2e/.data`. Umgebung: macOS 27.0, Python 3.13.15, Node.js 22.21.0, Google Chrome 153.0.8010.53. Dieses Artefakt beeinflusst kein Testergebnis.

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
| `.venv/bin/python -m unittest discover -s tools -p test_*.py` | 135 | 0 | OK |
| `.venv/bin/python -m unittest discover -s tests -t .` | 208 | 0 | OK |
| alle Validatoren unter `tools/` einschließlich `validate_reference_assessment.py`, `derive_case_reference.py --check` und `tools/traceability.py` | — | 0 | PASS, ohne Befund |
| `cd web && npm run build` (Typprüfung einschließlich `e2e/` und Produktionsbuild) | — | 0 | ohne Warnung |
| `cd web && npx vitest run` | 32 | 0 | OK |
| `cd web && npx playwright test` | 30 (+ 6 übersprungen) | 0 | OK |

Gegenüber EV-009 neu: TC-061 (5 Tests in `tests/test_case_study_evaluation.py`, Fallstudie gegen die eingefrorene Referenz), 6 Validator-Tests der Referenz, der Test zur kennungsunabhängigen Reihenfolge des Nachweisregisters (Befund F-2) und die Prüfung der gespeicherten Bewertung ohne Wirkung im Abnahmeablauf (Befund F-3). Übersprungen sind die Screenshot-Erzeugung (3, EV-010) und die Fallstudien-Spezifikationen (3), die nur auf ausdrücklichen Aufruf laufen; ihr Lauf ist in EV-016 belegt.

Geprüfte Testfälle: alle 60 automatisierten TC (TC-001 bis TC-061 ohne den Validatorlauf TC-029).

Grenzen: nur Google Chrome; automatisierte Barrierefreiheitsprüfung ersetzt keine manuelle Screenreader-Prüfung.

Bewertung: **PASS**.
