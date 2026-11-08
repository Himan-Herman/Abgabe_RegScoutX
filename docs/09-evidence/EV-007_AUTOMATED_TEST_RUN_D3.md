# EV-007 — Automatisierter Testlauf Demonstrator D3

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: vollständige unittest-Suiten auf Basis von Commit `13dd6c1` einschließlich Berichtsmodell, HTML- und PDF-Bericht (ReportLab 5.0.1) und zentraler Sprachausgabe (Meilenstein D3). Persistenz- und Berichtstests schreiben nur in temporäre Verzeichnisse mit synthetischen Daten. Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.5 |
| rr_applicability | 0.4 |
| data_model | 0.8 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `-m unittest discover -s tools -p test_*.py` | 129 | 0 | OK |
| `-m unittest discover -s tests -t .` | 177 | 0 | OK |

Neu in diesem Lauf: `tests/test_reporting.py` (17 Tests: `ReportModelTest`, `HtmlReportTest`, `PdfReportTest`, `HistoricalReportTest`, `ReportAuditTest`) und `tests/test_i18n.py` (8 Tests: Schlüsselmengen DE/EN, Platzhalter, fehlende und verwaiste Schlüssel, zentrale Code-Bezeichnungen, Formatierung, keine sichtbaren Texte in Reporting-Modulen), zwei Architekturtests (Renderer nur über Dokumentblöcke, ReportLab nur im PDF-Renderer). Der PDF-Smoke-Test prüft Gültigkeit, Seitenzahl, eingebettete Schriften, Reihenfolge aller Abschnitte mit Seitenzahlen und byte-gleiche Wiederholung. Begleitend liefen alle Validatoren und `tools/traceability.py` ohne Befund (42 von 43 `SR`, 43 von 43 `RUL` durch TC verifiziert).

Zusätzlich manuell gesichtet (keine TC-Evidenz): PDF-Seiten des Referenzfalls TC-036 (Kopf, Profil, Regelverweise, Kennzahlen, Themen- und Phasentabellen, Anforderungsblöcke, Schlussseiten) sowie der HTML-Bericht in Light und Dark und bei 375 px Breite mit 200 % Schriftgröße ohne horizontalen Überlauf.

Geprüfte Testfälle: alle 53 automatisierten TC (TC-001 bis TC-054 ohne den Validatorlauf TC-029), darunter neu TC-051 bis TC-054.

Bewertung: **PASS**.
