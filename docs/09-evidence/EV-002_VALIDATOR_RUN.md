# EV-002 — Validatorlauf Block 5

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: alle Validatoren unter `tools/` auf Basis von Commit `04672b3` einschließlich der Block-5-Änderungen.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.3 |
| rr_applicability | 0.4 |
| data_model | 0.4 |
| rr_measure | 0.1 |

| Validator | Exit-Code | Ausgabe |
| --- | --- | --- |
| `tools/validate_rr_catalog.py` | 0 | RR catalog validation: PASS · version: 0.26 · requirements: 959 |
| `tools/validate_rul_catalog.py` | 0 | RUL catalog validation: PASS · version: 0.2 · rules: 43 |
| `tools/validate_sr_catalog.py` | 0 | SR catalog validation: PASS · version: 0.3 · requirements: 43 |
| `tools/validate_data_model.py` | 0 | Data model validation: PASS · version: 0.4 · entities: 9 |
| `tools/validate_rr_applicability.py` | 0 | RR applicability validation: PASS · version: 0.4 · requirements: 959 CONDITIONAL=629 NOT_STATED=61 REGULAR=269 |
| `tools/validate_standards_mapping.py` | 0 | Standards mapping validation: PASS · version: 1.1 · candidates: 594 CROSSWALK_ONLY=2 CROSS_NORM_MERGE=15 EXISTING_RR_SUPPORT=1 NEW_UNIQUE_RR=576 · merges: 6; new RR: 582; relations: 6 |
| `tools/validate_rr_measures.py` | 0 | RR measure catalog validation: PASS · version: 0.1 · measures: 15; evidence types: 15 · requirements: MAPPED=457 REVIEW_REQUIRED=502 |
| `tools/validate_test_catalog.py` | 0 | Test catalog validation: PASS · test cases: 40 AUTOMATED=39 VALIDATOR=1 golden=4 · evidence: 3 |
| `tools/traceability.py` | 0 | Traceability check: PASS · links: 4284 ·   ALLOCATED_TO: 94 ·   APPLICABILITY_BLOCK: 959 |

Geprüfte Testfälle: TC-029, TC-030, TC-035.

Bewertung: **PASS**.
