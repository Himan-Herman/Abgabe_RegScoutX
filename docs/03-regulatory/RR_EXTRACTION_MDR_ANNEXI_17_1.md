# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 17.1

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.17.1` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Kernbereich |
| Expected Theme | Robustheit |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.24 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M17_1-A` bis `M17_1-D` sind ausschließlich temporäre Evidenzkennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Neue MDR-Gap-`RR`-Kandidaten | **4** — `M17_1-A` bis `M17_1-D` |
| davon regulär | 4 |
| davon conditional | 0 |
| MDR-intern deduplizierte Atome | 0 |
| Unresolved | 0 |
| Deferred | 0 |
| Out-of-Scope-Atome | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

| Fundstelle | Ergebnis |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.1/Satz.1` | 3 `RR` |
| `SRC-001#Anh.I/Nr.17.1/Satz.2` | 1 `RR` |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 4 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Quellenstruktur

`SRC-001#Anh.I/Nr.17.1` besteht aus genau zwei grammatischen Sätzen.

| Locator | Inhalt |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.1/Satz.1` | Produkte mit programmierbaren Elektroniksystemen einschließlich Software sowie Software, die selbst ein Produkt ist; Auslegung zur Gewährleistung von Wiederholbarkeit, Zuverlässigkeit und einer der bestimmungsgemäßen Verwendung entsprechenden Leistung |
| `SRC-001#Anh.I/Nr.17.1/Satz.2` | Single-Fault-Zustand; geeignete Vorkehrungen zur Beseitigung oder möglichst weitgehenden Verringerung der daraus resultierenden Risiken **oder** Leistungsbeeinträchtigungen |

Weitere Satznummern werden **nicht** gebildet. Für einen einleitenden Rahmen wird **kein** eigenes Locator-Element eingeführt; das entspricht dem zulässigen Elementvokabular aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4.

---

## 4. Vollständige `0 / 1 / n`-Prüfung

| Locator bzw. Aussage | Ergebnis | Kandidaten |
| --- | --- | --- |
| Produktkategorien in Satz 1 | 0 eigene `RR` | Applicability- bzw. Scope-Bedingung |
| Gemeinsamer Designrahmen in Satz 1 | 0 zusätzliche `RR` | vorgeschriebene Handlungsform |
| Wiederholbarkeit | 1 `RR` | `M17_1-A` |
| Zuverlässigkeit | 1 `RR` | `M17_1-B` |
| Leistung entsprechend der bestimmungsgemäßen Verwendung | 1 `RR` | `M17_1-C` |
| `SRC-001#Anh.I/Nr.17.1/Satz.2` | 1 `RR` | `M17_1-D` |
| **Gesamt** | **4** | |

**Applicability:** Die Produktkategorien — Produkte mit programmierbaren Elektroniksystemen einschließlich Software sowie Software, die selbst ein Produkt ist — sind Applicability- bzw. Scope-Bedingungen und erzeugen **0** eigene `RR`. Sie bleiben in den Requirement Texts der materiellen Kandidaten quellentreu erhalten. Eine separate Scope-`RR` wird **nicht** gebildet.

**Satz 1 — Atomisierung:** Für `M17_1-A`, `M17_1-B` und `M17_1-C` sind beide Split-Bedingungen erfüllt: Der Erfüllungsstatus ist jeweils unabhängig sinnvoll bestimmbar, und jeder Teil bildet einen vollständigen regulatorischen Produkt-Sollzustand. Die gemeinsame vorgeschriebene Handlungsform „sind so auszulegen, dass … gewährleistet ist" erzeugt **keine** zusätzliche aggregierende `RR`.

---

## 5. Kandidaten

### M17_1-A — Gewährleistung der Wiederholbarkeit programmierbarer Medizinprodukte

- **Title EN:** Ensuring Repeatability of Programmable Medical Devices
- **DE:** Der Hersteller muss sicherstellen, dass Produkte mit programmierbaren Elektroniksystemen einschließlich Software sowie Software, die selbst ein Produkt ist, so ausgelegt sind, dass ihre Wiederholbarkeit gewährleistet ist.
- **EN:** The manufacturer shall ensure that devices incorporating electronic programmable systems, including software, and software that are devices in themselves are designed to ensure repeatability.
- **Primary:** `SRC-001#Anh.I/Nr.17.1/Satz.1`
- **Supplementary:** keine
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Wiederholbarkeit besitzt einen eigenständig vollständigen und gegenüber Zuverlässigkeit sowie zweckbestimmungsgemäßer Leistung unabhängig bestimmbaren Sollzustand.

### M17_1-B — Gewährleistung der Zuverlässigkeit programmierbarer Medizinprodukte

- **Title EN:** Ensuring Reliability of Programmable Medical Devices
- **DE:** Der Hersteller muss sicherstellen, dass Produkte mit programmierbaren Elektroniksystemen einschließlich Software sowie Software, die selbst ein Produkt ist, so ausgelegt sind, dass ihre Zuverlässigkeit gewährleistet ist.
- **EN:** The manufacturer shall ensure that devices incorporating electronic programmable systems, including software, and software that are devices in themselves are designed to ensure reliability.
- **Primary:** `SRC-001#Anh.I/Nr.17.1/Satz.1`
- **Supplementary:** keine
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Zuverlässigkeit ist eine eigenständig vollständige Produkteigenschaft und nicht lediglich Modalität von Wiederholbarkeit oder Leistung.

### M17_1-C — Gewährleistung der Leistung entsprechend der Zweckbestimmung

- **Title EN:** Ensuring Performance in Line with Intended Use
- **DE:** Der Hersteller muss sicherstellen, dass Produkte mit programmierbaren Elektroniksystemen einschließlich Software sowie Software, die selbst ein Produkt ist, so ausgelegt sind, dass ihre Leistung ihrer bestimmungsgemäßen Verwendung entspricht.
- **EN:** The manufacturer shall ensure that devices incorporating electronic programmable systems, including software, and software that are devices in themselves are designed to ensure performance in line with their intended use.
- **Primary:** `SRC-001#Anh.I/Nr.17.1/Satz.1`
- **Supplementary:** keine
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Die zweckbestimmungsgemäße Leistung ist gegenüber Wiederholbarkeit und Zuverlässigkeit eigenständig statusfähig.

**Abgrenzung:** Keine Ausweitung auf die vollständige klinische Leistungsbewertung. Der Sollzustand bleibt ausschließlich der konkrete softwarebezogene Leistungsbezug aus Nr. 17.1.

### M17_1-D — Beherrschung von Folgen eines Single-Fault-Zustands

- **Title EN:** Control of Consequences of a Single-Fault Condition
- **DE:** Der Hersteller muss für Produkte im Anwendungsbereich von Anhang I Nr. 17.1 für den Fall des Erstauftretens eines Defekts geeignete Vorkehrungen treffen, um sich daraus ergebende Risiken oder Leistungsbeeinträchtigungen auszuschließen oder so weit wie möglich zu verringern.
- **EN:** For devices within the scope of Annex I, Section 17.1, the manufacturer shall, in the event of a single fault condition, adopt appropriate means to eliminate or reduce as far as possible consequent risks or impairment of performance.
- **Primary:** `SRC-001#Anh.I/Nr.17.1/Satz.2`
- **Supplementary:** keine
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

---

## 6. Satz 2 — finale Nachadjudikation

Zunächst geprüft wurde ein Split in zwei Kandidaten: `M17_1-D` für die resultierenden Risiken und ein weiterer Kandidat für die Leistungsbeeinträchtigungen. Dieser Split wurde nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 **verworfen**. Final besteht **eine** gemeinsame `RR`.

**Quellenstruktur:** geeignete Vorkehrungen sind zu treffen · um auszuschließen oder so weit wie möglich zu verringern · resultierende Risiken **oder** Leistungsbeeinträchtigungen.

**Begründung:** Risiken und Leistungsbeeinträchtigungen sind zwei mögliche Folgen desselben Single-Fault-Zustands unter demselben normativen Handlungsbefehl. Die Oder-Struktur muss innerhalb **einer** `RR` erhalten bleiben. Zwei `RR` würden daraus faktisch zwei kumulative Gap-Status erzeugen und gegen die Regel zu alternativen Erfüllungswegen aus Methode Version 1.2 verstoßen.

Der verworfene Zuschnitt erhält **keine** permanente Bedeutung und **keine** permanente Identifikation.

### 6.1 Verworfene temporäre Split-Variante M17_1-E

Im ersten Atomisierungsschritt wurde die Leistungsbeeinträchtigung vorläufig als separater Kandidat `M17_1-E` betrachtet. Diese temporäre Split-Variante wurde in der gezielten Nachadjudikation verworfen.

**Grund:** Resultierende Risiken und Leistungsbeeinträchtigung stehen unter demselben normativen Handlungsbefehl und derselben Zielstruktur. Nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 darf die Oder-Struktur nicht in zwei faktisch kumulative Gap-`RR` aufgespalten werden, wenn keine zwei eigenständigen kumulativen Pflichten vorliegen. Die Leistungsbeeinträchtigung bleibt deshalb gemeinsam mit den resultierenden Risiken Bestandteil von `M17_1-D`.

| Merkmal | Status |
| --- | --- |
| `M17_1-E` | verworfen vor permanenter Katalogisierung |
| Finaler Kandidat | nein |
| Permanente `RR`-Identifikation | keine |

### 6.2 Status des Single-Fault-Zustands

Der Single-Fault-Zustand ist **kein** conditional Applicability-Trigger. Er ist die spezifizierte Fehler- bzw. Betriebsbedingung einer bereits bei der Produktauslegung zu erfüllenden Robustheitsanforderung.

Die Compliance-Frage besteht bereits vor dem tatsächlichen Auftreten eines Fehlers: Sind geeignete Vorkehrungen vorhanden, damit sich das Produkt unter der Single-Fault-Bedingung entsprechend der regulatorischen Anforderung verhält?

`M17_1-D` ist deshalb **regulär** und **nicht** conditional.

### 6.3 Atomizität innerhalb von Satz 2

| Aussage | Behandlung |
| --- | --- |
| geeignete Vorkehrungen sind zu treffen | Handlungsform innerhalb `M17_1-D`; keine eigene `RR` |
| Risiken **oder** Leistungsbeeinträchtigungen | Oder-Struktur innerhalb `M17_1-D`; kein Split |
| ausschließen oder verringern | alternative bzw. abgestufte Erfüllungswege; kein Split |
| so weit wie möglich | wesentliche Qualifikation; kein eigener Split |

### 6.4 Anhang I Nr. 2

`SRC-001#Anh.I/Nr.2` ist **kein** Supplementary-Locator von `M17_1-D`.

**Begründung:** Nr. 2 definiert die möglichst weitgehende **Risikoreduktion**. `M17_1-D` enthält in einer gemeinsamen Oder-Struktur jedoch resultierende Risiken **oder** Leistungsbeeinträchtigungen. Ein Supplementary-Locator auf Ebene der gesamten gemeinsamen `RR` könnte fälschlich den Eindruck erzeugen, der Nutzen-Risiko-Maßstab aus Nr. 2 definiere ebenso die Reduktion reiner Leistungsbeeinträchtigungen. Der Primary-Locator Satz 2 trägt die Qualifikation „so weit wie möglich" bereits selbst.

Nr. 2 wird hier ausschließlich als normativer Auslegungskontext des Risiko-Zweigs benannt. Supplementary von `M17_1-D`: leer. Nr. 2 systematisch extrahiert: **NEIN**.

---

## 7. MDR-interne Deduplizierung

| Bestehende `RR` | Ergebnis |
| --- | --- |
| `RR-151` — Beseitigung oder Kontrolle der bewerteten Risiken | keine Deduplizierung |
| `RR-153` — Erforderlichenfalls Anpassung der Kontrollmaßnahmen | keine Deduplizierung |
| `RR-158` — Beseitigung oder weitestmögliche Minimierung durch sichere Auslegung und Herstellung | keine Deduplizierung |
| `RR-159` — Schutzmaßnahmen für nicht auszuschließende Risiken | keine Deduplizierung |

**Begründung:** `M17_1-D` enthält einen spezifischen softwarebezogenen Single-Fault-Sollzustand und zusätzlich die mögliche Leistungsbeeinträchtigung. Die bestehenden `RR` aus Anhang I Nr. 3 und Nr. 4 betreffen allgemeinere Risikomanagement- bzw. Risikokontrollpflichten. Die Erfüllungsstatus sind unabhängig.

Für `M17_1-A`, `M17_1-B` und `M17_1-C` besteht keine bestehende statusidentische MDR-`RR`.

**MDR-intern vollständig dedupliziert: 0.**

---

## 8. Verhältnis zu Anhang I Nr. 17.2 und Nr. 17.4

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.2` | nicht extrahiert; Status `geplant`. Späterer Abgleich insbesondere `M17_1-A`, `M17_1-B` und `M17_1-C` mit Lebenszyklus-, Verifikations- und Validierungsbezügen sowie `M17_1-D` mit Risikomanagement- und Verifikationsbezügen. Kein Deferred; keine Inhalte aus Nr. 17.2 importiert. |
| `SRC-001#Anh.I/Nr.17.4` | nicht extrahiert; es wurden keine Informationssicherheits- oder Cybersecurity-Pflichten importiert. Der Themencluster `Robustheit` wurde nicht erweitert. |

**Cybersecurity-Scope erweitert: NEIN.**

---

## 9. IEC 62304

`SRC-007` wurde **nicht** extrahiert. Es wurden **keine** Klauselinhalte der Norm übernommen, insbesondere keine Konzepte zu Software-Sicherheitsklassen, zu vorbestehender Software, zu Software-Einheiten, zu Integrationsprüfungen oder zur Problemlösung. Der Norm-Crosswalk bleibt ein eigener späterer Arbeitsschritt.

---

## 10. Cross-Regulation

| Kandidat | Fachlicher Bezug im AI-Act-Bestand | Ergebnis |
| --- | --- | --- |
| `M17_1-A` | insbesondere `RR-075` | keine Deduplizierung |
| `M17_1-B` | insbesondere `RR-075`, mittelbar `RR-077` | keine Deduplizierung |
| `M17_1-C` | partiell `RR-074` und `RR-075` | keine Deduplizierung |
| `M17_1-D` | stark `RR-077` und `RR-078` | keine Deduplizierung |

**Begründung:** unterschiedliche Rechtsregime, regulatorische Rollen, Bezugsobjekte, Pflichtumfänge und Compliance-Ergebnisse.

| Merkmal | Ergebnis |
| --- | --- |
| Cross-Regulation-Deduplizierungen | 0 |
| Bestehende AI-`RR` ändern | NEIN |

---

## 11. Multilingualer Audit

| Merkmal | Ergebnis |
| --- | --- |
| DE/EN | geprüft |
| Ergänzend geprüft für die Fehlerbedingung | FR · IT · ES |
| Materiell auffällige Sprachstelle | 1 |
| Status | RESOLVED |
| Unresolved | 0 |
| Weitere atomizitätsrelevante Divergenzen | 0 |

**Adjudikation:** Der deutsche Ausdruck „für den Fall des Erstauftretens eines Defekts" wird im regulatorisch-systematischen Sinn eines Single-Fault-Zustands verstanden, nicht als historische Aussage darüber, dass ein bestimmter Defekt zum allerersten Mal überhaupt auftreten müsse. Für den deutschen Requirement Text bleibt dennoch die authentische Formulierung erhalten.

Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung priorisiert.

---

## 12. Theme-Audit

| Kandidat | Themencluster |
| --- | --- |
| `M17_1-A` | Robustheit |
| `M17_1-B` | Robustheit |
| `M17_1-C` | Robustheit |
| `M17_1-D` | Robustheit |

Je Kandidat genau ein Themencluster. Keine Mehrfachzuordnung und keine neue Taxonomie.

---

## 13. Context und 0-`RR`-Aussagen

| Nr. | Aussage | Behandlung |
| --- | --- | --- |
| 1 | Produktkategorien in Satz 1 | Applicability; 0 eigene `RR` |
| 2 | gemeinsamer Designrahmen in Satz 1 | 0 zusätzliche `RR` |
| 3 | geeignete Vorkehrungen sind zu treffen | Handlungsform von `M17_1-D`; 0 eigene `RR` |
| 4 | Risiken **oder** Leistungsbeeinträchtigungen | Oder-Struktur innerhalb `M17_1-D`; kein Split |
| 5 | ausschließen oder verringern | alternative bzw. abgestufte Erfüllungsstruktur; kein Split |
| 6 | `SRC-001#Anh.I/Nr.2` | Auslegungskontext des Risiko-Zweigs; kein Supplementary-Locator von `M17_1-D`; keine systematische Extraktion |
| 7 | temporäre Kennung `M17_1-E` — Leistungsbeeinträchtigung als zunächst separat geprüfter Satz-2-Split | verworfen und in `M17_1-D` integriert; keine eigene finale `RR` und keine permanente Identifikation. Begründung: Oder-Struktur und die Atomizitätsregeln aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |

---

## 14. Scope-Audit

| Bereich | Ergebnis |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.2` | nicht extrahiert |
| `SRC-001#Anh.I/Nr.17.4` | nicht extrahiert |
| `SRC-001#Anh.I/Nr.2` | nicht systematisch extrahiert |
| `SRC-007` — IEC 62304 | keine Inhalte importiert |
| Cybersecurity-Scope erweitert | NEIN |
| Out-of-Scope-Atome | 0 |

---

## 15. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. **Keine** Methodenänderung erforderlich.

Besonders bestätigt:

- Applicability erzeugt keine Gap-`RR`;
- mehrere selbständige Produktmerkmale können unter einem gemeinsamen Designverb getrennt werden;
- ein gemeinsames Designverb erzeugt keine Meta-`RR`;
- eine Aussage der Form `A oder B` wird nicht in zwei kumulative `RR` verfälscht;
- Handlungsform und Ergebnis derselben Pflicht werden nicht künstlich getrennt;
- eine Fehlerbedingung ist nicht automatisch conditional Applicability;
- alternative Erfüllungswege bleiben innerhalb derselben `RR`;
- allgemeine Risikokontrollpflichten deduplizieren eine spezifische Single-Fault-Pflicht nicht automatisch.

---

## 16. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.17.1`. 4 finale neue MDR-Gap-`RR`-Kandidaten `M17_1-A` bis `M17_1-D`, alle regulär und 0 conditional. Satz 1 ergibt 3 `RR` für Wiederholbarkeit, Zuverlässigkeit und zweckbestimmungsgemäße Leistung; Satz 2 ergibt 1 gemeinsame Single-Fault-`RR` mit erhaltener Oder-Struktur. Die zunächst als `M17_1-E` geprüfte separate `RR` zur Leistungsbeeinträchtigung wurde nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 verworfen und in die gemeinsame Satz-2-`RR` `M17_1-D` zurückgeführt. 0 MDR-interne Deduplizierungen, 0 unresolved, 0 deferred, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. |
