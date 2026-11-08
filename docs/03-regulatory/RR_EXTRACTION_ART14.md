# Systematische RR-Extraktion — SRC-002 Art. 14

Version 1.1 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` |
| Quellenbereich | `SRC-002#Art.14` |
| Rechtsstand | konsolidierter Stand 27.07.2026 gemäß [SOURCES.md](SOURCES.md) |
| Coverage-Kategorie | Kernbereich |
| Themenbereich | Menschliche Aufsicht |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.5 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren; die Kandidaten tragen ausschließlich die temporären Kennungen `A14-A` bis `A14-J`. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Methodisches Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Neue materielle Kandidaten | **10** — `A14-A` bis `A14-J` |
| davon regulär aktivierbar | 9 |
| davon conditional | 1 — `A14-J` |
| Unresolved | 0 |
| Deferred | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 10 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-002#Art.14/Abs.1` | 1 `RR` | A14-A |
| `SRC-002#Art.14/Abs.2` | 0 eigene `RR` | Zweck- und Risikokontext der menschlichen Aufsicht; `supplementary` |
| `SRC-002#Art.14/Abs.3` | 2 `RR` | A14-B, A14-C |
| `SRC-002#Art.14/Abs.3/Buchst.a` | 0 eigenständige `RR` | Bestandteil der Alternativstruktur von A14-C |
| `SRC-002#Art.14/Abs.3/Buchst.b` | 0 eigenständige `RR` | Bestandteil der Alternativstruktur von A14-C |
| `SRC-002#Art.14/Abs.4` | 0 eigene `RR` | gemeinsamer Rahmen für die Buchst. a bis e; `supplementary` |
| `SRC-002#Art.14/Abs.4/Buchst.a` | 2 `RR` | A14-D, A14-E |
| `SRC-002#Art.14/Abs.4/Buchst.b` | 1 `RR` | A14-F |
| `SRC-002#Art.14/Abs.4/Buchst.c` | 1 `RR` | A14-G |
| `SRC-002#Art.14/Abs.4/Buchst.d` | 1 `RR` | A14-H |
| `SRC-002#Art.14/Abs.4/Buchst.e` | 1 `RR` | A14-I |
| `SRC-002#Art.14/Abs.5/UAbs.1` | 1 conditional `RR` | A14-J |
| `SRC-002#Art.14/Abs.5/UAbs.2` | 0 eigene `RR` | Scope- und Applicability-Ausnahme zu A14-J |

Alle operativen Fundstellen des aktuellen Art.-14-Bestands sind entschieden; es verbleibt keine Fundstelle ohne Entscheidung.

---

## 4. Kandidaten

### A14-A — Wirksame menschliche Aufsicht durch Systemgestaltung

- **Title EN:** Effective Human Oversight Through System Design
- **DE:** Der Anbieter muss sicherstellen, dass ein Hochrisiko-KI-System so konzipiert und entwickelt wird, dass es während der Dauer seiner Verwendung, einschließlich durch geeignete Instrumente einer Mensch-Maschine-Schnittstelle, von natürlichen Personen wirksam beaufsichtigt werden kann.
- **EN:** The provider shall ensure that a high-risk AI system is designed and developed so that it can be effectively overseen by natural persons during the period in which it is in use, including through appropriate human-machine interface tools.
- **Primary:** `SRC-002#Art.14/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung
- **Uncertainty:** null

**Atomizität:** Eine `RR`. Konzeption und Entwicklung zielen gemeinsam auf denselben funktionalen Systemzustand; die Instrumente der Mensch-Maschine-Schnittstelle sind eine Umsetzungsmodalität und keine eigenständige Pflicht.

**Cross-Article:** Keine Dublette zu `RR-001` oder `RR-002`.

### A14-B — Angemessenheit der Maßnahmen zur menschlichen Aufsicht

- **Title EN:** Proportionality of Human Oversight Measures
- **DE:** Der Anbieter muss sicherstellen, dass die Maßnahmen zur menschlichen Aufsicht den einschlägigen Risiken, dem Grad der Autonomie und dem Nutzungskontext des Hochrisiko-KI-Systems angemessen sind.
- **EN:** The provider shall ensure that the human oversight measures are commensurate with the relevant risks, the level of autonomy and the context of use of the high-risk AI system.
- **Primary:** `SRC-002#Art.14/Abs.3`
- **Supplementary:** `SRC-002#Art.14/Abs.2` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null

**Atomizität:** Eigenständiger Status gegenüber A14-C. Eine formal zulässige Maßnahmenart kann gleichwohl hinsichtlich Risiko, Autonomiegrad oder Nutzungskontext unangemessen sein.

### A14-C — Sicherstellung der menschlichen Aufsicht durch geeignete Maßnahmenarten

- **Title EN:** Ensuring Human Oversight Through Appropriate Types of Measures
- **DE:** Der Anbieter muss sicherstellen, dass die menschliche Aufsicht durch eine oder beide der folgenden Maßnahmenarten gewährleistet wird: vor dem Inverkehrbringen oder der Inbetriebnahme vom Anbieter bestimmte und, soweit technisch machbar, in das Hochrisiko-KI-System eingebaute Vorkehrungen oder vor diesem Zeitpunkt vom Anbieter bestimmte Vorkehrungen, die zur Umsetzung durch den Betreiber geeignet sind.
- **EN:** The provider shall ensure that human oversight is provided through either one or both of the following types of measures: measures identified by the provider before placing the high-risk AI system on the market or putting it into service and, where technically feasible, built into the system, or measures identified by the provider before that time that are appropriate to be implemented by the deployer.
- **Primary:** `SRC-002#Art.14/Abs.3` · `SRC-002#Art.14/Abs.3/Buchst.a` · `SRC-002#Art.14/Abs.3/Buchst.b`
- **Supplementary:** — (leer)
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null

**Atomizität:** Eine `RR`. Buchst. a und b sind wegen der Struktur „eine oder beide" bzw. „either one or both" **keine** zwei kumulativ erforderlichen `RR`. Die Alternativstruktur bleibt nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 6 innerhalb der `RR` erhalten und darf nicht in zwei kumulative Pflichten verfälscht werden.

### A14-D — Verständnis der Fähigkeiten und Grenzen des Systems

- **Title EN:** Understanding the System's Capabilities and Limitations
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System dem Betreiber so bereitgestellt wird, dass die mit der menschlichen Aufsicht betrauten natürlichen Personen, soweit angemessen und verhältnismäßig, die einschlägigen Fähigkeiten und Grenzen des Systems angemessen verstehen können.
- **EN:** The provider shall ensure that the high-risk AI system is provided to the deployer in such a way that natural persons assigned human oversight are enabled, as appropriate and proportionate, to properly understand the relevant capabilities and limitations of the system.
- **Primary:** `SRC-002#Art.14/Abs.4/Buchst.a`
- **Supplementary:** `SRC-002#Art.14/Abs.4` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Eigenständiger Status gegenüber A14-E.

### A14-E — Überwachung des Systembetriebs

- **Title EN:** Monitoring of System Operation
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System dem Betreiber so bereitgestellt wird, dass die mit der menschlichen Aufsicht betrauten natürlichen Personen, soweit angemessen und verhältnismäßig, seinen Betrieb ordnungsgemäß überwachen können, einschließlich zur Erkennung und Behebung von Anomalien, Fehlfunktionen und unerwarteter Leistung.
- **EN:** The provider shall ensure that the high-risk AI system is provided to the deployer in such a way that natural persons assigned human oversight are enabled, as appropriate and proportionate, to duly monitor its operation, including with a view to detecting and addressing anomalies, dysfunctions and unexpected performance.
- **Primary:** `SRC-002#Art.14/Abs.4/Buchst.a`
- **Supplementary:** `SRC-002#Art.14/Abs.4` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Erkennung und Behebung sowie die genannten Störungsarten konkretisieren dieselbe operative Monitoringfähigkeit.

**Cross-Article:** Ein Abgleich mit Art. 26 Abs. 5 war im ursprünglichen Extraktionsstand vorgemerkt. Nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.15 wurde die Deployer-Perspektive nicht aktiviert, und Art. 26 Abs. 5 ist nach Exclusion Criterion E-10 aus dem aktiven Gap-Korpus ausgeschlossen. Im aktuellen Gap-Scope erfolgt deshalb kein Art.-26-Abgleich (Abschnitt 8). A14-E bleibt materiell unverändert.

### A14-F — Bewusstsein für Automatisierungsbias

- **Title EN:** Awareness of Automation Bias
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System dem Betreiber so bereitgestellt wird, dass die mit der menschlichen Aufsicht betrauten natürlichen Personen, soweit angemessen und verhältnismäßig, sich der möglichen Neigung zu automatischem oder übermäßigem Vertrauen in die Systemausgabe bewusst bleiben können, insbesondere wenn das System Informationen oder Empfehlungen für Entscheidungen natürlicher Personen bereitstellt.
- **EN:** The provider shall ensure that the high-risk AI system is provided to the deployer in such a way that natural persons assigned human oversight are enabled, as appropriate and proportionate, to remain aware of the possible tendency to automatically rely or over-rely on the system's output, in particular where the system provides information or recommendations for decisions to be taken by natural persons.
- **Primary:** `SRC-002#Art.14/Abs.4/Buchst.b`
- **Supplementary:** `SRC-002#Art.14/Abs.4` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Eigenständiger Human-Oversight-Sollzustand.

### A14-G — Richtige Interpretation der Systemausgabe

- **Title EN:** Correct Interpretation of System Output
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System dem Betreiber so bereitgestellt wird, dass die mit der menschlichen Aufsicht betrauten natürlichen Personen, soweit angemessen und verhältnismäßig, seine Ausgabe richtig interpretieren können, wobei beispielsweise die vorhandenen Interpretationsinstrumente und -methoden zu berücksichtigen sind.
- **EN:** The provider shall ensure that the high-risk AI system is provided to the deployer in such a way that natural persons assigned human oversight are enabled, as appropriate and proportionate, to correctly interpret its output, taking into account, for example, the interpretation tools and methods available.
- **Primary:** `SRC-002#Art.14/Abs.4/Buchst.c`
- **Supplementary:** `SRC-002#Art.14/Abs.4` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Eine `RR`. Die Interpretationsinstrumente und -methoden konkretisieren den Interpretations-Sollzustand.

**Evidenznotiz:** Die frühere Formulierung „berücksichtigt werden können" wurde in der Nachadjudikation verworfen, weil sie den normativen Gehalt von „zu berücksichtigen sind" bzw. „taking into account" abschwächte. Die Atomisierung blieb dabei unverändert.

### A14-H — Möglichkeit zum Nichtverwenden oder Übersteuern der Systemausgabe

- **Title EN:** Ability Not to Use the System or to Override Its Output
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System dem Betreiber so bereitgestellt wird, dass die mit der menschlichen Aufsicht betrauten natürlichen Personen, soweit angemessen und verhältnismäßig, in einer bestimmten Situation entscheiden können, das System nicht zu verwenden oder seine Ausgabe außer Acht zu lassen, außer Kraft zu setzen oder rückgängig zu machen.
- **EN:** The provider shall ensure that the high-risk AI system is provided to the deployer in such a way that natural persons assigned human oversight are enabled, as appropriate and proportionate, in any particular situation, to decide not to use the system or otherwise to disregard, override or reverse its output.
- **Primary:** `SRC-002#Art.14/Abs.4/Buchst.d`
- **Supplementary:** `SRC-002#Art.14/Abs.4` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Die genannten Handlungsmöglichkeiten sind alternative Kontrollmöglichkeiten desselben Sollzustands.

### A14-I — Eingriff und sichere Unterbrechung des Systembetriebs

- **Title EN:** Intervention and Safe Interruption of System Operation
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System dem Betreiber so bereitgestellt wird, dass die mit der menschlichen Aufsicht betrauten natürlichen Personen, soweit angemessen und verhältnismäßig, in seinen Betrieb eingreifen oder ihn mittels einer Stopptaste oder eines vergleichbaren Verfahrens unterbrechen können, sodass das System in einem sicheren Zustand zum Stillstand kommen kann.
- **EN:** The provider shall ensure that the high-risk AI system is provided to the deployer in such a way that natural persons assigned human oversight are enabled, as appropriate and proportionate, to intervene in its operation or interrupt it through a stop button or a similar procedure that allows the system to come to a halt in a safe state.
- **Primary:** `SRC-002#Art.14/Abs.4/Buchst.e`
- **Supplementary:** `SRC-002#Art.14/Abs.4` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Atomizität:** Eingriff und Unterbrechung sind alternative Interventionswege; der sichere Zustand qualifiziert den Unterbrechungsmechanismus.

### A14-J — Zwei-Personen-Verifikation bei biometrischer Fernidentifizierung

- **Status:** conditional
- **Title EN:** Two-Person Verification for Remote Biometric Identification
- **DE:** Bei einem Hochrisiko-KI-System nach Anhang III Nummer 1 Buchstabe a muss der Anbieter sicherstellen, dass die Maßnahmen zur menschlichen Aufsicht so ausgestaltet sind, dass der Betreiber keine Handlung oder Entscheidung auf Grundlage des vom System hervorgebrachten Identifizierungsergebnisses trifft, solange diese Identifizierung nicht von mindestens zwei natürlichen Personen mit der erforderlichen Kompetenz, Ausbildung und Befugnis getrennt überprüft und bestätigt wurde; die Ausnahme nach Artikel 14 Absatz 5 Unterabsatz 2 bleibt unberührt.
- **EN:** For a high-risk AI system referred to in Annex III, point 1(a), the provider shall ensure that the human oversight measures are designed so that no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority; the exception in Article 14(5), second subparagraph, remains unaffected.
- **Primary:** `SRC-002#Art.14/Abs.5/UAbs.1`
- **Supplementary:** `SRC-002#Anh.III/Nr.1/Buchst.a` · `SRC-002#Art.14/Abs.5/UAbs.2` · `SRC-002#Art.16/Buchst.a`
- **Theme:** Menschliche Aufsicht
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null

**Trigger:** Das betrachtete Hochrisiko-KI-System fällt zusätzlich unter `SRC-002#Anh.III/Nr.1/Buchst.a` als biometrisches Fernidentifizierungssystem.

**Applicability-Ausnahme:** `SRC-002#Art.14/Abs.5/UAbs.2`. Die Ausnahme erzeugt **keine** eigene `RR`; sie begrenzt den Anwendungsbereich von A14-J.

**Atomizität:** Eine `RR`. Die separate Verifikation, die Bestätigung, die Mindestzahl von zwei Personen sowie die notwendige Kompetenz, Ausbildung und Befugnis sind kumulative Bestandteile eines einheitlichen verstärkten Human-Oversight-Schutzmechanismus.

---

## 5. Multilingualer Divergenzfall zu A14-J

Geprüft nach dem Multilingual Source Divergence Protocol in [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 9.1.

### 5.1 Feststellung

| Fassung | Befund zu `SRC-002#Art.14/Abs.5/UAbs.1` |
| --- | --- |
| DE | enthält ausdrücklich den Ausschließlichkeitsqualifier „allein aufgrund" |
| EN | kein entsprechendes „solely" |
| FR | kein entsprechender Ausschließlichkeitsqualifier |
| IT | kein entsprechender Ausschließlichkeitsqualifier |
| ES | kein entsprechender Ausschließlichkeitsqualifier |

Materielle Divergenz: **ja**.

Keine Sprachfassung wurde automatisch priorisiert oder als führend erklärt; keine Fassung wird als unzutreffend bewertet. Die Anzahl übereinstimmender Fassungen wurde **nicht** als Mehrheitsregel verwendet.

### 5.2 Adjudizierte einheitliche Bedeutung — Variante A

Keine Handlung oder Entscheidung darf auf dem vom System erzeugten Identifizierungsergebnis beruhen, solange die Identifizierung nicht separat von mindestens zwei entsprechend qualifizierten natürlichen Personen verifiziert und bestätigt wurde.

### 5.3 Begründung

- unmittelbarer mehrsprachiger Normvergleich der authentischen Fassungen;
- systematischer Kontext des Art. 14 als Regelung der materiellen menschlichen Aufsicht;
- einschlägiger Erwägungsgrund zum verstärkten Human-Oversight-Mechanismus bei biometrischer Fernidentifizierung;
- die Verwendung ausdrücklicher Ausschließlichkeitsformulierungen an anderen Stellen des Rechtsakts zeigt, dass ein solcher Qualifier gezielt ausgedrückt werden kann, wenn er gewollt ist.

### 5.4 Ergebnis

A14-J bleibt conditional aktivierbar; `uncertainty` ist `null`. Die amtliche Textdivergenz wird durch diese Adjudikation nicht als nie bestehend dargestellt, sondern bleibt in Abschnitt 5.1 dokumentiert.

---

## 6. Cross-Article-Abgleich mit Art. 13

| `RR` | Befund |
| --- | --- |
| `RR-001` | keine echte Dublette |
| `RR-002` | keine echte Dublette |
| `RR-053` | keine echte Dublette |
| `RR-056` | keine echte Dublette |
| `RR-058` | keine echte Dublette |

Besonders zu `RR-058`: Diese `RR` ist eine Informationspflicht **über** die Maßnahmen der menschlichen Aufsicht. Art. 14 normiert die materiellen Human-Oversight-Maßnahmen selbst. Die Erfüllungsstatus können unabhängig voneinander unterschiedlich sein.

Echte Duplikate: **0**. Die sachlichen Beziehungen sind damit dokumentiert, ohne dass eine Deduplizierung erfolgt.

---

## 7. Abgleich mit Art. 9

Keine echte Dublette zu den bestehenden Art.-9-`RR`.

Art. 9 regelt den allgemeinen Risikomanagementrahmen; Art. 14 regelt spezifische materielle Human-Oversight-Sollzustände. Eine rein thematische Beziehung rechtfertigt nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) und [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 5 keine Deduplizierung.

---

## 8. Art.-26-Scope-Entscheidung

### 8.1 Ursprünglicher Extraktionsstand

Zum Zeitpunkt der Extraktion war die conditional Deployer-Perspektive noch nicht entschieden. Vorgemerkt waren deshalb zwei spätere Cross-Article-Prüfungen:

| Kandidat | Vorgemerkter Abgleich |
| --- | --- |
| A14-E | Art. 26 Abs. 5 |
| A14-J | Art. 26 Abs. 2 |

Diese Vormerkung entsprach dem damaligen Entscheidungsstand. Sie war ausdrücklich kein Grund für einen zurückgestellten Status und keine dokumentierte Unsicherheit.

### 8.2 Spätere Scope-Entscheidung

Mit [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.15 (Abschnitt 10.12) wurde festgestellt:

- Core-Adressat von `SRC-002` bleibt der Anbieter bzw. Provider;
- die Deployer-Perspektive ist nicht aktiviert;
- `SRC-002#Art.26/Abs.2`, `SRC-002#Art.26/Abs.4` und `SRC-002#Art.26/Abs.5` sind nach Exclusion Criterion E-10 aus dem aktiven Gap-Korpus ausgeschlossen;
- eine Art.-26-Extraktion erfolgt nicht.

### 8.3 Aktueller Stand

Die vorgemerkten Cross-Article-Prüfungen werden im aktuellen Gap-Scope **nicht** durchgeführt.

| Merkmal | Befund |
| --- | --- |
| A14-E | unverändert |
| A14-J | unverändert |
| Deduplizierung | keine |
| Katalogänderung | keine |

Das bedeutet **nicht**, dass Art. 26 regulatorisch irrelevant wäre oder keine sachliche Beziehung zu Art. 14 hätte. Eine spätere Aktivierung der Deployer-Perspektive ist nicht ausgeschlossen, würde aber eine formelle Coverage Change Control vor jeder Art.-26-Extraktion erfordern.

---

## 9. Locator-Audit

Alle formalen Lokatoren dieser Evidenz entsprechen der Syntax aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4. Geprüft wurden die `Primary`- und `Supplementary`-Angaben aller zehn Kandidaten sowie die Trigger- und Applicability-Lokatoren von A14-J.

Ein Lokatorelement `Chapeau` wird **nicht** verwendet. Die Begriffe „Chapeau" und „gemeinsamer Rahmen" erscheinen ausschließlich in Prosa zur Beschreibung der Textfunktion.

---

## 10. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war für diesen Quellenbereich ausreichend. Eine Methodenänderung ist **nicht** erforderlich.

Die Methode deckte insbesondere ab:

- Zweckbestimmung gegenüber eigenständiger `RR`,
- Proportionalitätsanforderung,
- Alternativstruktur „eine oder beide",
- Struktur aus gemeinsamem Rahmen und Unterpflichten,
- atomare Human-Oversight-Fähigkeiten,
- conditional Applicability,
- Cross-Article-Deduplizierung,
- multilinguale Divergenz.

Es wurde **keine** Art.-14-Sonderregel eingeführt.

---

## 11. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | angewandte Extraktions-, Atomizitäts- und Source-Fidelity-Methode (Version 1.2) |
| [COVERAGE_PLAN.md](COVERAGE_PLAN.md) | Freigabe des Quellenbereichs und Bearbeitungsstatus (Version 1.5) |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | führende Vergabestelle; hier nicht verändert |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |
| [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | Identifikatoren und Lokator-Syntax |
| [RR_EXTRACTION_ART13.md](RR_EXTRACTION_ART13.md) | Herkunft der im Cross-Article-Abgleich geprüften Art.-13-`RR` |
| [RR_EXTRACTION_ART9.md](RR_EXTRACTION_ART9.md) | Herkunft der im Abgleich geprüften Art.-9-`RR` |

---

## 12. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-002` Art. 14; 10 Kandidaten A14-A bis A14-J, davon 9 regulär aktivierbar und A14-J conditional; 0 unresolved, 0 deferred; A14-G nach Source-Fidelity-Prüfung korrigiert; multilingualer Divergenzfall zu A14-J nach Methode Version 1.2 adjudiziert. Keine Identifikatorvergabe. |
| 1.1 | Scope-Konsistenz nach der in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.15 dokumentierten Nichtaktivierung der Deployer-Perspektive: Die ursprünglich vorgemerkten Abgleiche A14-E ↔ Art. 26 Abs. 5 und A14-J ↔ Art. 26 Abs. 2 entfallen im aktuellen Gap-Scope. Keine materielle Änderung der zehn Art.-14-Kandidaten, ihrer normativen Inhalte, Lokatoren, Klassifikationen oder Katalogintegration. |
