# Systematische RR-Extraktion — SRC-002 Art. 15

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` |
| Aktiver Quellenbereich | `SRC-002#Art.15/Abs.1` · `SRC-002#Art.15/Abs.3` · `SRC-002#Art.15/Abs.4` |
| Kontextuell geprüft, kein eigener Gap-Coverage-Bereich | `SRC-002#Art.15/Abs.2` · `SRC-002#Art.15/Abs.5` |
| Rechtsstand | konsolidierter Stand 27.07.2026 gemäß [SOURCES.md](SOURCES.md) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.7 |
| Bearbeitungsstatus der aktiven Bereiche | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Extraktionsstand. Sie vergibt **keine** permanenten `RR`-Identifikatoren; die Kandidaten tragen ausschließlich die temporären Kennungen `A15-A` bis `A15-G`. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Methodisches Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Finale neue Gap-`RR`-Kandidaten | **7** — `A15-A` bis `A15-G` |
| davon regulär | 5 |
| davon conditional | 2 — `A15-F`, `A15-G` |
| Unresolved | 0 |
| Deferred | 0 |
| Echte 0-`RR`-Fundstellen | 1 — `SRC-002#Art.15/Abs.4/UAbs.2` |
| Cross-Source-dedupliziert | 0 |
| Atomar erkannt, aber außerhalb Gap-Themen-Scope | 1 — Cybersecurity-Komponente aus `SRC-002#Art.15/Abs.1` |
| Operative aktive Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 7 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Vollständige `0 / 1 / n`-Prüfung

### 3.1 `SRC-002#Art.15/Abs.1`

Die vollständige Atomisierung des Absatzes ergibt **drei** eigenständige atomare Sollzustände:

| Nr. | Gegenstand | Behandlung |
| --- | --- | --- |
| 1 | Accuracy | A15-A |
| 2 | Robustness | A15-B |
| 3 | Cybersecurity | eigenständig atomar, aber außerhalb des Gap-Themen-Scope (Abschnitt 4) |

Die Lifecycle-Consistency-Klausel „perform consistently in those respects throughout their lifecycle" ist **keine** vierte `RR`. Sie qualifiziert jeweils die drei genannten Eigenschaften und bleibt deshalb Bestandteil der jeweiligen `RR`.

Damit wurde die Scope- und Atomizitätsregel aus [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 9.4 eingehalten: Der Absatz wurde zuerst vollständig atomisiert; die Cybersecurity-Komponente wurde **nicht** vorab entfernt.

### 3.2 `SRC-002#Art.15/Abs.3`

1 neue `RR` — A15-C.

Es besteht ein partieller Overlap mit `RR-050`, jedoch kein identischer Erfüllungsstatus. Eine Deduplizierung erfolgt nicht (Abschnitt 6).

### 3.3 `SRC-002#Art.15/Abs.4`

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-002#Art.15/Abs.4/UAbs.1` | 2 `RR` | A15-D (materieller Resilienz-Sollzustand), A15-E (technische und organisatorische Maßnahmen) |
| `SRC-002#Art.15/Abs.4/UAbs.2` | 0 `RR` | siehe Begründung unten |
| `SRC-002#Art.15/Abs.4/UAbs.3` | 2 conditional `RR` | A15-F, A15-G |

**Zu UAbs. 2 — 0 `RR`:** Die Formulierung „kann" bzw. „may be achieved" beschreibt technische Redundanz, Backup und Fail-Safe lediglich als mögliche technische Lösung. Daraus wird **keine** gesetzliche Pflicht abgeleitet; die Stelle bleibt Auslegungskontext.

A15-F und A15-G stehen unter der gemeinsamen Design- bzw. Development-Qualifikation des Unterabsatzes (Abschnitt 7).

---

## 4. Cybersecurity-Komponente aus `SRC-002#Art.15/Abs.1`

Die Atomisierung ergibt einen methodisch eigenständigen Sollzustand:

- ein angemessenes Cybersecurity-Niveau,
- eine hinsichtlich der Cybersecurity über den Lebenszyklus beständige Leistung.

Daraus entsteht im aktuellen Projektscope **keine** Gap-`RR`.

**Begründung:** [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) erlaubt keine künstliche Erweiterung des Clusters `Robustheit` zu einem allgemeinen Cybersecurity-Cluster. Es wird **kein** neuer Themencluster geschaffen. `SRC-002#Art.15/Abs.5` bestätigt systematisch den eigenständigen Cybersecurity-Regelungsgegenstand, wird aber selbst nicht als Gap-`RR` extrahiert und bleibt nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 9.5 außerhalb der Gap-Coverage.

**Kategorie dieser Entscheidung:** atomar erkannt, aber außerhalb Gap-Themen-Scope.

Ausdrücklich **nicht**: 0-`RR`, Cross-Source-Deduplizierung, unresolved oder deferred.

---

## 5. Kandidaten

### A15-A — Angemessenes und lebenszyklusbeständiges Genauigkeitsniveau

- **Title EN:** Appropriate and Lifecycle-Consistent Level of Accuracy
- **DE:** Der Anbieter muss sicherstellen, dass ein Hochrisiko-KI-System so konzipiert und entwickelt wird, dass es ein angemessenes Maß an Genauigkeit erreicht und hinsichtlich seiner Genauigkeit während seines gesamten Lebenszyklus beständig funktioniert.
- **EN:** The provider shall ensure that a high-risk AI system is designed and developed so that it achieves an appropriate level of accuracy and performs consistently in that respect throughout its lifecycle.
- **Primary:** `SRC-002#Art.15/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Accuracy besitzt gegenüber Robustheit und Cybersecurity einen unabhängig bestimmbaren Erfüllungsstatus. Die lebenszyklusweite Beständigkeit gehört zu demselben Accuracy-Sollzustand.

**Lifecycle-Begründung:** `Planung und Konzeption` wird nicht aufgenommen, weil „designed and developed" nach dem kontrollierten Vokabular die technische Realisierung betrifft. `Verifikation und Validierung` wird nicht aufgenommen, weil sie lediglich eine mögliche Nachweisphase darstellt.

### A15-B — Angemessenes und lebenszyklusbeständiges Robustheitsniveau

- **Title EN:** Appropriate and Lifecycle-Consistent Level of Robustness
- **DE:** Der Anbieter muss sicherstellen, dass ein Hochrisiko-KI-System so konzipiert und entwickelt wird, dass es ein angemessenes Maß an Robustheit erreicht und hinsichtlich seiner Robustheit während seines gesamten Lebenszyklus beständig funktioniert.
- **EN:** The provider shall ensure that a high-risk AI system is designed and developed so that it achieves an appropriate level of robustness and performs consistently in that respect throughout its lifecycle.
- **Primary:** `SRC-002#Art.15/Abs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Robustheit bildet gegenüber Accuracy und Cybersecurity einen eigenständig statusfähigen Sollzustand. Die Lifecycle-Consistency bleibt Bestandteil derselben `RR`.

### A15-C — Angabe von Genauigkeitsniveau und Genauigkeitsmetriken

- **Title EN:** Declaration of Accuracy Levels and Accuracy Metrics
- **DE:** Der Anbieter muss sicherstellen, dass die Maße an Genauigkeit und die relevanten Genauigkeitsmetriken des Hochrisiko-KI-Systems in den beigefügten Betriebsanleitungen angegeben werden.
- **EN:** The provider shall ensure that the levels of accuracy and the relevant accuracy metrics of the high-risk AI system are declared in the accompanying instructions for use.
- **Primary:** `SRC-002#Art.15/Abs.3`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Accuracy-Level und zugehörige Accuracy-Metriken bilden einen einheitlichen Informationsgegenstand.

### A15-D — Widerstandsfähigkeit gegenüber Fehlern, Störungen und Unstimmigkeiten

- **Title EN:** Resilience to Errors, Faults and Inconsistencies
- **DE:** Der Anbieter muss sicherstellen, dass das Hochrisiko-KI-System so widerstandsfähig wie möglich gegenüber Fehlern, Störungen oder Unstimmigkeiten ist, die innerhalb des Systems oder seiner Betriebsumgebung auftreten können, insbesondere infolge der Interaktion mit natürlichen Personen oder anderen Systemen.
- **EN:** The provider shall ensure that the high-risk AI system is as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which it operates, in particular due to interaction with natural persons or other systems.
- **Primary:** `SRC-002#Art.15/Abs.4/UAbs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Fehler, Störungen und Unstimmigkeiten konkretisieren denselben Resilienz-Sollzustand. `Verifikation und Validierung` ist keine Erfüllungsphase dieser materiellen Systemeigenschaft.

### A15-E — Technische und organisatorische Robustheitsmaßnahmen

- **Title EN:** Technical and Organisational Robustness Measures
- **DE:** Der Anbieter muss sicherstellen, dass in diesem Zusammenhang technische und organisatorische Maßnahmen ergriffen werden.
- **EN:** The provider shall ensure that technical and organisational measures are taken in this regard.
- **Primary:** `SRC-002#Art.15/Abs.4/UAbs.1`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** nein

**Atomizität:** Die Maßnahmepflicht ist ausdrücklich normiert und statusmäßig vom resultierenden Resilienz-Sollzustand A15-D unterscheidbar. „Technisch und organisatorisch" bleibt eine kumulative Maßnahmenklassifikation derselben Pflicht.

**Evidenznotiz:** Die frühere Paraphrase „um … zu gewährleisten" bzw. „to support the resilience" wurde verworfen, weil sie eine stärkere Zweck- bzw. Erfolgsbeziehung formulierte als der authentische Satz „in diesem Zusammenhang" bzw. „in this regard".

### A15-F — Beseitigung oder Verringerung von Feedback-Loop-Risiken

- **Title EN:** Elimination or Reduction of Feedback-Loop Risks
- **DE:** Bei einem Hochrisiko-KI-System, das nach dem Inverkehrbringen oder der Inbetriebnahme weiterlernt, muss der Anbieter sicherstellen, dass das System so entwickelt wird, dass das Risiko, dass möglicherweise verzerrte Ausgaben Eingaben für künftige Vorgänge beeinflussen und dadurch Rückkopplungsschleifen entstehen, beseitigt oder so weit wie möglich verringert wird.
- **EN:** For a high-risk AI system that continues to learn after being placed on the market or put into service, the provider shall ensure that the system is developed so as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations through feedback loops.
- **Primary:** `SRC-002#Art.15/Abs.4/UAbs.3`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** ja

**Trigger:** Das Hochrisiko-KI-System lernt nach dem Inverkehrbringen oder der Inbetriebnahme weiter.

**Atomizität:** Eigenständiges präventives Entwicklungsziel. „Beseitigen oder so weit wie möglich verringern" bleibt als Alternativstruktur innerhalb derselben `RR` erhalten.

### A15-G — Angemessene Mitigation bestehender Feedback-Loops

- **Title EN:** Appropriate Mitigation of Feedback Loops
- **DE:** Bei einem Hochrisiko-KI-System, das nach dem Inverkehrbringen oder der Inbetriebnahme weiterhin dazulernt, muss der Anbieter sicherstellen, dass das System so entwickelt wird, dass auf auftretende Rückkopplungsschleifen angemessen mit geeigneten Risikominderungsmaßnahmen eingegangen wird.
- **EN:** For a high-risk AI system that continues to learn after being placed on the market or put into service, the provider shall ensure that the system is developed in such a way as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Primary:** `SRC-002#Art.15/Abs.4/UAbs.3`
- **Supplementary:** `SRC-002#Art.16/Buchst.a`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** ja

**Trigger:** Das Hochrisiko-KI-System lernt nach dem Inverkehrbringen oder der Inbetriebnahme weiter.

**Atomizität:** Eigenständiges Entwicklungsziel gegenüber A15-F. Ein Systemdesign kann das Entstehungsrisiko angemessen reduzieren, aber dennoch keine angemessene Behandlung verbleibender Rückkopplungsschleifen sicherstellen — und umgekehrt.

**Evidenznotiz:** Die frühere Paraphrase ohne „so entwickelt wird" bzw. „is developed in such a way" wurde verworfen, weil sie die gemeinsame Design- bzw. Development-Qualifikation verlor.

---

## 6. Deduplizierungsentscheidung A15-C ↔ `RR-050`

| Merkmal | Befund |
| --- | --- |
| Materieller Overlap | ja |
| Vollständig statusidentisch | nein |
| Doppel-Gap-Risiko | partiell ja |
| Ergebnis | keine Cross-Source-Deduplizierung |

`RR-050` verlangt einen breiteren Informationsblock: Accuracy einschließlich Metriken, Robustheit, Cybersecurity, die Angabe, wogegen getestet und validiert wurde, sowie die erwartbaren Werte. `SRC-002#Art.15/Abs.3` verlangt spezifisch die Accuracy-Level, die relevanten Accuracy-Metriken und deren Angabe in den Betriebsanleitungen.

**Beispiel für unterschiedlichen Status:** Accuracy-Level und Accuracy-Metriken sind angegeben, Robustheits- oder Cybersecurity-Informationen fehlen. Dann ist A15-C erfüllt und `RR-050` nicht erfüllt.

Das partielle Doppel-Gap-Risiko reicht wegen der unterschiedlichen Sollzustände nicht für eine vollständige Cross-Source-Deduplizierung aus.

Final: A15-C bleibt eine eigenständige `RR`. `RR-050` erfährt **keine** materielle Änderung. `SRC-002#Art.15/Abs.3` wird **nicht** als `supplementary`-Lokator bei `RR-050` ergänzt; maßgeblich ist das Minimalitätsprinzip aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8.

---

## 7. Feedback-Loop-Split A15-F / A15-G

A15-F und A15-G bleiben zwei `RR`.

| Split-Bedingung nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 4 | Befund |
| --- | --- |
| 1 — Erfüllungsstatus können unabhängig unterschiedlich sein | erfüllt |
| 2 — jeder Bestandteil bildet eine vollständige regulatorisch sinnvolle Compliance-Aussage | erfüllt |

Die gemeinsame Design- bzw. Development-Qualifikation bleibt in **beiden** `RR` erhalten.

- A15-F: präventive Verringerung des Entstehungsrisikos.
- A15-G: das Design stellt die angemessene Behandlung tatsächlich auftretender Rückkopplungsschleifen sicher.

Daraus wird **keine** operative Betreiberpflicht gemacht; Adressat bleibt der Anbieter.

---

## 8. Multilingualer Audit

Geprüft nach dem Multilingual Source Divergence Protocol in [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 9.1.

Fundstelle: `SRC-002#Art.15/Abs.4/UAbs.3`.

| Fassung | Befund |
| --- | --- |
| EN | verzerrte Ausgaben beeinflussen die Eingaben künftiger Vorgänge — Output-Input-Struktur ausdrücklich |
| FR | entsprechende Output-Input-Struktur |
| ES | entsprechende Output-Input-Struktur |
| IT | entsprechende Output-Input-Struktur |
| DE | verkürzt formuliert, dass verzerrte Ausgaben künftige Vorgänge beeinflussen, ohne die Eingaben ausdrücklich zu nennen |

Materielle Divergenz: **ja**. Unresolved: **0**.

Keine Sprachfassung wurde priorisiert oder als führend erklärt; die Anzahl übereinstimmender Fassungen wurde **nicht** als Mehrheitsregel verwendet.

**Adjudikation:** Gemeinsamer normativer Gehalt ist die Rückkopplung von Ausgaben auf Eingaben. Systematisch bestätigt dies `SRC-002#Art.10/Abs.2/Buchst.f`, der denselben Feedback-Loop-Mechanismus auch im deutschen Text ausdrücklich über den Einfluss von Ausgaben auf Eingaben künftiger Operationen beschreibt. A15-F enthält deshalb die Formulierung, dass verzerrte Ausgaben Eingaben für künftige Vorgänge beeinflussen.

Die spätere Source-Fidelity-Korrektur von A15-G verändert diese Adjudikation **nicht**.

---

## 9. Cross-Article-Abgleich

| Bezug | Befund |
| --- | --- |
| Art. 9 | keine echte Dublette |
| Art. 10 | keine echte Dublette zu A15-F und A15-G; Art. 10 betrifft Data Governance und Datensätze, Art. 15 das fortlaufende Systemverhalten weiterlernender Systeme |
| Art. 13 | A15-C mit partiellem Overlap zu `RR-050`, jedoch keine Deduplizierung (Abschnitt 6) |
| Art. 14 | keine echte Dublette |
| Art. 17 | späterer Deduplizierungs- und Traceability-Punkt; kein Aktivierungsblocker |
| Art. 72 | späterer Traceability-Punkt; kein Aktivierungsblocker |

---

## 10. Locator-Audit

Alle formalen Lokatoren entsprechen der Syntax aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4. Ein Lokatorelement `Chapeau` wird nicht verwendet; externe URLs kommen nicht vor.

`Primary` ist jeweils so präzise wie möglich gesetzt; `supplementary` enthält ausschließlich die zur normativen Bestimmung erforderliche Ergänzung. Es wurden **keine** zusätzlichen Cross-Article-Lokatoren aufgenommen, die lediglich Zusammenhänge sichtbar machen würden.

---

## 11. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war für diesen Quellenbereich ausreichend. Eine Methodenänderung ist **nicht** erforderlich.

Abgedeckte Fallgestaltungen:

- Split kumulativer Systemeigenschaften,
- gemeinsame Lifecycle-Qualifikation nach dem Split,
- atomarer, aber außerhalb des Gap-Themen-Scope liegender Cybersecurity-Sollzustand,
- partieller Cross-Source-Overlap ohne vollständige Deduplizierung,
- Pflicht gegenüber optionaler technischer Lösung,
- conditional Requirements,
- präventive gegenüber mitigierenden Feedback-Loop-Designzielen,
- multilinguale Divergenz,
- Source-Fidelity-Nachadjudikation,
- Lifecycle-Audit.

Es wurde **keine** Art.-15-Sonderregel eingeführt.

---

## 12. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | angewandte Extraktions-, Atomizitäts- und Source-Fidelity-Methode (Version 1.2) |
| [COVERAGE_PLAN.md](COVERAGE_PLAN.md) | Freigabe der Quellenbereiche, Scope- und Atomizitätsregel zu Abs. 1, Einordnung von Abs. 2 und Abs. 5 (Version 1.7) |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | führende Vergabestelle; hier nicht verändert |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |
| [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | Identifikatoren und Lokator-Syntax |
| [RR_EXTRACTION_ART13.md](RR_EXTRACTION_ART13.md) | Herkunft von `RR-050` |
| [RR_EXTRACTION_ART14.md](RR_EXTRACTION_ART14.md) | vorangegangene systematische Extraktion |

---

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: vollständige systematische Extraktion der freigegebenen Bereiche `SRC-002` Art. 15 Abs. 1, Abs. 3 und Abs. 4; sieben Gap-`RR`-Kandidaten A15-A bis A15-G, davon fünf regulär und zwei conditional; 0 unresolved, 0 deferred; Cybersecurity-Komponente aus Abs. 1 atomar, aber außerhalb Gap-Themen-Scope; Abs. 4 UAbs. 2 mit 0 `RR`; multilingualer Feedback-Loop-Fall adjudiziert; A15-E und A15-G nach gezielter Source-Fidelity-Prüfung korrigiert; Lifecycle-Zuordnungen nach [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) auditiert. Keine Identifikatorvergabe. |
