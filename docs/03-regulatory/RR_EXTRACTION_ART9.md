# Systematische RR-Extraktion — SRC-002 Art. 9

Version 1.2 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` |
| Quellenbereich | `SRC-002#Art.9` |
| Coverage-Kategorie | Kernbereich |
| Themenbereich | Qualitäts- und Risikomanagement |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der ersten systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** `RR`-Identifikatoren; die Kandidaten tragen ausschließlich temporäre Kennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Methodisches Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Ursprünglicher systematischer Durchlauf | 30 Kandidaten |
| Nach Anti-Over-Splitting und Art.-9-interner Atomisierung | **25** materielle Kandidaten |
| Nach finaler Cross-Source-Deduplizierung gegen den vollständigen Art.-13-Bestand | **24** eigenständige `RR`-Kandidaten |
| davon unmittelbar katalogisierbar | 24 |
| Cross-Source-dedupliziert, 0 eigene `RR` | 1 — Kandidat T |
| Zurückgestellt (deferred) | 0 |
| Ungelöst (unresolved) | 0 |

Kandidat V zählt zu den 24 unmittelbar katalogisierbaren Kandidaten. Kandidat T zählt nach der Cross-Source-Deduplizierung **nicht** mehr als eigenständige `RR` (Abschnitt 5). Für V und T ist kein permanenter Identifikator vergeben.

Beim Anti-Over-Splitting wurden mehrere zeitliche, methodische und Akzeptanzkriterien entsprechend [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 6 **nicht** zu Mikro-`RR` verselbständigt.

Es war **keine** quantitative Zielzahl Auswahlkriterium. Die Zahl 25 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Finaler Kandidatenbestand

Die 25 materiellen Kandidaten sind: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, XY, AD.

Diese Menge bildet den Stand nach Art.-9-interner Atomisierung ab und bleibt zur Nachvollziehbarkeit vollständig erhalten. Kandidat T war auf dieser Ebene zunächst materieller Kandidat; nach der Cross-Source-Deduplizierung gegen den vollständigen Art.-13-Bestand bildet T **keine** eigenständige `RR` (Abschnitt 5). Final eigenständige `RR`-Kandidaten sind alle genannten Kandidaten außer T, insgesamt 24.

`XY` ist der kombinierte Nachfolger der früher getrennt geführten Kandidaten X und Y.

Nicht mehr eigenständig bestehen: **Z, AA, AB, AC**. Ihr normativer Inhalt wurde vollständig in Kandidat W integriert. Es gingen dabei keine normativen Inhalte verloren.

---

## 4. Unmittelbar katalogisierbare Kandidaten

24 Kandidaten: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, U, V, W, XY, AD.

### A — Einrichtung des Risikomanagementsystems

- **Title EN:** Establishment of the Risk Management System
- **DE:** Der Anbieter muss sicherstellen, dass für jedes Hochrisiko-KI-System ein Risikomanagementsystem eingerichtet wird.
- **EN:** The provider shall ensure that a risk management system is established for each high-risk AI system.
- **Primary:** `SRC-002#Art.9/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null

### B — Anwendung des Risikomanagementsystems

- **Title EN:** Implementation of the Risk Management System
- **DE:** Der Anbieter muss sicherstellen, dass das Risikomanagementsystem des Hochrisiko-KI-Systems angewandt wird.
- **EN:** The provider shall ensure that the risk management system of the high-risk AI system is implemented.
- **Primary:** `SRC-002#Art.9/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null

### C — Dokumentation des Risikomanagementsystems

- **Title EN:** Documentation of the Risk Management System
- **DE:** Der Anbieter muss sicherstellen, dass das Risikomanagementsystem des Hochrisiko-KI-Systems dokumentiert wird.
- **EN:** The provider shall ensure that the risk management system of the high-risk AI system is documented.
- **Primary:** `SRC-002#Art.9/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null

### D — Aufrechterhaltung des Risikomanagementsystems

- **Title EN:** Maintenance of the Risk Management System
- **DE:** Der Anbieter muss sicherstellen, dass das Risikomanagementsystem des Hochrisiko-KI-Systems aufrechterhalten wird.
- **EN:** The provider shall ensure that the risk management system of the high-risk AI system is maintained.
- **Primary:** `SRC-002#Art.9/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null

### E — Lebenszyklusweite Planung des Risikomanagementprozesses

- **Title EN:** Lifecycle Planning of the Risk Management Process
- **DE:** Der Anbieter muss sicherstellen, dass der Risikomanagementprozess als kontinuierlicher iterativer Prozess für den gesamten Lebenszyklus des Hochrisiko-KI-Systems geplant wird.
- **EN:** The provider shall ensure that the risk management process is planned as a continuous iterative process for the entire lifecycle of the high-risk AI system.
- **Primary:** `SRC-002#Art.9/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null

### F — Kontinuierliche iterative Durchführung des Risikomanagementprozesses

- **Title EN:** Continuous Iterative Operation of the Risk Management Process
- **DE:** Der Anbieter muss sicherstellen, dass der Risikomanagementprozess während des gesamten Lebenszyklus des Hochrisiko-KI-Systems kontinuierlich und iterativ durchgeführt wird.
- **EN:** The provider shall ensure that the risk management process is run continuously and iteratively throughout the entire lifecycle of the high-risk AI system.
- **Primary:** `SRC-002#Art.9/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null

### G — Regelmäßige systematische Überprüfung des Risikomanagementsystems

- **Title EN:** Regular Systematic Review of the Risk Management System
- **DE:** Der Anbieter muss sicherstellen, dass das Risikomanagementsystem regelmäßig und systematisch überprüft wird.
- **EN:** The provider shall ensure that the risk management system is subject to regular systematic review.
- **Primary:** `SRC-002#Art.9/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null

### H — Aktualisierung des Risikomanagementsystems

- **Title EN:** Updating of the Risk Management System
- **DE:** Der Anbieter muss sicherstellen, dass das Risikomanagementsystem im Rahmen des kontinuierlichen iterativen Lebenszyklusprozesses aktualisiert wird.
- **EN:** The provider shall ensure that the risk management system is updated as part of the continuous iterative lifecycle process.
- **Primary:** `SRC-002#Art.9/Abs.2/Satz.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null

### I — Ermittlung bekannter und vorhersehbarer Risiken

- **Title EN:** Identification of Known and Foreseeable Risks
- **DE:** Der Anbieter muss bekannte und vernünftigerweise vorhersehbare Risiken ermitteln, die das Hochrisiko-KI-System bei bestimmungsgemäßer Verwendung für Gesundheit, Sicherheit oder Grundrechte verursachen kann, soweit sie in den durch Art. 9 Abs. 3 bestimmten Risikoumfang fallen.
- **EN:** The provider shall identify known and reasonably foreseeable risks that the high-risk AI system may pose to health, safety or fundamental rights when used in accordance with its intended purpose, insofar as they fall within the risk scope defined by Article 9(3).
- **Primary:** `SRC-002#Art.9/Abs.2/Buchst.a`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Satz.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

### J — Analyse bekannter und vorhersehbarer Risiken

- **Title EN:** Analysis of Known and Foreseeable Risks
- **DE:** Der Anbieter muss bekannte und vernünftigerweise vorhersehbare Risiken analysieren, die das Hochrisiko-KI-System bei bestimmungsgemäßer Verwendung für Gesundheit, Sicherheit oder Grundrechte verursachen kann, soweit sie in den durch Art. 9 Abs. 3 bestimmten Risikoumfang fallen.
- **EN:** The provider shall analyse known and reasonably foreseeable risks that the high-risk AI system may pose to health, safety or fundamental rights when used in accordance with its intended purpose, insofar as they fall within the risk scope defined by Article 9(3).
- **Primary:** `SRC-002#Art.9/Abs.2/Buchst.a`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Satz.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

### K — Abschätzung von Risiken bei bestimmungsgemäßer Verwendung und vorhersehbarer Fehlanwendung

- **Title EN:** Estimation of Risks During Intended Use and Foreseeable Misuse
- **DE:** Der Anbieter muss die Risiken abschätzen, die bei bestimmungsgemäßer Verwendung des Hochrisiko-KI-Systems sowie unter Bedingungen einer vernünftigerweise vorhersehbaren Fehlanwendung entstehen können, soweit sie in den durch Art. 9 Abs. 3 bestimmten Risikoumfang fallen.
- **EN:** The provider shall estimate the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose and under conditions of reasonably foreseeable misuse, insofar as they fall within the risk scope defined by Article 9(3).
- **Primary:** `SRC-002#Art.9/Abs.2/Buchst.b`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Satz.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

**Evidenzbegründung:** Die amtliche DE/EN-Verknüpfungsdivergenz in dieser Fundstelle wurde nach dem Multilingual Source Divergence Protocol aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 anhand von Regelungszusammenhang, Systematik und Zweck adjudiziert. Es erfolgte keine automatische Priorisierung einer Sprachfassung.

### L — Bewertung von Risiken bei bestimmungsgemäßer Verwendung und vorhersehbarer Fehlanwendung

- **Title EN:** Evaluation of Risks During Intended Use and Foreseeable Misuse
- **DE:** Der Anbieter muss die Risiken bewerten, die bei bestimmungsgemäßer Verwendung des Hochrisiko-KI-Systems sowie unter Bedingungen einer vernünftigerweise vorhersehbaren Fehlanwendung entstehen können, soweit sie in den durch Art. 9 Abs. 3 bestimmten Risikoumfang fallen.
- **EN:** The provider shall evaluate the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose and under conditions of reasonably foreseeable misuse, insofar as they fall within the risk scope defined by Article 9(3).
- **Primary:** `SRC-002#Art.9/Abs.2/Buchst.b`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Satz.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

**Evidenzbegründung:** wie bei K — Adjudikation der amtlichen DE/EN-Verknüpfungsdivergenz nach dem Multilingual Source Divergence Protocol, ohne Sprachpriorisierung.

### M — Bewertung weiterer Risiken aus Post-Market-Daten

- **Title EN:** Evaluation of Additional Risks from Post-Market Data
- **DE:** Der Anbieter muss weitere möglicherweise auftretende Risiken auf Grundlage der Auswertung der Daten aus dem System zur Beobachtung nach dem Inverkehrbringen bewerten, soweit diese Risiken in den durch Art. 9 Abs. 3 bestimmten Risikoumfang fallen.
- **EN:** The provider shall evaluate other risks that may arise on the basis of the analysis of data from the post-market monitoring system, insofar as those risks fall within the risk scope defined by Article 9(3).
- **Primary:** `SRC-002#Art.9/Abs.2/Buchst.c`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Satz.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Post-Market-Überwachung
- **Uncertainty:** null

### N — Ergreifen geeigneter gezielter Risikomanagementmaßnahmen

- **Title EN:** Adoption of Appropriate Targeted Risk Management Measures
- **DE:** Der Anbieter muss geeignete und gezielte Risikomanagementmaßnahmen ergreifen, um die nach Art. 9 Abs. 2 Buchst. a ermittelten Risiken innerhalb des durch Art. 9 Abs. 3 begrenzten Risikoumfangs zu bewältigen.
- **EN:** The provider shall adopt appropriate and targeted risk management measures to address the risks identified under Article 9(2)(a) within the risk scope limited by Article 9(3).
- **Primary:** `SRC-002#Art.9/Abs.2/Buchst.d`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Satz.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

### O — Berücksichtigung von Wechselwirkungen regulatorischer Anforderungen

- **Title EN:** Consideration of Interactions Between Regulatory Requirements
- **DE:** Der Anbieter muss bei den Risikomanagementmaßnahmen die Auswirkungen und möglichen Wechselwirkungen berücksichtigen, die sich aus der kombinierten Anwendung der Anforderungen aus Kapitel III Abschnitt 2 ergeben, sodass Risiken wirksam minimiert und die Maßnahmen zur Erfüllung dieser Anforderungen angemessen austariert werden.
- **EN:** The provider shall give due consideration, when applying risk management measures, to the effects and possible interactions arising from the combined application of the requirements in Chapter III, Section 2, so that risks are effectively minimised while an appropriate balance is maintained in implementing those measures.
- **Primary:** `SRC-002#Art.9/Abs.4`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Buchst.d` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

### P — Vertretbarkeit gefahrenspezifischer Restrisiken

- **Title EN:** Acceptability of Hazard-Specific Residual Risks
- **DE:** Der Anbieter muss sicherstellen, dass jedes relevante Restrisiko, das mit einer bestimmten Gefahr verbunden ist, nach Anwendung der Risikomanagementmaßnahmen als vertretbar beurteilt wird.
- **EN:** The provider shall ensure that each relevant residual risk associated with a specific hazard is judged acceptable after application of the risk management measures.
- **Primary:** `SRC-002#Art.9/Abs.5/UAbs.1`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Buchst.d` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Änderung und Wartung
- **Uncertainty:** null

### Q — Vertretbarkeit des Gesamtrestrisikos

- **Title EN:** Acceptability of the Overall Residual Risk
- **DE:** Der Anbieter muss sicherstellen, dass das Gesamtrestrisiko des Hochrisiko-KI-Systems nach Anwendung der Risikomanagementmaßnahmen als vertretbar beurteilt wird.
- **EN:** The provider shall ensure that the overall residual risk of the high-risk AI system is judged acceptable after application of the risk management measures.
- **Primary:** `SRC-002#Art.9/Abs.5/UAbs.1`
- **Supplementary:** `SRC-002#Art.9/Abs.2/Buchst.d` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung · Änderung und Wartung
- **Uncertainty:** null

### R — Beseitigung oder Verringerung von Risiken durch Auslegung und Entwicklung

- **Title EN:** Elimination or Reduction of Risks Through Design and Development
- **DE:** Der Anbieter muss bei der Festlegung der geeignetsten Risikomanagementmaßnahmen sicherstellen, dass die ermittelten und bewerteten Risiken soweit technisch möglich durch eine geeignete Auslegung und Entwicklung des Hochrisiko-KI-Systems beseitigt oder verringert werden.
- **EN:** When determining the most appropriate risk management measures, the provider shall ensure that identified and evaluated risks are eliminated or reduced, insofar as technically feasible, through adequate design and development of the high-risk AI system.
- **Primary:** `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.a`
- **Supplementary:** `SRC-002#Art.9/Abs.5/UAbs.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

Der zu breite Lokator `SRC-002#Art.9/Abs.2` wurde hier bewusst **nicht** als `supplementary` übernommen.

### S — Minderungs- und Kontrollmaßnahmen für nicht eliminierbare Risiken

- **Title EN:** Mitigation and Control Measures for Non-Eliminable Risks
- **DE:** Der Anbieter muss, soweit dies angemessen ist, geeignete Minderungs- und Kontrollmaßnahmen für Risiken anwenden, die nicht beseitigt werden können.
- **EN:** Where appropriate, the provider shall implement adequate mitigation and control measures for risks that cannot be eliminated.
- **Primary:** `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.b`
- **Supplementary:** `SRC-002#Art.9/Abs.5/UAbs.2` · `SRC-002#Art.9/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

### U — Schulung der Betreiber als Risikomanagementmaßnahme

- **Title EN:** Training of Deployers as a Risk Management Measure
- **DE:** Der Anbieter muss bei der Festlegung der geeignetsten Risikomanagementmaßnahmen gegebenenfalls eine angemessene Schulung der Betreiber sicherstellen.
- **EN:** When determining the most appropriate risk management measures, the provider shall, where appropriate, ensure appropriate training of deployers.
- **Primary:** `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.c`
- **Supplementary:** `SRC-002#Art.9/Abs.5/UAbs.2` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### V — Berücksichtigung von Betreibermerkmalen und Nutzungskontext

- **Title EN:** Consideration of Deployer Characteristics and Context of Use
- **DE:** Der Anbieter muss zur Beseitigung oder Verringerung von Risiken im Zusammenhang mit der Nutzung des Hochrisiko-KI-Systems die vom Betreiber zu erwartenden technischen Kenntnisse und Erfahrungen, seinen Bildungsstand sowie seine Aus- und Fortbildung und den voraussichtlichen Nutzungskontext gebührend berücksichtigen.
- **EN:** The provider shall, with a view to eliminating or reducing risks related to the use of the high-risk AI system, give due consideration to the technical knowledge, experience, education and training to be expected from the deployer, as well as the presumable context in which the system is intended to be used.
- **Primary:** `SRC-002#Art.9/Abs.5/UAbs.3`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null

Zur Auflösung der Sprachfassungsdivergenz dieses Kandidaten siehe Abschnitt 6. Es ist **kein** Identifikator vergeben.

### W — Testen zur Ermittlung geeigneter Risikomanagementmaßnahmen

- **Title EN:** Testing to Identify Appropriate Risk Management Measures
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System zur Ermittlung der am besten geeigneten gezielten Risikomanagementmaßnahmen zu geeigneten Zeitpunkten während des gesamten Entwicklungsprozesses und jedenfalls vor dem Inverkehrbringen oder der Inbetriebnahme anhand vorab festgelegter, für die Zweckbestimmung geeigneter Metriken und Wahrscheinlichkeitsschwellenwerte getestet wird.
- **EN:** The provider shall ensure that the high-risk AI system is tested for the purpose of identifying the most appropriate and targeted risk management measures, at appropriate times throughout the development process and in any event before it is placed on the market or put into service, against predefined metrics and probabilistic thresholds appropriate to its intended purpose.
- **Primary:** `SRC-002#Art.9/Abs.6/Satz.1` · `SRC-002#Art.9/Abs.8/Satz.1` · `SRC-002#Art.9/Abs.8/Satz.2`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Verifikation und Validierung
- **Uncertainty:** null

**Integration:** Die früheren Kandidaten Z, AA, AB und AC bestehen **nicht** als eigene `RR`. Z und AA konkretisierten den Prüfzeitpunkt, AB und AC die Testkriterien; ihr normativer Gehalt ist vollständig in W erhalten. Die drei `primary`-Lokatoren bilden den zwingend zusammenwirkenden Normzusammenhang ab und entsprechen der Ausnahme für mehrere Hauptfundstellen nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 10.4.

### XY — Testen auf zweckbestimmungsgemäße Funktion und Abschnitt-2-Compliance

- **Title EN:** Testing for Intended-Purpose Performance and Section 2 Compliance
- **DE:** Der Anbieter muss sicherstellen, dass das Testen bestätigt, dass das Hochrisiko-KI-System beständig im Einklang mit seiner Zweckbestimmung funktioniert und die Anforderungen aus Kapitel III Abschnitt 2 erfüllt.
- **EN:** The provider shall ensure that testing confirms that the high-risk AI system performs consistently in accordance with its intended purpose and complies with the requirements of Chapter III, Section 2.
- **Primary:** `SRC-002#Art.9/Abs.6/Satz.2`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Verifikation und Validierung
- **Uncertainty:** null

`XY` ist der kombinierte Nachfolger der früher getrennt geführten Kandidaten X und Y.

### AD — Berücksichtigung Minderjähriger und anderer schutzbedürftiger Gruppen

- **Title EN:** Consideration of Minors and Other Vulnerable Groups
- **DE:** Der Anbieter muss bei der Umsetzung des Risikomanagementsystems berücksichtigen, ob das Hochrisiko-KI-System angesichts seiner Zweckbestimmung wahrscheinlich nachteilige Auswirkungen auf Personen unter 18 Jahren oder gegebenenfalls auf andere schutzbedürftige Gruppen haben wird.
- **EN:** When implementing the risk management system, the provider shall consider whether, in view of its intended purpose, the high-risk AI system is likely to adversely affect persons under the age of 18 or, where appropriate, other vulnerable groups.
- **Primary:** `SRC-002#Art.9/Abs.9`
- **Supplementary:** — (leer)
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null

---

## 5. Cross-Source-Deduplizierung Kandidat T

| Merkmal | Angabe |
| --- | --- |
| Fundstelle | `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.c` |
| Gegenstand | Bereitstellung der gemäß Art. 13 erforderlichen Informationen als Bestandteil der Auswahl geeigneter Risikomanagementmaßnahmen |
| Grundlage | vollständige systematische Art.-13-Extraktion in [RR_EXTRACTION_ART13.md](RR_EXTRACTION_ART13.md) Version 1.0 |
| Finale Entscheidung | **0 eigene `RR` nach Cross-Source-Deduplizierung** |
| Permanenter Identifikator | keiner |

### 5.1 Komponenten der Fundstelle

`SRC-002#Art.9/Abs.5/UAbs.2/Buchst.c` enthält zwei getrennte Komponenten:

1. die Bereitstellung der gemäß Art. 13 erforderlichen Informationen — Gegenstand von T;
2. gegebenenfalls die Schulung der Betreiber.

Die Trainingskomponente besteht bereits als `RR-026` (Kandidat U). `RR-026` wird **nicht** geändert.

### 5.2 Begründung

Die Informationskomponente besitzt keinen unabhängig bestimmbaren Gap-Status:

- Sind alle jeweils anwendbaren Art.-13-Informationspflichten erfüllt, fehlt kein zusätzlicher informationsbezogener Sollzustand von T.
- Ist eine einschlägige Art.-13-Informationspflicht nicht erfüllt, ist derselbe reale Mangel bereits über die betreffende Art.-13-`RR` erfasst.

Eine zusätzliche `RR` für T würde denselben Mangel aggregiert doppelt bewerten.

### 5.3 Abgleich mit dem Art.-13-Bestand

| `RR` | Befund |
| --- | --- |
| `RR-001` | kein materieller T-Erfüllungsgehalt; betrifft technische Systemtransparenz nach Art. 13 Abs. 1 |
| `RR-002` | kein materieller T-Erfüllungsgehalt; betrifft technische Systemtransparenz nach Art. 13 Abs. 1 |
| `RR-046` bis `RR-062` | bilden den materiellen Informationsbereitstellungsgehalt von T ab, jeweils soweit die konkrete Pflicht anwendbar ist |

Keine einzelne dieser `RR` wird durch T ersetzt. T ist der aggregierte Cross-Article-Verweis auf diesen Informationskomplex.

### 5.4 Traceability

Der Lokator `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.c` wird **nicht** als `supplementary`-Lokator zu `RR-046` bis `RR-062` hinzugefügt. Er ist für die vollständige normative Bestimmung keiner einzelnen Art.-13-`RR` erforderlich; eine 17-fache `supplementary`-Referenz wäre redundant und widerspräche dem Minimalitätsprinzip aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8.

Die Traceability bleibt durch die in diesem Abschnitt dokumentierte Cross-Source-Deduplizierungsentscheidung erhalten.

### 5.5 Finaler Status

Kandidat T: **0 eigene `RR` nach Cross-Source-Deduplizierung.**

Artefaktstatus wie `zurückgezogen` oder `ersetzt` werden nicht vergeben, weil T nie einen permanenten `RR`-Identifikator hatte.

---

## 6. Adjudikation Kandidat V

Lokator: `SRC-002#Art.9/Abs.5/UAbs.3`

### 6.1 Ausgangsdivergenz

| Fassung | Merkmalsreihe |
| --- | --- |
| DE | technische Kenntnisse, Erfahrungen, Bildungsstand |
| EN | technical knowledge, experience, education and training |

### 6.2 Weitere geprüfte authentische Fassungen

Die französische, die spanische und die italienische Fassung unterscheiden den Bildungsaspekt und den Ausbildungs- bzw. Trainingsaspekt ebenfalls.

Diese Feststellung wird **nicht** als Mehrheitsargument verwendet. Nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 9.1 bildet die Anzahl übereinstimmender Sprachfassungen keine Mehrheitsregel und ersetzt keine unionsrechtliche Auslegung; die Fassungen dienen hier ausschließlich als weiteres Material des Sprachvergleichs.

### 6.3 Methodische Grundlage

Angewandt wurde das Multilingual Source Divergence Protocol aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2. Keine Sprachfassung wurde priorisiert oder als führend erklärt; keine Fassung wird als unzutreffend bewertet.

Die Auflösung stützt sich auf:

- den Sprachvergleich,
- den unmittelbaren Regelungszusammenhang,
- die Systematik,
- den Regelungszweck.

### 6.4 Regelungszusammenhang und Systematik

- `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.c` behandelt die Schulung der Betreiber ausdrücklich als regulatorisch eigenständiges Konzept. Der Begriff dient hier ausschließlich als Auslegungskontext.
- `SRC-002#Art.4/Abs.1` verwendet im aktuellen Rechtsstand eine parallele Merkmalsstruktur und bildet in der deutschen Fassung den Ausbildungs- bzw. Trainingsaspekt ausdrücklich als „Aus- und Fortbildung" ab.

Art. 4 dient ausschließlich als systematischer Auslegungskontext. Er wird **nicht** als `supplementary`-Lokator des Kandidaten V geführt; das entspricht dem Minimalitätsprinzip aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8.

### 6.5 Adjudizierte normative Bedeutung

Der gemeinsame unionsrechtliche Normgehalt umfasst:

- technische Kenntnisse,
- Erfahrung,
- den Bildungsaspekt,
- den Ausbildungs- bzw. Trainingsaspekt,
- den voraussichtlichen Nutzungskontext.

Der deutsche und der englische Anforderungstext des Kandidaten V drücken diese einheitliche Bedeutung semantisch äquivalent aus. Die amtliche Textdivergenz wird damit nicht als nie bestehend dargestellt, sondern bleibt in Abschnitt 6.1 dokumentiert.

### 6.6 Atomizität

**Ergebnis: 1 `RR`.**

Die genannten Merkmale sind kumulative Beurteilungsfaktoren derselben normativen Handlung. Die bloße Aufzählung rechtfertigt nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 6 keinen Split. Die zweite Bedingung des Split-Tests aus Abschnitt 4 ist nicht erfüllt, weil die einzelnen Faktoren isoliert keine vollständigen selbstständigen Compliance-Pflichten bilden.

Der voraussichtliche Nutzungskontext bleibt Bestandteil derselben `RR`.

### 6.7 Finaler Status

| Merkmal | Befund |
| --- | --- |
| Sprachfassungsdivergenz | adjudiziert |
| Status | aktivierbar |
| `uncertainty` | null |
| Permanenter Identifikator | noch keiner vergeben |
| Katalogisierung | noch nicht erfolgt |

---

## 7. Finale 0-RR- und Nicht-Split-Entscheidungen

| Fundstelle bzw. Kandidat | Entscheidung |
| --- | --- |
| `SRC-002#Art.9/Abs.2/Satz.2` | Chapeau — keine eigene `RR` |
| `SRC-002#Art.9/Abs.3` | Scope-Qualifier — keine eigene `RR` |
| `SRC-002#Art.9/Abs.5/UAbs.2` | Chapeau der Maßnahmenhierarchie — keine eigene `RR` |
| `SRC-002#Art.9/Abs.7` | fakultative Testmodalität — keine eigene `RR` |
| `SRC-002#Art.9/Abs.10` | fakultative Integrationsmöglichkeit — keine eigene `RR` |
| Z, AA | keine eigenen `RR`; Timing-Konkretisierung in W |
| AB, AC | keine eigenen `RR`; Testkriterien in W |
| `SRC-002#Art.9/Abs.5/UAbs.2/Buchst.c` — Informationskomponente (Kandidat T) | 0 eigene `RR` nach Cross-Source-Deduplizierung; materieller Gap-Gehalt in `RR-046` bis `RR-062`; Trainingskomponente separat als `RR-026` |

---

## 8. Methodenaudit

- Die Extraktionsmethode musste hinsichtlich der **Atomizität** nicht geändert werden.
- Das Anti-Over-Splitting beruhte ausschließlich auf der strengen Anwendung der bestehenden Regeln aus Abschnitt 4 und 6 der Methode.
- Die multilingualen Divergenzen zeigten dagegen eine echte allgemeine Lücke in der Source-Fidelity-Logik.
- Diese Lücke wurde **vor** jeder Aktivierung mit [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 geschlossen.
- Es wurde **keine** Art.-9-spezifische Sonderregel eingeführt; die ergänzte Regel ist allgemein formuliert.
- Kandidat V konnte unter Anwendung der bestehenden Methode Version 1.2 adjudiziert werden; eine weitere Methodenänderung war nicht erforderlich.
- Die Cross-Source-Deduplizierung von Kandidat T erforderte ebenfalls keine Methodenänderung. Sie folgt aus dem fehlenden unabhängigen Erfüllungsstatus, der Vermeidung aggregierter Doppel-Gaps und der Locator-Minimalität; eine Art.-9-spezifische Sonderregel wurde nicht eingeführt.

---

## 9. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | angewandte Extraktions-, Atomizitäts- und Source-Fidelity-Methode (Version 1.2) |
| [COVERAGE_PLAN.md](COVERAGE_PLAN.md) | Freigabe des Quellenbereichs und Bearbeitungsstatus |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | führende Vergabestelle; hier noch nicht verändert |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |
| [RR_EXTRACTION_PILOT_ART13_1.md](RR_EXTRACTION_PILOT_ART13_1.md) | erster Pilot |
| [RR_EXTRACTION_PILOT_ART10_2_F_G.md](RR_EXTRACTION_PILOT_ART10_2_F_G.md) | zweiter Pilot |

---

## 10. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: final adjudizierter Stand der systematischen `0 / 1 / n`-Prüfung von `SRC-002#Art.9` mit 25 materiellen Kandidaten, davon 23 unmittelbar katalogisierbar, ein zurückgestellter und ein ungelöster Kandidat. Keine Identifikatorvergabe. |
| 1.1 | Kandidat V nach Anwendung des multilingualen Source-Divergence-Protokolls adjudiziert und als unmittelbar katalogisierbar eingestuft; Zahl der unmittelbar katalogisierbaren Kandidaten von 23 auf 24 erhöht. Kandidat T bleibt unverändert zurückgestellt. Keine Identifikatorvergabe und keine Katalogänderung. |
| 1.2 | Kandidat T nach vollständiger systematischer Art.-13-Extraktion und Cross-Source-Deduplizierung final als 0 eigene `RR` adjudiziert; materieller Informationsgehalt durch `RR-046` bis `RR-062` abgedeckt, Trainingskomponente weiterhin `RR-026`; zurückgestellter Bestand auf 0 reduziert. Keine Identifikatorvergabe. |
