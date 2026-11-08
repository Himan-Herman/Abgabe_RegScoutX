# EV-004 — Automatisierter Testlauf Block-5-Abschluss

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: unittest-Suiten auf Basis von Commit `16e08a1` einschließlich der Abschlussänderungen (TC-041, `rr_measure_version`). Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.3 |
| rr_applicability | 0.4 |
| data_model | 0.5 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `-m unittest discover -s tools -p test_*.py` | 128 | 0 | OK |
| `-m unittest discover -s tests -t .` | 102 | 0 | OK |

Gezielte Tests:

- `test_g2_eifu_in_addition_to_paper (tests.test_applicability_engine.TopLevelRoutingTest.test_g2_eifu_in_addition_to_paper) ... ok`
- `test_g3_src009_article_3_1_path_is_structurally_unreachable (tests.test_applicability_engine.TopLevelRoutingTest.test_g3_src009_article_3_1_path_is_structurally_unreachable) ... ok`
- `test_versions_are_pinned (tests.test_catalog_repository.CatalogRepositoryTest.test_versions_are_pinned) ... ok`
- `test_version_set_matches_data_model (tests.test_catalog_repository.CatalogRepositoryTest.test_version_set_matches_data_model) ... ok`

Geprüfte Testfälle: TC-028, TC-041.

Bewertung: **PASS**.
