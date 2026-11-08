# EV-013 — Evaluationslauf R2 der Fallstudie: Soll/Ist-Vergleich

Version 1.0 · Status: aktiv · Datum: 28.09.2026

| Merkmal | Angabe |
| --- | --- |
| Lauf | `.venv/bin/python -m evaluation.run_evaluation --revision R2 --repetitions 20 --performance 10` |
| Softwarestand | Commit `219134c` (Korrekturen F-2 `6c4610a`, F-3 `219134c`; Werkzeug angeglichen, F-5) |
| Referenz | unverändert, SHA-256 `45cf843e993eb7c9fc17dfeb810541b667087bbbd3effc726188d04f6ad2fc66` (EV-011) |
| Zeitraum (UTC) | 2026-09-28 22:13–22:31 |
| Artefakte | [results/R2/metrics.json](../08-evaluation/results/R2/metrics.json) (SHA-256 `62e053a00e18c08a243f3b8ee416406b432f412d26dee00a362b61b9f53464ed`), [results/R2/system_output.json](../08-evaluation/results/R2/system_output.json), PDF-Berichte `case-study-report_R2_de.pdf` (`12c2275d48271a48b8929718aaf29d68b114ee8753cb70478d9bb5a0183cb9c5`) und `_en.pdf` (`d919221be91bfc4a3c7e9021fac477976552c7bf0677158b34cd401b7efe62d9`) in [evaluation/](evaluation/) |

Ergebnis: Anwendbarkeit 959/959, Precision und Recall der Menge `APPLICABLE` 1,0, Begründungscodes 959/959; Gap 32/32 mit allen Nebenmerkmalen; Requirement Completeness 542/542, Gap Completeness 32/32; Nachvollziehbarkeit 116 PASS / 4 NA / 1 FAIL (T6 RR-205, Befund F-4); Leistung (Median): Anlegen 0,35 s, Anforderungsliste 0,11 s, Berichtsdokument 0,19 s, HTML 0,18 s, PDF 2,44 s. Einzelheiten: [EVALUATION_RESULTS.md](../08-evaluation/EVALUATION_RESULTS.md).

Bewertung gegen TC-061: **PASS**.
