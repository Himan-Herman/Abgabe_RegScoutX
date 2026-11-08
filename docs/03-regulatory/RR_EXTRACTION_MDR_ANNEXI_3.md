# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 3

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.3` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Kernbereich |
| Expected Theme | Qualitäts- und Risikomanagement |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.18 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M3-A` bis `M3-K` sind ausschließlich temporäre Evidenzkennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Neue MDR-Gap-`RR`-Kandidaten | **11** — `M3-A` bis `M3-K` |
| davon regulär | 10 |
| davon conditional | 1 — `M3-K` |
| MDR-intern deduplizierte Atome | 4 |
| Unresolved | 0 |
| Deferred | 0 |
| Out-of-Scope-Atome | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 11 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Locator-Entscheidung

Die Quellenstruktur wurde im aktuellen `SRC-001`-Rechtsstand verifiziert. Verbindlich sind für diesen Quellenbereich die folgenden internen Lokatoren:

| Locator | Inhalt |
| --- | --- |
| `SRC-001#Anh.I/Nr.3/Satz.1` | vier Grundpflichten am Risikomanagementsystem |
| `SRC-001#Anh.I/Nr.3/Satz.2` | kontinuierlicher iterativer Lebenszyklusprozess und regelmäßige systematische Aktualisierung |
| `SRC-001#Anh.I/Nr.3/Satz.3` | einleitender normativer Rahmen für Buchst. a bis f |
| `SRC-001#Anh.I/Nr.3/Buchst.a` bis `SRC-001#Anh.I/Nr.3/Buchst.f` | die sechs Buchstaben der Durchführungspflichten |

`Satz.3` bezeichnet den dritten Satz einschließlich seines einleitenden Rahmens für die nachfolgenden Buchstaben a bis f. Für diesen einleitenden Rahmen wird **kein** eigenes Locator-Element eingeführt; er wird ausschließlich über `Satz.3` geführt. Das entspricht dem zulässigen Elementvokabular aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4.

---

## 4. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.3/Satz.1` | 0 neue `RR` | vier Sollzustände vollständig MDR-intern dedupliziert (Abschnitt 5 und 8) |
| `SRC-001#Anh.I/Nr.3/Satz.2` | 2 `RR` | `M3-A`, `M3-B` |
| `SRC-001#Anh.I/Nr.3/Satz.3` | 0 eigene `RR` | einleitender normativer Rahmen; Supplementary-Kontext für `M3-C` bis `M3-K` |
| `SRC-001#Anh.I/Nr.3/Buchst.a` | 2 `RR` | `M3-C`, `M3-D` |
| `SRC-001#Anh.I/Nr.3/Buchst.b` | 2 `RR` | `M3-E`, `M3-F` |
| `SRC-001#Anh.I/Nr.3/Buchst.c` | 2 `RR` | `M3-G`, `M3-H` |
| `SRC-001#Anh.I/Nr.3/Buchst.d` | 1 `RR` | `M3-I` |
| `SRC-001#Anh.I/Nr.3/Buchst.e` | 1 `RR` | `M3-J` |
| `SRC-001#Anh.I/Nr.3/Buchst.f` | 1 conditional `RR` | `M3-K` |
| **Gesamt** | **11** | |

---

## 5. Satz 1 — MDR-interne Deduplizierung

`SRC-001#Anh.I/Nr.3/Satz.1` enthält die vier Grundpflichten `establish`, `implement`, `document` und `maintain` am Risikomanagementsystem. Diese vier Sollzustände erzeugen **keine** neuen `RR`.

| Sollzustand | Behandlung | Bestehende `RR` |
| --- | --- | --- |
| Einführen / `establish` | vollständig dedupliziert | `RR-116` |
| Dokumentieren / `document` | vollständig dedupliziert | `RR-117` |
| Umsetzen / `implement` | vollständig dedupliziert | `RR-118` |
| Fortschreiben / `maintain` | vollständig dedupliziert | `RR-119` |

**Begründung:**

- identischer Herstelleradressat;
- identisches Risikomanagementsystem als Bezugsobjekt;
- identische normative Handlungen;
- identischer Trigger;
- identisches Compliance-Ergebnis;
- `SRC-001#Art.10/Abs.2` verweist ausdrücklich auf Anhang I Abschnitt 3.

Die deutschen Varianten — `SRC-001#Art.10/Abs.2` mit „angewandt" und „aufrechterhalten", `SRC-001#Anh.I/Nr.3/Satz.1` mit „umsetzen" und „fortschreiben" — erzeugen keinen unterschiedlichen Sollgehalt. Die englische Fassung verwendet an beiden Stellen `implement` und `maintain`.

**Neue `RR` aus Satz 1: 0.**

---

## 6. Kandidaten

### M3-A — Risikomanagement als kontinuierlicher iterativer Prozess über den Produktlebenszyklus

- **Title EN:** Risk Management as a Continuous Iterative Process across the Device Lifecycle
- **DE:** Der Hersteller muss das Risikomanagement als kontinuierlichen iterativen Prozess während des gesamten Lebenszyklus des Produkts führen.
- **EN:** The manufacturer shall conduct risk management as a continuous iterative process throughout the entire lifecycle of the device.
- **Primary:** `SRC-001#Anh.I/Nr.3/Satz.2`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** „während des gesamten Lebenszyklus" ist zwingende Zeit- und Scope-Qualifikation desselben kontinuierlichen iterativen Prozesses. Daraus entsteht **keine** eigene zusätzliche `RR`.

**MDR-interner Abgleich:** keine Dublette zu `RR-116` bis `RR-119`; diese betreffen Bestand und Pflege des Systems, nicht die Prozessform.

### M3-B — Regelmäßige systematische Aktualisierung des Risikomanagements

- **Title EN:** Regular Systematic Updating of Risk Management
- **DE:** Der Hersteller muss das Risikomanagement regelmäßig systematisch aktualisieren.
- **EN:** The manufacturer shall subject risk management to regular systematic updating.
- **Primary:** `SRC-001#Anh.I/Nr.3/Satz.2`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Verifikation und Validierung · Konformitätsbewertung · Inverkehrbringen, Inbetriebnahme und Betrieb · Post-Market-Überwachung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** `M3-A` und `M3-B` bleiben getrennt.

| Prüfung | Ergebnis | Begründung |
| --- | --- | --- |
| Split-Bedingung 1 | erfüllt | Ein Prozess kann kontinuierlich und iterativ konzipiert bzw. geführt werden, ohne dass seine Aktualisierung tatsächlich in regelmäßiger und systematischer Weise erfolgt. |
| Split-Bedingung 2 | erfüllt | Die regelmäßige systematische Aktualisierung bildet einen eigenständig prüfbaren regulatorischen Sollzustand und ist nicht nur eine sprachliche Modalität ohne eigenen Compliance-Gehalt. |

**Keine Deduplizierung gegen `RR-119`:** `RR-119` betrifft die Aufrechterhaltung des Risikomanagementsystems, `M3-B` die regelmäßige systematische Aktualisierung des Risikomanagements. Das sind unterschiedliche prüfbare Sollzustände.

### M3-C — Festlegung eines Risikomanagementplans je Produkt

- **Title EN:** Establishment of a Risk Management Plan for Each Device
- **DE:** Der Hersteller muss für jedes Produkt einen Risikomanagementplan festlegen.
- **EN:** The manufacturer shall establish a risk management plan for each device.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.a`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** „für jedes Produkt" ist Scope-Bestandteil und **keine** eigene `RR`.

### M3-D — Dokumentation des Risikomanagementplans je Produkt

- **Title EN:** Documentation of the Risk Management Plan for Each Device
- **DE:** Der Hersteller muss den Risikomanagementplan für jedes Produkt dokumentieren.
- **EN:** The manufacturer shall document the risk management plan for each device.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.a`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**MDR-interner Abgleich:** keine Deduplizierung gegen `RR-117`. `RR-117` betrifft die Dokumentation des Risikomanagementsystems, `M3-D` die Dokumentation des konkreten Risikomanagementplans je Produkt.

### M3-E — Identifikation der bekannten und vorhersehbaren Gefährdungen

- **Title EN:** Identification of Known and Foreseeable Hazards
- **DE:** Der Hersteller muss die bekannten und vorhersehbaren Gefährdungen, die mit jedem Produkt verbunden sind, identifizieren.
- **EN:** The manufacturer shall identify the known and foreseeable hazards associated with each device.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.b`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M3-F — Analyse der bekannten und vorhersehbaren Gefährdungen

- **Title EN:** Analysis of Known and Foreseeable Hazards
- **DE:** Der Hersteller muss die bekannten und vorhersehbaren Gefährdungen, die mit jedem Produkt verbunden sind, analysieren.
- **EN:** The manufacturer shall analyse the known and foreseeable hazards associated with each device.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.b`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M3-G — Einschätzung der Risiken bei bestimmungsgemäßer Verwendung und vorhersehbarer Fehlanwendung

- **Title EN:** Estimation of Risks in Intended Use and Reasonably Foreseeable Misuse
- **DE:** Der Hersteller muss die Risiken einschätzen, die mit der bestimmungsgemäßen Verwendung verbunden sind und die bei einer vernünftigerweise vorhersehbaren Fehlanwendung auftreten.
- **EN:** The manufacturer shall estimate the risks associated with, and occurring during, the intended use and during reasonably foreseeable misuse.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.c`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Bestimmungsgemäße Verwendung und vernünftigerweise vorhersehbare Fehlanwendung bilden eine gemeinsame zwingende Reichweite; das ist **kein** Splitgrund.

### M3-H — Bewertung der Risiken bei bestimmungsgemäßer Verwendung und vorhersehbarer Fehlanwendung

- **Title EN:** Evaluation of Risks in Intended Use and Reasonably Foreseeable Misuse
- **DE:** Der Hersteller muss die Risiken bewerten, die mit der bestimmungsgemäßen Verwendung verbunden sind und die bei einer vernünftigerweise vorhersehbaren Fehlanwendung auftreten.
- **EN:** The manufacturer shall evaluate the risks associated with, and occurring during, the intended use and during reasonably foreseeable misuse.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.c`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M3-I — Beseitigung oder Kontrolle der bewerteten Risiken

- **Title EN:** Elimination or Control of the Assessed Risks
- **DE:** Der Hersteller muss die nach Anhang I Abschnitt 3 Buchstabe c bewerteten Risiken gemäß den Anforderungen nach Anhang I Abschnitt 4 beseitigen oder kontrollieren.
- **EN:** The manufacturer shall eliminate or control the risks referred to in point (c) in accordance with the requirements of Section 4 of Annex I.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.d`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Buchst.c` · `SRC-001#Anh.I/Nr.3/Satz.3` · `SRC-001#Anh.I/Nr.4`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** „beseitigen oder kontrollieren" sind alternative Erfüllungswege derselben Verpflichtung.

**Supplementary-Kontext:** `SRC-001#Anh.I/Nr.4` ist notwendiger normativer Kontext, weil die Pflicht die Art der Risikokontrolle ausdrücklich hiernach bestimmt. Nr. 4 wird hier **nicht** systematisch extrahiert.

### M3-J — Bewertung der Auswirkungen von Fertigungs- und Post-Market-Informationen auf das Risikobild

- **Title EN:** Evaluation of the Impact of Production and Post-Market Information on the Risk Profile
- **DE:** Der Hersteller muss die Auswirkungen der in der Fertigungsphase und insbesondere durch das System zur Überwachung nach dem Inverkehrbringen gewonnenen Informationen auf Gefährdungen und deren Häufigkeit, auf die Abschätzung der verbundenen Risiken sowie auf das Gesamtrisiko, das Nutzen-Risiko-Verhältnis und die Risikoakzeptanz bewerten.
- **EN:** The manufacturer shall evaluate the impact of information from the production phase and, in particular, from the post-market surveillance system, on hazards and the frequency of occurrence thereof, on estimates of their associated risks, as well as on the overall risk, benefit-risk ratio and risk acceptability.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.e`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Post-Market-Überwachung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** ein Hauptbefehl mit mehreren zwingenden Bewertungsgegenständen. Es erfolgt **keine** Mikroatomisierung nach Gefährdungen, Häufigkeit, Risikoabschätzungen, Gesamtrisiko, Nutzen-Risiko-Verhältnis und Risikoakzeptanz.

**Theme:** Die Informationen aus dem System zur Überwachung nach dem Inverkehrbringen sind Input der Risikomanagementbewertung. Das Theme bleibt deshalb `Qualitäts- und Risikomanagement`.

**Späterer Cross-Article-Abgleich:** `SRC-001#Art.83`. **Kein** Deferred.

### M3-K — Erforderlichenfalls Anpassung der Kontrollmaßnahmen

- **Title EN:** Amendment of Control Measures Where Necessary
- **DE:** Ergibt die Bewertung nach Anhang I Abschnitt 3 Buchstabe e einen Anpassungsbedarf, so muss der Hersteller die Kontrollmaßnahmen gemäß den Anforderungen nach Anhang I Abschnitt 4 anpassen.
- **EN:** Where the evaluation referred to in point (e) shows it to be necessary, the manufacturer shall amend control measures in line with the requirements of Section 4 of Annex I.
- **Primary:** `SRC-001#Anh.I/Nr.3/Buchst.f`
- **Supplementary:** `SRC-001#Anh.I/Nr.3/Buchst.e` · `SRC-001#Anh.I/Nr.3/Satz.3` · `SRC-001#Anh.I/Nr.4`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Die Bewertung nach Buchstabe e ergibt einen Anpassungsbedarf.

**Atomizität:** keine Zusammenführung mit `M3-J`. `M3-J` betrifft die Bewertung, `M3-K` die gegebenenfalls daraus folgende Anpassung; die Erfüllungsstatus sind unterschiedlich.

---

## 7. Conditional-Audit

| Kategorie | Anzahl | Kandidaten |
| --- | --- | --- |
| Regulär | 10 | `M3-A` · `M3-B` · `M3-C` · `M3-D` · `M3-E` · `M3-F` · `M3-G` · `M3-H` · `M3-I` · `M3-J` |
| Conditional | 1 | `M3-K` |

Trigger von `M3-K`: Die Bewertung nach Buchstabe e ergibt einen Anpassungsbedarf. Der Vorbehalt „erforderlichenfalls" bleibt vollständig im Requirement Text erhalten; es wird **keine** unbedingte Pflicht formuliert.

---

## 8. Deduplizierungsregister

| Nr. | Fundstelle | Gegenstand | Bestehende `RR` | Ergebnis |
| --- | --- | --- | --- | --- |
| 1 | `SRC-001#Anh.I/Nr.3/Satz.1` | Einführung des RMS | `RR-116` | keine neue `RR` |
| 2 | `SRC-001#Anh.I/Nr.3/Satz.1` | Dokumentation des RMS | `RR-117` | keine neue `RR` |
| 3 | `SRC-001#Anh.I/Nr.3/Satz.1` | Umsetzung des RMS | `RR-118` | keine neue `RR` |
| 4 | `SRC-001#Anh.I/Nr.3/Satz.1` | Fortschreibung des RMS | `RR-119` | keine neue `RR` |

`RR-116` bis `RR-119` bleiben materiell unverändert.

---

## 9. Abgleich mit RR-133

| Gegenüberstellung | Inhalt |
| --- | --- |
| `RR-133` | Einbindung des Risikomanagements in das QMS — QMS-Integrationspflicht |
| `M3-A` bis `M3-K` | materielle Risikomanagementpflichten |

**Ergebnis:** keine Deduplizierung. Die Erfüllungsstatus können unabhängig voneinander abweichen: Ein Qualitätsmanagementsystem kann das Risikomanagement formal abbilden, ohne dass die materiellen Pflichten erfüllt sind, und umgekehrt.

---

## 10. Cross-Regulation

Sachliche Beziehungen bestehen insbesondere zu `RR-007` bis `RR-029` aus dem Risikomanagement des EU AI Act.

| Merkmal | Ergebnis |
| --- | --- |
| Cross-Regulation-Deduplizierungen | 0 |
| Bestehende AI-`RR` ändern | NEIN |

**Begründung:** unterschiedliche Rechtsregime, unterschiedliche regulatorische Rollen, unterschiedliche Bezugsobjekte und unterschiedliche normative Herkunft. Eine gemeinsame organisatorische Umsetzung oder gemeinsame Evidenz begründet **keine** normative Deduplizierung.

---

## 11. Multilingualer Audit

| Fassung | Behandlung |
| --- | --- |
| DE | geprüft |
| EN | geprüft |
| FR | zusätzlich geprüft |
| IT | zusätzlich geprüft |

| Merkmal | Ergebnis |
| --- | --- |
| Materielle Divergenzen | 0 |
| Weitere Sprachen erforderlich | NEIN |
| Unresolved | 0 |

**Top-Level:** Die deutsche Fassung verwendet zwischen `SRC-001#Art.10/Abs.2` und `SRC-001#Anh.I/Nr.3/Satz.1` unterschiedliche sprachliche Varianten für `implement` und `maintain`. Die englische Fassung bleibt an beiden Stellen bei `implement` und `maintain`. Es besteht kein unterschiedlicher Sollgehalt.

**Zu Satz 2:**

| Fassung | Formulierung |
| --- | --- |
| DE | regelmäßige systematische Aktualisierung |
| EN | regular systematic updating |
| FR | periodische systematische Aktualisierung |
| IT | costante e sistematico aggiornamento |

Die italienische sprachliche Nuance wird im systematischen Kontext als wiederkehrende bzw. fortlaufende systematische Aktualisierung verstanden und erzeugt **keinen** unterschiedlichen atomaren Sollzustand. Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung automatisch als vorrangig behandelt.

---

## 12. Context und 0-`RR`-Aussagen

| Fundstelle | Gegenstand | Behandlung |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.3/Satz.2` | „ist zu verstehen als" | Auslegungsformel ohne eigene `RR` |
| `SRC-001#Anh.I/Nr.3/Satz.2` | „während des gesamten Lebenszyklus" | zwingende Zeitqualifikation von `M3-A` |
| `SRC-001#Anh.I/Nr.3/Satz.3` | Einleitung der Buchstaben a bis f | Supplementary-Kontext |
| `SRC-001#Anh.I/Nr.3/Buchst.a` | „für jedes Produkt" | Scope von `M3-C` und `M3-D` |
| `SRC-001#Anh.I/Nr.3/Buchst.b` | bekannte und vorhersehbare Gefährdungen | Pflichtumfang von `M3-E` und `M3-F` |
| `SRC-001#Anh.I/Nr.3/Buchst.c` | bestimmungsgemäße Verwendung und vorhersehbare Fehlanwendung | gemeinsame Pflichtreichweite von `M3-G` und `M3-H` |
| `SRC-001#Anh.I/Nr.3/Buchst.d` und `Buchst.f` | Verweis auf Abschnitt 4 | notwendiger normativer Supplementary-Kontext |
| `SRC-001#Anh.I/Nr.3/Buchst.e` | sechs Bewertungsgegenstände | gemeinsamer Pflichtumfang von `M3-J` |

---

## 13. Scope-Audit

| Bereich | Ergebnis |
| --- | --- |
| `SRC-001#Anh.I/Nr.4` | nicht systematisch extrahiert |
| `SRC-001#Art.83` | nicht systematisch extrahiert |
| ISO 14971 | keine Inhalte importiert |
| Out-of-Scope-Atome | 0 |

Es wurden **keine** anderen MDR-Bereiche bearbeitet.

---

## 14. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. **Keine** Methodenänderung erforderlich.

Besonders bestätigt:

- ein Split erfolgt nur bei beiden erfüllten Bedingungen;
- die Alternativen „beseitigen oder kontrollieren" bleiben gemeinsam;
- Listenobjekte werden nicht mechanisch atomisiert;
- Scope-Qualifikationen erzeugen keine eigene `RR`;
- die Fundstellendopplung desselben Sollzustands erzeugt keine neue `RR`;
- notwendige normative Querverweise können Supplementary-Kontext sein, ohne den referenzierten Bereich vorzeitig zu extrahieren.

---

## 15. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.3`. 11 finale neue MDR-Gap-`RR`-Kandidaten `M3-A` bis `M3-K`, davon 10 regulär und 1 conditional. Vier Top-Level-Sollzustände aus Satz 1 wurden vollständig gegen `RR-116` bis `RR-119` dedupliziert. 0 unresolved, 0 deferred, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen. Die Satzstruktur wurde mit den präzisen internen Lokatoren `Satz.1` bis `Satz.3` dokumentiert. |
