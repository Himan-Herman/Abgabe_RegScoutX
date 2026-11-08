# Eingefrorene Evaluationseingaben

Version 1.1 · Status: aktiv · ergänzt: 04.11.2026

Dieser Ordner enthält Katalogfassungen, gegen die die Evaluation der Fallstudie (R1, R2) gelaufen ist und die nach der Evaluation fortgeschrieben wurden. Sie sind keine Arbeitskataloge: Der Demonstrator lädt ausschließlich die Kataloge unter `docs/03-regulatory/`. Die Dateien werden nicht geändert.

| Datei | Fassung | SHA-256 | Herkunft | Verwendet von |
| --- | --- | --- | --- | --- |
| `RR_MEASURE_CATALOG_0.1.yaml` | `RR_MEASURE_CATALOG.yaml` Version 0.1 | `3b8fffa428212207d4eb6d2443e84f9c1c8071b325102c920d5ce9b2e0cf544d` | byte-genau aus Commit `8b0ec2f` (unverändert seit `16e08a1`) | `tools/derive_case_reference.py` (Reproduktion der Referenz), `tests/_catalogs.py` (TC-061) |
| `RUL_CATALOG_0.2.yaml` | `RUL_CATALOG.yaml` Version 0.2 | `2db67d46d097eadcff27b2ac36b3c2eb5fd5d6ac4c4d2ba0367e1a937865df0b` | byte-genau aus `17011f3`; identisch zur dokumentierten R1/R2-Regelfassung | Referenz-Reproduktion und TC-061 über `tools/frozen_evaluation_inputs.py` |
| `RR_APPLICABILITY_0.4.yaml` | `RR_APPLICABILITY.yaml` Version 0.4 | `58e5b8ff7022e31520b79ce3bf225510b70948b7c91b63adf65a6344687104be` | byte-genau aus `17011f3`; identisch zur dokumentierten R1/R2-Zuordnung | Referenz-Reproduktion und TC-061 über `tools/frozen_evaluation_inputs.py` |

Begründung und Methode der Fortschreibung auf Version 0.2: [../../03-regulatory/RR_MEASURE_METHOD.md](../../03-regulatory/RR_MEASURE_METHOD.md) Abschnitt 7. Die Evaluationsergebnisse ([../EVALUATION_RESULTS.md](../EVALUATION_RESULTS.md)) gelten für Version 0.1 und werden nicht neu berechnet.

Die beiden ergänzten Kopien sichern den Stand vor der Anhang-III-Korrektur in RUL 0.3 / RR_APPLICABILITY 0.5. Der gemeinsame Leser prüft alle drei eingefrorenen Kataloge vor Verwendung auf vollständige SHA-256-Identität und Version. TC-061 ist nachgelagerte Regression, keine neue R1/R2-Durchführung. Referenzdatei, R1/R2-Ergebnisse und EV-001 bis EV-018 bleiben byte-identisch.
