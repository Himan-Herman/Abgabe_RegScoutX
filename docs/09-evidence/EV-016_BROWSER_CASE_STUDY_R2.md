# EV-016 — Browser-Durchlauf der Fallstudie und Fallstudien-Screenshots (R2)

Version 1.0 · Status: aktiv · Datum: 29.09.2026

| Merkmal | Angabe |
| --- | --- |
| Lauf | `cd web && RX_CASE_STUDY=1 RX_REVISION=R2 npx playwright test e2e/case-study.spec.ts e2e/case-study-performance.spec.ts` (3 Tests, alle bestanden) |
| Softwarestand | Commit `219134c`, gebaute Oberfläche, lokaler Server mit frischen Testdaten, Google Chrome 153 |
| Eingaben | [results/case_inputs.json](../08-evaluation/results/case_inputs.json) (aus der Referenz exportiertes Profil und Szenario, ohne Soll-Ergebnisse) |
| Ergebnis | [results/R2/browser_case_study.json](../08-evaluation/results/R2/browser_case_study.json), [results/R2/browser_performance.json](../08-evaluation/results/R2/browser_performance.json) |
| Screenshots | [screenshots/B6/](screenshots/B6/): `01-case-profile`, `02-applicability`, `03-gap-lens`, `04-gap-requirement`, `05-decision-trace`, `06-evidence`, `07-report` |

Die Fallstudie wurde vollständig über die Oberfläche erfasst: Profil adaptiv (41 Antworten), 22 Erfüllungsangaben an anwendbaren RR, 8 Nachweisreferenzen, davon 3 mit vorgesehener Maßnahme. Vergleich mit dem API-Lauf R2: 956 von 956 vergleichbaren RR identisch (Anwendbarkeit, Begründung, Gap-Status, Gap-Begründung, Gap-Kennzeichen, Bewertungs-, Nachweis- und Maßnahmenstatus, Anzahl Nachweise), identische Summen. Die Angaben C1–C3 an nicht anwendbaren bzw. ungeklärten RR sind in der Oberfläche bewusst nicht erfassbar und daher vom Vergleich ausgenommen. Leistung im Browser (Median aus 10): Explorer laden 798 ms, Suche 37,5 ms.

Bewertung gegen TC-061: **PASS**.
