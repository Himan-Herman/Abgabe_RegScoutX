# Systematische RR-Extraktion — SRC-002 Art. 13

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` |
| Quellenbereich | `SRC-002#Art.13` |
| Coverage-Kategorie | Kernbereich |
| Themenbereich | Transparenz |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.3 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |
| Rechtsstand | konsolidierter Stand 27.07.2026 gemäß [SOURCES.md](SOURCES.md) |

Diese Evidenzdatei dokumentiert den final adjudizierten Extraktionsstand des Quellenbereichs. Sie vergibt **keine** neuen permanenten `RR`-Identifikatoren.

`RR-001` und `RR-002` sind bestehender Pilotbestand aus [RR_EXTRACTION_PILOT_ART13_1.md](RR_EXTRACTION_PILOT_ART13_1.md) und werden hier ausschließlich referenziert. Die neuen Kandidaten tragen ausschließlich die temporären Kennungen `A13-A` bis `A13-Q`; die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

Art. 13 bleibt im Coverage-Plan `in Prüfung`, bis die Katalogintegration und die nachgelagerten Prüfungen erfolgt sind.

---

## 2. Methodisches Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Bestehende `RR` systematisch bestätigt | 2 — `RR-001` und `RR-002` |
| Neue materielle Kandidaten | **17** — `A13-A` bis `A13-Q` |
| davon unmittelbar katalogisierbar | 17 |
| Unresolved innerhalb Art. 13 | 0 |
| Deferred innerhalb Art. 13 | 0 |
| Echte 0-`RR`-Fundstellen | 1 — `SRC-002#Art.13/Abs.3` |

Kandidat T aus [RR_EXTRACTION_ART9.md](RR_EXTRACTION_ART9.md) bleibt weiterhin zurückgestellt (`deferred`) und ist **nicht** Teil dieser Zählung. Zur Vorbereitung der späteren Entscheidung siehe Abschnitt 9.

Es war **keine** quantitative Zielzahl Splitting- oder Inclusion-Kriterium. Die Zahl 17 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-002#Art.13/Abs.1/Satz.1` | 1 `RR` | bereits `RR-001`; keine neue `RR` |
| `SRC-002#Art.13/Abs.1/Satz.2` | 1 `RR` | bereits `RR-002`; keine neue `RR` |
| `SRC-002#Art.13/Abs.2` | 1 neue `RR` | A13-A |
| `SRC-002#Art.13/Abs.3` | 0 eigene `RR` | gemeinsamer Mindestinhaltsrahmen der Buchst. a bis f; `supplementary` (Abschnitt 6) |
| `SRC-002#Art.13/Abs.3/Buchst.a` | 1 neue `RR` | A13-B |
| `SRC-002#Art.13/Abs.3/Buchst.b` | 1 neue residuale `RR` | A13-C |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.i` | 1 neue `RR` | A13-D |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.ii` | 2 neue `RR` | A13-E, A13-F |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.iii` | 1 neue `RR` | A13-G |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.iv` | 1 neue `RR` | A13-H |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.v` | 1 neue `RR` | A13-I |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.vi` | 1 neue `RR` | A13-J |
| `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.vii` | 1 neue `RR` | A13-K |
| `SRC-002#Art.13/Abs.3/Buchst.c` | 1 neue `RR` | A13-L |
| `SRC-002#Art.13/Abs.3/Buchst.d` | 1 neue `RR` | A13-M |
| `SRC-002#Art.13/Abs.3/Buchst.e` | 3 neue `RR` | A13-N, A13-O, A13-P |
| `SRC-002#Art.13/Abs.3/Buchst.f` | 1 neue `RR` | A13-Q |

Alle operativen Fundstellen des aktuellen Art.-13-Bestands sind in dieser Tabelle entschieden.

---

## 4. Bestehender Pilotbestand

| `RR` | Primary | Ergebnis |
| --- | --- | --- |
| `RR-001` | `SRC-002#Art.13/Abs.1/Satz.1` | materiell bestätigt |
| `RR-002` | `SRC-002#Art.13/Abs.1/Satz.2` | materiell bestätigt |

Daraus folgt: keine Textänderung, keine neue Atomisierung, keine neue Identifikatorvergabe und keine `replaces`/`replaced_by`-Beziehung.

Der systematische Durchlauf ergab **keinen** methodischen Widerspruch zum Pilot.

---

## 5. Neue Kandidaten

Für alle 17 Kandidaten gilt: Themencluster `Transparenz`, Lebenszyklusphase `Inverkehrbringen, Inbetriebnahme und Betrieb`, `uncertainty` = `null`. Es wird **keine** permanente `RR`-ID vergeben.

### A13-A — Bereitstellung und Informationsqualität der Betriebsanleitungen

- **Title EN:** Instructions for Use and Information Quality
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System in einem geeigneten digitalen Format bereitgestellt oder auf andere Weise mit Betriebsanleitungen versehen wird, die präzise, vollständige, korrekte und eindeutige Informationen in einer für die Betreiber relevanten, barrierefrei zugänglichen und verständlichen Form enthalten.
- **EN:** The provider shall ensure that the high-risk AI system is accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- **Primary:** `SRC-002#Art.13/Abs.2`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Format und Informationsqualitätsmerkmale konkretisieren dieselbe Informationsbereitstellungspflicht und werden nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 6 nicht separat mikroatomisiert.

### A13-B — Anbieter- und Bevollmächtigtenangaben

- **Title EN:** Provider and Authorised Representative Details
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen seinen Namen und seine Kontaktangaben sowie gegebenenfalls den Namen und die Kontaktangaben seines Bevollmächtigten enthalten.
- **EN:** The provider shall ensure that the instructions for use contain its identity and contact details and, where applicable, the identity and contact details of its authorised representative.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.a`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-C — Information über weitere Merkmale, Fähigkeiten und Leistungsgrenzen

- **Title EN:** Information on Additional Characteristics, Capabilities and Performance Limitations
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen Informationen über weitere Merkmale, Fähigkeiten und Leistungsgrenzen des Hochrisiko-KI-Systems enthalten, soweit diese nicht bereits durch die in Artikel 13 Absatz 3 Buchstabe b Ziffern i bis vii ausdrücklich genannten Informationsgegenstände erfasst sind.
- **EN:** The provider shall ensure that the instructions for use contain information on additional characteristics, capabilities and limitations of performance of the high-risk AI system insofar as they are not already covered by the information expressly specified in Article 13(3), point (b), subpoints (i) to (vii).
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Evidenznotiz zur Residualisierung:** Die Begriffe „weitere" bzw. „additional" und die Abgrenzung gegenüber Ziff. i bis vii sind eine **methodische Residualisierung** zur Vermeidung eines aggregierenden Doppelstatus. Sie dürfen **nicht** als wörtlicher zusätzlicher Quellenqualifier dargestellt werden. Normative Grundlage der Residualisierung ist die offene Struktur „einschließlich" bzw. „including" in Buchst. b. A13-C bewertet ausschließlich den über Ziff. i bis vii hinausgehenden Gehalt; die dort ausdrücklich genannten Informationsgegenstände werden über A13-D bis A13-K erfasst.

### A13-D — Information über die Zweckbestimmung

- **Title EN:** Information on the Intended Purpose
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen die Zweckbestimmung des Hochrisiko-KI-Systems angeben.
- **EN:** The provider shall ensure that the instructions for use state the intended purpose of the high-risk AI system.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.i`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-E — Information über getestete, validierte und erwartbare Leistungsniveaus

- **Title EN:** Information on Tested, Validated and Expected Performance Levels
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen das Maß an Genauigkeit einschließlich der zugehörigen Metriken sowie die Robustheit und Cybersicherheit gemäß Artikel 15 angeben, gegen die das Hochrisiko-KI-System getestet und validiert wurde und die zu erwarten sind.
- **EN:** The provider shall ensure that the instructions for use state the levels of accuracy, including the relevant metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.ii`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-F — Information über Umstände mit Einfluss auf erwartete Leistungsniveaus

- **Title EN:** Information on Circumstances Affecting Expected Performance Levels
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen alle bekannten und vorhersehbaren Umstände angeben, die sich auf das erwartete Maß an Genauigkeit, Robustheit oder Cybersicherheit des Hochrisiko-KI-Systems auswirken können.
- **EN:** The provider shall ensure that the instructions for use state any known and foreseeable circumstances that may have an impact on the expected level of accuracy, robustness or cybersecurity of the high-risk AI system.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.ii`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-G — Information über risikorelevante Nutzungsumstände

- **Title EN:** Information on Risk-Relevant Circumstances of Use
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen alle bekannten oder vorhersehbaren Umstände im Zusammenhang mit der bestimmungsgemäßen Verwendung oder einer vernünftigerweise vorhersehbaren Fehlanwendung angeben, die zu Risiken für Gesundheit, Sicherheit oder Grundrechte gemäß Artikel 9 Absatz 2 führen können.
- **EN:** The provider shall ensure that the instructions for use state any known or foreseeable circumstances related to use in accordance with the intended purpose or under conditions of reasonably foreseeable misuse that may lead to risks to health, safety or fundamental rights referred to in Article 9(2).
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.iii`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-H — Information über technische Fähigkeiten zur Erläuterung von Ausgaben

- **Title EN:** Information on Technical Capabilities for Explaining Outputs
- **DE:** Der Anbieter muss gegebenenfalls sicherstellen, dass die Betriebsanleitungen die technischen Fähigkeiten und Merkmale des Hochrisiko-KI-Systems angeben, die die Bereitstellung von Informationen ermöglichen, die zur Erläuterung seiner Ausgaben relevant sind.
- **EN:** Where applicable, the provider shall ensure that the instructions for use state the technical capabilities and characteristics of the high-risk AI system to provide information relevant to explaining its output.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.iv`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-I — Information über personengruppenspezifische Leistung

- **Title EN:** Information on Performance for Specific Persons or Groups
- **DE:** Der Anbieter muss gegebenenfalls sicherstellen, dass die Betriebsanleitungen Informationen über die Leistung des Hochrisiko-KI-Systems in Bezug auf bestimmte Personen oder Personengruppen enthalten, auf die das System bestimmungsgemäß angewandt werden soll.
- **EN:** Where appropriate, the provider shall ensure that the instructions for use contain information on the performance of the high-risk AI system regarding specific persons or groups of persons on which the system is intended to be used.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.v`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-J — Information über Eingabedaten und verwendete Datensätze

- **Title EN:** Information on Input Data and Data Sets Used
- **DE:** Der Anbieter muss gegebenenfalls sicherstellen, dass die Betriebsanleitungen unter Berücksichtigung der Zweckbestimmung Spezifikationen für die Eingabedaten oder andere relevante Informationen über die verwendeten Trainings-, Validierungs- und Testdatensätze enthalten.
- **EN:** Where appropriate, the provider shall ensure that the instructions for use contain specifications for the input data or other relevant information concerning the training, validation and testing data sets used, taking into account the intended purpose.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.vi`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-K — Information zur Interpretation und angemessenen Nutzung

- **Title EN:** Information Enabling Interpretation and Appropriate Use
- **DE:** Der Anbieter muss gegebenenfalls sicherstellen, dass die Betriebsanleitungen Informationen enthalten, die es den Betreibern ermöglichen, die Ausgabe des Hochrisiko-KI-Systems zu interpretieren und das System angemessen zu nutzen.
- **EN:** Where applicable, the provider shall ensure that the instructions for use contain information enabling deployers to interpret the output of the high-risk AI system and use the system appropriately.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.b/Ziff.vii`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.13/Abs.3/Buchst.b` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Keine Dublette zu `RR-001`.** `RR-001` bezeichnet den technischen Transparenz-Sollzustand, der durch Konzeption und Entwicklung des Systems herzustellen ist. A13-K bezeichnet die konkrete Informationsbereitstellung in den Betriebsanleitungen. Die Erfüllungsstatus können unabhängig voneinander unterschiedlich sein.

### A13-L — Information über vorab bestimmte Änderungen

- **Title EN:** Information on Pre-Determined Changes
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen etwaige Änderungen des Hochrisiko-KI-Systems und seiner Leistung angeben, die der Anbieter zum Zeitpunkt der ersten Konformitätsbewertung vorab bestimmt hat.
- **EN:** The provider shall ensure that the instructions for use state any changes to the high-risk AI system and its performance that were pre-determined by the provider at the time of the initial conformity assessment.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.c`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-M — Information über Maßnahmen der menschlichen Aufsicht

- **Title EN:** Information on Human Oversight Measures
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen die Maßnahmen zur menschlichen Aufsicht gemäß Artikel 14 enthalten, einschließlich der technischen Maßnahmen, die zur Erleichterung der Interpretation der Ausgaben des Hochrisiko-KI-Systems durch die Betreiber getroffen wurden.
- **EN:** The provider shall ensure that the instructions for use contain the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate interpretation of the outputs of the high-risk AI system by deployers.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.d`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

A13-M ist eine Informationspflicht über die Aufsichtsmaßnahmen. Die materiellen Art.-14-Pflichten werden dadurch **nicht** dupliziert.

### A13-N — Information über erforderliche Rechen- und Hardware-Ressourcen

- **Title EN:** Information on Required Computational and Hardware Resources
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen die für das Hochrisiko-KI-System erforderlichen Rechen- und Hardware-Ressourcen angeben.
- **EN:** The provider shall ensure that the instructions for use state the computational and hardware resources required for the high-risk AI system.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.e`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-O — Information über die erwartete Lebensdauer

- **Title EN:** Information on Expected Lifetime
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen die erwartete Lebensdauer des Hochrisiko-KI-Systems angeben.
- **EN:** The provider shall ensure that the instructions for use state the expected lifetime of the high-risk AI system.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.e`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-P — Information über Wartungs- und Pflegemaßnahmen

- **Title EN:** Information on Maintenance and Care Measures
- **DE:** Der Anbieter muss sicherstellen, dass die Betriebsanleitungen alle erforderlichen Wartungs- und Pflegemaßnahmen einschließlich ihrer Häufigkeit angeben, die für das ordnungsgemäße Funktionieren des Hochrisiko-KI-Systems erforderlich sind, auch in Bezug auf Software-Updates.
- **EN:** The provider shall ensure that the instructions for use state all necessary maintenance and care measures, including their frequency, required to ensure the proper functioning of the high-risk AI system, including as regards software updates.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.e`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

### A13-Q — Beschreibung der Mechanismen zur Nutzung von Protokollen

- **Title EN:** Description of Mechanisms for Handling Logs
- **DE:** Der Anbieter muss gegebenenfalls sicherstellen, dass die Betriebsanleitungen die im Hochrisiko-KI-System enthaltenen Mechanismen beschreiben, die es den Betreibern ermöglichen, die Protokolle gemäß Artikel 12 ordnungsgemäß zu erfassen, zu speichern und auszuwerten.
- **EN:** Where relevant, the provider shall ensure that the instructions for use describe the mechanisms included in the high-risk AI system that allow deployers to properly collect, store and interpret the logs in accordance with Article 12.
- **Primary:** `SRC-002#Art.13/Abs.3/Buchst.f`
- **Supplementary:** `SRC-002#Art.13/Abs.3` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

---

## 6. 0-`RR`-Entscheidung

`SRC-002#Art.13/Abs.3` → **0 eigene `RR`**.

Begründung: Der Chapeau bildet den gemeinsamen Mindestinhaltsrahmen der Buchst. a bis f. Eine zusätzliche aggregierte `RR` würde dieselben Informationspflichten doppelt bewerten und widerspräche dem Anti-Over-Splitting nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 6.

Der normative Gehalt bleibt erhalten: Der Chapeau wird bei allen aus Abs. 3 gewonnenen Kandidaten als `supplementary`-Lokator geführt.

---

## 7. Multilingualer Audit

Geprüft nach dem Multilingual Source Divergence Protocol in [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 9.1.

| Nr. | Fundstelle | Befund | Status |
| --- | --- | --- | --- |
| 1 | Abs. 2 | DE „präzise" gegenüber EN „concise" | resolved |
| 2 | Abs. 2 | DE „barrierefrei zugänglich" gegenüber EN „accessible"; FR „accessibles", ES „accesible", IT „accessibili" | resolved |
| 3 | Abs. 3 Buchst. a | DE „Name" gegenüber EN „identity" | resolved |
| 4 | Abs. 3 Buchst. f | DE „auswerten" gegenüber EN „interpret" | resolved |

Zu Nr. 2: `SRC-002#Art.16/Buchst.l` wurde ausschließlich als systematischer Terminologiekontext herangezogen. Er wird **nicht** als `supplementary`-Lokator von A13-A geführt.

Keine Sprachfassung wurde priorisiert oder als führend erklärt; die Anzahl übereinstimmender Fassungen wurde nicht als Mehrheitsregel verwendet; es erfolgte keine private Wortlautangleichung.

Materielle unresolved Sprachfassungsdivergenzen innerhalb der finalen Art.-13-Extraktion: **0**.

---

## 8. Cross-Article-Deduplizierung

| Bezug | Kandidat | Befund |
| --- | --- | --- |
| Art. 9 | A13-G | Informationspflicht über risikorelevante Umstände; keine Duplikation materieller Risikomanagementpflichten |
| Art. 10 | A13-J | Informationspflicht über Eingabedaten und Datensätze; keine Duplikation materieller Data-Governance-Pflichten |
| Art. 12 | A13-Q | Beschreibung der Log-Mechanismen; keine Duplikation technischer Logging-Pflichten |
| Art. 14 | A13-M | Informationspflicht über Maßnahmen der menschlichen Aufsicht; keine Duplikation materieller Art.-14-Pflichten |
| Art. 15 | A13-E, A13-F | Transparenz über Leistungsniveaus; keine Duplikation technischer Art.-15-Pflichten |

**Offener Abgleich:** `SRC-002#Art.15/Abs.3` enthält selbst instruktionenbezogenen Gehalt zum Genauigkeitsniveau und zu den zugehörigen Metriken. Bei der späteren systematischen Art.-15-Extraktion ist deshalb ein ausdrücklicher Deduplizierungsabgleich mit A13-E erforderlich. Diese Frage wird hier **nicht** entschieden.

---

## 9. Kandidat T — Vorbereitung der Overlap-Entscheidung

Kandidat T aus [RR_EXTRACTION_ART9.md](RR_EXTRACTION_ART9.md) bleibt **deferred**. Es wird kein Identifikator vergeben, keine Aktivierung vorgenommen und keine Verwerfung ausgesprochen.

| Bezug | Overlap mit T |
| --- | --- |
| `RR-001` | kein Overlap |
| `RR-002` | kein Overlap |
| A13-A | partieller Overlap |
| A13-B bis A13-Q | jeweils partieller Overlap |

Begründung: T verweist aggregiert auf die gemäß Art. 13 erforderlichen Informationen. Die einzelnen A13-Kandidaten bilden jeweils konkrete Teile dieses Informationskomplexes ab.

Diese Matrix bereitet ausschließlich die nachgelagerte Cross-Source-Deduplizierungsentscheidung vor. Eine finale Entscheidung über T wird hier **nicht** getroffen.

---

## 10. Themencluster und Lebenszyklusphase

Alle 17 neuen Kandidaten tragen den Themencluster `Transparenz` und die Lebenszyklusphase `Inverkehrbringen, Inbetriebnahme und Betrieb` nach [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md).

Begründung: Primärer normativer Gegenstand ist die Bereitstellung beziehungsweise der Inhalt der Betriebsanleitungen für die Betreiber. Die vorgelagerte Entstehung einzelner Informationen in Entwicklung, Test, Risikomanagement oder Konformitätsbewertung erzeugt **keine** zusätzliche Erfüllungsphase dieser Art.-13-Informationspflichten.

---

## 11. Methodenaudit

Änderung von [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) erforderlich: **nein**.

Die Methode Version 1.2 konnte auf alle aufgetretenen Fallgestaltungen angewandt werden:

- Chapeau gegenüber eigener `RR`,
- offene Struktur „einschließlich" bzw. „including",
- residuale Abgrenzung,
- konditionale Pflichten,
- Anti-Over-Splitting,
- Informationspflicht gegenüber Sachpflicht,
- Cross-Article-Deduplizierung,
- Multilingual Source Divergence Protocol.

Es wurde **keine** Art.-13-Sonderregel eingeführt.

---

## 12. Abschlussstatus

| Merkmal | Befund |
| --- | --- |
| `0 / 1 / n`-Prüfung des gesamten aktuellen Art. 13 | vollständig |
| Bestehende `RR` | 2 |
| Neue Kandidaten | 17 |
| Unresolved | 0 |
| Deferred innerhalb Art. 13 | 0 |
| Katalogisierung | bereit, noch nicht erfolgt |
| Coverage-Status | weiterhin `in Prüfung` |

Damit ist **nicht** gesagt, dass Art. 13 coverage-seitig abgeschlossen sei, dass Kandidat T entschieden sei oder dass die gesamte `SRC-002`-Coverage abgeschlossen sei.

---

## 13. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | angewandte Extraktions-, Atomizitäts- und Source-Fidelity-Methode (Version 1.2) |
| [COVERAGE_PLAN.md](COVERAGE_PLAN.md) | Freigabe des Quellenbereichs und Bearbeitungsstatus (Version 1.3) |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | führende Vergabestelle; hier nicht verändert |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |
| [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | Identifikatoren, Lokator-Syntax und Traceability-Pfade |
| [RR_EXTRACTION_PILOT_ART13_1.md](RR_EXTRACTION_PILOT_ART13_1.md) | erster Pilot; Ursprung von `RR-001` und `RR-002` |
| [RR_EXTRACTION_ART9.md](RR_EXTRACTION_ART9.md) | Herkunft des zurückgestellten Kandidaten T |
| [RR_EXTRACTION_ART10.md](RR_EXTRACTION_ART10.md) | vorangegangene systematische Extraktion |

---

## 14. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: final adjudizierter Stand der vollständigen systematischen `0 / 1 / n`-Prüfung von `SRC-002` Art. 13; `RR-001` und `RR-002` bestätigt; 17 neue unmittelbar katalogisierbare Kandidaten A13-A bis A13-Q; 0 unresolved; 0 deferred innerhalb Art. 13; Kandidat T bleibt separat zurückgestellt. Keine Identifikatorvergabe. |
