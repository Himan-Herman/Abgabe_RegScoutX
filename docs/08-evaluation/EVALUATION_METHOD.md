# Evaluationsmethode (Block 6)

Version 1.0 · Status: eingefroren (Phase A, vor dem Evaluationslauf) · Stand: 28.09.2026

Dieses Dokument legt **vor** dem Evaluationslauf fest, was gemessen wird, woran es gemessen wird und wie Abweichungen behandelt werden. Grundlage sind die Bewertungskriterien des Exposés ([EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 3: Korrektheit, Vollständigkeit, Reproduzierbarkeit, Nachvollziehbarkeit; ergänzend Verständlichkeit und Konsistenz). Der Demonstrator ist Prüfmittel der entwickelten Methodik, nicht Gegenstand einer Produktbewertung. Die Fallstudie steht in [CASE_STUDY.md](CASE_STUDY.md), die Referenz in [REFERENCE_ASSESSMENT.yaml](REFERENCE_ASSESSMENT.yaml).

---

## 1. Evaluation Freeze

| Merkmal | Stand |
| --- | --- |
| Evaluierter Softwarestand | Commit `ee76ef8` (main = origin/main, Arbeitsbaum sauber); der Referenz-Freeze-Commit ändert ausschließlich Dokumentation und Prüfwerkzeuge unter `tools/`, nicht `regscoutx/` oder `web/` |
| Katalogstände (`CatalogVersionSet`) | SOURCES 1.6 · RR_CATALOG 0.26 · RUL_CATALOG 0.2 · DATA_MODEL 0.8 · RR_APPLICABILITY 0.4 · RR_MEASURE 0.1 |
| weitere Stände | SR_CATALOG 0.6 · TC_CATALOG 0.6 · Berichtsschema 1.0 (`REPORT_SCHEMA_VERSION`) · Persistenzformat `regscoutx.assessment` 1.0 · Web-Oberfläche 0.4.0 |
| Golden Cases | TC-036 bis TC-039 unverändert seit ihrer Adjudikation (Commit `16e08a1`, geprüft durch Vergleich der `golden_case`-Inhalte) |
| Gate vor dem Freeze | alle Validatoren PASS; `tools/` 129 und `tests/` 202 Tests OK; Frontend-Build ohne Warnung, Vitest 32 OK, Playwright 30 OK (3 bewusst übersprungene Screenshot-Tests) |
| Zeitpunkt (Metadatum) | 2026-09-28T21:34Z |
| Umgebung | macOS 27.0, Apple M4 Max, 128 GB RAM; Python 3.13.15; Node.js 22.21.0; Google Chrome 153.0.8010.53; lokaler Einzelplatzbetrieb ohne Netzwerkzugriff nach außen |

**Freeze-Regel:** Nach dem Freeze fließen keine fachlichen Änderungen in denselben Evaluationslauf ein. Wird während der Evaluation ein Fehler gefunden, wird er als Befund dokumentiert, das Ergebnis vor der Korrektur bleibt erhalten, eine Korrektur wird separat committet und als neue **Evaluation Revision** (R2, R3 …) mit eigenem Lauf ausgewiesen. Referenzfehler werden als **Reference Correction** mit Begründung dokumentiert, nie still korrigiert.

## 2. Referenzbewertung

**Zeitliche Reihenfolge:** Referenz und Methode werden in Phase A erstellt, validiert, mit SHA-256 festgehalten ([EV-011](../09-evidence/EV-011_CASE_STUDY_REFERENCE_FREEZE.md)) und committet. Erst danach wird der Demonstrator für die Fallstudie ausgeführt (Phase B).

**Aufbau der Referenz:**

1. **Manuell adjudizierte Schicht (EV-003):** Profil, Regelpfade, Entscheidungsergebnisse, Zustand aller 16 Anwendbarkeitsbereiche, 22 entscheidungskritische RR und die Summen scope-bedingt nicht anwendbarer (70) bzw. ungeklärter (0) RR von TC-036.
2. **Regelbasierte Referenzableitung für alle 959 RR:** `tools/derive_case_reference.py` wendet die dokumentierte Auswertungssemantik ([RR_APPLICABILITY_MAPPING.md](../03-regulatory/RR_APPLICABILITY_MAPPING.md), [ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md) Abschnitt 8, `RequirementResult` in [DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml)) auf die adjudizierten Blockzustände und das eingefrorene Profil an. Das Werkzeug ist eine eigenständige zweite Umsetzung der dokumentierten Regeln; es importiert keinen Code aus `regscoutx/` und liest keine Laufzeitartefakte. Vor dem Schreiben prüft es die eigene Ableitung gegen die manuell adjudizierte Schicht (Blockzustände, 22 RR, Scope-Summen) und bricht bei Abweichung ab.
3. **Referenzauslegungen RI-1 bis RI-5:** Wo die Dokumentation eine Reihenfolge nicht ausdrücklich regelt (Vorrang einer nicht erfüllten modellierten gegenüber einer nicht modellierten Bedingung, Begründungscode bei gleichzeitig fehlender Eingabe, Nachweisstatus), ist die Auslegung vorab im Referenzartefakt festgehalten.

**Unabhängigkeit und Befangenheit (offen benannt):** Referenz und Demonstrator stammen vom selben Projektbearbeiter; es gibt keinen unabhängigen Goldstandard. Die Referenzableitung setzt dieselben dokumentierten Regeln ein, die auch der Demonstrator umsetzt. Die Übereinstimmung misst daher die **Konformität der Umsetzung mit der dokumentierten, adjudizierten Methodik**; die fachliche Richtigkeit der Zuordnung selbst gegenüber dem Rechtstext beruht auf den Adjudikationen der Blöcke 1 bis 3 und wird hier nicht erneut geprüft. Dem Bearbeiter waren aus der Entwicklung (D4) die Gesamtzahlen des Referenzprofils in der Oberfläche bekannt; die Referenz wurde ausschließlich über die dokumentierten Regeln abgeleitet und nicht an solche Zahlen angepasst.

**Referenzinhalt je RR:** Status (`APPLICABLE`, `NOT_APPLICABLE`, `APPLICABILITY_UNRESOLVED`), Begründungscode, angewandte Referenzregel (RB-0 bis RB-9) und Bereich; für den Gap-Referenz-Umfang zusätzlich erwarteter Gap-Status, Gap-Begründung, Gap-Kennzeichen, Bewertungszustand, Nachweisstatus, Maßnahmenstatus und Maßnahmen, Primär- und Ergänzungsquellen, Lebenszyklusphasen.

## 3. Gap-Referenz-Umfang und Szenario

Die Auswahl ist deterministisch, verwendet ausschließlich Referenz und Kataloge und ist vor dem Systemlauf festgelegt (Umsetzung in `tools/derive_case_reference.py`):

| Menge | Regel (je Themencluster in Vokabularreihenfolge, RR aufsteigend nach Kennung, nur Referenz-`APPLICABLE`) |
| --- | --- |
| A1 | erste reguläre RR mit zugeordneter Maßnahme (`MAPPED`) |
| A2 | erste bedingte RR mit zugeordneter Maßnahme |
| A3 | erste RR mit offener Maßnahmenzuordnung (`REVIEW_REQUIRED`) |
| A4 | erste weitere RR einer im Themencluster noch nicht vertretenen Quellenfamilie (MDR, AI Act, Normen) |
| B | erste weitere anwendbare RR (ohne Erfüllungsangabe) |
| D | nach A und B: je Quelle SRC-001, SRC-002, SRC-005, SRC-006, SRC-007, SRC-008, die im Umfang noch nicht als Primärquelle vertreten ist, die erste anwendbare RR (unabhängig vom Themencluster) |
| C1 | erste RR mit Referenz `CONDITIONALITY_NOT_DOCUMENTED` (ungeklärt), mit Erfüllungsangabe |
| C2 | erste RR mit Referenz `LOCAL_CONDITION_NOT_MODELLED` (ungeklärt), mit Erfüllungsangabe |
| C3 | erste scope-inaktive RR mit zugeordneter Maßnahme (nicht anwendbar), mit Erfüllungsangabe |

Ergebnis: 32 RR (20 aus A, 7 aus B, 2 aus D, 3 aus C) über alle acht Themencluster, die Primärquellen MDR (SRC-001), AI Act (SRC-002), ISO 13485 (SRC-005), ISO 14971 (SRC-006), IEC 62304 (SRC-007), IEC 62366-1 (SRC-008) sowie die eIFU-Verordnung (SRC-009, C3), reguläre und bedingte RR und beide Maßnahmenstatus. Nicht jede Menge ist in jedem Themencluster besetzbar (z. B. keine reguläre RR mit zugeordneter Maßnahme in „Data Governance“); das ist Folge des Katalogs, nicht einer Auswahl.

**Szenario:** Die Mengen A und D erhalten (in dieser Reihenfolge) Erfüllungsangaben im festen Zyklus erfüllt mit Nachweis → teilweise erfüllt mit Nachweis → nicht erfüllt → erfüllt ohne Nachweis → nicht bewertet → teilweise erfüllt ohne Nachweis; C1 erfüllt mit Nachweis, C2 nicht erfüllt, C3 teilweise erfüllt mit Nachweis. Begründungen sind ein fester Hinweistext; Nachweisreferenzen tragen die erste vorgesehene Maßnahme der RR, sofern zugeordnet. Erwartete Gap-Ergebnisse folgen der dokumentierten Ableitungstabelle (ARCHITECTURE.md Abschnitt 8).

## 4. Systemlauf

Der Fall wird über den realen Anwendungspfad ausgeführt: lokaler Server (`regscoutx/web_server.py`) und Anwendungs-API per HTTP mit denselben Anfragen wie die Oberfläche. Ablauf: Bewertung anlegen; Profil **adaptiv** erfassen (immer die jeweils nächste offene Frage des Fragebogens beantworten, solange das Fallprofil dafür einen Wert enthält); Erfüllungsangaben setzen; Nachweisreferenzen anlegen und zuordnen; Anforderungen, Anforderungsdetails, Matrix, Revisionen und Audit lesen; Berichtsdokument DE/EN, HTML und PDF DE/EN erzeugen. Ergänzend wird die Fallstudie im Browser (Playwright, Chrome) über die Oberfläche erfasst; das dort entstehende fachliche Ergebnis (Fingerprint) muss dem API-Lauf entsprechen. Laufwerkzeuge liegen unter `evaluation/`, Ergebnisse unter `docs/08-evaluation/results/`.

## 5. Metriken

### 5.1 Korrektheit

- **Applicability Agreement (alle 959 RR):** Anzahl und Anteil identischer Status System vs. Referenz; Konfusionsmatrix 3 × 3; Abweichungen nach Referenz- und Systemstatus. Sekundär: Übereinstimmung der Begründungscodes.
- **Menge `APPLICABLE`:** TP = beide `APPLICABLE`; FP = System `APPLICABLE`, Referenz nicht; FN = Referenz `APPLICABLE`, System nicht. Precision = TP/(TP+FP), Recall = TP/(TP+FN), jeweils nur berichtet, wenn der Nenner > 0 ist. `APPLICABILITY_UNRESOLVED` wird nicht als negativ gezählt, sondern in der Konfusionsmatrix als eigene Kategorie ausgewiesen (FP/FN gegenüber `UNRESOLVED` getrennt benannt).
- **Gap Agreement (32 RR des Gap-Referenz-Umfangs):** Anzahl und Anteil identischer Gap-Status; Abweichungen je Gap-Kategorie. Sekundär: Gap-Begründung, Gap-Kennzeichen, Bewertungszustand, Nachweisstatus. Wegen der kleinen Menge werden nur absolute Zahlen und Anteile berichtet, keine Inferenzstatistik.

### 5.2 Vollständigkeit (innerhalb des definierten Untersuchungsumfangs)

- **Requirement Completeness:** Anteil der Referenz-`APPLICABLE`-RR, die das System als `APPLICABLE` ausweist (= Recall).
- **Gap Completeness:** Anteil der 32 RR, für die das System einen vollständigen Datensatz ausgibt: RR-Kennung, Anwendbarkeit, Gap-Status, Primärquelle (= Katalog), Lebenszyklusphasen (= Katalog), Maßnahmenstatus und Maßnahmen (= RR_MEASURE) sowie eine Herleitung (ausgewertete Bedingungen oder herangezogene Entscheidungen). Ein Datensatz ist vollständig, wenn alle sieben Bestandteile vorhanden und gleich der Referenz bzw. dem Katalog sind.

Es wird keine Abdeckung der gesamten MDR, des gesamten AI Act oder der Normen behauptet.

### 5.3 Reproduzierbarkeit

20 vollständige Wiederholungen mit identischem Profil, identischen Erfüllungsangaben und Nachweisreferenzen, identischem `CatalogVersionSet` und Referenz-Commit, jeweils als neue Bewertung über den adaptiven HTTP-Pfad. Verglichen werden fachlicher Fingerprint, Anwendbarkeit je RR, Gap-Status je RR, Entscheidungen mit Regelpfaden, Summen und Inhaltshash des Berichtsdokuments (DE und EN) sowie der HTML- und PDF-Artefakte. Nicht verglichen werden Zeitstempel, Bewertungskennungen und vom Server vergebene Nachweiskennungen. Ergebnis: N/N identische fachliche Ergebnisse.

### 5.4 Nachvollziehbarkeit

Stichprobe (vorab festgelegt, `traceability_sample`): je Themencluster die erste RR aus Menge A sowie C1 bis C3 (11 RR). Für jede RR werden aus Anforderungsdetail (Anwendungs-API, dieselbe Quelle wie die Oberfläche) und HTML-Bericht folgende Kriterien geprüft:

| Nr. | Kriterium | PASS | NOT_APPLICABLE |
| --- | --- | --- | --- |
| T1 | Nutzereingabe | jede Profileingabe der lokalen Bedingungen der RR ist mit Wert ausgewiesen; bei rein entscheidungsbasierter Anwendbarkeit sind die herangezogenen Entscheidungen mit ihren Regelpfaden ausgewiesen | — |
| T2 | Prädikat/Bedingung | alle Bereichs- und lokalen Prädikate der Zuordnung sind mit dem Referenzwert ausgewiesen | RR ohne Zuordnung |
| T3 | RUL/Entscheidung | jede entscheidungsbasierte Bedingung ist mit Entscheidungsbereich, Status und mindestens einer RUL ausgewiesen | keine entscheidungsbasierte Bedingung |
| T4 | Anwendbarkeitsstatus | Status und Begründung gleich der Referenz | — |
| T5 | RR | Kennung und Titel ausgewiesen | — |
| T6 | Primärquelle | Primärquellen gleich dem Katalog, im Bericht zur RR enthalten | — |
| T7 | Ergänzende Quelle | Ergänzungsquellen gleich dem Katalog | keine Ergänzungsquelle im Katalog |
| T8 | Lebenszyklus | Phasen gleich dem Katalog | — |
| T9 | Gap-Status | gleich der Referenz | — |
| T10 | Maßnahmenzuordnung | Status und Maßnahmen gleich RR_MEASURE | — |
| T11 | Nachweisstatus | gleich der Referenz; zugeordnete Referenzen ausgewiesen | — |

Sonst FAIL. Keine Punktwerte.

### 5.5 Verständlichkeit und Konsistenz (kriteriengestützte Artefaktprüfung)

Keine Nutzerstudie. Geprüft werden Artefakte (Oberfläche über Screenshots und Accessibility-Baum, HTML- und PDF-Bericht, Sprachressourcen) gegen vorab festgelegte Kriterien; Bewertung PASS / PARTIAL / FAIL mit kurzer Evidenz:

| Nr. | Kriterium | Prüfweg |
| --- | --- | --- |
| K1 | Status eindeutig bezeichnet | Bezeichnungen je Statusart (Anwendbarkeit, Gap, Bewertungszustand, Nachweis, Maßnahme) in DE und EN paarweise verschieden; in der Oberfläche Form + Text |
| K2 | Quelle erkennbar | Primärquelle im Anforderungsdetail und je RR im Bericht |
| K3 | Begründung erreichbar | Anwendbarkeits- und Gap-Begründung im Detail, Herleitung im Decision Trace und im Bericht |
| K4 | Gap und Anwendbarkeit getrennt | getrennte Kennzeichen und Felder in Oberfläche und Bericht |
| K5 | Ungeklärt klar erkennbar | eigener Status, eigene Form/Farbe, Kennzahl und Hinweis |
| K6 | Nachweisstatus nicht mit Erfüllung verwechselt | Bezeichnungen „Nachweisreferenz vorhanden“ vs. „erfüllt (Nutzerangabe mit Nachweisreferenz)“; erfüllt ohne Nachweis ergibt Nachweisprüfung erforderlich |
| K7 | Lebenszyklus sichtbar | Lebenszyklusband im Detail, Phasen im Bericht |
| K8 | Web und PDF widerspruchsfrei | Abschnitt 6 |
| K9 | DE und EN semantisch konsistent | Abschnitt 6 |

Es ist **kein unabhängiges fachliches Review** vorgesehen oder durchgeführt. Ein Formular für ein späteres Review steht in Anhang A; es enthält keine Ergebnisse.

## 6. DE/EN- und Web/PDF-Konsistenz

- **DE/EN:** Berichtsdokument und Artefakte in beiden Sprachen aus derselben Revision. Verglichen werden fachliche Werte (RR-Kennungen, Zahlen, Codes der Anwendbarkeit, Gap- und Maßnahmenstatus, Quellenlokatoren); sprachlich dürfen Texte variieren. Die Anforderungsliste der API ist sprachneutral.
- **Web/PDF:** Die Web-Berichtsansicht rendert das Berichtsdokument der API; verglichen werden Berichtsdokument (Web), HTML und PDF auf Bewertungskennung, Revision, Katalogversionen, Summen, Status je RR, zentrale offene Punkte, Quellen, Lebenszyklus und Nachweise sowie auf den Inhaltshash. Für das PDF wird der Text aus den Inhaltsströmen über die eingebetteten ToUnicode-Tabellen gelesen (ohne zusätzliche Abhängigkeit); Pixelgleichheit wird nicht erwartet.

## 7. Leistung (ergänzend)

Je Operation zehn Messungen, berichtet wird der Median (zusätzlich Minimum und Maximum): Bewertung mit vollständigem Fallprofil anlegen, Anforderungsliste, Anforderungsdetail, Berichtsdokument (ReportModel und Dokument), HTML, PDF (je DE); Suche im Explorer im Browser. Keine Verallgemeinerung auf andere Rechner oder Lastsituationen.

## 8. Abweichungsanalyse

Jede Abweichung wird einer Klasse zugeordnet: Reference Error, Rule Implementation Error, Applicability Error, Gap Logic Error, Data Mapping Error, Presentation Error, Versioning Error, Test Fixture Error, Other; mit Root Cause und Behandlung. Sollwerte werden nicht geändert; Softwarekorrekturen erfolgen separat mit ergänzendem Test und neuer Evaluation Revision; das Ergebnis vor der Korrektur bleibt erhalten.

## 9. Grenzen der Methode

Ein Hauptfall; Referenz durch den Projektbearbeiter, kein unabhängiger Goldstandard und kein Expertenreview; Referenzableitung nach denselben dokumentierten Regeln (Konformitäts-, nicht Rechtsrichtigkeitsprüfung); keine Nutzerstudie; Browser-Tests nur mit Chrome; kein Screenreader-Test; 502 Maßnahmenzuordnungen weiterhin `REVIEW_REQUIRED`; definierter regulatorischer Umfang der Kataloge; zeitliche Gültigkeit der Katalogfassungen; Einzelplatz-Demonstrator.

## Anhang A – Formular für ein fachliches Review (nicht ausgefüllt)

| Nr. | Prüffrage | Bewertung (PASS / PARTIAL / FAIL) | Begründung | Prüfende Person, Datum |
| --- | --- | --- | --- | --- |
| R1 | Ist die Einordnung der Fallstudie (Qualifikation, Klasse, AI-Act-Status) aus den Annahmen nachvollziehbar? | | | |
| R2 | Sind die als anwendbar ausgewiesenen Anforderungen für den Fall fachlich plausibel (Stichprobe)? | | | |
| R3 | Sind ungeklärte Anforderungen zutreffend als offen gekennzeichnet? | | | |
| R4 | Ist die Herleitung je Anforderung für eine Fachperson verständlich? | | | |
| R5 | Sind Gap-Status und Nachweisstatus unmissverständlich getrennt? | | | |
| R6 | Ist der Bericht als Arbeitsgrundlage für eine Gap-Analyse geeignet? | | | |

## Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung vor dem Evaluationslauf (Phase A): Freeze, Referenzaufbau, Gap-Referenz-Umfang, Metriken, Kriterien, Konsistenzprüfung, Leistung, Abweichungsanalyse, Grenzen, Review-Formular. |
