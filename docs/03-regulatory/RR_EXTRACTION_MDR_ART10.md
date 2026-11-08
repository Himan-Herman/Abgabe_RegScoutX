# Systematische RR-Extraktion — SRC-001 Art. 10

Version 1.1 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Art.10/Abs.2` · `SRC-001#Art.10/Abs.9` — Einleitung sowie Buchst. c, d, e, l, m · `SRC-001#Art.10/Abs.9/Buchst.g` · `SRC-001#Art.10/Abs.9/Buchst.i` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.16 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` (alle vier Bereiche) |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung der freigegebenen Bereiche von `SRC-001` Art. 10. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M10-A` bis `M10-AA` sind ausschließlich temporäre Evidenzkennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Finale MDR-Gap-`RR`-Kandidaten | **27** — `M10-A` bis `M10-Z` sowie `M10-AA` |
| davon regulär | 5 |
| davon conditional | 22 |
| Unresolved | 0 |
| Deferred | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Out-of-Scope-Atome | 0 |
| Operative aktive Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 27 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Finale ID-Ordnung

Die Evidenz verwendet ausschließlich folgende finale Reihenfolge ohne Lücken:

`M10-A` · `M10-B` · `M10-C` · `M10-D` · `M10-E` · `M10-F` · `M10-G` · `M10-H` · `M10-I` · `M10-J` · `M10-K` · `M10-L` · `M10-M` · `M10-N` · `M10-O` · `M10-P` · `M10-Q` · `M10-R` · `M10-S` · `M10-T` · `M10-U` · `M10-V` · `M10-W` · `M10-X` · `M10-Y` · `M10-Z` · `M10-AA`

Im Zuge der Nachadjudikation verworfene Kandidatenzuschnitte werden **nicht** zusätzlich als aktive Kandidaten geführt.

---

## 4. Nachadjudikation und temporäres Mapping

Der ursprüngliche Research-Stand umfasste **31** Gap-`RR`-Kandidaten sowie **1** separates Out-of-Scope-Atom (`production` aus `SRC-001#Art.10/Abs.9/Buchst.g`). Nach gezielter Nachadjudikation ergibt sich der finale Stand von **27** Gap-`RR`-Kandidaten und **0** Out-of-Scope-Atomen (Abschnitt 2).

**Rechnerische Überleitung:**

| Schritt | Gap-`RR`-Kandidaten | Out-of-Scope-Atome |
| --- | --- | --- |
| Ursprünglicher Research-Stand | 31 | 1 (`production`) |
| A. Ursprüngliche M10-M + M10-N → 1 `RR` | −1 | ±0 |
| B. Buchst. g: 4 Gap-`RR`-Kandidaten → 1 gemeinsame Produktrealisierungs-`RR` | −3 | ±0 |
| B. Buchst. g: bisher separater Produktionsanteil wird Bestandteil dieser gemeinsamen `RR` | ±0 | −1 |
| **Finaler Stand** | **31 − 1 − 3 = 27** | **1 → 0** |

### A. Zusammenführung zu final M10-M

Die ursprünglichen Kandidaten M10-M und M10-N wurden zu final `M10-M` zusammengeführt.

`in the most effective manner` und die Proportionalität nach Risikoklasse und Produktart sind kumulative Qualitätsmerkmale derselben QMS-Compliance-Funktion.

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | erfüllt |
| Split-Bedingung 2 | nicht erfüllt |

### B. Buchst. g als gemeinsame RR zur Produktrealisierung

Im ursprünglichen Research-Stand war `SRC-001#Art.10/Abs.9/Buchst.g` in **vier** Gap-`RR`-Kandidaten (planning, design, development, service provision) sowie **zusätzlich** ein separates Out-of-Scope-Atom `production` aufgeteilt. Diese Aufteilung wurde verworfen. Die vier Gap-`RR`-Kandidaten werden zu **einer** gemeinsamen `RR` zur Produktrealisierung (`M10-S`) zusammengeführt (4 → 1); der bisher separat geführte Produktionsanteil wird Bestandteil dieser gemeinsamen `RR` (Out-of-Scope 1 → 0).

`including` konkretisiert den zwingenden Umfang des einheitlichen QMS-Prozessbereichs Produktrealisierung.

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | erfüllt |
| Split-Bedingung 2 | nicht erfüllt |

Der Produktionsbestandteil wird deshalb **nicht** separat Out-of-Scope gestellt.

### C. Theme M10-F

| Merkmal | Angabe |
| --- | --- |
| Ursprüngliches Theme | Software-Lebenszyklus |
| Finales Theme | Qualitäts- und Risikomanagement |
| Grund | übergreifende regulatorische Change-Control- bzw. Compliance-Pflicht |

### D. Lifecycle M10-C und M10-D

`Planung und Konzeption` wurde nach Prüfung des normativen Verweises auf Anhang I Nr. 3 zusätzlich als Lebenszyklusphase aufgenommen.

### E. Anhang I Nr. 3 als Supplementary-Locator für M10-A bis M10-D

`SRC-001#Anh.I/Nr.3` wird für `M10-A` bis `M10-D` als notwendiger Supplementary-Locator geführt. Dies ist **keine** vorgezogene systematische Extraktion von Anhang I Nr. 3.

---

## 5. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Kandidaten |
| --- | --- | --- |
| `SRC-001#Art.10/Abs.2` | 4 `RR` | `M10-A` bis `M10-D` |
| `SRC-001#Art.10/Abs.9/UAbs.1/Satz.1` | 1 `RR` | `M10-E` |
| `SRC-001#Art.10/Abs.9/UAbs.1/Satz.2` | 1 conditional `RR` | `M10-F` |
| `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` | 7 conditional `RR` — davon 6 QMS-Handlungs-`RR` und 1 gemeinsame wirksame/proportionale Compliance-`RR` | `M10-G` bis `M10-M` |
| `SRC-001#Art.10/Abs.9/UAbs.2/Satz.1` | 1 conditional `RR` | `M10-N` |
| `SRC-001#Art.10/Abs.9/UAbs.2/Satz.2` | 1 conditional `RR` | `M10-O` |
| `SRC-001#Art.10/Abs.9/UAbs.3` | 0 eigene `RR` | einleitender Kontext für Buchst. a–m; Supplementary-Kontext für `M10-P` bis `M10-AA` |
| `SRC-001#Art.10/Abs.9/Buchst.c` | 1 conditional `RR` | `M10-P` |
| `SRC-001#Art.10/Abs.9/Buchst.d` | 1 conditional `RR` | `M10-Q` |
| `SRC-001#Art.10/Abs.9/Buchst.e` | 1 conditional `RR` | `M10-R` |
| `SRC-001#Art.10/Abs.9/Buchst.g` | 1 conditional `RR` | `M10-S` |
| `SRC-001#Art.10/Abs.9/Buchst.i` | 3 conditional `RR` | `M10-T` bis `M10-V` |
| `SRC-001#Art.10/Abs.9/Buchst.l` | 2 conditional `RR` | `M10-W` und `M10-X` |
| `SRC-001#Art.10/Abs.9/Buchst.m` | 3 conditional `RR` | `M10-Y`, `M10-Z`, `M10-AA` |
| **Gesamt** | **27** | |

---

## 6. Kandidaten

### 6.1 `SRC-001#Art.10/Abs.2`

### M10-A — Einrichtung des Risikomanagementsystems

- **Title EN:** Establishment of the Risk Management System
- **DE:** Der Hersteller muss ein Risikomanagementsystem nach Anhang I Abschnitt 3 einrichten.
- **EN:** The manufacturer shall establish a risk management system as described in Section 3 of Annex I.
- **Primary:** `SRC-001#Art.10/Abs.2`
- **Supplementary:** `SRC-001#Anh.I/Nr.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M10-B — Dokumentation des Risikomanagementsystems

- **Title EN:** Documentation of the Risk Management System
- **DE:** Der Hersteller muss das Risikomanagementsystem nach Anhang I Abschnitt 3 dokumentieren.
- **EN:** The manufacturer shall document the risk management system described in Section 3 of Annex I.
- **Primary:** `SRC-001#Art.10/Abs.2`
- **Supplementary:** `SRC-001#Anh.I/Nr.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M10-C — Anwendung des Risikomanagementsystems

- **Title EN:** Implementation of the Risk Management System
- **DE:** Der Hersteller muss das Risikomanagementsystem nach Anhang I Abschnitt 3 anwenden.
- **EN:** The manufacturer shall implement the risk management system described in Section 3 of Annex I.
- **Primary:** `SRC-001#Art.10/Abs.2`
- **Supplementary:** `SRC-001#Anh.I/Nr.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M10-D — Aufrechterhaltung des Risikomanagementsystems

- **Title EN:** Maintenance of the Risk Management System
- **DE:** Der Hersteller muss das Risikomanagementsystem nach Anhang I Abschnitt 3 aufrechterhalten.
- **EN:** The manufacturer shall maintain the risk management system described in Section 3 of Annex I.
- **Primary:** `SRC-001#Art.10/Abs.2`
- **Supplementary:** `SRC-001#Anh.I/Nr.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Gemeinsamer Hinweis zu M10-A bis M10-D:** Anhang I Nr. 3 ist notwendiger normativer Kontext des in Art. 10 Abs. 2 bezeichneten Risikomanagementsystems. Die Detailpflichten aus Anhang I Nr. 3 werden hier **nicht** systematisch extrahiert.

### 6.2 `SRC-001#Art.10/Abs.9`

### M10-E — Verfahren zur Sicherstellung der Serienkonformität

- **Title EN:** Procedures to Maintain Conformity in Series Production
- **DE:** Der Hersteller muss über Verfahren verfügen, die gewährleisten, dass die Anforderungen der MDR auch bei serienmäßiger Herstellung jederzeit eingehalten werden.
- **EN:** The manufacturer shall ensure that procedures are in place to keep series production in conformity with the requirements of the MDR.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.1`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M10-F — Zeitgerechte Berücksichtigung relevanter Änderungen

- **Title EN:** Timely Consideration of Relevant Changes
- **DE:** Der Hersteller muss Änderungen an Auslegung oder Merkmalen des Produkts sowie Änderungen harmonisierter Normen oder Gemeinsamer Spezifikationen, auf die bei der Konformitätserklärung Bezug genommen wird, zeitgerecht angemessen berücksichtigen.
- **EN:** The manufacturer shall adequately take into account, in a timely manner, changes in device design or characteristics and changes in harmonised standards or common specifications by reference to which conformity of the device is declared.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.2`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Eine der im Satz genannten relevanten Änderungen tritt ein.

**Theme-Nachadjudikation:** ursprünglich `Software-Lebenszyklus`; final `Qualitäts- und Risikomanagement`, weil es sich um eine übergreifende regulatorische Change-Control- bzw. Compliance-Pflicht handelt (Abschnitt 4, C).

**Cross-Regulation:** sachliche Beziehung zu `RR-084`; **keine** Deduplizierung.

### M10-G — Einrichtung des Qualitätsmanagementsystems

- **Title EN:** Establishment of the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller ein Qualitätsmanagementsystem einrichten.
- **EN:** For devices other than investigational devices, the manufacturer shall establish a quality management system.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-H — Dokumentation des Qualitätsmanagementsystems

- **Title EN:** Documentation of the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller das Qualitätsmanagementsystem dokumentieren.
- **EN:** For devices other than investigational devices, the manufacturer shall document the quality management system.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-I — Anwendung des Qualitätsmanagementsystems

- **Title EN:** Implementation of the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller das Qualitätsmanagementsystem anwenden.
- **EN:** For devices other than investigational devices, the manufacturer shall implement the quality management system.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-J — Aufrechterhaltung des Qualitätsmanagementsystems

- **Title EN:** Maintenance of the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller das Qualitätsmanagementsystem aufrechterhalten.
- **EN:** For devices other than investigational devices, the manufacturer shall maintain the quality management system.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-K — Aktualisierung des Qualitätsmanagementsystems

- **Title EN:** Keeping the Quality Management System Up to Date
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller das Qualitätsmanagementsystem ständig auf dem neuesten Stand halten.
- **EN:** For devices other than investigational devices, the manufacturer shall keep the quality management system up to date.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-L — Kontinuierliche Verbesserung des Qualitätsmanagementsystems

- **Title EN:** Continual Improvement of the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller das Qualitätsmanagementsystem kontinuierlich verbessern.
- **EN:** For devices other than investigational devices, the manufacturer shall continually improve the quality management system.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-M — Wirksame und proportionale Gewährleistung der MDR-Konformität durch das QMS

- **Title EN:** Effective and Proportionate Assurance of MDR Compliance by the QMS
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss das Qualitätsmanagementsystem die Einhaltung der MDR auf die wirksamste Weise und in einer der Risikoklasse und der Art des Produkts angemessenen Weise gewährleisten.
- **EN:** For devices other than investigational devices, the quality management system shall ensure compliance with the MDR in the most effective manner and in a manner that is proportionate to the risk class and the type of device.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Atomizität (Nachadjudikation):** Zusammenführung der ursprünglich getrennten Kandidaten zur wirksamsten Weise und zur Proportionalität. `in the most effective manner` und die Proportionalität nach Risikoklasse und Produktart sind kumulative Qualitätsmerkmale derselben QMS-Compliance-Funktion. Split-Bedingung 1 erfüllt, Split-Bedingung 2 nicht erfüllt (Abschnitt 4, A).

### M10-N — Organisatorischer Geltungsumfang des QMS

- **Title EN:** Organisational Scope of the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss das Qualitätsmanagementsystem alle Teile und Elemente der Herstellerorganisation umfassen, die mit der Qualität von Prozessen, Verfahren und Produkten befasst sind.
- **EN:** For devices other than investigational devices, the quality management system shall cover all parts and elements of the manufacturer's organisation dealing with the quality of processes, procedures and devices.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.2/Satz.1`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-O — Steuerung der QMS-Governance-Strukturen

- **Title EN:** Governance of QMS Structures and Resources
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss das Qualitätsmanagementsystem die erforderlichen Strukturen, Verantwortlichkeiten, Verfahren, Prozesse und Managementressourcen steuern, die zur Umsetzung der für die MDR-Konformität erforderlichen Grundsätze und Maßnahmen notwendig sind.
- **EN:** For devices other than investigational devices, the quality management system shall govern the structure, responsibilities, procedures, processes and management resources required to implement the principles and actions necessary to achieve compliance with the MDR.
- **Primary:** `SRC-001#Art.10/Abs.9/UAbs.2/Satz.2`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-P — Verantwortlichkeit der Leitung im QMS

- **Title EN:** Management Responsibility in the QMS
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem die Verantwortlichkeit der Leitung umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses management responsibility.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.c`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Cross-Regulation:** **keine** Dublette zu `RR-102`.

### M10-Q — Ressourcenmanagement einschließlich Zulieferer- und Unterauftragnehmersteuerung

- **Title EN:** Resource Management Including Supplier and Subcontractor Control
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem ein Ressourcenmanagement umfasst, einschließlich der Auswahl und Kontrolle von Zulieferern und Unterauftragnehmern.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses resource management, including the selection and control of suppliers and subcontractors.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.d`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Cross-Regulation:** **keine** Dublette zu `RR-101`.

### M10-R — Einbindung des Risikomanagements in das QMS

- **Title EN:** Inclusion of Risk Management in the QMS
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem das Risikomanagement gemäß Anhang I Abschnitt 3 umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses risk management as set out in Section 3 of Annex I.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.e`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Cross-Article:** **keine** interne Deduplizierung zu M10-A bis M10-D. Späterer systematischer Abgleich mit `SRC-001#Anh.I/Nr.3` (Abschnitt 9).

**Cross-Regulation:** **keine** Dublette zu `RR-095`.

### M10-S — Produktrealisierung im Qualitätsmanagementsystem

- **Title EN:** Product Realisation within the Quality Management System
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem die Produktrealisierung einschließlich Planung, Auslegung, Entwicklung, Herstellung und Bereitstellung von Dienstleistungen umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses product realisation, including planning, design, development, production and service provision.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.g`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Atomizität:** eine gemeinsame `RR`. Planung, Auslegung, Entwicklung, Herstellung und Dienstleistungsbereitstellung sind zwingende Bestandteile des gemeinsamen QMS-Prozessbereichs Produktrealisierung (Abschnitt 4, B).

**Production:** **kein** separates Out-of-Scope-Atom.

### M10-T — Aufstellung des PMS-Systems als QMS-Aspekt

- **Title EN:** Setting-Up of the Post-Market Surveillance System as a QMS Aspect
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem die Aufstellung eines Systems zur Überwachung nach dem Inverkehrbringen gemäß Artikel 83 umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses the setting-up of a post-market surveillance system in accordance with Article 83.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.i`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Cross-Article:** späterer Abgleich mit `SRC-001#Art.83` (Abschnitt 9). **Kein** Deferred.

### M10-U — Anwendung des PMS-Systems als QMS-Aspekt

- **Title EN:** Implementation of the Post-Market Surveillance System as a QMS Aspect
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem die Anwendung des Systems zur Überwachung nach dem Inverkehrbringen gemäß Artikel 83 umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses the implementation of the post-market surveillance system in accordance with Article 83.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.i`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Cross-Article:** späterer Abgleich mit `SRC-001#Art.83` (Abschnitt 9). **Kein** Deferred.

### M10-V — Aufrechterhaltung des PMS-Systems als QMS-Aspekt

- **Title EN:** Maintenance of the Post-Market Surveillance System as a QMS Aspect
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem die Aufrechterhaltung des Systems zur Überwachung nach dem Inverkehrbringen gemäß Artikel 83 umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses the maintenance of the post-market surveillance system in accordance with Article 83.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.i`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Post-Market-Monitoring
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Cross-Article:** späterer Abgleich mit `SRC-001#Art.83` (Abschnitt 9). **Kein** Deferred.

### M10-W — Management korrektiver und präventiver Maßnahmen

- **Title EN:** Management of Corrective and Preventive Actions
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem das Management korrektiver und präventiver Maßnahmen umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses the management of corrective and preventive actions.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.l`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-X — Überprüfung der Wirksamkeit korrektiver und präventiver Maßnahmen

- **Title EN:** Verification of the Effectiveness of Corrective and Preventive Actions
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem die Überprüfung der Wirksamkeit korrektiver und präventiver Maßnahmen umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system addresses verification of the effectiveness of corrective and preventive actions.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.l`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-Y — Überwachung und Messung der Ergebnisse

- **Title EN:** Monitoring and Measurement of Output
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem Verfahren zur Überwachung und Messung der Ergebnisse umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system includes processes for monitoring and measurement of output.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.m`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

### M10-Z — Datenanalyse im QMS

- **Title EN:** Data Analysis within the QMS
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem Verfahren zur Datenanalyse umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system includes processes for data analysis.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.m`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

**Hinweis:** allgemeine QMS-Datenanalyse; **nicht** automatisch Data Governance.

### M10-AA — Produktverbesserung im QMS

- **Title EN:** Product Improvement within the QMS
- **DE:** Für Produkte, bei denen es sich nicht um Prüfprodukte handelt, muss der Hersteller sicherstellen, dass das Qualitätsmanagementsystem Verfahren zur Produktverbesserung umfasst.
- **EN:** For devices other than investigational devices, the manufacturer shall ensure that the quality management system includes processes for product improvement.
- **Primary:** `SRC-001#Art.10/Abs.9/Buchst.m`
- **Supplementary:** `SRC-001#Art.10/Abs.9/UAbs.1/Satz.3` · `SRC-001#Art.10/Abs.9/UAbs.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Produkt ist kein Prüfprodukt.

---

## 7. Conditional-Audit

| Kategorie | Anzahl | Kandidaten |
| --- | --- | --- |
| Regulär | 5 | `M10-A` · `M10-B` · `M10-C` · `M10-D` · `M10-E` |
| Conditional | 22 | `M10-F` · `M10-G` · `M10-H` · `M10-I` · `M10-J` · `M10-K` · `M10-L` · `M10-M` · `M10-N` · `M10-O` · `M10-P` · `M10-Q` · `M10-R` · `M10-S` · `M10-T` · `M10-U` · `M10-V` · `M10-W` · `M10-X` · `M10-Y` · `M10-Z` · `M10-AA` |

Trigger von `M10-F`: Eine der im Satz genannten relevanten Änderungen tritt ein. Trigger von `M10-G` bis `M10-AA`: Produkt ist kein Prüfprodukt.

---

## 8. Cross-Regulation-Abgleich mit `SRC-002`

| MDR-Kandidat | AI-Act-Bestand | Ergebnis |
| --- | --- | --- |
| `M10-A` bis `M10-D` | `RR-007` bis `RR-010` | keine Deduplizierung |
| MDR-QMS-Chapeau | `RR-081` / `RR-082` | keine Deduplizierung |
| `M10-F` | `RR-084` | sachliche Beziehung; keine Deduplizierung |
| `M10-P` | `RR-102` | keine Deduplizierung |
| `M10-Q` | `RR-101` | keine Deduplizierung |
| `M10-R` | `RR-095` | keine Deduplizierung |
| `M10-S` | AI-Art.-17-Design-/Development-Bestand | keine Deduplizierung |
| `M10-T` bis `M10-V` | `RR-096` bis `RR-098` | keine Deduplizierung |

**Begründung:** unterschiedliche regulatorische Rollen, Rechtsregime, Bezugsobjekte, Trigger und Compliance-Sollzustände. Eine spätere gemeinsame organisatorische Evidenz beseitigt die getrennte normative Herkunft nicht.

| Merkmal | Ergebnis |
| --- | --- |
| Cross-Regulation-Deduplizierungen | 0 |
| Bestehende AI-`RR` ändern | NEIN |

---

## 9. Spätere MDR-interne Abgleiche

| Quellenbereich | Behandlung | Abgleich insbesondere mit | Status |
| --- | --- | --- | --- |
| `SRC-001#Anh.I/Nr.3` | später eigenständig systematisch extrahieren | `M10-A`, `M10-B`, `M10-C`, `M10-D`, `M10-R` | kein Deferred |
| `SRC-001#Art.83` | später eigenständig systematisch extrahieren | `M10-T`, `M10-U`, `M10-V` | kein Deferred |

Diese späteren Abgleiche sind **kein** Grund für einen zurückgestellten Status und **keine** dokumentierte Unsicherheit.

---

## 10. Multilingualer Audit

| Merkmal | Ergebnis |
| --- | --- |
| DE/EN | PASS |
| Materielle Divergenzen | 0 |
| Weitere Sprachen erforderlich | NEIN |
| Unresolved | 0 |

Geprüfte atomizitätsrelevante Begriffe, unter anderem: einrichten / establish · dokumentieren / document · anwenden / implement · aufrechterhalten / maintain · keep up to date · continually improve · most effective manner · proportionate · responsibility of management · resource management · product realisation · planning · design · development · production · service provision · setting-up · corrective and preventive actions · verification of effectiveness · monitoring and measurement · data analysis · product improvement.

---

## 11. Scope-Audit

| Bereich | Ergebnis |
| --- | --- |
| Nicht freigegebene Buchstaben von `SRC-001#Art.10/Abs.9` (a, b, f, h, j, k) | nicht extrahiert |
| `SRC-001#Anh.I/Nr.3` | nicht systematisch extrahiert |
| `SRC-001#Art.83` | nicht systematisch extrahiert |
| ISO 13485 | keine Klauseln extrahiert |
| ISO 14971 | keine Klauseln extrahiert |
| IEC 62304 | keine Klauseln extrahiert |
| Out-of-Scope-Atome aus dem final adjudizierten aktiven Art.-10-Bereich | 0 |

---

## 12. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. **Keine** Methodenänderung erforderlich.

Besonders bestätigt:

- mehrere Verben allein erzeugen keinen Split;
- unterschiedliche Teilstatus allein genügen nicht;
- Modalitäten und Qualitätsmerkmale derselben Hauptpflicht bleiben zusammen;
- `including` erzeugt keinen automatischen Split;
- Scope-Ausschlüsse dürfen keinen Split erzeugen;
- QMS-Integration und materielle Fachpflicht können getrennte Erfüllungsstatus besitzen;
- normative Incorporation-by-reference kann Supplementary-Kontext erfordern, ohne den referenzierten Quellenbereich vorzeitig vollständig zu extrahieren.

---

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Vollständige systematische Extraktion der freigegebenen Bereiche von `SRC-001` Art. 10. Final 27 Gap-`RR`-Kandidaten `M10-A` bis `M10-AA`, davon 5 regulär und 22 conditional; 0 unresolved, 0 deferred, 0 Cross-Regulation-Deduplizierungen und 0 Out-of-Scope-Atome. Nach gezielter Nachadjudikation wurden die zwei ursprünglich getrennten QMS-Compliance-Qualitätsdimensionen zu einer `RR` zusammengeführt, Art. 10 Abs. 9 Buchst. g als einheitlicher QMS-Prozessbereich Produktrealisierung behandelt, `M10-F` dem Cluster Qualitäts- und Risikomanagement zugeordnet, für `M10-C` und `M10-D` Planung und Konzeption ergänzt und Anhang I Nr. 3 als notwendiger Supplementary-Kontext für `M10-A` bis `M10-D` bestätigt. |
| 1.1 | Formale Präzisierung der Art.-10-Abs.-9-Lokatoren auf die Unterabsatzstruktur (`UAbs.1/Satz.1` bis `UAbs.1/Satz.3`, `UAbs.2/Satz.1` und `UAbs.2/Satz.2`, `UAbs.3` als einleitender Kontext der Buchstabenliste) sowie explizite Dokumentation der rechnerischen Überleitung vom ursprünglichen Research-Stand mit 31 Gap-`RR`-Kandidaten und einem separaten Production-Out-of-Scope-Atom zum finalen Stand von 27 Gap-`RR`-Kandidaten und 0 Out-of-Scope-Atomen. Keine materielle Änderung der 27 finalen Kandidaten. |
