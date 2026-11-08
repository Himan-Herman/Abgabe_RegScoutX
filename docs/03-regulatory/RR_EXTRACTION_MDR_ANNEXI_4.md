# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 4

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.4` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Kernbereich |
| Expected Theme | Qualitäts- und Risikomanagement |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.20 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M4-A` bis `M4-I` sind ausschließlich temporäre Evidenzkennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Neue MDR-Gap-`RR`-Kandidaten | **9** — `M4-A` bis `M4-I` |
| davon regulär | 7 |
| davon conditional | 2 — `M4-F`, `M4-H` |
| MDR-intern deduplizierte Atome | 0 |
| Unresolved | 0 |
| Deferred | 0 |
| Out-of-Scope-Atome | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 9 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Quellenstruktur und Lokatoren

Die Quellenstruktur wurde im aktuellen `SRC-001`-Rechtsstand verifiziert. Nr. 4 besteht aus vier Sätzen; der dritte Satz führt die Buchstaben a bis c ein.

| Locator | Inhalt |
| --- | --- |
| `SRC-001#Anh.I/Nr.4/Satz.1` | Sicherheitsgrundsätze und allgemein anerkannter Stand der Technik für Risikokontrollmaßnahmen |
| `SRC-001#Anh.I/Nr.4/Satz.2` | Akzeptabilität des gefahrenspezifischen Restrisikos und des Gesamtrestrisikos |
| `SRC-001#Anh.I/Nr.4/Satz.3` | vorgeschriebene Rangfolge bei der Wahl der am besten geeigneten Lösungen |
| `SRC-001#Anh.I/Nr.4/Satz.4` | Information der Anwender über etwaige Restrisiken |
| `SRC-001#Anh.I/Nr.4/Buchst.a` bis `SRC-001#Anh.I/Nr.4/Buchst.c` | die drei Stufen der Rangfolge |

Für den einleitenden Rahmen des dritten Satzes wird **kein** eigenes Locator-Element eingeführt; er wird ausschließlich über `Satz.3` geführt. Das entspricht dem zulässigen Elementvokabular aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4.

---

## 4. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Kandidaten |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.4/Satz.1` | 1 `RR` | `M4-A` |
| `SRC-001#Anh.I/Nr.4/Satz.2` | 2 `RR` | `M4-B`, `M4-C` |
| `SRC-001#Anh.I/Nr.4/Satz.3` | 1 eigenständige `RR` zur Prioritätshierarchie | `M4-D` |
| `SRC-001#Anh.I/Nr.4/Buchst.a` | 1 `RR` | `M4-E` |
| `SRC-001#Anh.I/Nr.4/Buchst.b` | 1 conditional `RR` | `M4-F` |
| `SRC-001#Anh.I/Nr.4/Buchst.c` | 2 `RR` | `M4-G`, `M4-H` |
| `SRC-001#Anh.I/Nr.4/Satz.4` | 1 `RR` | `M4-I` |
| **Gesamt** | **9** | |

---

## 5. Kandidaten

### M4-A — Sicherheitsgrundsätze und Stand der Technik bei Risikokontrollmaßnahmen

- **Title EN:** Safety Principles and State of the Art for Risk Control Measures
- **DE:** Der Hersteller muss sicherstellen, dass die für Auslegung und Herstellung des Produkts getroffenen Risikokontrollmaßnahmen den Sicherheitsgrundsätzen entsprechen und dabei den allgemein anerkannten Stand der Technik berücksichtigen.
- **EN:** The manufacturer shall ensure that risk control measures adopted for the design and manufacture of the device conform to safety principles, taking account of the generally acknowledged state of the art.
- **Primary:** `SRC-001#Anh.I/Nr.4/Satz.1`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Sicherheitsgrundsätze und Stand der Technik bleiben gemeinsam.

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | abstrakt unterscheidbar |
| Split-Bedingung 2 | nicht erfüllt |

Der allgemein anerkannte Stand der Technik ist verbindliches Qualitätsmerkmal desselben Risikokontroll-Sollzustands und bildet keine eigenständige vollständige Compliance-Aussage.

**Scope:** Die Erwähnung der Herstellung macht die Pflicht **nicht** zu einer ausgeschlossenen Produktionspflicht; primärer normativer Gegenstand ist die Risikokontrolle.

### M4-B — Akzeptabilität gefahrenspezifischer Restrisiken

- **Title EN:** Acceptability of Hazard-Specific Residual Risks
- **DE:** Der Hersteller muss die Risiken so managen, dass das mit jeder einzelnen Gefährdung verbundene Restrisiko als akzeptabel eingestuft wird.
- **EN:** The manufacturer shall manage risks so that the residual risk associated with each individual hazard is judged acceptable.
- **Primary:** `SRC-001#Anh.I/Nr.4/Satz.2`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

### M4-C — Akzeptabilität des Gesamtrestrisikos

- **Title EN:** Acceptability of the Overall Residual Risk
- **DE:** Der Hersteller muss die Risiken so managen, dass das Gesamtrestrisiko als akzeptabel eingestuft wird.
- **EN:** The manufacturer shall manage risks so that the overall residual risk is judged acceptable.
- **Primary:** `SRC-001#Anh.I/Nr.4/Satz.2`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität zu `M4-B` und `M4-C`:** Beide Split-Bedingungen sind erfüllt. Das gefahrenspezifische und das aggregierte Gesamtrestrisiko besitzen unabhängig bewertbare Compliance-Status: Jedes einzelne Restrisiko kann akzeptabel eingestuft sein, während das Gesamtrestrisiko es nicht ist, und umgekehrt.

### M4-D — Einhaltung der Prioritätshierarchie bei Risikokontrollmaßnahmen

- **Title EN:** Compliance with the Priority Order for Risk Control Measures
- **DE:** Bei der Wahl der am besten geeigneten Lösungen muss der Hersteller die Risikokontrollmaßnahmen in der vorgeschriebenen Reihenfolge priorisieren: zunächst Risikobeseitigung oder -minimierung durch sichere Auslegung und Herstellung, anschließend gegebenenfalls angemessene Schutzmaßnahmen für nicht auszuschließende Risiken und danach Sicherheitsinformationen sowie gegebenenfalls Anwenderschulung.
- **EN:** When selecting the most appropriate solutions, the manufacturer shall follow the prescribed order of priority: first eliminating or reducing risks as far as possible through safe design and manufacture, then, where appropriate, taking adequate protection measures for risks that cannot be eliminated, and thereafter providing information for safety and, where appropriate, training to users.
- **Primary:** `SRC-001#Anh.I/Nr.4/Satz.3`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Die Prioritätsreihenfolge besitzt einen eigenen Erfüllungsstatus. Sie bewertet **nicht** erneut die materielle Erfüllung von Buchst. a bis c, sondern deren regulatorisch vorgeschriebene Rangfolge. Damit entsteht keine Doppelzählung gegenüber `M4-E` bis `M4-H`.

### M4-E — Beseitigung oder weitestmögliche Minimierung von Risiken durch sichere Auslegung und Herstellung

- **Title EN:** Elimination or Reduction of Risks as Far as Possible Through Safe Design and Manufacture
- **DE:** Der Hersteller muss Risiken durch sichere Auslegung und Herstellung beseitigen oder so weit wie möglich minimieren; die Risikominderung ist dabei so weit vorzunehmen, wie dies ohne negative Auswirkungen auf das Nutzen-Risiko-Verhältnis möglich ist.
- **EN:** The manufacturer shall eliminate or reduce risks as far as possible through safe design and manufacture, with risk reduction being pursued as far as possible without adversely affecting the benefit-risk ratio.
- **Primary:** `SRC-001#Anh.I/Nr.4/Buchst.a`
- **Supplementary:** `SRC-001#Anh.I/Nr.4/Satz.3` · `SRC-001#Anh.I/Nr.2`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** „beseitigen oder minimieren" sind alternative bzw. abgestufte Erfüllungswege derselben Pflicht. „so weit wie möglich" ist wesentliche normative Qualifikation und **keine** eigene `RR`.

**Supplementary-Kontext:** `SRC-001#Anh.I/Nr.2` definiert für diesen Anhang die Bedeutung der weitestmöglichen Risikominderung und ist deshalb notwendiger normativer Kontext. Nr. 2 wurde **nicht** systematisch extrahiert; aus Nr. 2 entsteht keine `RR`.

### M4-F — Schutzmaßnahmen für nicht auszuschließende Risiken

- **Title EN:** Protective Measures for Risks That Cannot Be Eliminated
- **DE:** Soweit angemessen, muss der Hersteller im Hinblick auf Risiken, die nicht ausgeschlossen werden können, angemessene Schutzmaßnahmen ergreifen und dabei, soweit erforderlich, Alarmvorrichtungen vorsehen.
- **EN:** Where appropriate, the manufacturer shall take adequate protection measures in relation to risks that cannot be eliminated, including alarms where necessary.
- **Primary:** `SRC-001#Anh.I/Nr.4/Buchst.b`
- **Supplementary:** `SRC-001#Anh.I/Nr.4/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Ein Risiko kann nicht beseitigt werden und Schutzmaßnahmen sind nach der Prioritätshierarchie angemessen; Alarmvorrichtungen nur, soweit erforderlich.

**Atomizität:** Alarmvorrichtungen erhalten **keine** eigene `RR`. Die Formulierung „soweit erforderlich einschließlich Alarmvorrichtungen" konkretisiert die gemeinsame Schutzmaßnahmenpflicht. Beide Vorbehalte bleiben im Requirement Text erhalten.

### M4-G — Bereitstellung von Sicherheitsinformationen

- **Title EN:** Provision of Information for Safety
- **DE:** Der Hersteller muss im Rahmen der vorgeschriebenen Risikokontrollhierarchie Sicherheitsinformationen (Warnungen, Vorsichtshinweise und Kontraindikationen) bereitstellen.
- **EN:** The manufacturer shall, within the prescribed risk-control hierarchy, provide information for safety (warnings, precautions and contra-indications).
- **Primary:** `SRC-001#Anh.I/Nr.4/Buchst.c`
- **Supplementary:** `SRC-001#Anh.I/Nr.4/Satz.3`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Warnungen, Vorsichtshinweise und Kontraindikationen erhalten **keine** separaten `RR`. Sie bestimmen den Inhalt derselben Sicherheitsinformationspflicht.

**Theme-Begründung:** Primärer normativer Gegenstand ist die Bereitstellung von Information an den Anwender; die Einbettung in Nr. 4 erzwingt keine Zuordnung zum Cluster Qualitäts- und Risikomanagement.

### M4-H — Anwenderschulung als Risikokontrollmaßnahme

- **Title EN:** User Training as a Risk Control Measure
- **DE:** Soweit angemessen, muss der Hersteller im Rahmen der vorgeschriebenen Risikokontrollhierarchie Schulungen für Anwender bereitstellen.
- **EN:** Where appropriate, the manufacturer shall, within the prescribed risk-control hierarchy, provide training to users.
- **Primary:** `SRC-001#Anh.I/Nr.4/Buchst.c`
- **Supplementary:** `SRC-001#Anh.I/Nr.4/Satz.3`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null
- **Conditional:** JA
- **Trigger:** Eine Anwenderschulung ist im konkreten Risikokontrollkontext angemessen.

**Atomizität:** `M4-G` und `M4-H` bleiben getrennt. Sicherheitsinformation und erforderliche Schulung können unabhängig voneinander erfüllt oder verletzt werden; beide Split-Bedingungen sind erfüllt.

### M4-I — Information der Anwender über Restrisiken

- **Title EN:** Information of Users About Residual Risks
- **DE:** Der Hersteller muss die Anwender über etwaige Restrisiken informieren.
- **EN:** The manufacturer shall inform users of any residual risks.
- **Primary:** `SRC-001#Anh.I/Nr.4/Satz.4`
- **Supplementary:** keine
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** eigenständiger Sollzustand gegenüber `M4-G`. `M4-G` betrifft die allgemeine Sicherheitsinformation nach Buchst. c, `M4-I` die spezifische Information über die tatsächlich verbleibenden Restrisiken. Ein Hersteller kann allgemeine Sicherheitsinformationen bereitstellen, ohne alle verbleibenden Restrisiken mitzuteilen.

---

## 6. Conditional-Audit

| Kategorie | Anzahl | Kandidaten |
| --- | --- | --- |
| Regulär | 7 | `M4-A` · `M4-B` · `M4-C` · `M4-D` · `M4-E` · `M4-G` · `M4-I` |
| Conditional | 2 | `M4-F` · `M4-H` |

Die Bedingungen bleiben vollständig im Requirement Text erhalten. Es wird **keine** neue Schemaart und kein zusätzliches Feld eingeführt.

---

## 7. Theme-Audit

| Kandidat | Themencluster |
| --- | --- |
| `M4-A` | Qualitäts- und Risikomanagement |
| `M4-B` | Qualitäts- und Risikomanagement |
| `M4-C` | Qualitäts- und Risikomanagement |
| `M4-D` | Qualitäts- und Risikomanagement |
| `M4-E` | Qualitäts- und Risikomanagement |
| `M4-F` | Qualitäts- und Risikomanagement |
| `M4-G` | Transparenz |
| `M4-H` | Qualitäts- und Risikomanagement |
| `M4-I` | Transparenz |

Jeder Kandidat trägt genau **ein** Themencluster. Es wurde keine Mehrfachzuordnung und keine neue Taxonomie eingeführt.

---

## 8. MDR-interne Deduplizierung

| Bestehende `RR` | Ergebnis |
| --- | --- |
| `RR-151` — Beseitigung oder Kontrolle der bewerteten Risiken | keine vollständige Deduplizierung |
| `RR-153` — Erforderlichenfalls Anpassung der Kontrollmaßnahmen | keine vollständige Deduplizierung |

**Anzahl vollständig deduplizierter Atome: 0.**

**Begründung:** `RR-151` enthält die abstrakte Pflicht, die bewerteten Risiken gemäß Abschnitt 4 zu beseitigen oder zu kontrollieren. `RR-153` enthält die triggerabhängige Anpassung von Kontrollmaßnahmen gemäß Abschnitt 4. `M4-A` bis `M4-I` legen dagegen die konkreten materiellen Sollzustände für Qualität, Akzeptabilität, Priorität und Ausgestaltung der Risikokontrolle sowie die zugehörigen Informationspflichten fest. Die Erfüllungsstatus sind unabhängig: Ein Hersteller kann Risiken kontrollieren, ohne die vorgeschriebene Rangfolge einzuhalten oder die Akzeptabilitätsschwelle zu erreichen.

Dass `RR-151` und `RR-153` `SRC-001#Anh.I/Nr.4` bereits als Supplementary-Locator führen, begründet für sich genommen **keine** Deduplizierung. `RR-151` und `RR-153` bleiben unverändert.

---

## 9. Cross-Regulation

| MDR-Kandidat | AI-Act-Bestand | Ergebnis |
| --- | --- | --- |
| `M4-B` | `RR-022` | keine Deduplizierung |
| `M4-C` | `RR-023` | keine Deduplizierung |
| `M4-E` | `RR-024` | keine Deduplizierung |
| `M4-F` | `RR-025` | keine Deduplizierung |
| `M4-H` | `RR-026` | keine Deduplizierung |

**Begründung:** unterschiedliche Rechtsregime, regulatorische Rollen, Bezugsobjekte, Trigger und Compliance-Sollzustände. Eine nahezu identische Prozesslogik oder eine gemeinsame organisatorische Evidenz begründet **keine** normative Identität.

| Merkmal | Ergebnis |
| --- | --- |
| Cross-Regulation-Deduplizierungen | 0 |
| Bestehende AI-`RR` ändern | NEIN |

---

## 10. Context und 0-`RR`-Aussagen

| Fundstelle | Gegenstand | Behandlung |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.4/Satz.1` | allgemein anerkannter Stand der Technik | kein separater Kandidat; Qualifikation von `M4-A` |
| `SRC-001#Anh.I/Nr.4/Buchst.a` | „beseitigen oder minimieren" | alternative Erfüllungswege; kein Split |
| `SRC-001#Anh.I/Nr.2` | Bedeutung der weitestmöglichen Risikominderung | Supplementary-Kontext von `M4-E`; keine systematische Extraktion |
| `SRC-001#Anh.I/Nr.4/Buchst.b` | Alarmvorrichtungen | keine eigene `RR`; Konkretisierung von `M4-F` |
| `SRC-001#Anh.I/Nr.4/Buchst.c` | Warnungen, Vorsichtshinweise, Kontraindikationen | keine Einzel-`RR`; Inhalt von `M4-G` |

---

## 11. Multilingualer Audit

| Merkmal | Ergebnis |
| --- | --- |
| DE/EN | PASS |
| Materielle Divergenzen | 0 |
| Weitere Sprachen erforderlich | NEIN |
| Unresolved | 0 |

Geprüfte atomizitätsrelevante Begriffe, unter anderem: Sicherheitsgrundsätze / safety principles · allgemein anerkannter Stand der Technik / generally acknowledged state of the art · Restrisiko je Gefährdung / residual risk associated with each hazard · Gesamtrestrisiko / overall residual risk · als akzeptabel eingestuft / judged acceptable · Rangfolge / order of priority · beseitigen oder minimieren / eliminate or reduce · so weit wie möglich / as far as possible · sichere Auslegung und Herstellung / safe design and manufacture · gegebenenfalls / where appropriate · angemessene Schutzmaßnahmen / adequate protection measures · soweit erforderlich einschließlich Alarmvorrichtungen / including alarms if necessary · nicht auszuschließende Risiken / risks that cannot be eliminated · Sicherheitsinformationen / information for safety · Warnungen / warnings · Vorsichtshinweise / precautions · Kontraindikationen / contra-indications · Schulungen für Anwender / training to users · über etwaige Restrisiken unterrichten / inform users of any residual risks.

Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung automatisch als vorrangig behandelt.

---

## 12. Scope-Audit

| Bereich | Ergebnis |
| --- | --- |
| `SRC-001#Anh.I/Nr.2` | nicht systematisch extrahiert; ausschließlich Supplementary-Kontext von `M4-E` |
| Andere MDR-Bereiche | nicht systematisch extrahiert |
| ISO 14971 | keine Inhalte importiert |
| Out-of-Scope-Atome | 0 |

---

## 13. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. **Keine** Methodenänderung erforderlich.

Besonders bestätigt:

- Qualitätskriterien derselben Hauptpflicht bleiben zusammen;
- gefahrenspezifisches Restrisiko und Gesamtrestrisiko besitzen getrennte Erfüllungsstatus;
- die Prioritätshierarchie besitzt einen eigenen Erfüllungsstatus;
- Alternativen erzeugen keinen künstlichen Split;
- eine normative Definition aus einem nicht aktivierten Bereich kann Supplementary-Kontext sein;
- `including` erzeugt keinen automatischen Split;
- Sicherheitsinformation und Schulung können getrennte Pflichten bilden;
- allgemeine Sicherheitsinformation und Restrisikoinformation bleiben getrennt;
- die Konkretisierung einer referenzierten Top-Level-Pflicht ist nicht automatisch eine Deduplizierung.

---

## 14. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.4`. 9 finale neue MDR-Gap-`RR`-Kandidaten `M4-A` bis `M4-I`, davon 7 regulär und 2 conditional. 0 MDR-interne Deduplizierungen, 0 unresolved, 0 deferred, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen. `SRC-001#Anh.I/Nr.2` wurde ausschließlich als notwendiger normativer Supplementary-Kontext für `M4-E` verwendet und nicht systematisch extrahiert. |
