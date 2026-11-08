# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 23.1

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.23.1` (Chapeau sowie Buchst. a bis h) |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Kernbereich |
| Expected Theme Clusters | Transparenz, Gebrauchstauglichkeit (Ex-ante-Erwartung) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.31 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M23_1-A` bis `M23_1-V` sind ausschließlich temporäre Evidenzkennungen; die permanenten Identifikatoren werden ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml) vergeben.

**Grundlage** sind zwei abgeschlossene Research-Berichte:

| Bezeichnung | Inhalt |
| --- | --- |
| Research-Bericht A | vollständige ursprüngliche `0 / 1 / n`-Extraktion von Nr. 23.1 |
| Research-Bericht B | gezielte Nachadjudikation zu `M23_1-U`/`M23_1-V` (Triggerlogik), `M23_1-C`/`M23_1-D` (Empfängerkreis), `M23_1-P` (negative Ausnahme) und `M23_1-R` (externe Rechtsquelle) |

Bei diesen vier nachadjudizierten Punkten hat Bericht B Vorrang vor Bericht A (Abschnitt 17). Die finalen DE-/EN-Requirement-Texte beruhen auf den Kurzfassungen aus Bericht A und wurden als strukturierte normative Paraphrasen gesondert fachlich freigegeben; sie sind keine wörtlichen Gesetzeszitate.

**Quellentreue:** Einzelne Verweise in Bericht B auf eine ältere MDR-Konsolidierung und auf nicht rechtsverbindliche MDCG-Guidance sind **nicht** Entscheidungsgrundlage dieser Extraktion und werden nicht übernommen. Sämtliche Entscheidungen sind ausschließlich gegen `SRC-001` in der Fassung `02017R0745-20260719` dokumentiert.

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Geprüfte potenzielle Einheiten | **27** |
| Neue MDR-Gap-`RR`-Kandidaten | **22** — `M23_1-A` bis `M23_1-V` |
| davon regulär | 13 |
| davon conditional | 9 — `M23_1-E`, `M23_1-F`, `M23_1-M`, `M23_1-Q`, `M23_1-R`, `M23_1-S`, `M23_1-T`, `M23_1-U`, `M23_1-V` |
| 0-`RR` / keine separate `RR` | 5 |
| Out-of-Scope-Atome | 0 |
| MDR-intern vollständig deduplizierte Atome | 0 |
| Unresolved | 0 |
| Deferred | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |
| SOURCE_DEPENDENCY | `M23_1-R` (zwingend); `M23_1-U` und `M23_1-V` (für die vollständige Operationalisierung) |

| Themencluster | Anzahl |
| --- | --- |
| Transparenz | 13 |
| Gebrauchstauglichkeit | 9 |

Es wurde **keine** quantitative Zielzahl verwendet; die Zahl 22 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode ([COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12).

---

## 3. Source Verification

**Ergebnis `SRC-001`: PASS.**

| Merkmal | Befund |
| --- | --- |
| Verwendete Fassung | ausschließlich die MDR-Fassung `02017R0745-20260719`, Stand 19.07.2026; EUR-Lex kennzeichnet genau diese Fassung als aktuelle konsolidierte Version |
| Geprüfte Sprachfassungen | DE und EN primär |
| Geprüfter Umfang | Chapeau sowie Buchst. a bis h |
| Strukturübereinstimmung DE/EN | DE und EN stimmen hinsichtlich der für Atomisierung und Conditionality relevanten Strukturen überein: `may`/„können" bei zulässigen Informationsorten, `shall` bei Website-Bereitstellung und -Aktualisierung, `where appropriate`/„gegebenenfalls", die Ausnahme in Buchst. d, die Erlaubnisse in Buchst. b, c, e und f sowie die drei konditionalen Ebenen von Buchst. h |
| Weitere Sprachfassung | für die finale Atomisierung nicht erforderlich |
| Sprachliche Unterschiede | „aktualisiert" gegenüber `kept up to date` sowie DE „Spezifikationen" gegenüber EN `CS` verändern die zu entscheidende Pflichtstruktur nicht |
| Unresolved Sprachdivergenzen | 0 |

---

## 4. Chapeau (Nr. 23.1, Satz 1 und Satz 2)

**Ergebnis: 6 `RR` und 1 0-`RR`-Element.**

Die MDR verlangt Identifizierungs-, Sicherheits- und Leistungsinformationen; die möglichen Orte Produkt, Verpackung und Gebrauchsanweisung sind dagegen permissive Erfüllungsorte. Bei bestehender Herstellerwebsite sind Bereitstellung **und** Aktualhaltung verpflichtend.

### 4.1 Identifizierungs- und Informationspflichten (Satz 1)

| Kandidat | Ergebnis | Begründung |
| --- | --- | --- |
| `M23_1-A` — Identifizierung des Produkts | eigene `RR` | Ein Produkt kann eindeutig identifizierbar sein, während der Hersteller nicht identifizierbar ist, oder umgekehrt. Beide Split-Bedingungen sind erfüllt. |
| `M23_1-B` — Identifizierung des Herstellers | eigene `RR` | aus demselben Grund |
| `M23_1-C` — relevante Sicherheitsinformationen | eigene `RR` | Sicherheits- und Leistungsinformationen besitzen unabhängig bewertbare Compliance-Zustände. |
| `M23_1-D` — relevante Leistungsinformationen | eigene `RR` | wie `M23_1-C` |

### 4.2 Empfängerkreiserweiterung bei `M23_1-C` und `M23_1-D` (final nach Bericht B)

Der Chapeau verlangt Sicherheits- und Leistungsinformationen, die für den Anwender oder, soweit einschlägig, eine andere Person relevant sind. Die Bedingung „soweit einschlägig" / `as appropriate` betrifft die **Erweiterung des Empfängerkreises**, nicht die Existenz der Grundpflicht gegenüber dem Anwender.

| Merkmal | `M23_1-C` und `M23_1-D` |
| --- | --- |
| Outer Conditional | NEIN |
| Inner Conditional der gesamten `RR` | NEIN |
| Grundpflicht gegenüber dem vorgesehenen Anwender | unbedingt |
| Bedingte Empfängerkreiserweiterung | JA |
| Auslöser der Erweiterung | Die jeweilige Sicherheits- bzw. Leistungsinformation ist für eine andere Person als den Anwender relevant. |
| Methodische Einordnung | bedingte Umfangsqualifikation derselben Pflicht; keine Bedingung der gesamten `RR` |

Eine Modellierung als `Inner Conditional = JA` würde fälschlich suggerieren, die gesamte Sicherheits- bzw. Leistungsinformationspflicht gelte nur bei Eintritt dieser Bedingung. Echte Bedingungen werden von Ausnahmen, alternativen Erfüllungsformen und Modalitäten unterschieden. Da das Katalogschema kein eigenes Feld vorsieht, bleibt die Empfängerkreiserweiterung im Requirement Text erhalten („für den Anwender sowie, soweit einschlägig, für andere Personen relevanten …" / „relevant to the user or, as appropriate, any other person"). Die Formulierung bildet die Erweiterung ab, ohne zu suggerieren, dass Informationen einer anderen Person unmittelbar separat bereitgestellt werden müssen.

### 4.3 Informationsorte (Satz 2) — 0 `RR`

Produkt selbst, Verpackung oder Gebrauchsanweisung: **0 `RR` — PERMISSION / Erfüllungsmodalität.** „können" / `may appear` eröffnet zulässige Informationsorte. Daraus entsteht keine zusätzliche Pflicht, sämtliche drei Medien zu verwenden.

### 4.4 Website (Satz 2)

| Kandidat | Ergebnis | Trigger |
| --- | --- | --- |
| `M23_1-E` — Bereitstellung auf der Herstellerwebsite | eigene `RR`, conditional | Hersteller verfügt über eine Website |
| `M23_1-F` — Aktualhaltung der Informationen auf der Herstellerwebsite | eigene `RR`, conditional | Hersteller verfügt über eine Website |

**Split-Test erfüllt:** Informationen können online verfügbar, aber veraltet sein. Umgekehrt setzt Aktualhaltung zwar faktisch Verfügbarkeit voraus; der Sollzustand des aktuellen Inhalts bleibt aber regulatorisch eigenständig prüfbar. Das englische `made available and kept up to date` bestätigt diese Zweiteilung.

---

## 5. Buchstabe a

### 5.1 Satz 1 — Merkmalsreihe

Satz 1 enthält fünf ausdrücklich normierte Eigenschaften von Kennzeichnung und Gebrauchsanweisung: Medium, Format, Inhalt, Lesbarkeit und Anbringungsstelle. Alle fünf stehen unter demselben Eignungsmaßstab bezüglich Produkt, Zweckbestimmung und Nutzerprofil.

Es greift der Merkmalsreihen-Fall nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 7 (Fall B): Ein Split ist geboten, wenn jedes Merkmal eigenständig verlangt wird und sein Status unabhängig abweichen kann. Die Methode unterscheidet zwischen unselbständigen Konkretisierungen und selbständig bewertbaren Merkmalen. Hier liegen selbständig bewertbare Merkmale vor: Ein Label kann z. B. geeignet lesbar, aber im falschen Medium oder an ungeeigneter Stelle bereitgestellt werden. Die Aussagen „Medium muss geeignet sein", „Format muss geeignet sein" usw. sind jeweils vollständige Soll-Aussagen.

**Ergebnis: 5 `RR`** — `M23_1-G` (Medium), `M23_1-H` (Format), `M23_1-I` (Inhalt), `M23_1-J` (Lesbarkeit), `M23_1-K` (Anbringungsstelle).

Die Kriterien Produkt, Zweckbestimmung, technische Kenntnisse, Erfahrung, Ausbildung und Schulung werden **nicht** nochmals atomisiert; sie konkretisieren jeweils den Eignungsmaßstab.

### 5.2 Satz 2

| Kandidat | Ergebnis | Begründung |
| --- | --- | --- |
| `M23_1-L` — Verständlichkeit der Gebrauchsanweisung | eigene `RR` | Die Gebrauchsanweisung muss in einer für den vorgesehenen Anwender ohne Schwierigkeiten verständlichen Form formuliert sein. |
| `M23_1-M` — Ergänzung durch Zeichnungen und Schaubilder | eigene `RR`, conditional (Trigger „gegebenenfalls" / `where appropriate`) | Verständlichkeit kann gegeben sein, obwohl im konkreten Fall erforderliche grafische Ergänzungen fehlen. Umgekehrt ersetzen Zeichnungen eine sprachlich unverständliche Gebrauchsanweisung nicht. Beide Komponenten besitzen vollständige regulatorische Sollzustände. |

**Ergebnis Buchst. a: 7 `RR`.**

### 5.3 Theme Buchst. a

| Kandidaten | Theme | Begründung |
| --- | --- | --- |
| `M23_1-G`, `M23_1-H`, `M23_1-J`, `M23_1-K`, `M23_1-L`, `M23_1-M` | Gebrauchstauglichkeit | Im Vordergrund steht die nutzerbezogene Erfassbarkeit bzw. Darstellungsform der Herstellerinformation. |
| `M23_1-I` | Transparenz | Primärer normativer Gegenstand ist die inhaltliche Eignung der Herstellerinformation. |

---

## 6. Buchstabe b

Grundregel: Vorgeschriebene Kennzeichnungsinformationen befinden sich auf dem Produkt selbst. Nur falls dies nicht praktikabel oder angemessen ist, **dürfen** einige oder alle Angaben auf Einzel- oder Mehrfachverpackung erscheinen.

**Ergebnis: 1 `RR` — `M23_1-N`.** Der Verpackungsfall wird **nicht** als zweite `RR` abgespalten: „können" / `may` definiert einen bedingten alternativen Erfüllungsweg zur Grundpflicht. Die Ausnahme bleibt im Requirement Text erhalten, ohne aus einer Erlaubnis eine Pflicht zu machen.

**Software-Scope: IN SCOPE.** Software kann nach der MDR selbst ein Medizinprodukt sein; die MDR definiert die Kennzeichnung als schriftliche, gedruckte oder grafische Information am Produkt oder seiner Verpackung. Die Verpflichtung ist daher nicht allein aufgrund des Verpackungsbegriffs physischer Hardware vorbehalten.

**Interner Kontext:** Zur vollständigen Bestimmung, **welche** Informationen „für die Kennzeichnung vorgeschrieben" sind, ist Nr. 23.2 interner MDR-Kontext. Nr. 23.2 wird hier ausdrücklich **nicht** extrahiert und nicht als Supplementary-Locator geführt.

**Theme:** Transparenz.

---

## 7. Buchstabe c

| Bestandteil | Ergebnis | Begründung |
| --- | --- | --- |
| Kennzeichnung in vom Menschen lesbarer Form | 1 `RR` — `M23_1-O` | Die Pflicht ist eindeutig mit `shall` bzw. „werden" formuliert. |
| Ergänzung durch RFID, Barcode oder sonstige maschinenlesbare Informationen | 0 `RR` — PERMISSION | Mit `may be supplemented` bzw. „können … ergänzt werden" permissiv formuliert; darf nicht als Gap-Pflicht erscheinen. |

**Software-Scope: IN SCOPE.** Gerade bei Software kann eine vom Menschen lesbare Information innerhalb der Produktoberfläche oder anderer zulässiger Informationsmedien relevant sein.

**Theme `M23_1-O`:** Gebrauchstauglichkeit.

---

## 8. Buchstabe d — negative Ausnahme (final nach Bericht B)

Buchst. d beginnt mit einer allgemeinen Grundpflicht: Die Gebrauchsanweisung ist zusammen mit dem Produkt bereitzustellen. Anschließend folgt ausdrücklich „abweichend davon" / `by way of exception` eine Befreiung für bestimmte Produkte der Klassen I und IIa.

**Ergebnis: 1 reguläre `RR` — `M23_1-P`.** Die Ausnahme wird **nicht** zu einer positiven zweiten `RR`.

**Logik der Ausnahme:** Die Grundpflicht entfällt nur, wenn kumulativ

1. das Produkt der Klasse I oder IIa angehört,
2. die sichere Anwendung ohne Gebrauchsanweisung gewährleistet ist und
3. an anderer Stelle des Abschnitts 23 keine Gebrauchsanweisung verlangt wird.

```
IFU_REQUIRED = NOT (
  CLASS in {I, IIa}
  AND SAFE_USE_WITHOUT_IFU
  AND NO_OTHER_SECTION_23_IFU_REQUIREMENT
)
```

Klasse I oder IIa ist **kein** positiver Trigger der Grundpflicht, sondern nur eine notwendige Voraussetzung der negativen Ausnahme. Unzulässig wäre insbesondere die Lesart `IF Klasse I oder IIa → IFU-Pflicht`.

| Merkmal | `M23_1-P` |
| --- | --- |
| Outer Conditional | NEIN |
| Inner Conditional | NEIN |
| Ausnahme | negative Ausnahme mit drei kumulativen Voraussetzungen; im Requirement Text vollständig erhalten |
| Zählung | regulär |

Eine hypothetische `RR` „Der Hersteller muss gewährleisten, dass Klasse-I-/IIa-Produkte sicher ohne Gebrauchsanweisung verwendet werden können" wäre methodisch falsch: Die Quelle verpflichtet den Hersteller nicht, diese Ausnahme nutzbar zu machen.

**Software-Scope: IN SCOPE. Theme:** Transparenz. **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb.

---

## 9. Buchstabe e

| Bestandteil | Ergebnis | Begründung |
| --- | --- | --- |
| eine einzige Ausfertigung der Gebrauchsanweisung bei Mehrfachlieferung an einen Anwender bzw. Ort mit Zustimmung des Käufers | 0 `RR` — PERMISSION | regulatorische Erlaubnis |
| kostenlose weitere Exemplare auf Anforderung des Käufers | 1 `RR` — `M23_1-Q` | eigenständiger Pflichtgehalt: Der Käufer darf weitere Exemplare verlangen, die kostenlos bereitgestellt werden müssen |

**Conditionality `M23_1-Q`:** mehrere Produkte werden an einen Anwender und/oder Ort geliefert **und** der Käufer fordert weitere Exemplare an.

**Software-Scope:** Die Pflicht besitzt auch für Software einen horizontalen Beitrag. Der Begriff „Exemplare" ist nicht zwingend auf gedruckte Papierunterlagen beschränkt; die Quelle begründet jedenfalls ein Recht auf weitere kostenfreie Ausfertigungen der Gebrauchsanweisung.

**Theme:** Transparenz.

---

## 10. Buchstabe f — `M23_1-R` und SOURCE_DEPENDENCY

Zu unterscheiden ist zwischen der Erlaubnis und ihrer normativen Begrenzung: Buchst. f erlaubt eine andere Form als Papier **nur** in dem Umfang und unter den Bedingungen des dort bezeichneten Durchführungsrechts.

**Ergebnis: 1 conditional `RR` — `M23_1-R`.** Das ist mehr als eine bloße Erlaubnis, weil die Wendung `only under the conditions` einen eigenständig prüfbaren Compliance-Rahmen erzeugt.

| Merkmal | `M23_1-R` |
| --- | --- |
| Outer Conditional | NEIN |
| Inner Conditional | JA |
| Trigger | Gebrauchsanweisung wird in Nicht-Papierform, z. B. elektronisch, bereitgestellt |
| SOURCE_DEPENDENCY | JA |

### 10.1 Externe normative Abhängigkeit

| Merkmal | Angabe laut Research-Berichten |
| --- | --- |
| Externe Rechtsquelle | Durchführungsverordnung (EU) 2021/2226 |
| Fassung | konsolidierte Fassung 16.07.2025, einschließlich der Änderung durch Durchführungsverordnung (EU) 2025/1234 |
| Status | laut EUR-Lex in Kraft |
| Bezug | Art. 1 legt ausdrücklich die Bedingungen fest, unter denen Gebrauchsanweisungen im Sinne von MDR Anhang I Nr. 23.1 Buchst. f elektronisch bereitgestellt werden dürfen. Art. 10 hebt die frühere Verordnung (EU) Nr. 207/2012 auf und bestimmt, dass Verweise darauf als Verweise auf 2021/2226 zu lesen sind. |
| Registrierung | **keine** `SRC`-ID, **kein** Supplementary-Locator, **keine** daraus extrahierte `RR` |

**Abgrenzung:**

- `SRC-001` bestimmt den MDR-Sollzustand: Nicht-Papier-Gebrauchsanweisungen sind nur im zulässigen Umfang und unter den einschlägigen Durchführungsbedingungen zulässig.
- Die externe Verordnung bestimmt die konkreten Durchführungsbedingungen; deren Inhalt steht nicht vollständig in der MDR. `SRC-001` allein reicht deshalb für die vollständige Ja/Nein-Prüfung dieses Gaps nicht aus.
- Die Dependency betrifft **nicht** Existenz, Atomizität oder normative Bedeutung von `M23_1-R`; diese sind aus `SRC-001` hinreichend bestimmt. Sie betrifft die nachgelagerte vollständige Operationalisierung des Gap-Tests.
- Daraus folgt kein Unresolved; `uncertainty` bleibt `null`; der Katalogstatus `aktiv` ist methodisch vertretbar. Die Extraktionsmethode unterscheidet zwischen einem unauflösbaren Sachverhalt und einer externen normativen Abhängigkeit.

### 10.2 Spätere Registrierung

| Frage | Ergebnis laut Bericht B |
| --- | --- |
| Registrierung von 2021/2226 für die spätere vollständige Operationalisierung erforderlich | JA |
| Registrierung vor Abschluss der Extraktion von Nr. 23.1 erforderlich | NEIN — nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 10.2 dürfen neue Quellenbereiche nicht ad hoc während einer laufenden Extraktion aufgenommen werden; sie sind vor ihrer eigenen Extraktion per Change Control freizugeben |
| Empfohlene spätere Einordnung | Ebene A (rechtsverbindliche Quelle), Nutzungsart `triggerbasiert` nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 4.2 |
| Empfohlener Trigger | elektronische bzw. Nicht-Papier-Gebrauchsanweisung im Anwendungsbereich von Nr. 23.1 Buchst. f |

Die Einordnung ist eine Empfehlung für eine spätere separate Coverage Change Control; sie wird hier nicht umgesetzt. Solange die Abhängigkeit für einen aktivierten eIFU-Fall offen ist, ist der Gesamtkorpus insoweit noch nicht vollständig operationalisiert. Das verhindert den Abschluss des Quellenbereichs `SRC-001#Anh.I/Nr.23.1` nicht.

---

## 11. Buchstabe g

**Ergebnis: 1 `RR` — `M23_1-S`.** Die Quelle verlangt einen einheitlichen Sollzustand: Mitzuteilende Restrisiken müssen in den Herstellerinformationen als Beschränkungen, Kontraindikationen, Vorsichtsmaßnahmen oder Warnungen enthalten sein. Die vier Formen werden **nicht** mikroatomisiert; sie sind zulässige Ausprägungen innerhalb derselben `RR`.

| Merkmal | `M23_1-S` |
| --- | --- |
| Inner Conditional | JA |
| Trigger | Es besteht ein Restrisiko, das dem Anwender und/oder einer anderen Person mitzuteilen ist |
| Theme | Transparenz — unmittelbarer Gegenstand ist die Mitteilung bzw. Aufnahme in die Herstellerinformationen, nicht die vorgelagerte Risikobewertung |
| Software-Scope | IN SCOPE |

---

## 12. Buchstabe h — `M23_1-T`, `M23_1-U`, `M23_1-V`

Buchst. h enthält drei aufeinander bezogene Regelungsebenen: Zunächst sollen Herstellerinformationen, soweit angemessen, international anerkannte Symbole verwenden. Danach müssen verwendete Symbole oder Identifizierungsfarben den harmonisierten Normen oder Gemeinsamen Spezifikationen entsprechen. Der unmittelbar folgende Satz regelt ausdrücklich den Gegenfall, dass für den betreffenden Bereich **keine** harmonisierten Normen oder Gemeinsamen Spezifikationen existieren.

### 12.1 `M23_1-T` — international anerkannte Symbole

Eigene conditional `RR`. Trigger: Verwendung international anerkannter Symbole ist „wo dies angebracht ist" / `where appropriate`. Theme: Gebrauchstauglichkeit.

`M23_1-T` wird nicht mit `M23_1-U`/`M23_1-V` zusammengefasst: Ein Hersteller kann beispielsweise ein standardkonformes Symbol verwenden und dennoch in einem anderen Bereich ein nicht standardisiertes Symbol ohne erforderliche Erläuterung einsetzen.

### 12.2 `M23_1-U` und `M23_1-V` — komplementäre Triggerzweige (final nach Bericht B)

Die zweite und dritte Regel sind als komplementäre Verzweigung zu lesen:

```
verwendetes Symbol / verwendete Identifizierungsfarbe
  → einschlägige harmonisierte Norm/CS vorhanden       → M23_1-U (Standard-/CS-Zweig)
  → keine einschlägige harmonisierte Norm/CS vorhanden → M23_1-V (No-standard-/No-CS-Zweig)
```

| Kandidat | Finaler Trigger | Rechtsfolge | Theme |
| --- | --- | --- | --- |
| `M23_1-U` | Symbol oder Identifizierungsfarbe wird verwendet **UND** für den betreffenden Bereich existiert eine einschlägige harmonisierte Norm oder Gemeinsame Spezifikation | Symbol bzw. Farbe muss dieser entsprechen | Gebrauchstauglichkeit |
| `M23_1-V` | Symbol oder Identifizierungsfarbe wird verwendet **UND** für den betreffenden Bereich existiert **keine** einschlägige harmonisierte Norm oder Gemeinsame Spezifikation | Erläuterung in der mit dem Produkt bereitgestellten Dokumentation | Transparenz |

- `M23_1-U` und `M23_1-V` sind **keine** kumulativ nebeneinander geltenden Anforderungen. Für dasselbe konkrete Symbol im selben sachlichen Bereich können sie nicht gleichzeitig aktiviert werden.
- „where appropriate" aus dem ersten Satz von Buchst. h ist **kein** zusätzlicher Trigger von `M23_1-U`. Es qualifiziert die vorgelagerte Verpflichtung aus `M23_1-T`, Herstellerinformationen in Form international anerkannter Symbole bereitzustellen. Sobald ein Symbol oder eine Identifizierungsfarbe tatsächlich verwendet wird, greifen `M23_1-U` oder `M23_1-V` nach ihrer jeweiligen Verzweigungslogik.
- Der ursprüngliche Trigger von `M23_1-U` in Bericht A („Symbol oder Identifizierungsfarbe wird verwendet") war unvollständig spezifiziert und ist durch Bericht B präzisiert (Abschnitt 17). Atomisierung, Anzahl der `RR` und Conditionality bleiben unverändert.

### 12.3 SOURCE_DEPENDENCY `M23_1-U` und `M23_1-V`

**SOURCE_DEPENDENCY: JA für beide**, für die spätere vollständige Operationalisierung.

| Kandidat | Später erforderlicher belastbarer Nachweis |
| --- | --- |
| `M23_1-U` | (1) ob für den konkreten Symbol- bzw. Farbbereich eine einschlägige harmonisierte Norm oder Gemeinsame Spezifikation existiert; (2) welche dies ist; (3) ob das tatsächlich verwendete Symbol bzw. Farbkennzeichen ihr entspricht |
| `M23_1-V` | dass für den konkreten Bereich gerade **keine** einschlägige harmonisierte Norm oder Gemeinsame Spezifikation existiert; erst dann wird der Erläuterungs-Fallback aktiviert |

Die MDR selbst enthält diese dynamische externe Bestandsinformation nicht; Buchst. h stellt nur die Entscheidungslogik bereit. `M23_1-U` und `M23_1-V` bleiben als MDR-`RR` vollständig bestimmbar und `aktiv`; die Applicability- bzw. Compliance-Entscheidung im konkreten Fall benötigt externe normative Evidenz. Es wird **keine** konkrete Norm oder Gemeinsame Spezifikation ausgewählt oder extrahiert.

---

## 13. 0-`RR`-Entscheidungen

| Nr. | Fundstelle | Bestandteil | Behandlung |
| --- | --- | --- | --- |
| 1 | Chapeau, Satz 2 | mögliche Orte Produkt, Verpackung, Gebrauchsanweisung | 0 `RR` — PERMISSION / Erfüllungsmodalität |
| 2 | Buchst. b | Verpackung als Fallback bei fehlender Praktikabilität bzw. Angemessenheit | keine separate `RR` — alternative Modalität innerhalb `M23_1-N` |
| 3 | Buchst. c | zusätzliche maschinenlesbare Informationen | 0 `RR` — PERMISSION |
| 4 | Buchst. d | Ausnahme für Klasse I/IIa | keine separate `RR` — negative Ausnahme innerhalb `M23_1-P` |
| 5 | Buchst. e | eine einzige Ausfertigung der Gebrauchsanweisung bei vereinbarter Mehrfachlieferung | 0 `RR` — PERMISSION |

Die Nutzerfaktoren in Buchst. a sowie Beschränkungen, Kontraindikationen, Vorsichtsmaßnahmen und Warnungen in Buchst. g werden **nicht** zusätzlich als 0-`RR` gezählt: Sie sind unselbständige Kriterien bzw. zulässige Ausprägungen innerhalb der jeweiligen finalen `RR`.

**Zählung:** 22 `RR` + 5 0-`RR`-Entscheidungen = 27 geprüfte potenzielle Einheiten.

---

## 14. Theme, Lebenszyklus und Conditionality

### 14.1 Lifecycle-Begründung

Die hohe Belegung von `Inverkehrbringen, Inbetriebnahme und Betrieb` ist sachlich erwartbar: Nr. 23.1 regelt gerade Informationen, die mit dem Produkt geliefert bzw. dem Nutzer bereitgestellt werden. `Entwicklung und Realisierung` wurde nur dort zusätzlich vergeben, wo die atomare Pflicht die Erstellung, Gestaltung bzw. inhaltliche Ausprägung des Informationsartefakts betrifft. `Änderung und Wartung` wurde nur bei solchen Qualitäts- bzw. Inhaltszuständen sowie bei der ausdrücklichen Website-Aktualisierung berücksichtigt. Eine reine spätere Nutzung der Information erzeugt keine zusätzliche Lebenszyklusphase.

| Phase | Anzahl Kandidaten |
| --- | --- |
| Planung und Konzeption | 0 |
| Entwicklung und Realisierung | 17 |
| Verifikation und Validierung | 0 |
| Konformitätsbewertung | 0 |
| Inverkehrbringen, Inbetriebnahme und Betrieb | 22 |
| Post-Market-Überwachung | 0 |
| Änderung und Wartung | 18 |

### 14.2 Übersicht

| Kandidat | Theme | Lebenszyklusphasen | Einordnung | Bedingung / Ausnahme / Modalität |
| --- | --- | --- | --- | --- |
| `M23_1-A` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-B` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-C` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | bedingte Empfängerkreiserweiterung (Abschnitt 4.2) |
| `M23_1-D` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | bedingte Empfängerkreiserweiterung (Abschnitt 4.2) |
| `M23_1-E` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | conditional | Hersteller verfügt über eine Website |
| `M23_1-F` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | conditional | Hersteller verfügt über eine Website |
| `M23_1-G` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-H` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-I` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-J` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-K` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-L` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-M` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | conditional | „gegebenenfalls" / `where appropriate` |
| `M23_1-N` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | alternative Erfüllungsmodalität Verpackung (0-`RR` Nr. 2) |
| `M23_1-O` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | regulär | — |
| `M23_1-P` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | regulär | negative Ausnahme mit drei kumulativen Voraussetzungen (Abschnitt 8) |
| `M23_1-Q` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | conditional | Mehrfachlieferung an einen Anwender und/oder Ort **und** Anforderung weiterer Exemplare durch den Käufer |
| `M23_1-R` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | conditional | Gebrauchsanweisung in Nicht-Papierform; SOURCE_DEPENDENCY |
| `M23_1-S` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | conditional | mitzuteilendes Restrisiko besteht |
| `M23_1-T` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | conditional | „wo dies angebracht ist" / `where appropriate` |
| `M23_1-U` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | conditional | Symbol/Farbe verwendet **und** einschlägige harmonisierte Norm/CS vorhanden; SOURCE_DEPENDENCY |
| `M23_1-V` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | conditional | Symbol/Farbe verwendet **und** keine einschlägige harmonisierte Norm/CS vorhanden; SOURCE_DEPENDENCY |

Outer Conditional: bei allen 22 Kandidaten NEIN; Nr. 23.1 ist ein Kernbereich ohne Coverage-Trigger.

### 14.3 Abbildung im Katalog

[RR_CATALOG.yaml](RR_CATALOG.yaml) besitzt keine eigenen Felder für Conditionality, Ausnahmen, Empfängerkreiserweiterungen, Modalitäten oder SOURCE_DEPENDENCY. Es wurden keine neuen Felder eingeführt. Bedingungen, die Ausnahme von `M23_1-P`, die Empfängerkreiserweiterung von `M23_1-C` und `M23_1-D` sowie die alternative Modalität von `M23_1-N` sind im jeweiligen Requirement Text erhalten; die vollständige Einordnung und die SOURCE_DEPENDENCY sind ausschließlich in dieser Evidenzdatei geführt.

---

## 15. Locator-Entscheidungen

| Kandidaten | Primary | Supplementary |
| --- | --- | --- |
| `M23_1-A` bis `M23_1-D` | `SRC-001#Anh.I/Nr.23.1/Satz.1` | keine |
| `M23_1-E`, `M23_1-F` | `SRC-001#Anh.I/Nr.23.1/Satz.2` | keine |
| `M23_1-G` bis `M23_1-K` | `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.1` | keine |
| `M23_1-L`, `M23_1-M` | `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.2` | keine |
| `M23_1-N` | `SRC-001#Anh.I/Nr.23.1/Buchst.b` | keine |
| `M23_1-O` | `SRC-001#Anh.I/Nr.23.1/Buchst.c` | keine |
| `M23_1-P` | `SRC-001#Anh.I/Nr.23.1/Buchst.d` | keine |
| `M23_1-Q` | `SRC-001#Anh.I/Nr.23.1/Buchst.e` | keine |
| `M23_1-R` | `SRC-001#Anh.I/Nr.23.1/Buchst.f` | keine |
| `M23_1-S` | `SRC-001#Anh.I/Nr.23.1/Buchst.g` | keine |
| `M23_1-T`, `M23_1-U`, `M23_1-V` | `SRC-001#Anh.I/Nr.23.1/Buchst.h` | keine |

**Begründung laut Bericht A:** Die Projektmethode erlaubt `Satz.` als Locator-Element ([DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4), verlangt zugleich aber das Minimalitätsprinzip ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8). Für Nr. 23.1 ist `/Satz.N` dort sinnvoll, wo es zwei unterschiedliche Sätze innerhalb desselben Chapeaus oder Buchstabens auseinanderhält. Supplementary-Locators werden grundsätzlich nicht geführt, soweit der jeweilige Requirement Text aus Nr. 23.1 vollständig bestimmbar ist. Bei `M23_1-N` ist Nr. 23.2 lediglich interner Kontext zur späteren Bestimmung der konkret vorgeschriebenen Kennzeichnungsangaben (Abschnitt 6). Durchführungsverordnung (EU) 2021/2226 wird nicht als Locator geführt (Abschnitt 10).

**Repository-Hinweis (keine Adjudikation):** Nr. 23.1 verwendet `Satz.`-Lokatoren für Chapeau und Buchst. a, nicht aber für Buchst. h; [RR_EXTRACTION_MDR_ANNEXI_22_1_22_3.md](RR_EXTRACTION_MDR_ANNEXI_22_1_22_3.md) Abschnitt 4.2 verzichtet für Nr. 22.1 bewusst darauf. Eine projektweite Abstimmung der `Satz.`-Verwendung ist nicht Gegenstand dieser Evidenz.

---

## 16. MDR-interne Deduplizierung

### 16.1 Gegen `RR-164`

| Kandidaten | Ergebnis | Begründung |
| --- | --- | --- |
| `M23_1-G` bis `M23_1-K` | PARTIAL_OVERLAP | Konkrete Überschneidung: Buchst. a verwendet wie `RR-164` technische Kenntnisse, Erfahrung sowie Ausbildungs- bzw. Schulungsmerkmale der vorgesehenen Anwender. Kein Duplikat: `RR-164` betrifft Nutzermerkmale bei anwendungsfehlerbezogener Produktauslegung bzw. Risikoreduktion; `M23_1-G` bis `M23_1-K` betreffen die Eignung von Kennzeichnung und Gebrauchsanweisung. Die Erfüllungsstatus können auseinanderfallen. |
| `M23_1-L`, `M23_1-M` | DISTINCT | — |
| übrige Kandidaten | NOT_APPLICABLE bzw. DISTINCT | — |

Damit ist der in [RR_EXTRACTION_MDR_ANNEXI_5.md](RR_EXTRACTION_MDR_ANNEXI_5.md) Abschnitt 8 und [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitte 10.16 und 10.21 vorgemerkte Abgleich mit `RR-164` durchgeführt.

### 16.2 Gegen `RR-175`

`RR-175` fordert leichte Verständlichkeit von Herstellerangaben und -anweisungen speziell bei Laienanwendung.

| Kandidaten | Ergebnis | Begründung |
| --- | --- | --- |
| `M23_1-G` bis `M23_1-K` | PARTIAL_OVERLAP | Die Informationsgestaltung kann dieselbe Verständlichkeitsdimension beeinflussen, ist aber breiter auf alle vorgesehenen Anwender gerichtet und normiert jeweils eigene Gestaltungseigenschaften. |
| `M23_1-L` | PARTIAL_OVERLAP | stärkste Beziehung: `M23_1-L` gilt allgemein für den vorgesehenen Nutzer der Gebrauchsanweisung, `RR-175` spezifisch für sämtliche Herstellerangaben und -anweisungen bei Laienanwendung |
| `M23_1-M` | PARTIAL_OVERLAP | Grafische Ergänzungen können der Verständlichkeit dienen, bilden aber eine eigenständige conditional Maßnahme. |
| übrige Kandidaten | DISTINCT bzw. NOT_APPLICABLE | — |

### 16.3 Gegen `RR-176`

`RR-176` verlangt die leichte Anwendbarkeit der Informationen bei Laienanwendung. Buchst. a verlangt Eignung bzw. Verständlichkeit, aber keine statusidentische allgemeine „leichte Anwendbarkeit".

| Kandidaten | Ergebnis |
| --- | --- |
| `M23_1-G` bis `M23_1-M` | DISTINCT |
| übrige Kandidaten | DISTINCT bzw. NOT_APPLICABLE |

### 16.4 Zusätzliche konkret dokumentierte Beziehungen

| Beziehung | Ergebnis | Begründung |
| --- | --- | --- |
| `M23_1-C` ↔ `RR-160` (Sicherheitsinformationen) | PARTIAL_OVERLAP | `RR-160` steht innerhalb der Risikokontrollhierarchie von Nr. 4; `M23_1-C` verlangt allgemein, dass relevante Sicherheitsinformationen das Produkt begleiten. `RR-160` kann daher nicht ersetzt werden. |
| `M23_1-S` ↔ `RR-162` (Restrisikoinformation) | PARTIAL_OVERLAP | `RR-162` verlangt die Information der Anwender über Restrisiken; `M23_1-S` spezifiziert zusätzlich, dass die mitzuteilenden Restrisiken in bestimmten Informationsformen in die Herstellerinformationen aufgenommen werden. Die Compliance-Status können voneinander abweichen. |

### 16.5 Ergebnis

| Merkmal | Ergebnis |
| --- | --- |
| Vollständige Deduplizierungen | 0 |
| Bestehende `RR` geändert | NEIN |

Ein partieller Overlap begründet nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 5.1 keine Deduplizierung.

---

## 17. Adjudikationsverlauf

Die folgenden Werte aus Bericht A wurden durch Bericht B ersetzt. Die ersetzten Werte sind nicht mehr gültig und werden ausschließlich zur Nachvollziehbarkeit festgehalten.

| Kandidat | Merkmal | Bericht A (ersetzt) | Bericht B (final) |
| --- | --- | --- | --- |
| `M23_1-U` | Trigger | Symbol oder Identifizierungsfarbe wird verwendet | Symbol oder Identifizierungsfarbe wird verwendet **und** für den betreffenden Bereich existiert eine einschlägige harmonisierte Norm oder Gemeinsame Spezifikation |
| `M23_1-V` | Einordnung | eine von drei voneinander unabhängigen Anforderungen in Buchst. h | komplementärer No-standard-/No-CS-Zweig zu `M23_1-U`; Trigger unverändert |
| `M23_1-C`, `M23_1-D` | Modellierung der Empfängerbedingung | „Grundpflicht NEIN; Empfängerkreiserweiterung conditional" | Outer NEIN, Inner der gesamten `RR` NEIN; bedingte Umfangsqualifikation im Requirement Text |
| `M23_1-P` | Conditionality | Inner Conditional JA (negative Ausnahme) | regulär; negative Ausnahme mit drei kumulativen Voraussetzungen |
| Gesamt | Zählung | 12 regulär / 10 conditional | 13 regulär / 9 conditional |
| `M23_1-R` | SOURCE_DEPENDENCY | JA | JA, unverändert; ergänzt um Abschlussstatus und empfohlene spätere Einordnung (Abschnitt 10.2) |

Unverändert durch Bericht B: 22 `RR`, 5 0-`RR`-Entscheidungen, Atomisierung, Themes, Lebenszyklusphasen, Locators, Deduplizierung, 0 Unresolved.

---

## 18. Kandidaten

### M23_1-A — Identifizierung des Produkts

- **Title EN:** Identification of the Device
- **DE:** Hersteller muss jedem Produkt die für dessen Identifizierung erforderlichen Angaben beifügen.
- **EN:** Manufacturer shall ensure that each device is accompanied by the information needed to identify it.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Satz.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-B — Identifizierung des Herstellers

- **Title EN:** Identification of the Manufacturer
- **DE:** Dem Produkt müssen die zur Identifizierung seines Herstellers erforderlichen Angaben beigefügt sein.
- **EN:** Each device shall be accompanied by information needed to identify its manufacturer.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Satz.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-C — Relevante Sicherheitsinformationen

- **Title EN:** Relevant Safety Information
- **DE:** Der Hersteller muss sicherstellen, dass jedem Produkt die für den Anwender sowie, soweit einschlägig, für andere Personen relevanten Sicherheitsinformationen beigefügt sind.
- **EN:** The manufacturer shall ensure that each device is accompanied by any safety information relevant to the user or, as appropriate, any other person.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Satz.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär; bedingte Empfängerkreiserweiterung (Abschnitt 4.2)

### M23_1-D — Relevante Leistungsinformationen

- **Title EN:** Relevant Performance Information
- **DE:** Der Hersteller muss sicherstellen, dass jedem Produkt die für den Anwender sowie, soweit einschlägig, für andere Personen relevanten Leistungsinformationen beigefügt sind.
- **EN:** The manufacturer shall ensure that each device is accompanied by any performance information relevant to the user or, as appropriate, any other person.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Satz.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär; bedingte Empfängerkreiserweiterung (Abschnitt 4.2)

### M23_1-E — Bereitstellung der Herstellerinformationen auf der Website

- **Title EN:** Availability of Manufacturer Information on the Website
- **DE:** Verfügt der Hersteller über eine Website, muss er sicherstellen, dass die Angaben zur Identifizierung des Produkts und des Herstellers sowie die relevanten Sicherheits- und Leistungsinformationen dort bereitgestellt werden.
- **EN:** Where the manufacturer has a website, the manufacturer shall ensure that the information needed to identify the device and its manufacturer and the relevant safety and performance information are made available on that website.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Satz.2`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Einordnung:** conditional — Hersteller verfügt über eine Website

### M23_1-F — Aktualhaltung der Website-Informationen

- **Title EN:** Keeping Website Information Up to Date
- **DE:** Verfügt der Hersteller über eine Website, muss er sicherstellen, dass die dort bereitgestellten Angaben zur Identifizierung des Produkts und des Herstellers sowie die relevanten Sicherheits- und Leistungsinformationen auf dem aktuellen Stand gehalten werden.
- **EN:** Where the manufacturer has a website, the manufacturer shall ensure that the information made available there to identify the device and its manufacturer and the relevant safety and performance information are kept up to date.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Satz.2`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** conditional — Hersteller verfügt über eine Website

### M23_1-G — Eignung des Mediums

- **Title EN:** Suitability of the Medium
- **DE:** Der Hersteller muss sicherstellen, dass das Medium der Kennzeichnung und der Gebrauchsanweisung dem jeweiligen Produkt, seiner Zweckbestimmung sowie den technischen Kenntnissen, der Erfahrung, der Ausbildung oder der Schulung der vorgesehenen Anwender angemessen ist.
- **EN:** The manufacturer shall ensure that the medium of the label and instructions for use is appropriate to the particular device, its intended purpose and the technical knowledge, experience, education or training of the intended user(s).
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.1`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-H — Eignung des Formats

- **Title EN:** Suitability of the Format
- **DE:** Der Hersteller muss sicherstellen, dass das Format der Kennzeichnung und der Gebrauchsanweisung dem jeweiligen Produkt, seiner Zweckbestimmung sowie den technischen Kenntnissen, der Erfahrung, der Ausbildung oder der Schulung der vorgesehenen Anwender angemessen ist.
- **EN:** The manufacturer shall ensure that the format of the label and instructions for use is appropriate to the particular device, its intended purpose and the technical knowledge, experience, education or training of the intended user(s).
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.1`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-I — Eignung des Inhalts

- **Title EN:** Suitability of the Content
- **DE:** Der Hersteller muss sicherstellen, dass der Inhalt der Kennzeichnung und der Gebrauchsanweisung dem jeweiligen Produkt, seiner Zweckbestimmung sowie den technischen Kenntnissen, der Erfahrung, der Ausbildung oder der Schulung der vorgesehenen Anwender angemessen ist.
- **EN:** The manufacturer shall ensure that the content of the label and instructions for use is appropriate to the particular device, its intended purpose and the technical knowledge, experience, education or training of the intended user(s).
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-J — Eignung der Lesbarkeit

- **Title EN:** Suitability of Legibility
- **DE:** Der Hersteller muss sicherstellen, dass die Lesbarkeit der Kennzeichnung und der Gebrauchsanweisung dem jeweiligen Produkt, seiner Zweckbestimmung sowie den technischen Kenntnissen, der Erfahrung, der Ausbildung oder der Schulung der vorgesehenen Anwender angemessen ist.
- **EN:** The manufacturer shall ensure that the legibility of the label and instructions for use is appropriate to the particular device, its intended purpose and the technical knowledge, experience, education or training of the intended user(s).
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.1`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-K — Eignung der Anbringungsstelle

- **Title EN:** Suitability of Location
- **DE:** Der Hersteller muss sicherstellen, dass die Anbringungsstelle der Kennzeichnung und der Gebrauchsanweisung dem jeweiligen Produkt, seiner Zweckbestimmung sowie den technischen Kenntnissen, der Erfahrung, der Ausbildung oder der Schulung der vorgesehenen Anwender angemessen ist.
- **EN:** The manufacturer shall ensure that the location of the label and instructions for use is appropriate to the particular device, its intended purpose and the technical knowledge, experience, education or training of the intended user(s).
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.1`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-L — Verständlichkeit der Gebrauchsanweisung

- **Title EN:** Understandability of the Instructions for Use
- **DE:** Der Hersteller muss sicherstellen, dass die Gebrauchsanweisung in Begriffen abgefasst ist, die für den vorgesehenen Anwender ohne Schwierigkeiten verständlich sind.
- **EN:** The manufacturer shall ensure that the instructions for use are written in terms readily understood by the intended user.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.2`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär

### M23_1-M — Ergänzung durch Zeichnungen und Schaubilder

- **Title EN:** Supplementation with Drawings and Diagrams
- **DE:** Gegebenenfalls muss der Hersteller sicherstellen, dass die Gebrauchsanweisung durch Zeichnungen und Schaubilder ergänzt wird.
- **EN:** Where appropriate, the manufacturer shall ensure that the instructions for use are supplemented with drawings and diagrams.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.a/Satz.2`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** conditional — „gegebenenfalls" / `where appropriate`

### M23_1-N — Anbringung vorgeschriebener Kennzeichnungsinformationen auf dem Produkt

- **Title EN:** Placement of Required Label Information on the Device
- **DE:** Der Hersteller muss sicherstellen, dass die für die Kennzeichnung vorgeschriebenen Angaben auf dem Produkt selbst angebracht sind; ist dies nicht praktikabel oder angemessen, dürfen einige oder alle Angaben auf der Verpackung jeder Einheit und/oder auf der Verpackung mehrerer Produkte erscheinen.
- **EN:** The manufacturer shall ensure that the information required on the label is provided on the device itself; if this is not practicable or appropriate, some or all of the information may appear on the packaging for each unit and/or on the packaging of multiple devices.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.b`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär; Verpackungsalternative als Modalität

### M23_1-O — Vom Menschen lesbare Kennzeichnung

- **Title EN:** Human-Readable Labelling
- **DE:** Der Hersteller muss sicherstellen, dass die Kennzeichnung in einem vom Menschen lesbaren Format bereitgestellt wird.
- **EN:** The manufacturer shall ensure that labels are provided in a human-readable format.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.c`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** regulär; maschinenlesbare Ergänzung ausschließlich 0-`RR` / PERMISSION

### M23_1-P — Bereitstellung der Gebrauchsanweisung zusammen mit dem Produkt

- **Title EN:** Provision of Instructions for Use with the Device
- **DE:** Der Hersteller muss sicherstellen, dass die Gebrauchsanweisung zusammen mit dem Produkt bereitgestellt wird. Dies gilt nicht, wenn kumulativ das Produkt der Klasse I oder IIa angehört, es ohne Gebrauchsanweisung sicher angewendet werden kann und an anderer Stelle des Abschnitts 23 nichts anderes vorgesehen ist.
- **EN:** The manufacturer shall ensure that instructions for use are provided together with the device. This does not apply where, cumulatively, the device is a class I or class IIa device, it can be used safely without instructions for use, and nothing to the contrary is provided for elsewhere in Section 23.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.d`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Einordnung:** regulär; negative Ausnahme (Abschnitt 8)

### M23_1-Q — Kostenlose weitere Exemplare der Gebrauchsanweisung auf Anforderung

- **Title EN:** Free Additional Copies of the Instructions for Use upon Request
- **DE:** Werden mehrere Produkte an einen Anwender und/oder Ort geliefert und fordert der Käufer weitere Exemplare der Gebrauchsanweisung an, muss der Hersteller sicherstellen, dass diese kostenlos bereitgestellt werden.
- **EN:** Where multiple devices are supplied to a single user and/or location and the purchaser requests further copies of the instructions for use, the manufacturer shall ensure that they are provided free of charge.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.e`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Einordnung:** conditional — Mehrfachlieferung und Anforderung durch den Käufer

### M23_1-R — Nicht papiergebundene Gebrauchsanweisung nur im zulässigen Durchführungsrahmen

- **Title EN:** Non-Paper Instructions for Use Only within the Applicable Implementing Framework
- **DE:** Stellt der Hersteller die Gebrauchsanweisung in anderer Form als auf Papier, etwa elektronisch, bereit, muss er sicherstellen, dass dies nur in dem Umfang und unter den Bedingungen erfolgt, die in den einschlägigen Durchführungsvorschriften festgelegt sind.
- **EN:** Where the manufacturer provides instructions for use in non-paper format, for example electronically, the manufacturer shall ensure that this is done only to the extent and under the conditions set out in the applicable implementing rules.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.f`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Einordnung:** conditional — Nicht-Papierform; SOURCE_DEPENDENCY Durchführungsverordnung (EU) 2021/2226 (Abschnitt 10)

### M23_1-S — Aufnahme mitzuteilender Restrisiken in Herstellerinformationen

- **Title EN:** Inclusion of Residual Risks in Manufacturer Information
- **DE:** Bestehen Restrisiken, die dem Anwender und/oder einer anderen Person mitzuteilen sind, muss der Hersteller sicherstellen, dass sie als Beschränkungen, Kontraindikationen, Vorsichtsmaßnahmen oder Warnungen in die von ihm bereitgestellten Informationen aufgenommen werden.
- **EN:** Where there are residual risks which are required to be communicated to the user and/or other person, the manufacturer shall ensure that they are included as limitations, contra-indications, precautions or warnings in the information supplied by the manufacturer.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.g`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** conditional — mitzuteilendes Restrisiko besteht

### M23_1-T — Verwendung international anerkannter Symbole

- **Title EN:** Use of Internationally Recognised Symbols
- **DE:** Soweit angebracht, muss der Hersteller sicherstellen, dass die von ihm bereitgestellten Informationen in Form international anerkannter Symbole erfolgen.
- **EN:** Where appropriate, the manufacturer shall ensure that the information supplied by the manufacturer takes the form of internationally recognised symbols.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.h`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** conditional — „wo dies angebracht ist" / `where appropriate`

### M23_1-U — Konformität verwendeter Symbole und Identifizierungsfarben

- **Title EN:** Conformity of Used Symbols and Identification Colours
- **DE:** Verwendet der Hersteller ein Symbol oder eine Identifizierungsfarbe und besteht für den betreffenden Bereich eine einschlägige harmonisierte Norm oder Gemeinsame Spezifikation, muss er sicherstellen, dass das Symbol bzw. die Identifizierungsfarbe dieser entspricht.
- **EN:** Where the manufacturer uses a symbol or identification colour and a relevant harmonised standard or common specification exists for the area concerned, the manufacturer shall ensure that the symbol or identification colour conforms to it.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.h`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** conditional — Standard-/CS-Zweig (Abschnitt 12.2); SOURCE_DEPENDENCY (Abschnitt 12.3)

### M23_1-V — Erläuterung von Symbolen und Identifizierungsfarben ohne harmonisierte Vorgabe

- **Title EN:** Explanation of Symbols and Identification Colours Where No Harmonised Standard or CS Exists
- **DE:** Verwendet der Hersteller ein Symbol oder eine Identifizierungsfarbe und besteht für den betreffenden Bereich keine einschlägige harmonisierte Norm oder Gemeinsame Spezifikation, muss er sicherstellen, dass das Symbol bzw. die Identifizierungsfarbe in der mit dem Produkt bereitgestellten Dokumentation erläutert wird.
- **EN:** Where the manufacturer uses a symbol or identification colour and no relevant harmonised standard or common specification exists for the area concerned, the manufacturer shall ensure that the symbol or identification colour is described in the documentation supplied with the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.1/Buchst.h`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Einordnung:** conditional — No-standard-/No-CS-Zweig (Abschnitt 12.2); SOURCE_DEPENDENCY (Abschnitt 12.3)

Für alle 22 Kandidaten gilt: Supplementary keine; `uncertainty` null; Katalogstatus `aktiv`.

---

## 19. Nicht extrahierte Bereiche

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.23.2` bis `Nr.23.4` | nicht extrahiert und nicht vorweggenommen; Nr. 23.2 nur interner Kontext zu `M23_1-N`; Nr. 23.4 bleibt `geplant` |
| Durchführungsverordnung (EU) 2021/2226 | nicht registriert, nicht extrahiert; ausschließlich externe normative Abhängigkeit zu `M23_1-R` |
| harmonisierte Normen und Gemeinsame Spezifikationen zu Symbolen und Farben | nicht ausgewählt, nicht extrahiert; externe Evidenz für `M23_1-U` und `M23_1-V` |
| `SRC-005` bis `SRC-008` sowie Kandidaten des [Standards-Landscape-Audits](../01-research/MEDICAL_DEVICE_STANDARDS_LANDSCAPE_AUDIT.md) | keine Norminhalte verwendet |

Keiner dieser Punkte ist ein zurückgestellter Fall oder ein Blocker für den Abschluss von Nr. 23.1.

---

## 20. Methodenaudit

| Prüfung | Ergebnis |
| --- | --- |
| Änderung an [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) erforderlich | NEIN — Version 1.2 deckt alle gefundenen Strukturen ab: selbständige Merkmalsreihen, permissives „können"/`may`, alternative Erfüllungswege, Ausnahmen einschließlich negativer Ausnahmen, Conditionality einschließlich komplementärer Triggerzweige, bedingte Umfangsqualifikationen, mehrere eigenständige Verben, externe normative Abhängigkeiten ohne Import fremder Requirements, kontrollierte Paraphrase und Minimalitätsprinzip der Locatorwahl |
| Änderung an [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) erforderlich | NEIN — alle finalen Anforderungen lassen sich eindeutig den bestehenden Clustern `Transparenz` oder `Gebrauchstauglichkeit` und den bestehenden Lebenszyklusphasen zuordnen; es entsteht kein Bedarf für einen eigenen Kennzeichnungs-, eIFU-, Symbol- oder Dokumentationscluster |
| Neues Katalogfeld | NEIN |

---

## 21. Quellenfundstellen der Research-Berichte

Wiedergegeben sind ausschließlich die Fundstellen zum verbindlichen Rechtsstand von `SRC-001` sowie zur externen Abhängigkeit, jeweils so, wie sie in den Berichten dokumentiert sind (einschließlich dort enthaltener URL-Parameter). Verweise auf eine ältere MDR-Konsolidierung und auf MDCG-Guidance sind gemäß Abschnitt 1 nicht übernommen. Die Fundstellen wurden für diese Datei nicht erneut aufgerufen.

| Bezug | Bezeichnung laut Bericht | URL laut Bericht |
| --- | --- | --- |
| `SRC-001`, DE | EUR-Lex - 02017R0745-20260719 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02017R0745-20260719 |
| `SRC-001`, EN | CL2017R0745EN0070010.0001_cp 1..1 | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02017R0745-20260719 |
| externe Abhängigkeit `M23_1-R` | Implementing regulation - 2021/2226 - EN - EUR-Lex | https://eur-lex.europa.eu/eli/reg_impl/2021/2226/oj/eng |
| externe Abhängigkeit `M23_1-R`, konsolidiert 16.07.2025 | EUR-Lex - 02021R2226-20250716 | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A02021R2226-20250716 |

---

## 22. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.23.1` mit den vollständigen Begründungen aus Research-Bericht A (ursprüngliche `0 / 1 / n`-Extraktion) und Research-Bericht B (Nachadjudikation zu `M23_1-U`/`M23_1-V`, `M23_1-C`/`M23_1-D`, `M23_1-P` und `M23_1-R`). 27 potenzielle Einheiten geprüft; 22 finale neue MDR-Gap-`RR`-Kandidaten `M23_1-A` bis `M23_1-V`, davon 13 regulär und 9 conditional; 5 0-`RR`-Entscheidungen. Themes: 13 × Transparenz, 9 × Gebrauchstauglichkeit. SOURCE_DEPENDENCY bei `M23_1-R` (Durchführungsverordnung (EU) 2021/2226, nicht registriert) sowie für die Operationalisierung von `M23_1-U` und `M23_1-V`. 0 vollständige Deduplizierungen gegen `RR-164`, `RR-175`, `RR-176`, `RR-160` und `RR-162`. 0 unresolved, 0 deferred. Entscheidungen ausschließlich gegen `02017R0745-20260719` dokumentiert. |
