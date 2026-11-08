# Systematische RR-Extraktion — SRC-009 Art. 3 bis 7 und Art. 9

Version 1.1 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-009` — Durchführungsverordnung (EU) 2021/2226 |
| Quellenbereiche | `SRC-009#Art.3`, `SRC-009#Art.4`, `SRC-009#Art.5`, `SRC-009#Art.6`, `SRC-009#Art.7`, `SRC-009#Art.9` |
| Rechtsstand | konsolidierte Fassung 16.07.2025 gemäß [SOURCES.md](SOURCES.md) (CELEX `02021R2226-20250716`), einschließlich der Änderung durch Durchführungsverordnung (EU) 2025/1234 |
| Quellenebene / Nutzungsart | Ebene A / `triggerbasiert` ([COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitte 9.9 und 10.23) |
| Coverage-Kategorie | `Ergänzend, conditional`; globaler Trigger: elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.33 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung. Sie vergibt **keine** permanenten `RR`-Identifikatoren; `S9-3-A` bis `S9-9-A` sind ausschließlich temporäre Evidenzkennungen. Permanente Identifikatoren werden ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml) vergeben.

**Grundlage** sind zwei abgeschlossene Research-Berichte:

| Bezeichnung | Inhalt |
| --- | --- |
| Research-Bericht A | vollständige ursprüngliche `0 / 1 / n`-Extraktion zu `SRC-009` Art. 3 bis 7 und Art. 9 |
| Research-Bericht B | gezielte Nachadjudikation zu `S9-5-A`, `S9-5-L`, `S9-6-A`/`S9-6-B`, `S9-5-V`/`S9-5-W` und zur Source-Level Conditionality |

Bei diesen nachadjudizierten Punkten hat Bericht B Vorrang (Abschnitt 17). Die Requirement Texte sind kontrollierte normative Paraphrasen und keine wörtlichen Zitate. Die Texte von `S9-4-C`, `S9-4-E`, `S9-4-H`, `S9-4-K`, `S9-5-B`, `S9-5-R`, `S9-5-V`, `S9-5-W`, `S9-6-D`, `S9-7-C`, `S9-7-F`, `S9-7-G` und `S9-7-I` wurden auf Grundlage der Berichte als eigenständig verständliche Katalogtexte gesondert fachlich freigegeben; der Text von `S9-4-J` wurde mit Version 1.1 redaktionell präzisiert (Abschnitt 19). Alle übrigen Texte sind unverändert aus Bericht A übernommen.

**Quellentreue:** Maßgeblich ist ausschließlich die konsolidierte Fassung `02021R2226-20250716`. Durchführungsverordnung (EU) 2025/1234 wird nur erwähnt, soweit die Änderung bzw. Streichung älterer Normbestandteile nachvollziehbar dokumentiert werden muss. Keine frühere Fassung wird als geltender Requirement Text verwendet.

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Geprüfte aktuelle potenzielle Einheiten | **67** |
| Neue Gap-`RR`-Kandidaten | **61** |
| davon regulär | 0 |
| davon conditional | 61 |
| 0-`RR`-Entscheidungen | 6 |
| Unresolved | 0 |
| Deferred | 0 |
| Vollständige Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

| Artikel | Finale Kandidaten | 0-`RR` |
| --- | --- | --- |
| Art. 3 | 1 | 2 |
| Art. 4 | 14 | 0 |
| Art. 5 | 23 | 1 |
| Art. 6 | 12 | 2 |
| Art. 7 | 10 | 1 |
| Art. 9 | 1 | 0 |
| **Gesamt** | **61** | **6** |

| Themencluster | Anzahl |
| --- | --- |
| Qualitäts- und Risikomanagement | 17 |
| Transparenz | 31 |
| Gebrauchstauglichkeit | 7 |
| Robustheit | 6 |
| Data Governance | 0 |
| Menschliche Aufsicht | 0 |
| Post-Market-Monitoring | 0 |
| Software-Lebenszyklus | 0 |
| **Gesamt** | **61** |

Es wurde **keine** quantitative Zielzahl verwendet ([COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12).

---

## 3. Source Verification

**Ergebnis `SRC-009`: PASS.**

| Merkmal | Befund |
| --- | --- |
| Verbindliche Arbeitsfassung | Durchführungsverordnung (EU) 2021/2226, konsolidierte Fassung 16.07.2025, CELEX `02021R2226-20250716`, in Kraft |
| Änderungsrechtsakt | Durchführungsverordnung (EU) 2025/1234 |
| Geprüfte Sprachfassungen | DE und EN primär; weitere Sprachfassungen nicht erforderlich |
| Sprachbefund | Für die atomizitäts- und conditionality-relevanten Begriffe keine materielle Divergenz; insbesondere `may`/„können", `shall`, `reasonably foreseeable`/„nach vernünftigem Ermessen", `verification and validation`/„Prüfung und Validierung" sowie die verschiedenen `if`- und Ausnahmestrukturen sind funktional konsistent |
| Unresolved Sprachdivergenzen | 0 |

### 3.1 Durch Verordnung (EU) 2025/1234 geänderte bzw. gestrichene Bestandteile

Die Änderungsverordnung hat Art. 3 Abs. 1 und 2 ersetzt, Art. 5 Nr. 12 gestrichen und Nr. 13 neu gefasst, Art. 6 Abs. 4 gestrichen, Art. 7 Abs. 2 Buchst. f gestrichen und Abs. 3 eingefügt, Art. 8 vollständig gestrichen sowie Art. 9 Abs. 2 gestrichen.

| Gestrichener Bestandteil | Behandlung |
| --- | --- |
| Art. 5 Nr. 12 | kein aktueller Extraktionsgegenstand |
| Art. 6 Abs. 4 | kein aktueller Extraktionsgegenstand |
| Art. 7 Abs. 2 Buchst. f | kein aktueller Extraktionsgegenstand |
| Art. 8 | vollständig gestrichen; keine Gap-Extraktion ([COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 9.9) |
| Art. 9 Abs. 2 | kein aktueller Extraktionsgegenstand; die frühere zusätzliche Websitepflicht entfällt |

Die gestrichenen Bestandteile werden **nicht** aus älteren Fassungen in die Extraktion zurückimportiert und **nicht** als 0-`RR` gezählt, weil sie kein Bestandteil des geltenden Arbeitsstands sind.

### 3.2 Methodische Leitlinie

Pflicht, Erlaubnis, Ausnahme, Trigger und Modalität werden auseinandergehalten; insbesondere wird eine Erlaubnis nicht als eigene positive Pflicht extrahiert.

---

## 4. Applicability-Baum

Der globale Source-Trigger aus dem Coverage-Plan genügt für die Quellenaktivierung, aber nicht für die einzelne Regelentscheidung. Die Quelle verlangt mehrere reproduzierbar unterscheidbare Zweige.

```text
Elektronische IFU für MDR-Medizinproduktesoftware?
│
├─ eIFU ERSETZT Papier-IFU  (REP)
│  │
│  ├─ Software gemäß MDR
│  │   └─ Art. 3 Abs. 3: eIFU mittels Software selbst zulässig
│  │
│  ├─ alternativ/projektergänzend:
│  │   Produkt für professionelle Nutzer → Art. 3 Abs. 1
│  │
│  ├─ professionelle Zweckbestimmung
│  │   + vernünftigerweise vorhersehbare Laiennutzung
│  │   └─ Art. 3 Abs. 2: Laien-IFU muss Papier sein
│  │
│  └─ Ersatzpfad aktiviert
│      ├─ Art. 4 Risikobewertung
│      ├─ Art. 5 Bedingungen
│      ├─ Art. 6 Informationspflichten
│      └─ Art. 7 Website-/Zugangsanforderungen
│
└─ eIFU ZUSÄTZLICH zu vollständiger Papier-IFU  (ADD)
   └─ Art. 9: inhaltliche Konsistenz
```

Weitere innere Zweige betreffen insbesondere eingebautes Anzeigesystem, Speichermedium, Papierexemplar auf Anforderung, sicherheitsrelevante Revision der Gebrauchsanweisung, Verfallsdatum, Website und UDI-Anwendungszeitpunkt. Der aktuelle Art. 3 bestätigt den Softwarepfad ausdrücklich; Art. 4 und 5 knüpfen an Art. 3 Abs. 1 und 3 an.

`REP` = eIFU **anstelle** der Papier-IFU; `ADD` = eIFU **zusätzlich** zur vollständigen Papier-IFU.

---

## 5. Art. 3

Art. 3 Abs. 1 und Abs. 3 eröffnen jeweils einen zulässigen eIFU-Pfad; Abs. 2 enthält dagegen eine echte Herstellerpflicht für den Fall vorhersehbarer Laiennutzung.

| Fundstelle | Ergebnis | Begründung |
| --- | --- | --- |
| Art. 3 Abs. 1 | 0 `RR` — PERMISSION / APPLICABILITY | Die Möglichkeit, Papier bei dem beschriebenen professionellen Nutzerpfad durch eIFU zu ersetzen, ist keine selbständige Compliance-Handlung. |
| Art. 3 Abs. 2 | 1 `RR` — `S9-3-A` | echte Herstellerpflicht bei vernünftigerweise vorhersehbarer Laiennutzung eines für professionelle Nutzer bestimmten Produkts |
| Art. 3 Abs. 3 | 0 `RR` — PERMISSION / APPLICABILITY | Für MDR-Software wird der zulässige Software-eIFU-Pfad eröffnet; die konkreten Anforderungen folgen erst aus Art. 4 bis 7. |

**Ergebnis Art. 3: 1 `RR`, 2 × 0 `RR`.**

---

## 6. Art. 4

Art. 4 Abs. 1 fordert zunächst eine **dokumentierte Risikobewertung**. Die Buchstaben a bis k sind kumulative Mindestinhalte. Abs. 2 verlangt die Aktualisierung anhand der Erfahrung nach dem Inverkehrbringen.

**Split Buchst. h:** Buchst. h enthält zwei funktional getrennte Gegenstände — Auswirkung der Nichtverfügbarkeit (`S9-4-I`) und vorhandene Sicherheitsmaßnahmen (`S9-4-J`). Beide können unabhängig unzureichend bewertet sein und bilden jeweils vollständige Risikobewertungsaussagen.

**Theme:** Alle Art.-4-Kandidaten erhalten `Qualitäts- und Risikomanagement`. Auch bei nutzer- oder robustheitsbezogenen Bewertungsgegenständen bleibt die atomare Handlung die verpflichtende Risikobewertung. Für Abs. 2 bleibt ebenfalls QRM primär: Die Erfahrung nach dem Inverkehrbringen ist hier Input einer Risikobewertungsaktualisierung, keine eigenständige Datenerhebungs- bzw. Monitoringpflicht. Die Phase `Post-Market-Überwachung` wird für `S9-4-N` als Lebenszyklusphase erfasst, nicht als Theme.

**Inner Conditional:** nur `S9-4-M` („soweit einschlägig"; Versionsverwaltung nach Art. 5 Nr. 8).

**Ergebnis Art. 4: 14 `RR`, 0 × 0 `RR`.**

---

## 7. Art. 5

Art. 5 enthält im aktuellen Stand die Nummern 1 bis 11 und 13; **Nr. 12 ist gestrichen**. Der Chapeau ist selbst eine Erlaubnis unter Bedingungen und erzeugt deshalb keine zusätzliche `RR`. Die Bedingungen sind verpflichtend, sobald der Ersatzpfad genutzt wird.

### 7.1 Split-Tests

| Nummer | Split | Begründung |
| --- | --- | --- |
| Nr. 3 | System (`S9-5-C`), Kostenfreiheit (`S9-5-D`), Frist (`S9-5-E`) | alle drei Status können unabhängig abweichen |
| Nr. 4 | Notfallinformationen (`S9-5-F`), Einschaltinformation bei eingebauter Anzeige (`S9-5-G`) | getrennte Informationsgegenstände; `S9-5-G` mit eigenem inneren Trigger |
| Nr. 5 | ordnungsgemäße Gestaltung (`S9-5-H`), Funktionsfähigkeit (`S9-5-I`), Verifikationsnachweis (`S9-5-J`), Validierungsnachweis (`S9-5-K`) | unabhängig statusfähige Sollzustände |
| Nr. 7 | Software- (`S9-5-M`) und Hardwareanforderungen (`S9-5-N`) | unabhängig statusfähig |
| Nr. 8 | Revisionskennzeichnung (`S9-5-O`), Nutzerinformation bei sicherheitsrelevanter Revision (`S9-5-P`) | zwei Pflichten |
| Nr. 9 | zehnjährige Verfügbarkeit (`S9-5-Q`), zwei Jahre über das letzte Verfallsdatum (`S9-5-R`) | zwei unabhängig zu erfüllende Mindestzeiträume |
| Nr. 11 | Websiteverfügbarkeit (`S9-5-T`), Sprachvorgabe (`S9-5-U`) | unabhängig statusfähig |
| Nr. 13 | Versionsverfügbarkeit (`S9-5-V`), Veröffentlichungsdaten (`S9-5-W`) | siehe Abschnitt 7.3 |

Die Splits folgen dem bestehenden Merkmals- und Status-Test ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitte 4 und 7) und nicht der bloßen Zahl der Wörter.

### 7.2 Ausnahme `S9-5-B`

Die Bereitstellungspflicht in allen Mitgliedstaaten, in denen das Produkt bereitgestellt oder in Betrieb genommen wird, gilt, es sei denn, eine Ausnahme ist gemäß der Risikobewertung nach Art. 4 ordnungsgemäß gerechtfertigt. Die Ausnahme ist Teil derselben `RR` und steht im Requirement Text; es wird keine separate `RR` erzeugt.

### 7.3 Art. 5 Nr. 13 — `S9-5-V` und `S9-5-W` (final nach Bericht B)

Struktur des aktuellen Wortlauts: Während der Fristen aus Nr. 9 und 10 müssen **alle herausgegebenen elektronischen Versionen** **und ihre Veröffentlichungsdaten** auf der Website verfügbar sein **oder**, hinsichtlich veralteter Versionen, auf Anfrage bereitgestellt werden.

**Finale Entscheidung: 2 `RR`.**

| Split-Bedingung | Ergebnis | Begründung |
| --- | --- | --- |
| 1 — unabhängiger Erfüllungsstatus | ERFÜLLT | Ein Hersteller kann sämtliche Versionen bereitstellen, ohne deren Veröffentlichungsdaten verfügbar zu machen. Ebenso könnten Veröffentlichungsdaten dokumentiert sein, während eine bestimmte Version selbst nicht zugänglich ist. |
| 2 — vollständige Compliance-Aussage | ERFÜLLT | Verfügbarkeit der herausgegebenen eIFU-Versionen und Verfügbarkeit der zugehörigen Veröffentlichungsdaten sind jeweils eigenständig vollständige Compliance-Aussagen. |

**Alternative für veraltete Versionen:** `or, as regards versions that are obsolete, be made available upon request` bezieht sich grammatisch auf den **gesamten koordinierten Gegenstand** („all issued electronic versions … and their date of publication"). Die Alternative ist deshalb in **beiden** atomaren `RR` quellentreu erhalten und wird nicht zu einer dritten `RR`.

### 7.4 Lifecycle-Nachadjudikation `S9-5-A` und `S9-5-L` (final nach Bericht B)

**`S9-5-A` — Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung; `Verifikation und Validierung`: NEIN.**

Art. 5 Nr. 1 verlangt, dass die Risikobewertung nach Art. 4 **ergibt/zeigt**, dass die elektronische Gebrauchsanweisung das durch die Papier-Gebrauchsanweisung erreichte Sicherheitsniveau erhält oder verbessert. Die Quelle verlangt hier weder eine Verifikation noch eine Validierung noch entsprechende Evidenz; das unterscheidet Nr. 1 gerade von Nr. 5, wo ausdrücklich Verifikations- und Validierungsnachweise gefordert werden. `demonstrate`/„ergibt" beschreibt bei Nr. 1 den geforderten **Aussagegehalt bzw. das Ergebnis der Risikobewertung**. Daraus darf die Phase `Verifikation und Validierung` nicht allein aufgrund einer nachweisenden bzw. evaluativen Wortwahl abgeleitet werden.

| Phase | Begründung |
| --- | --- |
| Planung und Konzeption | Die Entscheidung, Papier-IFU durch eIFU zu ersetzen, setzt die spezifische Risikobewertung und den Nachweis des mindestens gleichwertigen Sicherheitsniveaus voraus. |
| Entwicklung und Realisierung | Der eIFU-Ansatz und seine Risikokontrollen werden konkret ausgestaltet; die Risikobewertung muss den entstehenden Lösungszustand tragen. |
| Änderung und Wartung | Wird die eIFU-Lösung später relevant geändert, muss der Sicherheitsvergleich weiterhin erfüllt sein; konsistent mit der in Art. 4 Abs. 2 verlangten Aktualisierung der Risikobewertung. |

**`S9-5-L` — Entwicklung und Realisierung · Änderung und Wartung; `Verifikation und Validierung`: NEIN.**

Art. 5 Nr. 6 fordert einen **Produkt- bzw. Design-Sollzustand**: Bei einem eingebauten visuellen eIFU-Anzeigesystem darf die Anzeige der Gebrauchsanweisung die sichere Verwendung des Produkts nicht beeinträchtigen. Der Wortlaut verlangt keine eigenständige Verifikations- oder Validierungsaktivität. Dass dieser Sollzustand in einer professionellen Entwicklung sinnvollerweise verifiziert bzw. validiert wird, ist ein möglicher Nachweisweg, aber nicht die regulatorische Erfüllungsphase der atomaren Pflicht. `Inverkehrbringen, Inbetriebnahme und Betrieb` wird ebenfalls nicht ergänzt: Die Beeinträchtigung manifestiert sich zwar bei der Benutzung, die Herstellerpflicht besteht aber darin, das Anzeigesystem so zu gestalten, dass sie nicht entsteht.

**`S9-5-J` und `S9-5-K` bleiben unverändert** bei `Verifikation und Validierung`, weil Art. 5 Nr. 5 ausdrücklich Verifikations- bzw. Validierungsnachweise verlangt.

**Ergebnis Art. 5: 23 `RR`; Chapeau 0 `RR`.**

---

## 8. Art. 6

Der aktuelle Art. 6 enthält Abs. 1 bis 3 und Abs. 5; **Abs. 4 wurde 2025 gestrichen**. Abs. 3 Buchst. b und d enthalten jeweils mehrere unabhängig prüfbare Informationsgegenstände. Abs. 5 enthält zwei kumulative materielle Sollzustände (`S9-6-K`, `S9-6-L`); Symbole und Grafiken sowie zusätzliche Video- und Audiodateien sind dagegen permissiv.

### 8.1 Art. 6 Abs. 1 — `S9-6-A` und `S9-6-B` (final nach Bericht B)

Der geltende Wortlaut enthält erstens die allgemeine Verpflichtung, auf der Kennzeichnung deutlich anzugeben, dass die Gebrauchsanweisung elektronisch statt in Papierform bereitgestellt wird. Für Software verlangt derselbe Absatz zusätzlich, dass diese Information an der Stelle bereitgestellt wird, von der aus Zugang zur Software gewährt wird.

**Finale Entscheidung: 2 `RR`** — `S9-6-A` (Inhalt des deutlichen Hinweises) und `S9-6-B` (verpflichtender Bereitstellungsort dieses Hinweises bei Software).

| Split-Bedingung | Ergebnis | Begründung |
| --- | --- | --- |
| 1 — unabhängiger Erfüllungsstatus | ERFÜLLT | Der Hinweisinhalt kann korrekt und deutlich vorhanden sein, sich bei der Software aber nicht am vorgeschriebenen Zugangsort befinden; dann ist `S9-6-A` erfüllt und `S9-6-B` verletzt. Umgekehrt kann am richtigen Zugangsort ein Hinweis vorhanden sein, dessen Inhalt die elektronische-statt-Papier-Bereitstellung nicht hinreichend deutlich kenntlich macht. |
| 2 — vollständige Compliance-Aussage | ERFÜLLT | `S9-6-B` benötigt den referenzierten Informationsgegenstand aus Satz 1, bildet mit diesem notwendigen Kontext aber einen vollständigen eigenständigen Platzierungs-Sollzustand. Eine `RR` darf zwingend erforderlichen Kontext aus demselben Normzusammenhang beziehen. |

`S9-6-B` ist deshalb mehr als eine unselbständige Modalität: Die Quelle schreibt für Software einen spezifischen verpflichtenden Bereitstellungsort vor, dessen Compliance-Status unabhängig vom Inhalt des Hinweises abweichen kann. Keine Zusammenführung.

### 8.2 Art. 6 Abs. 2 — `S9-6-C` und `S9-6-D`

`S9-6-C` betrifft die Information, wie auf die eIFU zugegriffen werden kann; `S9-6-D` ihren Bereitstellungsort mit dem Papierfallback als alternativer Erfüllungsform. Art. 6 Abs. 2 verweist ausdrücklich auf Art. 6 Abs. 1 Unterabsatz 2. Der softwarebezogene Zugangsort aus Art. 6 Abs. 1 Unterabsatz 3 wird deshalb **nicht** in `S9-6-D` hineingezogen; er bleibt ausschließlich Gegenstand von `S9-6-B`.

### 8.3 Weitere Splits

| Fundstelle | Split | Begründung |
| --- | --- | --- |
| Abs. 3 Buchst. b | Basic UDI-DI bzw. UDI-DI (`S9-6-F`), zusätzliche Identifikationsangaben (`S9-6-G`) | unabhängig prüfbare Informationsgegenstände |
| Abs. 3 Buchst. d | Anforderungsweg (`S9-6-I`), Frist und Kostenfreiheit (`S9-6-J`) | unabhängig prüfbare Informationsgegenstände |
| Abs. 5 | vollständige Textform (`S9-6-K`), mindestens gleicher Informationsgehalt (`S9-6-L`) | zwei kumulative materielle Sollzustände |

**Ergebnis Art. 6: 12 `RR`, 2 × 0 `RR`** (Symbole/Grafiken; Video-/Audiodateien).

---

## 9. Art. 7

Art. 7 Abs. 1 verwendet einen alternativen Trigger — Speichermedium **oder** eingebautes visuelles Anzeigesystem. Das bleibt **eine** `RR` (`S9-7-A`), weil beide Alternativen denselben Sollzustand „zusätzlicher Websitezugang" auslösen. In Abs. 2 sind die einzelnen technischen Qualitätsmerkmale getrennt statusfähig (`S9-7-B` bis `S9-7-I`). Abs. 3 wurde 2025 neu eingefügt (`S9-7-J`).

**Art. 7 Abs. 2 Buchst. d — 0 `RR` — OUT_OF_SCOPE.** Die Website muss die Anforderungen der Verordnung (EU) 2016/679 erfüllen. Regulatorisch ist das eine echte Pflicht. Der primäre Gegenstand ist jedoch Datenschutz; [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 5 enthält bewusst keinen Datenschutzcluster. Die Pflicht wird nicht künstlich zu `Robustheit` umetikettiert. Die DSGVO bleibt als Source Dependency dokumentiert (Abschnitt 13).

**Art. 7 Abs. 2 Buchst. f** ist im aktuellen Rechtsstand gestrichen.

**Ergebnis Art. 7: 10 `RR`, 1 × 0 `RR`.**

---

## 10. Art. 9

Der aktuelle Art. 9 enthält nach der Änderung 2025 nur noch den ersten Absatz; die frühere zusätzliche Websitepflicht wurde gestrichen. Verbleibender Sollzustand ist die inhaltliche Konsistenz einer zusätzlich angebotenen eIFU mit der vollständigen Papierfassung (`S9-9-A`).

**Ergebnis Art. 9: 1 `RR`.**

---

## 11. 0-`RR`-Entscheidungen

| Nr. | Fundstelle | Gegenstand | Behandlung |
| --- | --- | --- | --- |
| 1 | Art. 3 Abs. 1 | Möglichkeit des professionellen eIFU-Ersatzpfads | 0 `RR` — PERMISSION / APPLICABILITY |
| 2 | Art. 3 Abs. 3 | Möglichkeit, MDR-Software-IFU mittels Software elektronisch statt auf Papier bereitzustellen | 0 `RR` — PERMISSION / APPLICABILITY |
| 3 | Art. 5 Chapeau | Möglichkeit der eIFU-Bereitstellung unter den folgenden Bedingungen | 0 `RR` — PERMISSION / gemeinsamer Rahmen |
| 4 | Art. 6 Abs. 5 | Symbole und Grafiken im Text | 0 `RR` — PERMISSION |
| 5 | Art. 6 Abs. 5 | zusätzliche Video- und Audiodateien | 0 `RR` — PERMISSION |
| 6 | Art. 7 Abs. 2 Buchst. d | DSGVO-Konformität der Website | 0 `RR` — OUT_OF_SCOPE |

Gestrichene Bestandteile sind nicht mitgezählt (Abschnitt 3.1). **67 geprüfte aktuelle potenzielle Einheiten = 61 `RR` + 6 0-`RR`.**

---

## 12. Conditionality

### 12.1 Source-Level Conditionality (final nach Bericht B)

**Macht allein die Governance-Bezeichnung `triggerbasiert` jede `RR` conditional? NEIN.** Die Nutzungsart ist eine Coverage- bzw. Source-Governance-Eigenschaft. Eine triggerbasierte Quelle könnte theoretisch auch einen Sollzustand enthalten, dessen rechtliche Applicability nicht vom Source-Aktivierungstrigger abhängt. Entscheidend bleibt die konkrete normative Applicability jeder `RR`.

**Sind trotzdem alle 61 Kandidaten conditional? JA.** Bei den extrahierten Bereichen bildet der Source-Trigger den realen rechtlichen Anwendungsrahmen der materiellen Pflichten ab:

- Art. 4 bis 7 greifen für den eIFU-statt-Papier-Pfad nach Art. 3.
- Art. 9 greift für den eIFU-zusätzlich-zu-Papier-Pfad.
- `S9-3-A` greift nur innerhalb der eIFU-Regelung und zusätzlich bei dem spezifischen Sachverhalt professioneller Nutzer mit vernünftigerweise vorhersehbarer Laiennutzung.

Damit besitzt jede der 61 `RR` mindestens eine rechtliche Applicability-Bedingung. Nicht weil `SRC-009` im Coverage-Plan triggerbasiert heißt, sind alle `RR` conditional, sondern weil die konkreten Pflichten aus Art. 3 bis 7 und 9 rechtlich nur in den jeweiligen eIFU-Anwendungszweigen gelten.

### 12.2 Outer und Inner Conditional

| Ebene | Bedeutung | Werte |
| --- | --- | --- |
| Outer Conditional | rechtlicher eIFU-Anwendungszweig, der die `RR` überhaupt aktiviert | Art. 4 bis 7: eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad, für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3; Art. 9: eIFU zusätzlich zu einer vollständigen Papier-IFU; `S9-3-A`: professioneller Nutzerpfad und vernünftigerweise vorhersehbare Laiennutzung |
| Inner Conditional | zusätzliche lokale Bedingung innerhalb einer bereits aktivierten `RR` | z. B. eingebautes Anzeigesystem, Anforderung der Papierfassung, sicherheitsbedingte Revision, bestimmtes Verfallsdatum, Website- bzw. Speichermedium-Konstellation, UDI-Registrierungszeitpunkt |

Eine lokale Bedingung ersetzt den Outer Trigger nicht.

### 12.3 Konsistenz mit MDR Anhang I Nr. 22

Bei [RR_EXTRACTION_MDR_ANNEXI_22_1_22_3.md](RR_EXTRACTION_MDR_ANNEXI_22_1_22_3.md) wurde die vorgesehene Laienanwendung nicht als eigene `RR` extrahiert, aber jede materielle Nr.-22-`RR` erhielt diese rechtliche Block-Applicability als Outer Conditional. Dasselbe Prinzip gilt hier: Die äußere Block-Applicability erzeugt die Conditionality der materiellen `RR`, ohne selbst eine `RR` zu werden.

### 12.4 Abbildung im Katalog

[RR_CATALOG.yaml](RR_CATALOG.yaml) besitzt keine eigenen Felder für Conditionality, Ausnahmen, Modalitäten, alternative Erfüllungswege oder Source Dependencies. Es wurden keine neuen Felder eingeführt. Innere Bedingungen, die Ausnahme von `S9-5-B` und die alternativen Erfüllungswege sind, soweit adjudiziert, im Requirement Text erhalten; die vollständige Einordnung einschließlich des Outer Conditional ist ausschließlich in dieser Evidenzdatei und im Coverage-Trigger geführt.

---

## 13. Source Dependencies

| Nr. | Abhängigkeit | Betroffen | Behandlung |
| --- | --- | --- | --- |
| 1 | mitgliedstaatliche Sprachfestlegung | `S9-5-U` | Für die konkrete Gap-Auswertung ist die Information erforderlich, welche EU-Amtssprache der betreffende Mitgliedstaat verlangt. SOURCE_DEPENDENCY: JA — jurisdiktionsabhängige Evidenz. Keine nationale Quelle erfunden oder registriert. |
| 2 | Verordnung (EU) 2016/679 (DSGVO) | Art. 7 Abs. 2 Buchst. d | Art. 7 Abs. 2 Buchst. d verweist unmittelbar auf die DSGVO. SOURCE_DEPENDENCY: JA; der materielle Datenschutz-Gap liegt jedoch außerhalb des RegScoutX-Themen-Scope und erzeugt keine `RR`. Keine DSGVO-`RR`, keine `SRC`-ID. |
| 3 | MDR-UDI (`SRC-001`) | `S9-6-F`, `S9-7-J` | `S9-6-F` hängt für die Bedeutung von Basic UDI-DI/UDI-DI von MDR-Bestimmungen ab. `S9-7-J` hängt für seinen Aktivierungszeitpunkt und die konkrete Datenbankpflicht insbesondere von MDR Art. 28, Art. 123 Abs. 3 Buchst. d/e und Anhang VI Teil B Nr. 22 ab; der `SRC-009`-Wortlaut nennt diese Abhängigkeit ausdrücklich. SOURCE_DEPENDENCY: JA, vollständig innerhalb der bereits registrierten `SRC-001`; keine neue Quelle. |
| 4 | interne `SRC-009`-Verweise | Art. 4 ↔ Art. 5; Art. 6 ↔ Art. 5 | interne normative Querverweise derselben Quelle; keine weitere `SRC` und keine neue Source Dependency |

Keine andere zwingende externe Quelle wurde für die 61 `RR` festgestellt. Es werden keine weiteren Quellen registriert.

---

## 14. Deduplizierung

**Vollständige Deduplizierungen: 0.** Keine bestehende `RR` wird geändert.

### 14.1 Verhältnis zu `RR-200`

`SRC-009` wurde als rechtsverbindliche Detailquelle registriert, weil MDR Anhang I Nr. 23.1 Buchst. f nur den Rahmen setzt. `SRC-009` konkretisiert `RR-200`, ersetzt sie aber nicht automatisch.

**Art. 4 bis 7 ↔ `RR-200`: PARTIAL_OVERLAP / normative Konkretisierung — keine Deduplizierung.** `RR-200` prüft auf MDR-Ebene, dass Nicht-Papier-Gebrauchsanweisungen nur im zulässigen Durchführungsrahmen bereitgestellt werden. Die `SRC-009`-Kandidaten prüfen die einzelnen Bedingungen dieses Rahmens; ein einzelner `SRC-009`-Gap kann unabhängig bestimmt werden. Das ist gerade die zusätzliche diagnostische Funktion der Quelle. `RR-200` bleibt unverändert; Primary bleibt `SRC-001#Anh.I/Nr.23.1/Buchst.f`.

### 14.2 Weitere Beziehungen

| Beziehung | Ergebnis | Begründung |
| --- | --- | --- |
| `S9-3-A` ↔ MDR-Laien- und Gebrauchsanweisungspflichten | PARTIAL_OVERLAP | eigener Trigger professioneller Nutzer mit vorhersehbarer Laiennutzung |
| `S9-4-B` bis `S9-4-E` ↔ `RR-164` (Nutzermerkmale) | PARTIAL_OVERLAP | hier Risikobewertungsinhalt statt Produktgestaltung |
| `S9-4-N` ↔ bestehende Risikomanagement- bzw. Aktualisierungs-`RR` | PARTIAL_OVERLAP | spezifische eIFU-Risikobewertung bleibt eigenständig |
| `S9-5-T` ↔ MDR-Website-Informationspflichten aus Anhang I Nr. 23.1 | PARTIAL_OVERLAP | nicht statusidentisch |
| `S9-6-F`/`S9-6-G` ↔ Produktidentifikations-`RR` aus Anhang I Nr. 23.1 | PARTIAL_OVERLAP | hier speziell Inhalt der eIFU-Zugangsinformation |
| `S9-6-H` ↔ Herstelleridentifikations- bzw. Kontaktinformationen | PARTIAL_OVERLAP | — |
| `S9-7-A` ↔ `S9-5-T` | PARTIAL_OVERLAP | Art. 7 Abs. 1 besitzt den engeren Trigger Speichermedium bzw. eingebaute Anzeige; keine vollständige Applicability-Identität |
| `S9-9-A` ↔ `RR-200` und Ersatzpfad | DISTINCT | Art. 9 betrifft ausdrücklich den Zusatzpfad eIFU zusätzlich zur vollständigen Papier-IFU |

---

## 15. Theme und Lebenszyklus

| Themencluster | Anzahl |
| --- | --- |
| Qualitäts- und Risikomanagement | 17 |
| Transparenz | 31 |
| Gebrauchstauglichkeit | 7 |
| Robustheit | 6 |
| Data Governance | 0 |
| Menschliche Aufsicht | 0 |
| Post-Market-Monitoring | 0 |
| Software-Lebenszyklus | 0 |
| **Gesamt** | **61** |

| Lebenszyklusphase | Anzahl Kandidaten |
| --- | --- |
| Planung und Konzeption | 14 |
| Entwicklung und Realisierung | 44 |
| Verifikation und Validierung | 2 |
| Konformitätsbewertung | 0 |
| Inverkehrbringen, Inbetriebnahme und Betrieb | 41 |
| Post-Market-Überwachung | 1 |
| Änderung und Wartung | 52 |

**Theme:** Die `0` bei `Post-Market-Monitoring` ist methodisch beabsichtigt: `S9-4-N` verlangt die Aktualisierung einer Risikobewertung anhand von Erfahrung nach dem Inverkehrbringen; primärer normativer Gegenstand bleibt QRM, `Post-Market-Überwachung` wird als Lebenszyklusphase erfasst.

**Lebenszyklus:** `Konformitätsbewertung = 0` ist mit dem aktuellen Rechtsstand konsistent, weil Art. 8 2025 vollständig gestrichen wurde. Die zwei Zuordnungen zu `Verifikation und Validierung` sind folgerichtig `S9-5-J` und `S9-5-K` (Abschnitt 7.4). Alle Werte stammen aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 3.

---

## 16. Kandidatenübersicht

`REP` = eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad; `ADD` = eIFU zusätzlich zur vollständigen Papier-IFU. Alle 61 Kandidaten sind conditional.

| Kandidat | Primary | Theme | Lebenszyklusphasen | Outer | Inner Conditional | Hinweis |
| --- | --- | --- | --- | --- | --- | --- |
| `S9-3-A` | `SRC-009#Art.3/Abs.2` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | Art. 3 Abs. 1 + Laiennutzung | NEIN | — |
| `S9-4-A` | `SRC-009#Art.4/Abs.1` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-B` | `SRC-009#Art.4/Abs.1/Buchst.a` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-C` | `SRC-009#Art.4/Abs.1/Buchst.b` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-D` | `SRC-009#Art.4/Abs.1/Buchst.c` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-E` | `SRC-009#Art.4/Abs.1/Buchst.d` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-F` | `SRC-009#Art.4/Abs.1/Buchst.e` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-G` | `SRC-009#Art.4/Abs.1/Buchst.f` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-H` | `SRC-009#Art.4/Abs.1/Buchst.g` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-I` | `SRC-009#Art.4/Abs.1/Buchst.h` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-J` | `SRC-009#Art.4/Abs.1/Buchst.h` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-K` | `SRC-009#Art.4/Abs.1/Buchst.i` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-L` | `SRC-009#Art.4/Abs.1/Buchst.j` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-4-M` | `SRC-009#Art.4/Abs.1/Buchst.k` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | JA — Versionsverwaltung nach Art. 5 Nr. 8 einschlägig | — |
| `S9-4-N` | `SRC-009#Art.4/Abs.2` | Qualitäts- und Risikomanagement | Post-Market-Überwachung · Änderung und Wartung | REP | NEIN | — |
| `S9-5-A` | `SRC-009#Art.5/Nr.1` | Qualitäts- und Risikomanagement | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | Lifecycle nach Bericht B |
| `S9-5-B` | `SRC-009#Art.5/Nr.2` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | NEIN | Ausnahme bei ordnungsgemäßer Rechtfertigung in der Risikobewertung nach Art. 4; Teil derselben RR |
| `S9-5-C` | `SRC-009#Art.5/Nr.3` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | NEIN | — |
| `S9-5-D` | `SRC-009#Art.5/Nr.3` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | JA — Papier-IFU angefordert | — |
| `S9-5-E` | `SRC-009#Art.5/Nr.3` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | JA — Anforderung bzw. Bestellung | zeitliche Alternativen bleiben erhalten |
| `S9-5-F` | `SRC-009#Art.5/Nr.4` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | sachlich nur soweit entsprechende Situationen bestehen |
| `S9-5-G` | `SRC-009#Art.5/Nr.4` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | JA — eingebautes Anzeigesystem | — |
| `S9-5-H` | `SRC-009#Art.5/Nr.5` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-5-I` | `SRC-009#Art.5/Nr.5` | Robustheit | Entwicklung und Realisierung · Änderung und Wartung | REP | NEIN | — |
| `S9-5-J` | `SRC-009#Art.5/Nr.5` | Qualitäts- und Risikomanagement | Verifikation und Validierung · Änderung und Wartung | REP | NEIN | — |
| `S9-5-K` | `SRC-009#Art.5/Nr.5` | Qualitäts- und Risikomanagement | Verifikation und Validierung · Änderung und Wartung | REP | NEIN | — |
| `S9-5-L` | `SRC-009#Art.5/Nr.6` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Änderung und Wartung | REP | JA — eingebautes Anzeigesystem | Lifecycle nach Bericht B |
| `S9-5-M` | `SRC-009#Art.5/Nr.7` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-5-N` | `SRC-009#Art.5/Nr.7` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-5-O` | `SRC-009#Art.5/Nr.8` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-5-P` | `SRC-009#Art.5/Nr.8` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | JA — sicherheitsrelevante Revision | — |
| `S9-5-Q` | `SRC-009#Art.5/Nr.9` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | JA — bestimmtes Verfallsdatum, kein Implantat | — |
| `S9-5-R` | `SRC-009#Art.5/Nr.9` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | JA — bestimmtes Verfallsdatum, kein Implantat | — |
| `S9-5-S` | `SRC-009#Art.5/Nr.10` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | JA — kein bestimmtes Verfallsdatum oder Implantat | — |
| `S9-5-T` | `SRC-009#Art.5/Nr.11` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-5-U` | `SRC-009#Art.5/Nr.11` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Jurisdiktionsabhängigkeit (SOURCE_DEPENDENCY) |
| `S9-5-V` | `SRC-009#Art.5/Nr.13` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | alternative Erfüllungsform für veraltete Versionen (auf Anfrage) |
| `S9-5-W` | `SRC-009#Art.5/Nr.13` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | alternative Erfüllungsform für veraltete Versionen (auf Anfrage); gleiche Zeiträume |
| `S9-6-A` | `SRC-009#Art.6/Abs.1` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Inhalt des Hinweises |
| `S9-6-B` | `SRC-009#Art.6/Abs.1` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | MDSW-spezifischer verpflichtender Bereitstellungsort |
| `S9-6-C` | `SRC-009#Art.6/Abs.2` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-6-D` | `SRC-009#Art.6/Abs.2` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Papierfallback als alternative Erfüllungsform |
| `S9-6-E` | `SRC-009#Art.6/Abs.3/Buchst.a` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-6-F` | `SRC-009#Art.6/Abs.3/Buchst.b` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | MDR-Querverweis (SOURCE_DEPENDENCY innerhalb SRC-001) |
| `S9-6-G` | `SRC-009#Art.6/Abs.3/Buchst.b` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-6-H` | `SRC-009#Art.6/Abs.3/Buchst.c` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-6-I` | `SRC-009#Art.6/Abs.3/Buchst.d` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-6-J` | `SRC-009#Art.6/Abs.3/Buchst.d` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-6-K` | `SRC-009#Art.6/Abs.5` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Symbole und Grafiken dürfen enthalten sein (Permission, 0-RR) |
| `S9-6-L` | `SRC-009#Art.6/Abs.5` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | — |
| `S9-7-A` | `SRC-009#Art.7/Abs.1` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | JA — Speichermedium oder eingebautes Anzeigesystem | — |
| `S9-7-B` | `SRC-009#Art.7/Abs.2/Buchst.a` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-C` | `SRC-009#Art.7/Abs.2/Buchst.a` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-D` | `SRC-009#Art.7/Abs.2/Buchst.b` | Robustheit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-E` | `SRC-009#Art.7/Abs.2/Buchst.b` | Robustheit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-F` | `SRC-009#Art.7/Abs.2/Buchst.c` | Robustheit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-G` | `SRC-009#Art.7/Abs.2/Buchst.c` | Robustheit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-H` | `SRC-009#Art.7/Abs.2/Buchst.e` | Robustheit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-I` | `SRC-009#Art.7/Abs.2/Buchst.e` | Gebrauchstauglichkeit | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | REP | NEIN | Website mit eIFU anstelle Papier |
| `S9-7-J` | `SRC-009#Art.7/Abs.3` | Transparenz | Inverkehrbringen, Inbetriebnahme und Betrieb | REP | JA — einschlägiger MDR-UDI-Registrierungszeitpunkt erreicht | MDR-UDI-Abhängigkeit (SOURCE_DEPENDENCY innerhalb SRC-001) |
| `S9-9-A` | `SRC-009#Art.9` | Transparenz | Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung | ADD | NEIN | — |

---

## 17. Adjudikationsverlauf

| Kandidat | Merkmal | Bericht A (ersetzt) | Bericht B (final) |
| --- | --- | --- | --- |
| `S9-5-A` | Lifecycle | Verifikation und Validierung | Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung |
| `S9-5-L` | Lifecycle | Entwicklung und Realisierung · Verifikation und Validierung · Änderung und Wartung | Entwicklung und Realisierung · Änderung und Wartung |
| `S9-5-V`, `S9-5-W` | Requirement Text | Alternative „auf Anfrage" nur bei `S9-5-V` | Alternative in beiden `RR` erhalten; 2 `RR` bestätigt |
| `S9-6-A`, `S9-6-B` | Atomisierung | 2 `RR` | 2 `RR` bestätigt; vollständige Split-Begründung ergänzt |
| alle 61 | Conditionality-Begründung | „SRC-009 ist eine triggerbasierte Quelle" | Conditionality folgt aus der konkreten rechtlichen Applicability, nicht aus der Nutzungsart (Abschnitt 12.1) |
| Gesamt | Lifecycle-Verteilung | P 13 · D 43 · V 4 · K 0 · O 41 · PM 1 · M 51 | P 14 · D 44 · V 2 · K 0 · O 41 · PM 1 · M 52 |
| Gesamt | Theme-Verteilung | Zwischenstand in Bericht A 34 Transparenz / 4 Gebrauchstauglichkeit, in Bericht A selbst korrigiert | 17 QRM · 31 Transparenz · 7 Gebrauchstauglichkeit · 6 Robustheit |

Unverändert durch Bericht B: 61 `RR`, 6 0-`RR`, Atomzahl, Themes, Conditionality-Zählung, Locators, Deduplizierung, 0 Unresolved.

---

## 18. Methodenaudit

| Prüfung | Ergebnis |
| --- | --- |
| Änderung an [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) erforderlich | NEIN — Version 1.2 löst sämtliche beobachteten Strukturen: Permission gegenüber Pflicht, conditional Compliance nach Nutzung einer Erlaubnis, kumulative Qualitätsmerkmale, alternative Erfüllungswege, lokale Trigger, gestrichene Normteile, Cross-Source-Konkretisierung, externe normative Abhängigkeiten und 0-`RR` wegen thematischem Scope. Die Nachadjudikation bestätigt: Gegenstand einer Pflicht ≠ Lebenszyklusphase; Nachweisbarkeit ≠ automatische V&V-Phase; Split nur bei unabhängigem Status **und** vollständiger Compliance-Aussage; Trigger und Modalitäten werden nicht künstlich verselbständigt. |
| Änderung an [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) erforderlich | NEIN — kein neuer Theme- oder Lifecycle-Wert erforderlich |
| Neues Katalogfeld | NEIN |

---

## 19. Kandidaten

### S9-3-A — Papier-IFU bei vorhersehbarer Laiennutzung

- **Title EN:** Paper IFU for Foreseeable Lay Use
- **DE:** Ist ein für professionelle Nutzer bestimmtes Produkt vernünftigerweise auch für eine Verwendung durch Laien vorhersehbar, muss der Hersteller die für Laien bestimmte Gebrauchsanweisung in Papierform bereitstellen.
- **EN:** Where lay use of a professionally intended device is reasonably foreseeable, the manufacturer shall provide the instructions intended for lay persons in paper form.
- **Primary:** `SRC-009#Art.3/Abs.2`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU-Regelung, professioneller Nutzerpfad (Art. 3 Abs. 1) und vernünftigerweise vorhersehbare Laiennutzung
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-A — Dokumentierte eIFU-Risikobewertung

- **Title EN:** Documented eIFU Risk Assessment
- **DE:** Hersteller muss vor dem Papierersatz eine dokumentierte Risikobewertung durchführen.
- **EN:** Manufacturer shall undertake a documented risk assessment before replacing paper IFU by eIFU.
- **Primary:** `SRC-009#Art.4/Abs.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-B — Nutzerkenntnisse, -erfahrung und -bedarf

- **Title EN:** User Knowledge, Experience and Needs
- **DE:** Die Risikobewertung muss Kenntnisstand, Erfahrung und Nutzerbedarf der vorgesehenen Nutzer erfassen.
- **EN:** The risk assessment shall cover intended-user knowledge, experience and needs.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.a`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-C — Nutzungsumgebung

- **Title EN:** Use Environment
- **DE:** Die Risikobewertung muss die Merkmale der vorgesehenen Nutzungsumgebung erfassen.
- **EN:** The risk assessment shall cover the characteristics of the intended environment of use.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.b`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-D — Nutzerkenntnisse zu Anzeige-Hardware/-Software

- **Title EN:** User Knowledge of Display Hardware and Software
- **DE:** Kenntnisse und Erfahrung der Nutzer hinsichtlich benötigter Hard-/Software müssen bewertet werden.
- **EN:** User knowledge and experience regarding required display hardware/software shall be assessed.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.c`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-E — Zugang zu elektronischen Ressourcen

- **Title EN:** Access to Electronic Resources
- **DE:** Die Risikobewertung muss den vorhersehbaren Zugang des Nutzers zu den bei der Nutzung benötigten elektronischen Ressourcen erfassen.
- **EN:** The risk assessment shall cover the user's access to the reasonably foreseeable electronic resources needed at the time of use.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.d`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-F — Leistungsfähigkeit des Manipulationsschutzes

- **Title EN:** Performance of Anti-Tampering Safeguards
- **DE:** Die Leistungsfähigkeit von Schutzvorkehrungen gegen Manipulation elektronischer Daten/Inhalte muss bewertet werden.
- **EN:** The performance of safeguards against tampering shall be assessed.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.e`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-G — Sicherheits- und Sicherungsmechanismen bei Fehlern

- **Title EN:** Safety and Back-Up Mechanisms for Faults
- **DE:** Sicherheits- und Backupmechanismen bei Hard-/Softwarefehlern müssen in die Bewertung einbezogen werden.
- **EN:** Safety and back-up mechanisms for hardware/software faults shall be covered.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.f`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-H — Vorhersehbare medizinische Notfälle

- **Title EN:** Foreseeable Medical Emergencies
- **DE:** Die Risikobewertung muss vorhersehbare medizinische Notfallsituationen erfassen, in denen Informationen in Papierform erforderlich sind.
- **EN:** The risk assessment shall cover foreseeable medical emergency situations requiring information in paper form.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.g`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-I — Auswirkung temporärer Nichtverfügbarkeit

- **Title EN:** Impact of Temporary Unavailability
- **DE:** Auswirkungen einer vorübergehenden Website-/Internet-/Zugangsnichtverfügbarkeit müssen bewertet werden.
- **EN:** The impact of temporary website/internet/access unavailability shall be assessed.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.h`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-J — Sicherheitsmaßnahmen bei Nichtverfügbarkeit

- **Title EN:** Safety Measures for Unavailability
- **DE:** Die Risikobewertung muss die verfügbaren Sicherheitsmaßnahmen zur Bewältigung einer vorübergehenden Nichtverfügbarkeit der spezifischen Website, des Internets im Allgemeinen oder des Zugangs hierzu in der Gesundheitseinrichtung erfassen.
- **EN:** The risk assessment shall cover the safety measures available to cope with temporary unavailability of the specific website or of the internet in general, or of access to them in the healthcare institution.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.h`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Redaktionelle Präzisierung mit Version 1.1: Die Änderung ist semantikneutral und macht den atomaren Sollzustand selbständig verständlich; zuvor verwies „solche Nichtverfügbarkeit" / `such unavailability` implizit auf `S9-4-I`. Keine neue Adjudikation; Atomisierung, Theme, Lebenszyklus und Conditionality unverändert.

### S9-4-K — Bewertung der Papierbereitstellungsfrist

- **Title EN:** Evaluation of Paper-IFU Provision Period
- **DE:** Die Risikobewertung muss den Zeitraum bewerten, innerhalb dessen die Gebrauchsanweisung auf Anforderung des Nutzers in Papierform bereitgestellt wird.
- **EN:** The risk assessment shall evaluate the period within which the instructions for use shall be provided in paper form at the user's request.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.i`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-L — Website-Kompatibilität mit Anzeigegeräten

- **Title EN:** Website Compatibility with Display Devices
- **DE:** Die Darstellungskompatibilität der Website mit unterschiedlichen möglichen Anzeigegeräten muss bewertet werden.
- **EN:** Website compatibility with different display devices shall be assessed.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.j`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-4-M — Verwaltung verschiedener IFU-Versionen

- **Title EN:** Management of Different IFU Versions
- **DE:** Soweit einschlägig, muss die Risikobewertung die Verwaltung verschiedener IFU-Versionen erfassen.
- **EN:** Where applicable, the risk assessment shall cover management of different IFU versions.
- **Primary:** `SRC-009#Art.4/Abs.1/Buchst.k`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — Versionsverwaltung nach Art. 5 Nr. 8 einschlägig
- **Hinweis:** —

### S9-4-N — Aktualisierung anhand von Post-Market-Erfahrung

- **Title EN:** Updating Based on Post-Market Experience
- **DE:** Die eIFU-Risikobewertung muss anhand der nach Markteinführung gewonnenen Erfahrung aktualisiert werden.
- **EN:** The eIFU risk assessment shall be updated in light of post-marketing experience.
- **Primary:** `SRC-009#Art.4/Abs.2`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Post-Market-Überwachung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-A — Nachweis mindestens gleichwertiger Sicherheit

- **Title EN:** Demonstration of At Least Equivalent Safety
- **DE:** Die Risikobewertung muss zeigen, dass eIFU das Sicherheitsniveau von Papier-IFU mindestens erhält.
- **EN:** The risk assessment shall demonstrate that eIFU maintains or improves the paper-IFU safety level.
- **Primary:** `SRC-009#Art.5/Nr.1`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Lifecycle nach Bericht B

### S9-5-B — Bereitstellung in allen einschlägigen Mitgliedstaaten

- **Title EN:** Provision in All Relevant Member States
- **DE:** Die elektronische Gebrauchsanweisung muss in allen Mitgliedstaaten bereitgestellt werden, in denen das Produkt bereitgestellt oder in Betrieb genommen wird, es sei denn, eine Ausnahme ist gemäß der Risikobewertung nach Artikel 4 ordnungsgemäß gerechtfertigt.
- **EN:** The electronic instructions for use shall be provided in all Member States where the device is made available or put into service, unless an exception is duly justified in the risk assessment referred to in Article 4.
- **Primary:** `SRC-009#Art.5/Nr.2`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Ausnahme bei ordnungsgemäßer Rechtfertigung in der Risikobewertung nach Art. 4; Teil derselben RR

### S9-5-C — System zur Bereitstellung einer Papier-IFU

- **Title EN:** System for Providing Paper IFU
- **DE:** Hersteller muss ein System für die Papierbereitstellung auf Nutzeranforderung vorhalten.
- **EN:** Manufacturer shall maintain a system for providing paper IFU on request.
- **Primary:** `SRC-009#Art.5/Nr.3`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-D — Kostenfreie Papier-IFU

- **Title EN:** Paper IFU Free of Additional Cost
- **DE:** Auf Anforderung muss die Papier-IFU ohne zusätzliche Kosten bereitgestellt werden.
- **EN:** Requested paper IFU shall be provided at no additional cost.
- **Primary:** `SRC-009#Art.5/Nr.3`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — Papier-IFU angefordert
- **Hinweis:** —

### S9-5-E — Fristgerechte Papier-IFU

- **Title EN:** Timely Provision of Paper IFU
- **DE:** Papier-IFU muss innerhalb des risikobewerteten Zeitraums und spätestens innerhalb der Quellenfrist bzw. bei entsprechender Bestellung bei Lieferung bereitgestellt werden.
- **EN:** Paper IFU shall be provided within the assessed period and the source-defined maximum deadline, or at delivery where requested at order.
- **Primary:** `SRC-009#Art.5/Nr.3`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — Anforderung bzw. Bestellung
- **Hinweis:** zeitliche Alternativen bleiben erhalten

### S9-5-F — Informationen zu vorhersehbaren medizinischen Notfällen

- **Title EN:** Information on Foreseeable Medical Emergencies
- **DE:** Auf Produkt oder Beipackzettel müssen einschlägige Informationen zu vorhersehbaren medizinischen Notfallsituationen bereitgestellt werden.
- **EN:** Relevant foreseeable medical-emergency information shall be provided on the device or a leaflet.
- **Primary:** `SRC-009#Art.5/Nr.4`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** sachlich nur soweit entsprechende Situationen bestehen

### S9-5-G — Information zum Einschalten bei eingebauter Anzeige

- **Title EN:** Start-Up Information for Built-In Display Systems
- **DE:** Bei eingebautem eIFU-Anzeigesystem muss über das Einschalten des Produkts informiert werden.
- **EN:** For a built-in eIFU display system, information on starting the device shall be provided.
- **Primary:** `SRC-009#Art.5/Nr.4`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — eingebautes Anzeigesystem
- **Hinweis:** —

### S9-5-H — Ordnungsgemäße Gestaltung der eIFU

- **Title EN:** Proper Design of eIFU
- **DE:** Der Hersteller muss die eIFU ordnungsgemäß gestalten.
- **EN:** The manufacturer shall ensure proper design of the eIFU.
- **Primary:** `SRC-009#Art.5/Nr.5`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-I — Ordnungsgemäße Funktionsfähigkeit der eIFU

- **Title EN:** Proper Functioning of eIFU
- **DE:** Der Hersteller muss die ordnungsgemäße Funktionsfähigkeit der eIFU gewährleisten.
- **EN:** The manufacturer shall ensure proper functioning of the eIFU.
- **Primary:** `SRC-009#Art.5/Nr.5`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-J — Verifikationsnachweis

- **Title EN:** Verification Evidence
- **DE:** Für Gestaltung/Funktion der eIFU muss Verifikation nachgewiesen werden.
- **EN:** Verification evidence shall be provided for the proper eIFU design/function.
- **Primary:** `SRC-009#Art.5/Nr.5`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Verifikation und Validierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-K — Validierungsnachweis

- **Title EN:** Validation Evidence
- **DE:** Für Gestaltung/Funktion der eIFU muss Validierung nachgewiesen werden.
- **EN:** Validation evidence shall be provided for the proper eIFU design/function.
- **Primary:** `SRC-009#Art.5/Nr.5`
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Verifikation und Validierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-L — Keine Beeinträchtigung sicherer Nutzung durch die Anzeige

- **Title EN:** No Impairment of Safe Use by eIFU Display
- **DE:** Bei eingebautem Anzeigesystem darf die Anzeige der eIFU die sichere Produktverwendung nicht beeinträchtigen.
- **EN:** A built-in eIFU display shall not impede safe use of the device.
- **Primary:** `SRC-009#Art.5/Nr.6`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — eingebautes Anzeigesystem
- **Hinweis:** Lifecycle nach Bericht B

### S9-5-M — Information über Softwareanforderungen

- **Title EN:** Information on Software Requirements
- **DE:** Hersteller muss die zur eIFU-Anzeige benötigten Softwareanforderungen angeben.
- **EN:** Required software for displaying eIFU shall be specified.
- **Primary:** `SRC-009#Art.5/Nr.7`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-N — Information über Hardwareanforderungen

- **Title EN:** Information on Hardware Requirements
- **DE:** Hersteller muss die zur eIFU-Anzeige benötigten Hardwareanforderungen angeben.
- **EN:** Required hardware for displaying eIFU shall be specified.
- **Primary:** `SRC-009#Art.5/Nr.7`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-O — System zur Kennzeichnung von IFU-Revisionen

- **Title EN:** System for Indicating IFU Revisions
- **DE:** Ein System muss klar anzeigen, wann die IFU revidiert wurde.
- **EN:** A system shall clearly indicate when the IFU has been revised.
- **Primary:** `SRC-009#Art.5/Nr.8`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-P — Information der Nutzer über sicherheitsrelevante Revisionen

- **Title EN:** User Notification of Safety-Related Revisions
- **DE:** Ist eine Revision aus Sicherheitsgründen erforderlich, muss jeder Nutzer darüber informiert werden.
- **EN:** Each user shall be informed where a revision was necessary for safety reasons.
- **Primary:** `SRC-009#Art.5/Nr.8`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — sicherheitsrelevante Revision
- **Hinweis:** —

### S9-5-Q — Zehnjährige eIFU-Verfügbarkeit

- **Title EN:** Ten-Year eIFU Availability
- **DE:** Bei Produkten mit Verfallsdatum außer Implantaten muss eIFU zehn Jahre nach dem letzten Inverkehrbringen verfügbar bleiben.
- **EN:** For defined-expiry, non-implantable devices, eIFU shall remain available for ten years after the last device was placed on the market.
- **Primary:** `SRC-009#Art.5/Nr.9`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — bestimmtes Verfallsdatum, kein Implantat
- **Hinweis:** —

### S9-5-R — Verfügbarkeit zwei Jahre über letztes Verfallsdatum

- **Title EN:** Availability for Two Years Beyond Final Expiry
- **DE:** Bei Produkten mit bestimmtem Verfallsdatum, die keine Implantate sind, muss die elektronische Gebrauchsanweisung zudem mindestens zwei Jahre nach Ablauf des letzten Verfallsdatums verfügbar bleiben.
- **EN:** For devices with a defined expiry date that are not implantable, the electronic instructions for use shall also remain available for at least two years beyond the final expiry date.
- **Primary:** `SRC-009#Art.5/Nr.9`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — bestimmtes Verfallsdatum, kein Implantat
- **Hinweis:** —

### S9-5-S — Fünfzehnjährige eIFU-Verfügbarkeit

- **Title EN:** Fifteen-Year eIFU Availability
- **DE:** Für Produkte ohne bestimmtes Verfallsdatum sowie Implantate gilt eine 15-jährige Verfügbarkeit nach letztem Inverkehrbringen.
- **EN:** Devices without a defined expiry date and implantables require fifteen-year eIFU availability after the last placing on the market.
- **Primary:** `SRC-009#Art.5/Nr.10`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — kein bestimmtes Verfallsdatum oder Implantat
- **Hinweis:** —

### S9-5-T — Verfügbarkeit der eIFU auf der Herstellerwebsite

- **Title EN:** eIFU Availability on Manufacturer Website
- **DE:** eIFU muss auf der Herstellerwebsite verfügbar sein.
- **EN:** eIFU shall be available on the manufacturer's website.
- **Primary:** `SRC-009#Art.5/Nr.11`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-5-U — Mitgliedstaatlich bestimmte EU-Amtssprache

- **Title EN:** Member-State-Determined Official Union Language
- **DE:** Die Website-eIFU muss in der vom Bereitstellungsmitgliedstaat bestimmten EU-Amtssprache verfügbar sein.
- **EN:** Website eIFU shall be available in an official Union language determined by the Member State of availability.
- **Primary:** `SRC-009#Art.5/Nr.11`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Jurisdiktionsabhängigkeit (SOURCE_DEPENDENCY)

### S9-5-V — Verfügbarkeit aller herausgegebenen eIFU-Versionen

- **Title EN:** Availability of All Issued eIFU Versions
- **DE:** Während der in Artikel 5 Nummern 9 und 10 festgelegten Zeiträume muss der Hersteller alle herausgegebenen elektronischen Versionen der Gebrauchsanweisung auf der Website verfügbar halten; veraltete Versionen dürfen stattdessen auf Anfrage bereitgestellt werden.
- **EN:** During the periods set out in Article 5, points (9) and (10), the manufacturer shall keep all issued electronic versions of the instructions for use available on the website; obsolete versions may instead be made available upon request.
- **Primary:** `SRC-009#Art.5/Nr.13`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** alternative Erfüllungsform für veraltete Versionen (auf Anfrage)

### S9-5-W — Verfügbarkeit der Veröffentlichungsdaten

- **Title EN:** Availability of Publication Dates
- **DE:** Während der in Artikel 5 Nummern 9 und 10 festgelegten Zeiträume muss der Hersteller die Veröffentlichungsdaten der herausgegebenen elektronischen Versionen der Gebrauchsanweisung verfügbar halten; bei veralteten Versionen dürfen die zugehörigen Veröffentlichungsdaten stattdessen auf Anfrage bereitgestellt werden.
- **EN:** During the periods set out in Article 5, points (9) and (10), the manufacturer shall keep the publication dates of the issued electronic versions of the instructions for use available; for obsolete versions, the corresponding publication dates may instead be made available upon request.
- **Primary:** `SRC-009#Art.5/Nr.13`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** alternative Erfüllungsform für veraltete Versionen (auf Anfrage); gleiche Zeiträume

### S9-6-A — Deutlicher Hinweis auf elektronische statt papiergebundene IFU

- **Title EN:** Clear Notice of Electronic Instead of Paper IFU
- **DE:** Hersteller muss deutlich kenntlich machen, dass die IFU elektronisch statt auf Papier bereitgestellt wird.
- **EN:** Manufacturer shall clearly indicate that IFU are supplied electronically instead of on paper.
- **Primary:** `SRC-009#Art.6/Abs.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Inhalt des Hinweises

### S9-6-B — Hinweis am Software-Zugangsort

- **Title EN:** Notice at the Software Access Location
- **DE:** Bei Software muss dieser Hinweis an der Stelle bereitgestellt werden, von der aus Zugang zur Software gewährt wird.
- **EN:** For software, the notice shall be provided at the location from which access to the software is granted.
- **Primary:** `SRC-009#Art.6/Abs.1`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** MDSW-spezifischer verpflichtender Bereitstellungsort

### S9-6-C — Information über den Zugang zur eIFU

- **Title EN:** Information on Accessing eIFU
- **DE:** Hersteller muss erklären, wie auf die eIFU zugegriffen werden kann.
- **EN:** Manufacturer shall provide information on how to access the eIFU.
- **Primary:** `SRC-009#Art.6/Abs.2`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-6-D — Bereitstellungsort der Zugangsinformation

- **Title EN:** Placement of eIFU Access Information
- **DE:** Die Information darüber, wie auf die elektronische Gebrauchsanweisung zugegriffen werden kann, muss auf der Verpackung jeder einzelnen Einheit oder gegebenenfalls auf der Verkaufsverpackung angebracht werden; bei fest installierten Medizinprodukten muss sie zusätzlich auf dem Produkt selbst angebracht werden. Ist diese Anbringung nicht praktikabel, muss die Information stattdessen auf Papier mit jedem Produkt mitgeliefert werden.
- **EN:** The information on how to access the electronic instructions for use shall be provided on the packaging for each unit or, where appropriate, on the sales packaging and, for fixed installed medical devices, also on the device itself. If such placement is not practicable, the information shall instead be provided in a paper document supplied with each device.
- **Primary:** `SRC-009#Art.6/Abs.2`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Papierfallback als alternative Erfüllungsform

### S9-6-E — Informationen zum Anzeigen der eIFU

- **Title EN:** Information Needed to View eIFU
- **DE:** Die Zugangsinformation muss alle zum Anzeigen benötigten Angaben enthalten.
- **EN:** Access information shall contain all information needed to view the eIFU.
- **Primary:** `SRC-009#Art.6/Abs.3/Buchst.a`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-6-F — Basic UDI-DI bzw. UDI-DI

- **Title EN:** Basic UDI-DI and/or UDI-DI
- **DE:** Die Zugangsinformation muss die einschlägige Basic UDI-DI und/oder UDI-DI enthalten.
- **EN:** Access information shall include the applicable Basic UDI-DI and/or UDI-DI.
- **Primary:** `SRC-009#Art.6/Abs.3/Buchst.b`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** MDR-Querverweis (SOURCE_DEPENDENCY innerhalb SRC-001)

### S9-6-G — Zusätzliche Produktidentifikationsangaben

- **Title EN:** Additional Device Identification Information
- **DE:** Zusätzlich müssen identifizierende Angaben wie Name und gegebenenfalls Modell enthalten sein.
- **EN:** Additional identifying information, including name and where applicable model, shall be included.
- **Primary:** `SRC-009#Art.6/Abs.3/Buchst.b`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-6-H — Herstellerkontaktdaten

- **Title EN:** Manufacturer Contact Details
- **DE:** Relevante Herstellerkontaktdaten müssen in den Zugangsinformationen enthalten sein.
- **EN:** Relevant manufacturer contact details shall be included.
- **Primary:** `SRC-009#Art.6/Abs.3/Buchst.c`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-6-I — Information zur Anforderung der Papier-IFU

- **Title EN:** Information on Requesting Paper IFU
- **DE:** Es muss angegeben werden, wo und wie die Papier-IFU angefordert werden kann.
- **EN:** Information shall state where and how paper IFU may be requested.
- **Primary:** `SRC-009#Art.6/Abs.3/Buchst.d`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-6-J — Information zu Frist und Kostenfreiheit der Papier-IFU

- **Title EN:** Information on Timing and Free Provision of Paper IFU
- **DE:** Es muss angegeben werden, innerhalb welcher Zeit die Papier-IFU kostenfrei erhältlich ist.
- **EN:** Information shall state the period within which paper IFU will be obtained at no additional cost.
- **Primary:** `SRC-009#Art.6/Abs.3/Buchst.d`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-6-K — Vollständige eIFU in Textform

- **Title EN:** Complete eIFU in Text Form
- **DE:** Die gesamte eIFU muss als Text verfügbar sein.
- **EN:** The eIFU shall be available entirely as text.
- **Primary:** `SRC-009#Art.6/Abs.5`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Symbole und Grafiken dürfen enthalten sein (Permission, 0-RR)

### S9-6-L — Mindestens gleicher Informationsgehalt wie Papier-IFU

- **Title EN:** At Least the Same Information as Paper IFU
- **DE:** Die eIFU muss mindestens denselben Informationsgehalt wie die Papierfassung besitzen.
- **EN:** eIFU shall contain at least the same information as the paper IFU.
- **Primary:** `SRC-009#Art.6/Abs.5`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** —

### S9-7-A — Zusätzlicher Websitezugang

- **Title EN:** Additional Website Access
- **DE:** Wird die eIFU auf Speichermedium oder über ein eingebautes visuelles Anzeigesystem bereitgestellt, muss sie zusätzlich über eine Website zugänglich sein.
- **EN:** Where eIFU are provided on storage media or via a built-in visual display, they shall also be accessible through a website.
- **Primary:** `SRC-009#Art.7/Abs.1`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — Speichermedium oder eingebautes Anzeigesystem
- **Hinweis:** —

### S9-7-B — Gebräuchliches Dateiformat

- **Title EN:** Commonly Used Format
- **DE:** Website-eIFU muss in einem gebräuchlichen Format bereitgestellt werden.
- **EN:** Website eIFU shall be provided in a commonly used format.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.a`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-C — Lesbarkeit mit frei verfügbarer Software

- **Title EN:** Readability with Freely Available Software
- **DE:** Das für die Website-eIFU verwendete Format muss mit frei verfügbarer Software lesbar sein.
- **EN:** The format used for the website eIFU shall be readable with freely available software.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.a`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-D — Schutz vor unbefugtem Zugriff

- **Title EN:** Protection Against Unauthorised Access
- **DE:** Die Website muss gegen unbefugten Zugriff geschützt sein.
- **EN:** The website shall be protected against unauthorised access.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.b`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-E — Schutz vor Inhaltsmanipulation

- **Title EN:** Protection Against Content Tampering
- **DE:** Die Website muss gegen Manipulation ihres Inhalts geschützt sein.
- **EN:** The website shall be protected against content tampering.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.b`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-F — Minimierung von Serverausfallzeiten

- **Title EN:** Minimisation of Server Downtime
- **DE:** Die Website ist so auszugestalten, dass Serverausfallzeiten so weit wie möglich verringert werden.
- **EN:** The website shall be designed so that server downtime is reduced as far as possible.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.c`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-G — Minimierung von Anzeigefehlern

- **Title EN:** Minimisation of Display Errors
- **DE:** Die Website ist so auszugestalten, dass Anzeigefehler so weit wie möglich verringert werden.
- **EN:** The website shall be designed so that display errors are reduced as far as possible.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.c`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-H — Stabilität der Internetadresse

- **Title EN:** Stability of the Internet Address
- **DE:** Die angegebene Internetadresse muss während der maßgeblichen Aufbewahrungsfristen stabil bleiben.
- **EN:** The internet address shall remain stable during the applicable retention periods.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.e`
- **Theme:** Robustheit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-I — Direkte Zugänglichkeit der Internetadresse

- **Title EN:** Direct Accessibility of the Internet Address
- **DE:** Die angegebene Internetadresse muss während der maßgeblichen Aufbewahrungsfristen unmittelbar zugänglich sein.
- **EN:** The internet address shall remain directly accessible during the applicable retention periods.
- **Primary:** `SRC-009#Art.7/Abs.2/Buchst.e`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** NEIN
- **Hinweis:** Website mit eIFU anstelle Papier

### S9-7-J — Übermittlung der eIFU-Internetadresse an die UDI-Datenbank

- **Title EN:** Provision of the eIFU Internet Address to the UDI Database
- **DE:** Spätestens ab dem einschlägigen MDR-UDI-Registrierungszeitpunkt muss der Hersteller die Internetadresse der UDI-Datenbank gemäß dem MDR übermitteln.
- **EN:** By the applicable MDR UDI-registration date, the manufacturer shall provide the internet address to the UDI database as prescribed.
- **Primary:** `SRC-009#Art.7/Abs.3`
- **Theme:** Transparenz
- **Lifecycle:** Inverkehrbringen, Inbetriebnahme und Betrieb
- **Outer Conditional:** JA — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad (für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3)
- **Inner Conditional:** JA — einschlägiger MDR-UDI-Registrierungszeitpunkt erreicht
- **Hinweis:** MDR-UDI-Abhängigkeit (SOURCE_DEPENDENCY innerhalb SRC-001)

### S9-9-A — Inhaltliche Konsistenz zusätzlicher eIFU mit der Papier-IFU

- **Title EN:** Content Consistency of Additional eIFU with Paper IFU
- **DE:** Wird zusätzlich zu einer vollständigen Papier-IFU eine eIFU bereitgestellt, muss deren Inhalt mit der Papierfassung übereinstimmen.
- **EN:** Where eIFU are provided in addition to complete paper IFU, their content shall be consistent with the paper version.
- **Primary:** `SRC-009#Art.9`
- **Theme:** Transparenz
- **Lifecycle:** Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung
- **Outer Conditional:** JA — eIFU zusätzlich zu einer vollständigen Papier-IFU
- **Inner Conditional:** NEIN
- **Hinweis:** —

Für alle 61 Kandidaten gilt: Supplementary keine; `uncertainty` null; Katalogstatus `aktiv`.

---

## 20. Quellenfundstellen der Research-Berichte

Wiedergegeben sind die Fundstellen zur verbindlichen konsolidierten Fassung sowie — ausschließlich zur Dokumentation der Änderungen und Streichungen — zum Änderungsrechtsakt, jeweils so, wie sie in den Berichten dokumentiert sind (einschließlich dort enthaltener URL-Parameter). Verweise der Berichte auf den ursprünglichen Basisrechtsakt `32021R2226` sind nicht übernommen, weil nur der konsolidierte Rechtsstand maßgeblich ist. Die Fundstellen wurden für diese Datei nicht erneut aufgerufen.

| Bezug | URL laut Bericht |
| --- | --- |
| `02021R2226-20250716`, EN | https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1757504502738&uri=CELEX%3A02021R2226-20250716 |
| `02021R2226-20250716`, EN | https://eur-lex.europa.eu/legal-content/en/TXT/?qid=1787112779242&uri=CELEX%3A02021R2226-20250716 |
| `02021R2226-20250716`, DE | https://eur-lex.europa.eu/legal-content/DE/TXT/?qid=1772901374787&uri=CELEX%3A02021R2226-20250716 |
| `02021R2226-20250716`, EN | https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1614000613788&uri=CELEX%3A02021R2226-20250716 |
| konsolidierte Fassung (ELI), EN-PDF | https://eur-lex.europa.eu/eli/reg_impl/2021/2226/2025-07-16/eng/pdf |
| `02021R2226-20250716`, DE (Bericht B) | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02021R2226-20250716 |
| `02021R2226-20250716`, EN (Bericht B) | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A02021R2226-20250716 |
| Änderungsrechtsakt (EU) 2025/1234 — nur Dokumentation der Änderungen und Streichungen | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?qid=1787975522296&uri=OJ%3AL_202501234 |

---

## 21. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-009` Art. 3 bis 7 und Art. 9 mit den vollständigen Begründungen aus Research-Bericht A und Research-Bericht B (Nachadjudikation zu `S9-5-A`, `S9-5-L`, `S9-6-A`/`S9-6-B`, `S9-5-V`/`S9-5-W` und zur Source-Level Conditionality). 67 geprüfte aktuelle potenzielle Einheiten; 61 finale Gap-`RR`-Kandidaten, alle conditional; 6 0-`RR`-Entscheidungen. Themes: 17 QRM, 31 Transparenz, 7 Gebrauchstauglichkeit, 6 Robustheit. Source Dependencies: mitgliedstaatliche Sprachfestlegung, DSGVO (Out-of-Scope), MDR-UDI innerhalb `SRC-001`. 0 vollständige Deduplizierungen; `RR-200` unverändert. Gestrichene Bestandteile des Rechtsstands 16.07.2025 nicht importiert. 0 unresolved, 0 deferred. |
| 1.1 | Redaktionelle Präzisierung des Requirement Texts DE/EN von `S9-4-J` (`SRC-009#Art.4/Abs.1/Buchst.h`, Katalog `RR-215`) als selbständig verständliche kontrollierte Paraphrase; der bisherige Text verwies mit „solche Nichtverfügbarkeit" / `such unavailability` implizit auf `S9-4-I`. Semantikneutral; keine neue Adjudikation; keine Änderung von Atomisierung, IDs, Theme, Lebenszyklus, Conditionality, Deduplizierung oder Coverage-Ergebnis. |
