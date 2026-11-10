# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 22.1 bis Nr. 22.3

Version 1.1 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.22.1` bis `SRC-001#Anh.I/Nr.22.3` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Ergänzungsbereich, Priorität `Ergänzend, conditional` |
| Coverage-Trigger | vorgesehene Laienanwendung |
| Expected Theme | Gebrauchstauglichkeit |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.29 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M22_1-A` bis `M22_3-B` sind ausschließlich temporäre Evidenzkennungen. Die permanenten Identifikatoren `RR-174` bis `RR-182` sind ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.18 vergeben; der Statusabschluss ist in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.30 Abschnitt 10.20 dokumentiert.

**Grundlage** sind zwei abgeschlossene Research-Berichte:

| Bezeichnung | Inhalt |
| --- | --- |
| Research-Bericht A | ursprüngliche vollständige `0 / 1 / n`-Extraktion von Nr. 22.1 bis Nr. 22.3 |
| Research-Bericht B | gezielte Nachadjudikation der Lebenszyklusphasen von `M22_1-A` bis `M22_1-C`, ihrer Konsistenzwirkung auf `M22_2-A` bis `M22_3-B` sowie der Locator-Frage |

Bei Lebenszyklus und Locator haben die Entscheidungen aus Bericht B Vorrang vor den früheren Werten aus Bericht A (Abschnitt 15). Atomisierung, Themes, Conditionality, Source Fidelity und Deduplizierung wurden durch Bericht B nicht neu geöffnet.

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Geprüfte normative Kandidatenatome | **10** |
| Neue MDR-Gap-`RR`-Kandidaten | **9** — `M22_1-A` bis `M22_3-B` |
| davon outer conditional (vorgesehene Laienanwendung) | 9 |
| davon zusätzlich inner conditional | 3 — `M22_2-D`, `M22_3-A`, `M22_3-B` |
| 0-`RR` / Out-of-Scope-Atome | 1 |
| MDR-intern vollständig deduplizierte Atome | 0 |
| Unresolved | 0 |
| Deferred | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

Die zehn geprüften Atome verteilen sich auf: 1 aus dem ersten und 2 aus dem zweiten grammatischen Satz von Nr. 22.1, 2 aus dem ersten, 1 aus dem zweiten und 2 aus dem dritten Spiegelstrich von Nr. 22.2 sowie 2 aus Nr. 22.3.

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 9 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Source Verification

**Ergebnis `SRC-001`: PASS.**

| Merkmal | Befund |
| --- | --- |
| Verwendete Fassung | ausschließlich die konsolidierte MDR-Fassung `02017R0745-20260719`, Stand 19.07.2026 |
| Primär geprüft | DE und EN |
| Gezielt ergänzend geprüft | FR desselben Rechtsstands, weil bei zwei Formulierungen eine DE/EN-Divergenz prüfungsrelevant ist |
| Vollständigkeit | Die EUR-Lex-Fassung enthält Nr. 22.1 bis Nr. 22.3 vollständig. Die englische Fassung bestätigt insbesondere `skills and means available`, `safely and accurately`, `if applicable` und `where appropriate`. |

### 3.1 Multilingualer Befund

| Stelle | DE | EN | FR | Befund |
| --- | --- | --- | --- | --- |
| Nr. 22.1 | Fertigkeiten und Möglichkeiten | `skills and means available` | `aptitudes et moyens` | keine materielle Divergenz für Atomisierung oder Applicability |
| Nr. 22.2, erster Spiegelstrich | sicher und fehlerfrei | `safely and accurately` | `correctement et en toute sécurité` | relevante lexikalische Divergenz (Abschnitt 3.2) |
| Nr. 22.3 | soweit angemessen / gegebenenfalls | `where appropriate` / `if applicable` | — | keine atomizitätsrelevante Divergenz festgestellt |

Die Requirement Texte von `M22_1-A` verwenden die Paraphrase „Fähigkeiten und Möglichkeiten der Laien" bzw. `lay persons' skills and available means`; nach dem Befund oben entsteht daraus keine materielle Abweichung.

### 3.2 Divergenz „fehlerfrei" / `accurately` / `correctement`

| Merkmal | Ergebnis |
| --- | --- |
| Betroffener Kandidat | `M22_2-B` |
| Materielle Divergenz | lexikalisch relevant |
| Status | adjudiziert |
| Unresolved | 0 |

**Warum kein Unresolved entsteht:** Für die Atomisierung ist die Divergenz auflösbar, weil alle drei Fassungen zwei kumulative Qualitätsdimensionen erkennen lassen: sichere Nutzung sowie eine zusätzliche Korrektheits- bzw. Genauigkeitsdimension. Die Split-Entscheidung zwischen `M22_2-A` und `M22_2-B` hängt damit nicht von der Wahl einer Sprachfassung ab.

**Source Fidelity:** Die deutsche und die englische Paraphrase dürfen diese Begriffe nicht künstlich auf einen einheitlichen stärkeren Begriff reduzieren. Der deutsche Requirement Text verwendet deshalb „fehlerfrei", der englische `accurately`. Es wurde keine Mehrheitsregel angewendet und keine Sprachfassung priorisiert ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 9.1).

**Vorbehalt für spätere Arbeitsschritte:** Die Divergenz darf bei einer späteren Operationalisierung von Prüfkriterien nicht stillschweigend vereinheitlicht werden. Für die aktuelle `RR`-Extraktion erzeugt sie kein Unresolved.

### 3.3 Gemeinsamer äußerer Anwendungsbereich

Der gemeinsame äußere Anwendungsbereich von Nr. 22 ist **keine** eigene Gap-Anforderung. Er bestimmt, **wann** sämtliche nachfolgenden Pflichten gelten: Der Hersteller sieht die Anwendung des Produkts durch Laien vor (Abschnitt 8).

---

## 4. Quellenstruktur und Locator-Entscheidung

### 4.1 Struktur

| Fundstelle | Struktur | Atome | Kandidaten |
| --- | --- | --- | --- |
| `SRC-001#Anh.I/Nr.22.1` | zwei grammatisch klar getrennte Sätze: (1) Auslegung und Herstellung unter Berücksichtigung der Laienmerkmale und Nutzungsschwankungen; (2) Qualitätsmaßstab für die beigefügten Angaben und Anweisungen | 3 | `M22_1-A` (Satz 1); `M22_1-B`, `M22_1-C` (Satz 2) |
| `SRC-001#Anh.I/Nr.22.2` | gemeinsamer Satzrahmen (Produkte zur Laienanwendung entsprechend auszulegen und herzustellen) mit drei Spiegelstrichen, die unterschiedliche Sollzustände enthalten | 5 | `M22_2-A`, `M22_2-B` (Spiegelstrich 1); Out-of-Scope-Atom (Spiegelstrich 2); `M22_2-C`, `M22_2-D` (Spiegelstrich 3) |
| `SRC-001#Anh.I/Nr.22.3` | ein Verfahren „soweit angemessen" mit zwei Funktionen: Kontrolle der vorgesehenen Funktion bei der Anwendung; gegebenenfalls Warnung bei ungültigem Ergebnis | 2 | `M22_3-A`, `M22_3-B` |

### 4.2 Locator-Entscheidung (final nach Research-Bericht B)

| Kandidaten | Primary | Supplementary |
| --- | --- | --- |
| `M22_1-A`, `M22_1-B`, `M22_1-C` | `SRC-001#Anh.I/Nr.22.1` | keine |
| `M22_2-A`, `M22_2-B`, `M22_2-C`, `M22_2-D` | `SRC-001#Anh.I/Nr.22.2` | keine |
| `M22_3-A`, `M22_3-B` | `SRC-001#Anh.I/Nr.22.3` | keine |

**Begründung zu Nr. 22.1:**

- Regulatorisch ist die Satzgrenze in Nr. 22.1 inhaltlich eindeutig: Der erste Satz betrifft Auslegung und Herstellung sowie Laienmerkmale und Nutzungsschwankungen, der zweite Satz Verständlichkeit und Anwendbarkeit der Herstellerinformationen.
- EUR-Lex stellt Nr. 22.1 jedoch als eine einzige nummerierte Untergliederung `22.1.` dar; die beiden Sätze besitzen im Rechtsakt **keine amtlichen eigenen Satznummern**.
- `/Satz.1` und `/Satz.2` wären sprachlich nachvollziehbare analytische Feingranularitäten, sollen aber nicht allein aus der Struktur des EUR-Lex-Textes als amtliche Quellenhierarchie behandelt werden. Der Locator auf Nummernebene ist die methodisch konservativere und quellentreuere Wahl.
- Das entspricht dem Minimalitätsprinzip der Extraktionsmethode ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8): so präzise wie erforderlich, ohne eine nicht gesicherte Quellenhierarchie zu erzeugen.
- Die Evidenz hält fest, dass `M22_1-A` aus dem ersten und `M22_1-B` sowie `M22_1-C` aus dem zweiten grammatischen Satz extrahiert wurden (Abschnitt 4.1).

**Begründung zu Nr. 22.2 und Nr. 22.3:** Für die Spiegelstriche wird bewusst der jeweilige Nummern-Locator als Primary verwendet. Ohne verifizierten kontrollierten Locator-Typ für einzelne Spiegelstriche wird keine Syntax wie `/Spiegelstrich.1` erfunden; das Elementvokabular in [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4 enthält kein Spiegelstrich-Element.

**Repository-Hinweis (keine Adjudikation):** Das Element `Satz.` ist in [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4 als zulässiges Lokator-Element definiert und wird in anderen Extraktionen für Anhang-I-Nummern verwendet, z. B. `SRC-001#Anh.I/Nr.3/Satz.1`, `SRC-001#Anh.I/Nr.4/Satz.1` und `SRC-001#Anh.I/Nr.17.1/Satz.1`. Die hier adjudizierte Locator-Entscheidung bleibt davon unberührt. Eine projektweite Abstimmung der `Satz.`-Verwendung ist nicht Gegenstand dieser Evidenz.

---

## 5. Vollständige `0 / 1 / n`-Prüfung

| Nr. | Normatives Kandidatenatom | Ergebnis | Kandidat |
| --- | --- | --- | --- |
| 1 | Nr. 22.1, Satz 1 — Auslegung und Herstellung zur zweckbestimmungsgemäßen Funktion unter Berücksichtigung der Fähigkeiten und Möglichkeiten der Laien sowie vorhersehbarer Schwankungen ihrer Verfahrensweise und Umgebung | 1 `RR` | `M22_1-A` |
| 2 | Nr. 22.1, Satz 2 — leichte Verständlichkeit der Herstellerangaben und -anweisungen für Laien | 1 `RR` | `M22_1-B` |
| 3 | Nr. 22.1, Satz 2 — leichte Anwendbarkeit der Herstellerangaben und -anweisungen für Laien | 1 `RR` | `M22_1-C` |
| 4 | Nr. 22.2, Spiegelstrich 1 — sichere Verwendung durch den vorgesehenen Anwender in allen Bedienungsphasen | 1 `RR` | `M22_2-A` |
| 5 | Nr. 22.2, Spiegelstrich 1 — fehlerfreie bzw. accurate Verwendung durch den vorgesehenen Anwender in allen Bedienungsphasen | 1 `RR` | `M22_2-B` |
| 6 | Nr. 22.2, Spiegelstrich 2 — Verringerung des Risikos unbeabsichtigter Schnitt- und Stichverletzungen wie Nadelstichverletzungen | 0 `RR` — OUT-OF-SCOPE | — |
| 7 | Nr. 22.2, Spiegelstrich 3 — Minimierung des Risikos falscher Handhabung | 1 `RR` | `M22_2-C` |
| 8 | Nr. 22.2, Spiegelstrich 3 — Minimierung des Risikos falscher Interpretation der Ergebnisse | 1 `RR` | `M22_2-D` |
| 9 | Nr. 22.3 — Verfahren zur Kontrolle der bestimmungsgemäßen Funktion bei der Anwendung | 1 `RR` | `M22_3-A` |
| 10 | Nr. 22.3 — Verfahren zur Warnung bei fehlendem gültigem Ergebnis | 1 `RR` | `M22_3-B` |
| | **Gesamt** | **9 `RR`, 1 Out-of-Scope** | |

---

## 6. Atomisierung und Split-Begründungen

Grundlage ist der Split-Test aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 4: Getrennt wird nur, wenn (1) die Erfüllungsstatus unabhängig voneinander unterschiedlich sein können und (2) jeder Bestandteil für sich eine vollständige, regulatorisch sinnvolle Compliance-Aussage bildet.

### 6.1 Nr. 22.1, Satz 1 — `M22_1-A`

Die Norm verbindet einen einzigen Produktsollzustand mit mehreren zu berücksichtigenden Faktoren: Das für Laien bestimmte Produkt soll seine Zweckbestimmung erfüllen können; dabei sind Fähigkeiten und Möglichkeiten der Laien sowie vorhersehbare Schwankungen ihrer Verfahrensweise und Umgebung einzubeziehen.

**Finale Atomisierung: 1 `RR`.**

**Keine Mikroatomisierung** nach Fähigkeiten, Möglichkeiten, Verfahrensweise und Umgebung:

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | kann faktisch unterschiedlich ausfallen |
| Split-Bedingung 2 | nicht erfüllt |

Diese Elemente definieren gemeinsam den spezifischen Laien-Nutzungs- und Nutzungskontext des einen Auslegungs- und Herstellungssollzustands. Eine `RR` je Faktor wäre dieselbe Mikroatomisierung, die bei `RR-164` bereits vermieden wurde.

### 6.2 Nr. 22.1, Satz 2 — `M22_1-B` und `M22_1-C`

Die Herstellerinformationen und -anweisungen müssen für Laien einerseits leicht verständlich und andererseits leicht anwendbar sein.

**Beide Split-Bedingungen sind erfüllt:**

1. Eine Anleitung kann verständlich formuliert sein, aber praktisch nicht ohne Schwierigkeiten anwendbar sein; umgekehrt kann eine Handlung einfach ausführbar sein, obwohl die Beschreibung schwer verständlich ist.
2. Beide Aussagen bilden eigenständig vollständige regulatorische Sollzustände: leichte Verständlichkeit und leichte Anwendbarkeit.

Die Trennung verändert das kumulative „und" nicht; beide Anforderungen bleiben zu erfüllen.

**Finale Atomisierung: 2 `RR`.**

### 6.3 Theme-Begründung Nr. 22.1

Theme für `M22_1-A`, `M22_1-B` und `M22_1-C`: **`Gebrauchstauglichkeit`**.

Bei `M22_1-B` und `M22_1-C` ist `Transparenz` nicht der primäre Gegenstand: Nr. 22.1 verlangt keine neue Informationskategorie, sondern die nutzerbezogene Qualität vorhandener Informationen und Anweisungen. Das entspricht der Abgrenzung in [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 1.8: Welche Information bereitgestellt werden muss, ist `Transparenz`; wie sie erfassbar und fehlerarm dargeboten wird, ist `Gebrauchstauglichkeit`.

### 6.4 Nr. 22.2, Spiegelstrich 1 — `M22_2-A` und `M22_2-B`

**Finale Atomisierung: 2 `RR`** — sichere Verwendung (`M22_2-A`) und fehlerfreie bzw. accurate Verwendung (`M22_2-B`).

**Beide Split-Bedingungen sind erfüllt.** Sichere Verwendung und fehlerfreie bzw. genaue Verwendung können voneinander abweichende Compliance-Status besitzen. Ein System kann beispielsweise ohne unmittelbares Sicherheitsrisiko bedienbar sein und dennoch relevante Bedienfehler ermöglichen. Umgekehrt ist fehlerarme Bedienung allein keine vollständige Aussage über sichere Nutzung. Die MDR stellt beide Anforderungen kumulativ nebeneinander.

**„in allen Bedienungsphasen" / `at all stages of the procedure`:** wird **nicht** separat atomisiert. Die Wendung bestimmt den Umfang beider Pflichten und ist keine eigene `RR`.

**„erforderlichenfalls nach angemessener Schulung und/oder Aufklärung" / `if necessary after appropriate training and/or information`:** ist **kein** Inner Trigger der beiden Hauptpflichten. Die sichere und die fehlerfreie bzw. genaue Verwendbarkeit gelten unabhängig davon. Die Wendung beschreibt eine zulässige bzw. erforderliche Modalität, falls Schulung oder Information hierfür benötigt wird. Aus Nr. 22.2 wird **keine** zusätzliche selbständige Schulungs-`RR` erzeugt.

### 6.5 Nr. 22.2, Spiegelstrich 3 — `M22_2-C` und `M22_2-D`

**Finale Atomisierung: 2 `RR`** — Risiko falscher Handhabung (`M22_2-C`) und Risiko falscher Interpretation der Ergebnisse (`M22_2-D`).

**Der Split ist zwingend:** Die Erfüllungsstatus können unabhängig voneinander abweichen, beide bilden vollständige regulatorische Compliance-Aussagen, und nur die Ergebnisinterpretation besitzt das zusätzliche „gegebenenfalls" / `if applicable`.

**Warum nur `M22_2-D` inner conditional ist:** Die Einschränkung „gegebenenfalls" / `if applicable` bezieht sich ausschließlich auf die Interpretation der Ergebnisse. Für `M22_2-C` besteht deshalb keine innere Conditionality. Für `M22_2-D` lautet der Inner Trigger: Die Interpretation von Ergebnissen durch den vorgesehenen Anwender ist im konkreten Produktkontext einschlägig.

„so gering wie möglich" / `as far as possible` bleibt bei beiden eine Modalität des Reduktionsgrads.

### 6.6 Nr. 22.3 — `M22_3-A` und `M22_3-B`

Nr. 22.3 verlangt „soweit angemessen" / `where appropriate` ein Verfahren, mit dem der Laie erstens die vorgesehene Funktion bei der Anwendung kontrollieren kann und zweitens gegebenenfalls bei einem ungültigen Ergebnis gewarnt wird.

**„soweit angemessen" / `where appropriate` ist echte innere Conditionality:** Die Wendung ist nicht lediglich eine Intensitätsmodalität, sondern entscheidet, ob die Pflicht zum Vorsehen des Verfahrens überhaupt greift.

**Keine weitergehenden Kriterien für „angemessen":** Die MDR definiert an dieser Stelle keine weitergehenden Entscheidungskriterien dafür, wann „angemessen" vorliegt. Solche Kriterien dürfen in dieser Extraktion nicht erfunden werden.

**Finale Atomisierung: 2 `RR`.** Beide Split-Bedingungen sind erfüllt: Ein Produkt kann eine Prüfmöglichkeit besitzen, ohne den Nutzer bei einem ungültigen Ergebnis zu warnen. Umgekehrt bildet die Warnfunktion einen eigenständig prüfbaren Sollzustand.

**Keine Verschmelzung bei `M22_3-B`:** Für `M22_3-B` gelten zwei Bedingungen: Trigger 1 „soweit angemessen" / `where appropriate` für das Verfahren und zusätzlich Trigger 2 „gegebenenfalls" / `if applicable` hinsichtlich der Warnfunktion. Trigger 1 betrifft das Vorsehen des Verfahrens, Trigger 2 zusätzlich die Warnfunktion. Das zweite `if applicable` wird deshalb nicht mit dem übergeordneten `where appropriate` verschmolzen.

---

## 7. Scope-Entscheidung — Out-of-Scope-Atom

| Merkmal | Ergebnis |
| --- | --- |
| Fundstelle | `SRC-001#Anh.I/Nr.22.2`, Spiegelstrich 2 zu unbeabsichtigtem Schneiden oder Stechen wie Nadelstichverletzungen |
| Ergebnis | 0 `RR` — OUT-OF-SCOPE |
| Grundlage | adjudizierte Scope-Entscheidung zum horizontalen Untersuchungsgegenstand KI-basierter Medizinproduktesoftware; eine Zuordnung zu einem einzelnen Exclusion Criterion ist in der Adjudikation nicht festgelegt |

**Normativer Befund:** Der Wortlaut enthält grundsätzlich einen eigenständigen regulatorischen Sollzustand: Entsprechende physische Verletzungsrisiken sind so weit wie möglich und angemessen zu verringern. „so weit wie möglich und angemessen" / `as far as possible and appropriate` ist dabei eine Modalität des geforderten Risikoreduktionsgrads, kein eigenständiger Trigger.

**Begründung der Scope-Entscheidung:** Schneiden, Stechen und Nadelstichverletzungen sind physische, hardwaregebundene Verletzungsmechanismen. Sie besitzen keinen horizontalen systematischen Beitrag zur Gap-Analyse einer Medizinproduktesoftware als solcher.

**Ausdrückliche Klarstellung:** Dies ist **keine** Aussage, dass die Pflicht für jedes Produkt mit Software rechtlich irrelevant wäre. Bei einem hardwarebezogenen Produkt, z. B. einem softwaregesteuerten Injektionssystem, kann sie produktbezogen relevant sein; sie gehört dann aber zu einer hardware- bzw. produktspezifischen Analyse und nicht in den hier definierten horizontalen Softwarekorpus.

---

## 8. Conditionality

### 8.1 Übersicht

| Kandidat | Outer Conditional | Outer Trigger | Inner Conditional | Inner Trigger | Modalität |
| --- | --- | --- | --- | --- | --- |
| `M22_1-A` | JA | vorgesehene Laienanwendung | NEIN | — | vorhersehbare Schwankungen bestimmen den Umfang des zu berücksichtigenden Kontexts |
| `M22_1-B` | JA | vorgesehene Laienanwendung | NEIN | — | — |
| `M22_1-C` | JA | vorgesehene Laienanwendung | NEIN | — | — |
| `M22_2-A` | JA | vorgesehene Laienanwendung | NEIN | — | erforderlichenfalls nach angemessener Schulung und/oder Aufklärung |
| `M22_2-B` | JA | vorgesehene Laienanwendung | NEIN | — | erforderlichenfalls nach angemessener Schulung und/oder Aufklärung |
| `M22_2-C` | JA | vorgesehene Laienanwendung | NEIN | — | Risiko so gering wie möglich |
| `M22_2-D` | JA | vorgesehene Laienanwendung | JA | Interpretation von Ergebnissen ist im konkreten Produktkontext einschlägig | Risiko so gering wie möglich |
| `M22_3-A` | JA | vorgesehene Laienanwendung | JA | Vorsehen des Verfahrens ist „soweit angemessen" | — |
| `M22_3-B` | JA | vorgesehene Laienanwendung | JA | 1. Verfahren ist „soweit angemessen" vorzusehen. 2. Warnfunktion ist zusätzlich „gegebenenfalls" einschlägig. | — |

### 8.2 Begriffe

- **Outer Conditional:** äußerer Anwendbarkeitsvorbehalt des gesamten Quellenbereichs (Abschnitt 3.3). Er entspricht dem Coverage-Trigger „vorgesehene Laienanwendung" in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 9.1 und gilt für alle 9 Kandidaten.
- **Inner Conditional:** zusätzliche Bedingung einer einzelnen Anforderung innerhalb des Quellenbereichs, von der abhängt, ob die Pflicht überhaupt greift.
- **Modalität:** Art, Umfang bzw. Maß der Pflichterfüllung derselben Pflicht; keine Bedingung und kein Split-Grund ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 6).

### 8.3 Abbildung im Katalog

[RR_CATALOG.yaml](RR_CATALOG.yaml) besitzt für Outer Conditional, Inner Conditional und Modalität **keine** eigenen Schemafelder. Es wurden keine neuen Felder eingeführt. Die Abbildung folgt den bisherigen conditional Anforderungen des Katalogs:

- Inner Conditional und Modalität sind im jeweiligen `requirement_text` erhalten („Soweit die Ergebnisinterpretation einschlägig ist", „Soweit angemessen", „Soweit angemessen und gegebenenfalls", „erforderlichenfalls nach angemessener Schulung und/oder Aufklärung", „so gering wie möglich").
- Der Laienbezug ist in den Requirement Texten von `M22_1-A` bis `M22_1-C` sowie `M22_3-A` und `M22_3-B` ausdrücklich enthalten. Bei `M22_2-A` bis `M22_2-D` bezeichnen die adjudizierten Requirement Texte den vorgesehenen Anwender; der äußere Laienvorbehalt ergibt sich für diese Kandidaten aus dem gemeinsamen Satzrahmen von Nr. 22.2, dem Primary Locator innerhalb von Nr. 22 und dem Coverage-Trigger.
- Die vollständige Trennung von Outer Conditional, Inner Conditional und Modalität ist ausschließlich in dieser Evidenzdatei geführt.

---

## 9. Source-Fidelity-Entscheidungen

- Die Divergenz „fehlerfrei" / `accurately` / `correctement` bleibt nach Abschnitt 3.2 erhalten; keine Vereinheitlichung auf einen stärkeren gemeinsamen Begriff.
- Die normativen Qualifikationen bleiben in beiden Sprachfassungen erhalten: „so gering wie möglich" / `as far as possible`, „soweit angemessen" / `where appropriate`, „gegebenenfalls" / `if applicable`, „erforderlichenfalls" / `if necessary`.
- Die normative Stärke wurde nicht verändert; es wurden keine Inhalte ergänzt.
- Für „angemessen" in Nr. 22.3 wurden keine Entscheidungskriterien ergänzt (Abschnitt 6.6).
- Es wurden keine Inhalte aus IEC 62366-1 (`SRC-008`), anderen Normen oder Kandidaten des Standards-Landscape-Audits (Entwicklungsarchiv; nicht im Abgabepaket) übernommen.

---

## 10. Theme und Lebenszyklus

### 10.1 Finale Zuordnung

| Kandidat | Themencluster | Lebenszyklusphasen (final) |
| --- | --- | --- |
| `M22_1-A` | Gebrauchstauglichkeit | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung |
| `M22_1-B` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung |
| `M22_1-C` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung |
| `M22_2-A` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung |
| `M22_2-B` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung |
| `M22_2-C` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung |
| `M22_2-D` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung |
| `M22_3-A` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung |
| `M22_3-B` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung |

| Phase | Anzahl Kandidaten |
| --- | --- |
| Planung und Konzeption | 1 |
| Entwicklung und Realisierung | 9 |
| Inverkehrbringen, Inbetriebnahme und Betrieb | 2 |
| Änderung und Wartung | 9 |
| Verifikation und Validierung, Konformitätsbewertung, Post-Market-Überwachung | 0 |

Je Kandidat genau ein Themencluster; keine Mehrfachzuordnung und keine neue Taxonomie. Alle Lebenszykluswerte stammen aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 3; ein Sammelwert wurde nicht verwendet.

**Grundsatz:** Die Lifecycle-Zuordnung ist eine projektmethodische Adjudikation, nicht zusätzlicher MDR-Wortlaut. Bei den Design- und Herstellungsanforderungen wird der spätere Zeitpunkt der Nutzung nicht mit der Phase der Herstellerpflicht verwechselt. Lebenszyklusphasen werden nach der tatsächlichen Geltung bzw. Erfüllung der konkreten Verpflichtung vergeben; mehrere Phasen sind zulässig ([CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 4).

### 10.2 Nachadjudikation `M22_1-A`

**Entscheidung zu `Planung und Konzeption`: JA.**

- Nr. 22.1 verlangt nicht lediglich einen nachträglich zu überprüfenden Produkteffekt. Bereits die **Auslegung und Herstellung** muss so erfolgen, dass die Zweckbestimmung unter Berücksichtigung der Fähigkeiten und Möglichkeiten der Laien sowie der vorhersehbaren Schwankungen ihrer Verfahrensweise und Umgebung erfüllt werden kann.
- Gerade diese zu berücksichtigenden Merkmale sind nach dem kontrollierten Lifecycle-Modell grundlegende Nutzungsannahmen vor der technischen Realisierung. Welche Fähigkeiten die vorgesehenen Laien besitzen, welche Mittel ihnen zur Verfügung stehen und welche vorhersehbaren Nutzungsschwankungen zu berücksichtigen sind, muss konzeptionell festgelegt werden, bevor diese Annahmen in die technische Auslegung umgesetzt werden können. `Planung und Konzeption` ist hier deshalb nicht bloß vorbereitende Projektorganisation, sondern eine tatsächliche Erfüllungsphase des geforderten Berücksichtigungssollzustands.
- `Entwicklung und Realisierung` bleibt zwingend, weil der MDR-Wortlaut ausdrücklich die Auslegung und Herstellung adressiert.
- `Änderung und Wartung` bleibt sachgerecht: Wird ein bestehendes System geändert und dadurch seine Auslegung erneut berührt, muss derselbe laienbezogene Sollzustand bei dieser Änderung gewahrt werden.

**Konsistenz zu `RR-164`: PASS.** `RR-164` und `M22_1-A` sind regulatorisch nicht identisch, besitzen für die Lifecycle-Frage aber denselben relevanten Strukturtyp: Beide verlangen, dass spezifische Merkmale der vorgesehenen Nutzer bzw. ihres Nutzungskontexts bei der Produktauslegung berücksichtigt werden. Nr. 5 Buchst. b nennt technische Kenntnisse, Erfahrung, Aus- und Weiterbildung, Anwendungsumgebung sowie gesundheitliche und körperliche Verfassung; Nr. 22.1 nennt speziell für Laien Fähigkeiten und Möglichkeiten sowie vorhersehbare Schwankungen von Verfahrensweise und Umgebung. Die Ergänzung von `Planung und Konzeption` bei `M22_1-A` beseitigt eine vorherige Lifecycle-Inkonsistenz, ohne die beiden Anforderungen inhaltlich gleichzusetzen.

### 10.3 Nachadjudikation `M22_1-B`

Sollzustand: Die vom Hersteller **beigefügten** Angaben und Anweisungen müssen für den Laien leicht verständlich sein.

| Phase | Entscheidung | Begründung |
| --- | --- | --- |
| Planung und Konzeption | NEIN | Nutzerannahmen können in die Planung einfließen, aber `M22_1-B` verlangt keinen eigenständigen Planungs- oder Konzeptionssollzustand. Die Verständlichkeit selbst wird dadurch noch nicht hergestellt. |
| Entwicklung und Realisierung | JA | Der Sollzustand „leicht verständlich" muss bei Erstellung, sprachlicher Gestaltung und nutzerorientierter Ausarbeitung der Angaben und Anweisungen tatsächlich erzeugt werden. |
| Inverkehrbringen, Inbetriebnahme und Betrieb | JA | Nicht weil der Nutzer die Information dort lediglich liest, sondern weil die MDR die Qualität gerade der vom Hersteller beigefügten bzw. bereitgestellten Angaben verlangt. Der verständliche Informationsgegenstand muss beim Übergang zum Nutzer in dieser Qualität vorliegen. |
| Änderung und Wartung | JA | Werden Angaben oder Anweisungen später geändert oder aktualisiert, muss derselbe Verständlichkeitssollzustand für die geänderte Fassung erneut eingehalten werden. |
| andere Phasen | NEIN | Insbesondere keine automatische `Verifikation und Validierung` oder `Konformitätsbewertung`; Nr. 22.1 verlangt an dieser Stelle keine eigenständige Verifikations-, Validierungs- oder Bewertungsaktivität. |

Der frühere alleinige Wert `Inverkehrbringen, Inbetriebnahme und Betrieb` (Abschnitt 15) war zu eng: Er erfasste den Zeitpunkt, zu dem der Informationsgegenstand beim Nutzer vorliegen muss, aber nicht die Phase, in der seine geforderte Verständlichkeit tatsächlich erzeugt wird.

### 10.4 Nachadjudikation `M22_1-C`

Sollzustand: die leichte **Anwendbarkeit** der vom Hersteller beigefügten Angaben und Anweisungen. Die Quelle fordert Verständlichkeit und Anwendbarkeit gemeinsam; die Atomisierung trennt beide Qualitätsmerkmale (Abschnitt 6.2).

| Phase | Entscheidung | Begründung |
| --- | --- | --- |
| Planung und Konzeption | NEIN | Nutzungskontext und Laienprofil sind notwendige Entwicklungsinputs; der atomare Sollzustand von `M22_1-C` ist aber die Anwendbarkeit der Information selbst, nicht die vorgelagerte Festlegung dieser Annahmen. |
| Entwicklung und Realisierung | JA | Die Information bzw. Anleitung muss so erstellt und gestaltet werden, dass sie vom Laien praktisch angewendet werden kann; hier wird der regulatorische Sollzustand hergestellt. |
| Inverkehrbringen, Inbetriebnahme und Betrieb | JA | Der Sollzustand betrifft die tatsächlich beigefügte Information. Sie muss in anwendbarer Form beim vorgesehenen Nutzer ankommen; die Phase wird nicht bloß aufgrund des späteren Lesens vergeben. |
| Änderung und Wartung | JA | Bei einer späteren Überarbeitung der Informationen muss deren leichte Anwendbarkeit erhalten bzw. erneut hergestellt werden. |
| andere Phasen | NEIN | Keine eigenständige Grundlage für Verifikation und Validierung, Konformitätsbewertung oder Post-Market-Überwachung. |

`M22_1-B` und `M22_1-C` erhalten damit aus demselben regulatorischen Strukturgrund dieselben Lebenszyklusphasen. Das ist keine mechanische Gleichsetzung, sondern folgt daraus, dass beide unterschiedliche Qualitätsmerkmale desselben Informationsgegenstands betreffen.

### 10.5 `M22_2-A` bis `M22_3-B` — keine Änderung

**Änderung erforderlich: NEIN.** Alle sechs Kandidaten behalten `Entwicklung und Realisierung` sowie `Änderung und Wartung`.

**Kein Konsistenzfehler durch `M22_1-A`:** Entscheidend ist der spezifische normative Gegenstand von `M22_1-A`: Dort schreibt Nr. 22.1 ausdrücklich die Berücksichtigung bestimmter Nutzer- und Nutzungskontextannahmen bei Auslegung und Herstellung vor. Nr. 22.2 formuliert demgegenüber konkrete Design-Ergebniszustände, etwa sichere bzw. fehlerfreie Nutzung und Verringerung von Handhabungs- bzw. Interpretationsfehlern. Nr. 22.3 verlangt konkrete produktseitige Prüf- und Warnverfahren. Dass diese Anforderungen in einer realen Produktentwicklung bereits in einer frühen Designplanung berücksichtigt werden können oder sollten, genügt nach der Projektmethodik nicht, um automatisch die Phase `Planung und Konzeption` hinzuzufügen; sonst würde nahezu jede Designanforderung zusätzlich zur Planungsphase erklärt.

**Kein Konsistenzfehler durch `M22_1-B` und `M22_1-C`:** Die Ergänzung der Informationsanforderungen um `Inverkehrbringen, Inbetriebnahme und Betrieb` führt nicht zu einer entsprechenden Erweiterung von `M22_3-A` und `M22_3-B`. Dort wird die Prüf- bzw. Warnfunktion während der Anwendung genutzt; der Hersteller erfüllt die atomare Produktanforderung aber durch das Vorsehen des entsprechenden Verfahrens im Produkt. Der Zeitpunkt der Nutzung des Features ist nicht automatisch eine zusätzliche Erfüllungsphase der Herstellerpflicht.

---

## 11. MDR-interne Deduplizierung gegen `RR-163` und `RR-164`

Der in [RR_EXTRACTION_MDR_ANNEXI_5.md](RR_EXTRACTION_MDR_ANNEXI_5.md) Abschnitt 8 und [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 10.16 vorgemerkte Abgleich ist hiermit durchgeführt. Keine der neun Anforderungen ist vollständig statusidentisch mit `RR-163` oder `RR-164`.

| Kandidat | ↔ `RR-163` | ↔ `RR-164` | Begründung |
| --- | --- | --- | --- |
| `M22_1-A` | PARTIAL_OVERLAP | PARTIAL_OVERLAP | Gemeinsame Bezüge zu Nutzungsumgebung bzw. Nutzerfähigkeiten; Nr. 22.1 verlangt jedoch speziell die zweckbestimmungsgemäße Funktion bei Laienanwendung. |
| `M22_1-B` | DISTINCT | DISTINCT | Eigenständiger Sollzustand zur Verständlichkeit von Information und Anweisungen. |
| `M22_1-C` | DISTINCT | DISTINCT | Eigenständiger Sollzustand zur praktischen Anwendbarkeit von Information und Anweisungen. |
| `M22_2-A` | PARTIAL_OVERLAP | PARTIAL_OVERLAP | Use-Error- bzw. Nutzerbezug vorhanden, aber eigener laienbezogener Ergebniszustand „sichere Verwendung in allen Bedienungsphasen". |
| `M22_2-B` | PARTIAL_OVERLAP | PARTIAL_OVERLAP | Gleiches Umfeld von Anwendungsfehlern, jedoch eigener Sollzustand der fehlerfreien bzw. accurate Nutzung. |
| `M22_2-C` | PARTIAL_OVERLAP | PARTIAL_OVERLAP | Stärkste Überschneidung: Falsche Handhabung ist unmittelbar anwendungsfehlerbezogen; Nr. 22.2 beschränkt die Pflicht aber weder auf ergonomische Ursachen noch auf den Nutzerfaktorenkatalog aus Nr. 5. |
| `M22_2-D` | PARTIAL_OVERLAP | PARTIAL_OVERLAP | Ergebnisinterpretationsfehler gehören zum weiteren Use-Error-Komplex, bilden aber einen spezielleren laienbezogenen und bedingten Sollzustand. |
| `M22_3-A` | DISTINCT | DISTINCT | Ein produktseitiges Prüfverfahren wird von Nr. 5 nicht verlangt. |
| `M22_3-B` | DISTINCT | DISTINCT | Eine Warnfunktion bei ungültigem Ergebnis wird von Nr. 5 nicht verlangt. |

**Gesamtbegründung:** Die Unterschiede sind regulatorisch relevant, weil Nr. 5 allgemein an vorgesehene Anwender und bestimmte Quellen von Anwendungsfehlern anknüpft, während Nr. 22 zusätzliche Pflichten speziell für Produkte zur Anwendung durch Laien festlegt. Ein partieller Overlap begründet nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 5.1 keine Deduplizierung.

| Merkmal | Ergebnis |
| --- | --- |
| DUPLICATE | 0 |
| Vollständige Deduplizierungen | 0 |
| `RR-163` und `RR-164` geändert | NEIN |

---

## 12. Kandidaten

### M22_1-A — Laiengerechte Auslegung und Herstellung zur zweckbestimmungsgemäßen Funktion

- **Title EN:** Design and Manufacture for Intended Performance in Lay Use
- **DE:** Der Hersteller muss Produkte zur Laienanwendung so auslegen und herstellen, dass sie ihre Zweckbestimmung unter Berücksichtigung der Fähigkeiten und Möglichkeiten der Laien sowie vorhersehbarer Schwankungen ihrer Verfahrensweise und Umgebung erfüllen können.
- **EN:** The manufacturer shall ensure that devices intended for lay use are designed and manufactured to perform appropriately for their intended purpose, taking account of lay persons' skills and available means and reasonably anticipated variation in technique and environment.
- **Primary:** `SRC-001#Anh.I/Nr.22.1`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** NEIN
- **Katalog:** `RR-174`

### M22_1-B — Verständlichkeit der Herstellerangaben und -anweisungen für Laien

- **Title EN:** Understandability of Manufacturer Information and Instructions for Lay Persons
- **DE:** Der Hersteller muss sicherstellen, dass seine Angaben und Anweisungen für Laien leicht verständlich sind.
- **EN:** The manufacturer shall ensure that the information and instructions it provides are easy for lay persons to understand.
- **Primary:** `SRC-001#Anh.I/Nr.22.1`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** NEIN
- **Katalog:** `RR-175`

### M22_1-C — Anwendbarkeit der Herstellerangaben und -anweisungen für Laien

- **Title EN:** Applicability of Manufacturer Information and Instructions for Lay Persons
- **DE:** Der Hersteller muss sicherstellen, dass seine Angaben und Anweisungen für Laien leicht anwendbar sind.
- **EN:** The manufacturer shall ensure that the information and instructions it provides are easy for lay persons to apply.
- **Primary:** `SRC-001#Anh.I/Nr.22.1`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** NEIN
- **Katalog:** `RR-176`

### M22_2-A — Sichere Verwendung durch den vorgesehenen Anwender in allen Bedienungsphasen

- **Title EN:** Safe Use by the Intended User at All Stages of the Procedure
- **DE:** Der Hersteller muss das Produkt so auslegen und herstellen, dass es vom vorgesehenen Anwender in allen Bedienungsphasen sicher verwendet werden kann, erforderlichenfalls nach angemessener Schulung und/oder Aufklärung.
- **EN:** The manufacturer shall ensure through design and manufacture that the device can be used safely by the intended user at all stages of the procedure, if necessary after appropriate training and/or information.
- **Primary:** `SRC-001#Anh.I/Nr.22.2`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** NEIN
- **Modalität:** erforderlichenfalls nach angemessener Schulung und/oder Aufklärung
- **Katalog:** `RR-177`

### M22_2-B — Fehlerfreie Verwendung durch den vorgesehenen Anwender in allen Bedienungsphasen

- **Title EN:** Accurate Use by the Intended User at All Stages of the Procedure
- **DE:** Der Hersteller muss das Produkt so auslegen und herstellen, dass es vom vorgesehenen Anwender in allen Bedienungsphasen fehlerfrei verwendet werden kann, erforderlichenfalls nach angemessener Schulung und/oder Aufklärung.
- **EN:** The manufacturer shall ensure through design and manufacture that the device can be used accurately by the intended user at all stages of the procedure, if necessary after appropriate training and/or information.
- **Primary:** `SRC-001#Anh.I/Nr.22.2`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** NEIN
- **Modalität:** erforderlichenfalls nach angemessener Schulung und/oder Aufklärung
- **Source Fidelity:** Sprachfassungsdivergenz „fehlerfrei" / `accurately` / `correctement` nach Abschnitt 3.2 erhalten.
- **Katalog:** `RR-178`

### M22_2-C — Minimierung des Risikos falscher Handhabung durch den vorgesehenen Anwender

- **Title EN:** Minimisation of Risk of Handling Error by the Intended User
- **DE:** Der Hersteller muss das Produkt so auslegen und herstellen, dass das Risiko einer falschen Handhabung durch den vorgesehenen Anwender so gering wie möglich gehalten wird.
- **EN:** The manufacturer shall ensure through design and manufacture that the risk of error by the intended user in handling the device is reduced as far as possible.
- **Primary:** `SRC-001#Anh.I/Nr.22.2`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** NEIN
- **Modalität:** Risiko so gering wie möglich
- **Katalog:** `RR-179`

### M22_2-D — Minimierung des Risikos falscher Interpretation von Ergebnissen

- **Title EN:** Minimisation of Risk of Erroneous Interpretation of Results
- **DE:** Soweit die Ergebnisinterpretation einschlägig ist, muss der Hersteller das Produkt so auslegen und herstellen, dass das Risiko einer falschen Interpretation durch den vorgesehenen Anwender so gering wie möglich gehalten wird.
- **EN:** If interpretation of results is applicable, the manufacturer shall ensure through design and manufacture that the risk of erroneous interpretation by the intended user is reduced as far as possible.
- **Primary:** `SRC-001#Anh.I/Nr.22.2`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** JA — Interpretation von Ergebnissen ist im konkreten Produktkontext einschlägig
- **Modalität:** Risiko so gering wie möglich
- **Katalog:** `RR-180`

### M22_3-A — Verfahren zur Kontrolle der bestimmungsgemäßen Funktion bei der Anwendung

- **Title EN:** Procedure for Verification of Intended Performance at the Time of Use
- **DE:** Soweit angemessen, muss der Hersteller das Produkt mit einem Verfahren versehen, anhand dessen der Laie bei der Anwendung kontrollieren kann, ob das Produkt bestimmungsgemäß arbeiten wird.
- **EN:** Where appropriate, the manufacturer shall ensure that the device includes a procedure enabling the lay person, at the time of use, to verify that it will perform as intended.
- **Primary:** `SRC-001#Anh.I/Nr.22.3`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** JA — Vorsehen des Verfahrens ist „soweit angemessen"
- **Katalog:** `RR-181`

### M22_3-B — Warnung bei fehlendem gültigem Ergebnis

- **Title EN:** Warning When No Valid Result Is Provided
- **DE:** Soweit angemessen und gegebenenfalls muss der Hersteller das Produkt mit einem Verfahren versehen, durch das der Laie gewarnt wird, wenn kein gültiges Ergebnis erzielt wurde.
- **EN:** Where appropriate and if applicable, the manufacturer shall ensure that the device includes a procedure by which the lay person is warned when the device has failed to provide a valid result.
- **Primary:** `SRC-001#Anh.I/Nr.22.3`
- **Supplementary:** keine
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Outer Conditional:** JA — vorgesehene Laienanwendung
- **Inner Conditional:** JA — 1. Verfahren ist „soweit angemessen" vorzusehen. 2. Warnfunktion ist zusätzlich „gegebenenfalls" einschlägig.
- **Katalog:** `RR-182`

---

## 13. Nicht extrahierte Bereiche

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.23.1` | trotz unmittelbarer Nachbarschaft im MDR-Text nicht extrahiert; bleibt separat `geplant` |
| `SRC-008` — IEC 62366-1 und andere Normen | nicht extrahiert; keine Norminhalte verwendet |
| Kandidaten des Standards-Landscape-Audits (Entwicklungsarchiv; nicht im Abgabepaket) | nicht registriert und nicht verwendet |

Keiner dieser Punkte ist ein zurückgestellter Fall oder ein Blocker für den Abschluss von Nr. 22.1 bis Nr. 22.3.

---

## 14. Methodenaudit

| Prüfung | Ergebnis |
| --- | --- |
| Änderung an [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) erforderlich | NEIN — Version 1.2 reicht aus; die kritischen Fälle lassen sich vollständig mit dem bestehenden Split-Test, den Regeln zu Bedingungen und Modalitäten, dem Source-Fidelity-Verfahren und der `0 / 1 / n`-Logik entscheiden. Lebenszyklusphasen werden bereits nach tatsächlicher Geltung bzw. Erfüllung der konkreten Verpflichtung vergeben; mehrere Phasen sind zulässig. |
| Änderung an [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) erforderlich | NEIN — alle neun Kandidaten lassen sich dem bestehenden Cluster `Gebrauchstauglichkeit` und den bestehenden Lebenszyklusphasen eindeutig zuordnen. Ein neuer Cluster für Laienanwendung, Information oder Warnfunktionen ist methodisch nicht erforderlich; die Nachadjudikation zeigt keinen fehlenden Phasentyp und keinen Taxonomiefehler. |
| Neues Katalogfeld | NEIN |

---

## 15. Adjudikationsverlauf

Dieser Abschnitt dokumentiert, welche Werte aus Research-Bericht A durch die Nachadjudikation in Research-Bericht B ersetzt wurden. Die ersetzten Werte sind nicht mehr gültig; sie werden ausschließlich zur Nachvollziehbarkeit festgehalten.

| Kandidat | Merkmal | Bericht A (ersetzt) | Bericht B (final) |
| --- | --- | --- | --- |
| `M22_1-A` | Lifecycle | Entwicklung und Realisierung · Änderung und Wartung | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung |
| `M22_1-B` | Lifecycle | Inverkehrbringen, Inbetriebnahme und Betrieb | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung |
| `M22_1-C` | Lifecycle | Inverkehrbringen, Inbetriebnahme und Betrieb | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung |
| `M22_1-A` | Primary | `SRC-001#Anh.I/Nr.22.1/Satz.1` | `SRC-001#Anh.I/Nr.22.1` |
| `M22_1-B`, `M22_1-C` | Primary | `SRC-001#Anh.I/Nr.22.1/Satz.2` | `SRC-001#Anh.I/Nr.22.1` |

Unverändert durch Bericht B: Zahl der `RR` (9), Out-of-Scope-Atom (1), Themes (9 × Gebrauchstauglichkeit), Conditionality, Deduplizierungen (0), Unresolved (0) sowie die Lifecycle-Werte von `M22_2-A` bis `M22_3-B`. Bereits [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.18 und Version 1.0 dieser Datei enthalten ausschließlich die finalen Werte aus Bericht B.

---

## 16. Quellenfundstellen der Research-Berichte

Die Fundstellen sind so wiedergegeben, wie sie in den Research-Berichten dokumentiert sind, einschließlich der dort enthaltenen URL-Parameter. Sie wurden für diese Datei nicht erneut aufgerufen.

| Bericht | Bezeichnung laut Bericht | URL laut Bericht |
| --- | --- | --- |
| A [1] | CL2017R0745DE0070010.0001_cp 1..1 (DE, konsolidiert 19.07.2026) | https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A02017R0745-20260719 |
| A [2] | CL2017R0745FR0070010.0001_cp 1..1 (FR, konsolidiert 19.07.2026) | https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=CELEX%3A02017R0745-20260719 |
| A [3] | CL2017R0745EN0070010.0001_cp 1..1 (EN, konsolidiert 19.07.2026) | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02017R0745-20260719 |
| B [1] | EUR-Lex - 02017R0745-20260719 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02017R0745-20260719 |

---

## 17. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3`. 10 normative Kandidatenatome geprüft; 9 finale neue MDR-Gap-`RR`-Kandidaten `M22_1-A` bis `M22_3-B`, alle outer conditional wegen vorgesehener Laienanwendung, davon 3 zusätzlich inner conditional (`M22_2-D`, `M22_3-A`, `M22_3-B`). 1 Out-of-Scope-Atom (unbeabsichtigtes Schneiden, Stechen bzw. Nadelstichverletzungen). Theme aller 9 Kandidaten Gebrauchstauglichkeit. Abgleich mit `RR-163` und `RR-164`: 0 vollständige Deduplizierungen. Sprachfassungsdivergenz „fehlerfrei" / `accurately` / `correctement` dokumentiert. 0 unresolved, 0 deferred. |
| 1.1 | Vollständige Integration der bereits abgeschlossenen Research-Begründungen aus Research-Bericht A (ursprüngliche `0 / 1 / n`-Extraktion) und Research-Bericht B (Nachadjudikation Lifecycle und Locator) zu Source Verification, Atomisierung und Split-Tests, Scope-Entscheidung, Conditionality, Source Fidelity, Lifecycle, Locator und Deduplizierung; Adjudikationsverlauf und Quellenfundstellen der Berichte ergänzt; Modalität von `M22_1-A` aus Bericht A nachgetragen; Repository-Hinweis zur projektweiten Verwendung des Lokator-Elements `Satz.` ergänzt. Keine Änderung der finalen `RR`-Entscheidungen, Texte, Themes, Lebenszyklusphasen, Conditionality, Locators oder Deduplizierungen. |
