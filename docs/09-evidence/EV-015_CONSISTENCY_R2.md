# EV-015 — DE/EN- und Web/PDF-Konsistenz sowie kriteriengestützte Verständlichkeitsprüfung (R2)

Version 1.0 · Status: aktiv · Datum: 28.09.2026

Grundlage: Primärlauf von R2 (EV-013), `results/R2/metrics.json` → `consistency`, `comprehension_checks`, `traceability`; Screenshots [screenshots/B6/](screenshots/B6/).

- **DE/EN:** 14 von 14 Berichtsabschnitten mit identischen sprachneutralen Werten; 959 identische RR-Kennungen; identische Kennungen im Berichtskopf.
- **Web/PDF:** gleicher Inhaltshash für Web-Berichtsdokument, HTML und PDF je Sprache; 33 107 von 33 107 Textbestandteilen im PDF-Text, 33 106 im sichtbaren HTML-Text (Beschriftung des Bewertungsverlaufs nur als `aria-label`, F-7). PDF-Text über die eingebetteten ToUnicode-Tabellen gelesen (`evaluation/pdf_text.py`).
- **Verständlichkeit (K1–K9):** 7 PASS, 2 PARTIAL (K2 Quellen nicht anwendbarer RR nicht im Bericht, F-4; K4 gleicher Wortlaut von Anwendbarkeits- und Gap-Kennzeichen bei inaktiven RR, F-6), 0 FAIL.

Kein unabhängiges fachliches Review durchgeführt; keine Nutzerstudie. Die Bewertung ist eine Artefaktprüfung durch den Projektbearbeiter.

Bewertung gegen TC-061: **PASS** (Konsistenzkriterien erfüllt; PARTIAL-Befunde dokumentiert).
