# EV-012 — Evaluationslauf R1 der Fallstudie (vor Korrektur)

Version 1.0 · Status: aktiv · Datum: 28.09.2026

| Merkmal | Angabe |
| --- | --- |
| Lauf | `.venv/bin/python -m evaluation.run_evaluation --revision R1 --repetitions 20 --performance 10` |
| Softwarestand | Commit `9928f1b` (Software identisch mit dem Freeze-Stand `ee76ef8`) |
| Referenz | REFERENCE_ASSESSMENT.yaml, SHA-256 `45cf843e993eb7c9fc17dfeb810541b667087bbbd3effc726188d04f6ad2fc66` (EV-011) |
| Zeitraum (UTC) | 2026-09-28 21:45–22:03 |
| Artefakte | [results/R1/metrics.json](../08-evaluation/results/R1/metrics.json), [results/R1/system_output.json](../08-evaluation/results/R1/system_output.json); die beiden R1-PDF-Berichte sind im Entwicklungsarchiv aufbewahrt und nicht Teil des Abgabepakets |
| Umgebung | Apple M4 Max, macOS 27.0, Python 3.13.15; lokaler Server über HTTP |

Ergebnis: Anwendbarkeit 959/959 (Begründungscodes 959/959), Gap 32/32, vollständige Datensätze 32/32, Nachvollziehbarkeit 114 PASS / 4 NA / 3 FAIL; fachliche Aspekte 20/20 reproduzierbar, das Berichtsdokument ohne Kennungen jedoch 0/20 (Nachweisregister nach Zufallskennung sortiert, Befund F-2). Befunde F-1 bis F-5 in [EVALUATION_RESULTS.md](../08-evaluation/EVALUATION_RESULTS.md) Abschnitt 10; das Ergebnis ist unverändert erhalten.

Bewertung gegen TC-061: **FAIL** (Reproduzierbarkeit des Berichtsdokuments nicht gegeben). Anlass für die Evaluation Revision R2.
