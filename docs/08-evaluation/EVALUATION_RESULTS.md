# Evaluationsergebnisse der Fallstudie (Block 6)

Version 1.2 · Status: aktiv · Stand: 29.09.2026

Ergebnisse der Evaluation nach [EVALUATION_METHOD.md](EVALUATION_METHOD.md) für die Fallstudie [CASE_STUDY.md](CASE_STUDY.md) gegen die vor dem Systemlauf eingefrorene Referenz [REFERENCE_ASSESSMENT.yaml](REFERENCE_ASSESSMENT.yaml) (SHA-256 `45cf843e…fc66`, Freeze-Commit `9928f1b`, [EV-011](../09-evidence/EV-011_CASE_STUDY_REFERENCE_FREEZE.md)). Alle Zahlen stammen aus den maschinenlesbaren Ergebnissen unter [results/](results/) und gelten für den definierten Untersuchungsumfang (versionierte Kataloge, ein Hauptfall). Es wird weder eine vollständige Abdeckung von MDR oder AI Act noch eine Zertifizierung, rechtliche Verbindlichkeit, klinische Validierung oder Nutzerakzeptanz behauptet.

---

## 1. Evaluationsläufe und Revisionen

| Revision | Softwarestand | Zeitraum (UTC) | Anlass | Ergebnisse |
| --- | --- | --- | --- | --- |
| R1 | `9928f1b` (Software identisch mit dem Freeze-Stand `ee76ef8`; der Commit enthält nur Referenz, Dokumentation und Prüfwerkzeuge) | 2026-09-28 21:45–22:03 | erster Evaluationslauf nach dem Referenz-Freeze | [results/R1/](results/R1/), [EV-012](../09-evidence/EV-012_EVALUATION_RUN_R1.md) |
| R2 | `219134c` (Korrekturen F-2 `6c4610a` und F-3 `219134c`; Werkzeugkorrektur F-5, Werkzeugstand `evaluation/` versioniert in `8b0ec2f`) | 2026-09-28 22:13–22:31 | Evaluation Revision nach Befunden aus R1 | [results/R2/](results/R2/), [EV-013](../09-evidence/EV-013_EVALUATION_RUN_R2.md) bis [EV-016](../09-evidence/EV-016_BROWSER_CASE_STUDY_R2.md) |

Vor R1 wurde das Laufwerkzeug einmal zur technischen Erprobung ausgeführt (Laufzeit, Größen und Inhaltshashes der Artefakte). Ein Vergleich mit der Referenz fand dabei nicht statt. Die Referenz wurde weder nach diesem Probelauf noch nach R1 oder R2 geändert (keine Reference Correction).

Systemlauf: lokaler Server und Anwendungs-API per HTTP; Bewertung angelegt, Profil adaptiv über 41 Fragen (keine Profilangabe blieb ungefragt), 25 Erfüllungsangaben, 10 Nachweisreferenzen, Berichtsdokument DE/EN, HTML und PDF DE/EN; 173 Anfragen, 45,8 s (R2). Ergebnis-Summen (R2): 542 anwendbar, 128 nicht anwendbar, 289 ungeklärt; 4 erfüllt, 4 teilweise erfüllt, 4 nicht erfüllt, 7 Nachweisprüfung erforderlich, 523 nicht bewertet; 15 Gaps; 284 anwendbare RR mit offener Maßnahmenzuordnung.

## 2. Korrektheit

### 2.1 Applicability Agreement (alle 959 RR)

| Referenz \ System | `APPLICABLE` | `NOT_APPLICABLE` | `APPLICABILITY_UNRESOLVED` |
| --- | --- | --- | --- |
| `APPLICABLE` | **542** | 0 | 0 |
| `NOT_APPLICABLE` | 0 | **128** | 0 |
| `APPLICABILITY_UNRESOLVED` | 0 | 0 | **289** |

Übereinstimmung **959 von 959 (100 %)**, 0 Abweichungen (R1 und R2). Menge `APPLICABLE`: TP 542, FP 0, FN 0; Precision 1,0, Recall 1,0; keine Verschiebung zwischen `APPLICABLE` und `APPLICABILITY_UNRESOLVED`. Begründungscodes: 959 von 959 gleich der Referenz (284 `SCOPE_ACTIVE`, 258 `LOCAL_CONDITIONS_MET`, 212 `LOCAL_CONDITION_NOT_MODELLED`, 70 `SCOPE_INACTIVE`, 61 `CONDITIONALITY_NOT_DOCUMENTED`, 58 `LOCAL_CONDITION_NOT_MET`, 16 `LOCAL_CONDITION_UNRESOLVED`).

**Einordnung:** Die Übereinstimmung belegt, dass der Demonstrator die dokumentierte, adjudizierte Anwendbarkeitsmethodik für diesen Fall vollständig übereinstimmend umsetzt. Weil die Referenz dieselbe dokumentierte Methodik unabhängig umsetzt, ist sie kein Beleg für die rechtliche Richtigkeit der Zuordnung selbst (EVALUATION_METHOD.md Abschnitt 2).

### 2.2 Gap Agreement (32 RR des Gap-Referenz-Umfangs)

| Gap-Status (Referenz) | RR | übereinstimmend |
| --- | --- | --- |
| `FULFILLED` | 4 | 4 |
| `PARTIALLY_FULFILLED` | 4 | 4 |
| `NOT_FULFILLED` | 4 | 4 |
| `EVIDENCE_REVIEW_REQUIRED` | 7 | 7 |
| `NOT_ASSESSED` | 10 | 10 |
| `APPLICABILITY_UNRESOLVED` | 2 | 2 |
| `NOT_APPLICABLE` | 1 | 1 |
| **gesamt** | **32** | **32** |

Übereinstimmung 32 von 32 (R1 und R2); ebenso Gap-Begründung, Gap-Kennzeichen, Bewertungszustand und Nachweisstatus je 32 von 32. Wegen der kleinen Menge wird keine Inferenzstatistik berichtet.

## 3. Vollständigkeit (im definierten Untersuchungsumfang)

- **Requirement Completeness:** 542 von 542 Referenz-`APPLICABLE`-RR als anwendbar ausgewiesen (Recall 1,0); zusätzlich keine ungeklärte oder nicht anwendbare RR als anwendbar.
- **Gap Completeness:** 32 von 32 RR mit vollständigem Datensatz (RR mit Titel, Anwendbarkeit, Gap-Status, Primärquelle = Katalog, Lebenszyklusphasen = Katalog, Maßnahmenstatus und Maßnahmen = RR_MEASURE, Herleitung).

## 4. Reproduzierbarkeit

| Aspekt (20 Wiederholungen über den adaptiven HTTP-Pfad) | R1 | R2 |
| --- | --- | --- |
| Anwendbarkeit und Begründung je RR | 20/20 | 20/20 |
| Gap-Status, -Begründung, -Kennzeichen je RR | 20/20 | 20/20 |
| alle Ergebnisfelder je RR (einschließlich Nachweis- und Maßnahmenstatus) | 20/20 | 20/20 |
| Entscheidungen mit Regelpfaden | 20/20 | 20/20 |
| Summen, Blockzustände, Pfad der Frageführung, Anforderungsdetails | 20/20 | 20/20 |
| Berichtsdokument DE bzw. EN ohne Kennungen und Zeitstempel | **0/20** | **20/20** |
| vollständige fachliche Sicht | 0/20 | **20/20** |
| Roh-Fingerprint bzw. Roh-Inhaltshash | 20 verschiedene Werte | 20 verschiedene Werte |

Die Rohwerte von Fingerprint und Inhaltshash unterscheiden sich je Lauf, weil sie die je Lauf neu vergebenen Bewertungs- bzw. Nachweiskennungen enthalten (Befund F-1). Mit festen Nachweiskennungen über den Anwendungseinstieg ergeben 20 Wiederholungen genau einen Fingerprint (`288a9dab…7d73`). In R1 unterschied sich das Berichtsdokument durch die Reihenfolge des Nachweisregisters (Befund F-2); nach der Korrektur ist es 20/20 identisch.

## 5. Nachvollziehbarkeit (Stichprobe von 11 RR, Kriterien T1–T11)

| RR | Themencluster / Quelle | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RR-082 | Qualitäts-/Risikomgmt. / AI Act | P | P | P | P | P | P | NA | P | P | P | P |
| RR-094 | Data Governance / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-076 | Transparenz / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-064 | Menschliche Aufsicht / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-074 | Robustheit / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-096 | Post-Market / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-172 | Software-Lebenszyklus / MDR | P | P | P | P | P | P | NA | P | P | P | P |
| RR-189 | Gebrauchstauglichkeit / MDR | P | P | P | P | P | P | NA | P | P | P | P |
| RR-001 | ungeklärt (C1) / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-034 | ungeklärt (C2) / AI Act | P | P | P | P | P | P | P | P | P | P | P |
| RR-205 | nicht anwendbar (C3) / eIFU | P | P | P | P | P | **F** | NA | P | P | P | P |

P = PASS, F = FAIL, NA = NOT_APPLICABLE (keine Ergänzungsquelle im Katalog). **R2: 116 PASS, 4 NOT_APPLICABLE, 1 FAIL** von 121 Prüfungen. Das FAIL betrifft T6 bei RR-205: Der Bericht führt nicht anwendbare RR nur mit Begründung, ohne Quellen (Befund F-4); in der Oberfläche und im Anforderungsdetail ist die Quelle vorhanden. R1: 114 PASS, 4 NA, 3 FAIL (zusätzlich T11 bei RR-001 und RR-205, Befunde F-3 und F-5).

## 6. Verständlichkeit und Konsistenz (kriteriengestützte Artefaktprüfung)

Kein unabhängiges fachliches Review durchgeführt; keine Nutzerstudie. Bewertung durch den Projektbearbeiter anhand der vorab festgelegten Kriterien und der Evidenz aus R2, Oberfläche (Screenshots [B6](../09-evidence/screenshots/B6/), D4-Evidenz) und Berichten.

| Nr. | Kriterium | Bewertung | Evidenz |
| --- | --- | --- | --- |
| K1 | Status eindeutig bezeichnet | PASS | keine doppelten Bezeichnungen innerhalb der fünf Statusarten in DE und EN; Oberfläche mit Form + Text (EV-009, axe ohne Befund) |
| K2 | Quelle erkennbar | PARTIAL | Primärquelle in 32 von 32 Anforderungsdetails und im Bericht für anwendbare und ungeklärte RR; für nicht anwendbare RR nicht im Bericht (F-4) |
| K3 | Begründung erreichbar | PASS | Anwendbarkeits- und Gap-Begründung je RR; Herleitung T2/T3 in 11 von 11 PASS; Decision Trace in der Oberfläche (Screenshot B6/05) |
| K4 | Gap und Anwendbarkeit getrennt | PARTIAL | getrennte Felder und Kennzeichen in Oberfläche, API und Bericht; bei ungeklärten bzw. nicht anwendbaren RR tragen beide Kennzeichen denselben Wortlaut („Anwendbarkeit ungeklärt“), was redundant wirkt (Befund F-6) |
| K5 | Ungeklärt klar erkennbar | PASS | eigener Status, eigene Form und Farbe, Kennzahl 289 in Einordnung und Gap-Übersicht, Hinweistext |
| K6 | Nachweisstatus nicht mit Erfüllung verwechselt | PASS | Nachweisbezeichnungen ohne Überschneidung mit den Gap-Bezeichnungen; „erfüllt“ ohne Nachweis ergibt in 7 von 7 Fällen „Nachweisprüfung erforderlich“ |
| K7 | Lebenszyklus sichtbar | PASS | Lebenszyklusband im Detail (Screenshot B6/04), Phasen je RR im Bericht; T8 11 von 11 |
| K8 | Web und PDF widerspruchsfrei | PASS | Abschnitt 7 |
| K9 | DE und EN semantisch konsistent | PASS | Abschnitt 7 |

## 7. DE/EN und Web/PDF

- **DE/EN:** Alle 14 Berichtsabschnitte tragen in beiden Sprachen identische sprachneutrale Werte (RR-, RUL- und Quellenkennungen samt Lokatoren, Status-Tonalitäten, numerische Tabellenwerte, Verteilungen, Verlauf); dieselben 959 RR-Kennungen; gleiche Kennungen im Berichtskopf. Die Anforderungsliste der API ist sprachneutral. Die Inhaltshashes unterscheiden sich je Sprache erwartungsgemäß (sprachabhängiger Inhalt).
- **Web/PDF:** Inhaltshash von Web-Berichtsdokument, HTML und PDF je Sprache identisch. Von 33 107 Textbestandteilen des Web-Berichtsdokuments (ohne Erzeugungszeitstempel) sind je Sprache 33 107 im PDF-Text (100 %) und 33 106 im sichtbaren HTML-Text enthalten; der eine Text ist die Beschriftung des Bewertungsverlaufs, die das HTML als zugänglichen Namen (`aria-label`) statt als sichtbaren Text führt (F-7). Damit stimmen Bewertungskennung, Revision, Versionen, Summen, Status je RR, offene Punkte, Quellen, Lebenszyklus und Nachweise überein.
- **Browser-Durchlauf (Oberfläche):** Die Fallstudie wurde zusätzlich vollständig über die Oberfläche erfasst (Profil adaptiv, 22 Erfüllungsangaben, 8 Nachweisreferenzen, davon 3 mit vorgesehener Maßnahme). Ergebnis: 956 von 956 vergleichbaren RR mit identischen Werten zum API-Lauf und identische Summen. Die drei Erfüllungsangaben an nicht anwendbaren bzw. ungeklärten RR (C1–C3) sind in der Oberfläche bewusst nicht erfassbar und wurden nur über die API gesetzt ([results/R2/browser_case_study.json](results/R2/browser_case_study.json)).

## 8. Leistung (ergänzend)

| Operation (R2, je 10 Messungen) | Median | Minimum | Maximum |
| --- | --- | --- | --- |
| Bewertung mit vollständigem Fallprofil anlegen (API) | 0,350 s | 0,330 s | 0,357 s |
| Anforderungsliste, 959 RR (API) | 0,110 s | 0,109 s | 0,129 s |
| Anforderungsdetail (API) | 0,111 s | 0,110 s | 0,121 s |
| ReportModel und Berichtsdokument DE (API) | 0,194 s | 0,184 s | 0,202 s |
| HTML-Bericht DE | 0,184 s | 0,182 s | 0,195 s |
| PDF-Bericht DE | 2,442 s | 2,403 s | 2,479 s |
| Explorer laden bis 959 Zeilen (Browser) | 0,798 s | 0,789 s | 0,805 s |
| Suche im Explorer (Browser) | 0,038 s | 0,027 s | 0,044 s |

Umgebung: Apple M4 Max, macOS 27.0, Python 3.13.15, Google Chrome 153, lokal ohne Netzwerk. Die Werte gelten nur für diese Umgebung und diesen Fall; eine Skalierbarkeitsaussage wird nicht abgeleitet.

## 9. UI- und Barrierefreiheitsevidenz

Übernommen aus D4 (nicht als Nutzerstudie): axe-core ohne Verstöße in allen Ansichten und fünf Konfigurationen, Responsive-Matrix 360–1440 px ohne horizontalen Überlauf, 200 % Zoom, Tastaturbedienung, Hell/Dunkel/hoher Kontrast, DE/EN ([EV-009](../09-evidence/EV-009_AUTOMATED_TEST_RUN_D4_WEB.md), [EV-010](../09-evidence/EV-010_DESIGN_EVIDENCE_D4.md)). Für die Fallstudie neu: sieben Screenshots in [screenshots/B6/](../09-evidence/screenshots/B6/) (Fallprofil, Anwendbarkeit, Gap-Übersicht, konkrete Gap-RR, Decision Trace, Nachweise, Ergebnisbericht).

## 10. Abweichungs- und Befundanalyse

Zwischen Referenz und System trat in keinem Lauf eine Abweichung bei Anwendbarkeit, Begründungscode oder Gap-Status auf. Die folgenden Befunde betreffen Reproduzierbarkeit, Nachvollziehbarkeit, Darstellung und das Evaluationswerkzeug:

| Befund | Klasse | Beschreibung | Root Cause | Behandlung |
| --- | --- | --- | --- | --- |
| F-1 | Other (Kennungsdesign) | Roh-Fingerprint je API-Lauf verschieden | Fingerprint umfasst die Nachweiskennungen; die API vergibt sie zufällig (UUIDv4). Dokumentiert ist nur der Ausschluss von Bewertungskennung und Zeitpunkten | nicht geändert (Änderung der Fingerprint-Semantik würde gespeicherte Bewertungen berühren); Vergleich ohne Kennungen nach Methode; Nachweis mit festen Kennungen 20/20; Empfehlung: kennungsneutraler Vergleichswert |
| F-2 | Presentation Error | Nachweisregister im Bericht nach Zufallskennung sortiert; Berichtsdokument bei gleichen Eingaben verschieden (R1 0/20) | Reihenfolge aus dem nach Kennung sortierten Register übernommen | korrigiert in `6c4610a` (Reihenfolge nach Inhalt), Regressionstest in TC-054; R2 20/20 |
| F-3 | Presentation Error | gespeicherte, derzeit wirkungslose Bewertung mit Nachweisen in der Detailansicht nicht sichtbar | Detail zeigte für nicht anwendbare RR nur den Hinweis auf fehlende Bewertbarkeit | korrigiert in `219134c` (Hinweis mit Status und Anzahl der Nachweise), Browser-Test ergänzt |
| F-4 | Presentation (Designentscheidung) | Bericht nennt für nicht anwendbare RR keine Quellen (T6 FAIL, K2 PARTIAL) | D3-Berichtsaufbau: nicht anwendbare RR kompakt mit Begründung | nicht geändert; als Grenze dokumentiert; Quelle in Oberfläche und API vorhanden |
| F-5 | Test Fixture Error | Werkzeug verglich DE/EN über Freitextzahlen, erwartete Leertexte gefüllter Tabellen, zählte Erzeugungszeitstempel; T11 prüfte bei nicht anwendbaren RR die Ergebnisnachweise statt der gespeicherten Zuordnung | Operationalisierung im Werkzeug gröber bzw. abweichend von der vorab festgelegten Methode und der Semantik `NOT_CONSIDERED` | Werkzeug vor R2 an die Methode angeglichen; Kriterien unverändert; R1-Werte erhalten |
| F-6 | Presentation | gleicher Wortlaut von Anwendbarkeits- und Gap-Kennzeichen bei ungeklärten bzw. nicht anwendbaren RR (K4 PARTIAL) | Gap-Ergebnis spiegelt die Anwendbarkeit mit derselben Bezeichnung | nicht geändert; Empfehlung: Gap-Kennzeichen bei inaktiven RR entfallen lassen oder als „nicht bewertbar“ bezeichnen |
| F-7 | Presentation (gering) | Beschriftung des Bewertungsverlaufs im HTML nur als `aria-label` | Gestaltung des HTML-Renderers | nicht geändert; kein Widerspruch zu PDF/Web |

Softwarekorrekturen erfolgten nach dem Befund in separaten Commits mit Tests; die Ergebnisse vor der Korrektur (R1) sind unverändert erhalten.

## 11. Nachvollziehbarkeitskette der Evaluation

Fallstudie ([CASE_STUDY.md](CASE_STUDY.md)) → Produktprofil (TC-036 `golden_case`, EV-003) → Referenz (REFERENCE_ASSESSMENT.yaml, EV-011) → `RUL`-Pfade RUL-001 und RUL-027 → 959 `RR` mit Anwendbarkeit → Bewertung über die Anwendungs-API (R1/R2) → Bericht (Inhaltshash, PDF in [../09-evidence/evaluation/](../09-evidence/evaluation/)) → EV-012 bis EV-016 → Metriken (results/R*/metrics.json) → TC-061 als Regressionstest.

## 12. Limitationen

- Einzelnes Hauptfallbeispiel; keine Aussage über andere Produktarten.
- Manuelle Referenz durch den Projektbearbeiter; kein unabhängiger Goldstandard; Referenzableitung nach derselben dokumentierten Methodik (Konformitäts-, keine Rechtsrichtigkeitsprüfung); dem Bearbeiter waren Gesamtzahlen des Referenzprofils aus der Entwicklung bekannt.
- Kein Expertenreview (Formular in EVALUATION_METHOD.md Anhang A vorbereitet, nicht ausgefüllt); keine Nutzerstudie; Verständlichkeit nur als kriteriengestützte Artefaktprüfung.
- Browser-Tests nur mit Google Chrome; kein Test mit Screenreadern.
- 502 von 959 Maßnahmenzuordnungen (im Fall 284 anwendbare RR) im evaluierten Katalog `RR_MEASURE` 0.1 `REVIEW_REQUIRED`. Die Post-Evaluation-Fassung 0.2 ordnet alle 959 `RR` zu; die Ergebnisse dieser Evaluation gelten weiterhin für 0.1 und werden nicht neu berechnet ([RR_MEASURE_METHOD.md](../03-regulatory/RR_MEASURE_METHOD.md) Abschnitt 7).
- Definierter regulatorischer Umfang der Kataloge; zeitliche Gültigkeit der Katalogfassungen; hypothetisches Bewertungsdatum 01.09.2028.
- Quellenstand: Normen über DIN-EN-Arbeitsfassungen; `SRC-005`-Berichtigung nicht geprüft (`OPEN_SOURCE_PACKAGE_CHECK`); `SRC-003` in der Fassung Juni 2025, Prüfung auf eine neuere Fassung nicht durchgeführt ([SOURCES.md](../03-regulatory/SOURCES.md) „Offene Verifikationspunkte“).
- Einzelplatz-Demonstrator ohne Mehrbenutzer- und Netzbetrieb.
- Kleiner Gap-Referenz-Umfang (32 RR); Anteile sind beschreibend, nicht inferenzstatistisch.

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Ergebnisse der Evaluation Revisionen R1 (vor Korrektur) und R2 (nach Korrektur der Befunde F-2 und F-3 und Angleichung des Werkzeugs F-5). |
| 1.1 | Redaktionell, ohne Änderung an Ergebnissen, Kennzahlen oder Bewertungen: Werkzeugstand von R2 (Commit `8b0ec2f`) benannt; „konform“ in Abschnitt 2.1 durch „übereinstimmend“ ersetzt, um eine Verwechslung mit regulatorischer Konformität auszuschließen; Quellenstand als Limitation ergänzt. |
| 1.2 | Limitation zur Maßnahmenzuordnung um die Post-Evaluation-Fassung `RR_MEASURE` 0.2 ergänzt; Bindung der Ergebnisse an 0.1 ausdrücklich vermerkt. Keine Änderung an Ergebnissen. |
