# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 23.4 (ausgewählte Buchstaben)

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.23.4`, **ausschließlich** Buchst. b, e, f, g, h, j, k, s und ab |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Ergänzungsbereich, Priorität `Ergänzend`, Trigger `—` |
| Expected Theme | Transparenz (Ex-ante-Erwartung) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.35 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

**Abgrenzung:** Dies ist **nicht** die vollständige Extraktion von Nr. 23.4, sondern ausschließlich die Prüfung der neun in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitte 9.1 und 10.25 freigegebenen Buchstaben b, e, f, g, h, j, k, s und ab. Die übrigen Buchstaben von Nr. 23.4 wurden weder geprüft noch extrahiert.

Grundlage ist die abgeschlossene Research-Adjudikation zu diesen Buchstaben. Die Temp-IDs `M23_4-B1` bis `M23_4-AB3` sind ausschließlich Evidenzkennungen; permanente IDs werden nur in [RR_CATALOG.yaml](RR_CATALOG.yaml) vergeben. Titel, Requirement Texte, Trigger, Modalitäten, Locators und Scope-Entscheidungen sind unverändert aus der Research-Adjudikation übernommen; die Texte sind kontrollierte normative Paraphrasen.

**Quellentreue:** Maßgeblich ist ausschließlich `02017R0745-20260719`. Einzelne Textverweise der Research-Adjudikation auf ältere EUR-Lex-Konsolidierungen werden nicht als Evidenzquellen übernommen.

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Geprüfte potenzielle Einheiten | **35** |
| Finale `RR` | **30** |
| davon regulär | 9 — `M23_4-B1`, `E1`, `H1`, `K1`, `K2`, `S1`, `AB1`, `AB2`, `AB3` |
| davon conditional | 21 |
| 0-`RR` / OUT_OF_SCOPE | 5 |
| Unresolved | 0 |
| Vollständige Deduplizierungen | 0 |

| Buchstabe | potenzielle Einheiten | `RR` | 0-`RR` |
| --- | --- | --- | --- |
| b | 5 | 5 | 0 |
| e | 1 | 1 | 0 |
| f | 3 | 3 | 0 |
| g | 4 | 4 | 0 |
| h | 1 | 1 | 0 |
| j | 3 | 3 | 0 |
| k | 7 | 5 | 2 |
| s | 8 | 5 | 3 |
| ab | 3 | 3 | 0 |
| **Gesamt** | **35** | **30** | **5** |

**Theme:** 30 × `Transparenz`. **Lebenszyklus:** alle 30 × Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung.

---

## 3. Source Verification

**PASS.** EUR-Lex weist den 19.07.2026 als geltende konsolidierte MDR-Fassung aus. Die ausgewählten Inhalte wurden in DE und EN abgeglichen; für die Atomisierung wurde keine materielle Sprachdivergenz festgestellt. Bei Buchst. h unterscheidet sich die Formulierung des Genauigkeitsbeispiels sprachlich etwas, ohne den übergeordneten Sollzustand „für die ordnungsgemäße Verwendung benötigte Spezifikationen" oder dessen Atomisierung zu verändern. Unresolved: 0.

---

## 4. Atomisierung je Buchstabe

### 4.1 Buchst. b — 5 `RR`

Die Gebrauchsanweisung muss die Zweckbestimmung sowie, soweit zutreffend, Indikationen, Kontraindikationen, Patientenzielgruppe(n) und vorgesehene Anwender eindeutig spezifizieren. Die fünf Informationsgegenstände sind eigenständig prüfbar — eine Gebrauchsanweisung kann etwa die Zweckbestimmung korrekt angeben, aber die Patientenzielgruppe unzureichend spezifizieren — und bilden jeweils eine vollständige Informationsanforderung. Das gemeinsame „soweit zutreffend" / `as appropriate` wird für die Detailangaben quellentreu erhalten: `B1` regulär, `B2` bis `B5` conditional.

### 4.2 Buchst. e — 1 `RR`

Die Gebrauchsanweisung muss die Leistungsmerkmale enthalten. Kein weiterer Split: „Leistungsmerkmale" ist der eine normative Informationsgegenstand; die konkreten Leistungsparameter eines Produkts werden nicht zu einzelnen regulatorischen Atomen. Regulär.

### 4.3 Buchst. f — 3 `RR`

Soweit einschlägig sind Informationen bereitzustellen, anhand deren ein Angehöriger der Gesundheitsberufe die Eignung des Produkts prüfen sowie passende Software und passende Zubehörteile auswählen kann. Der Split-Test ist für alle drei erfüllt: Die Produkteignung kann beurteilbar sein, obwohl Informationen zur Softwareauswahl fehlen; Informationen zur Softwareauswahl können vollständig sein, während Zubehörinformationen fehlen; jeder Sollzustand ergibt selbständig eine vollständige Informationspflicht. Alle drei sind wegen „gegebenenfalls" / `where applicable` conditional. Auch der Zubehörzweig bleibt conditional relevant; fehlendes Zubehör deaktiviert den Zweig, nicht den gesamten Buchstaben.

### 4.4 Buchst. g — 4 `RR`

Etwaige Restrisiken (`G1`), Kontraindikationen (`G2`), unerwünschte Nebenwirkungen (`G3`) und die diesbezügliche Patienteninformation (`G4`) werden getrennt. Alle vier können unabhängig unvollständig sein; bei `G4` kann beispielsweise die fachliche Nebenwirkungsinformation dokumentiert sein, während die für die Patientenkommunikation erforderliche Information fehlt. Die `RR` sind conditional auf das Vorliegen des jeweiligen Gegenstands; aus „etwaige" / `any` wird keine Pflicht erfunden, nicht existente Risiken oder Nebenwirkungen zu erzeugen oder zu deklarieren.

### 4.5 Buchst. h — 1 `RR`

Gefordert sind die Spezifikationen, die der Anwender zur ordnungsgemäßen Verwendung benötigt; der Genauigkeitsaspekt bei Messfunktionen ist ein Beispiel. Keine Mikroatomisierung nach einzelnen technischen Spezifikationen; das Genauigkeitsbeispiel erzeugt keine zusätzliche `RR`. Regulär.

### 4.6 Buchst. j — 3 `RR`

Besondere Einrichtungen (`J1`), besondere Schulung (`J2`) und besondere Qualifikationen des Anwenders bzw. anderer Personen (`J3`) sind unabhängig statusfähig und jeweils vollständige Informationsanforderungen. Alle sind conditional auf das tatsächliche Bestehen der jeweiligen Anforderung. Auch Medizinproduktesoftware kann besondere IT-Infrastruktur, Schulungen oder Nutzerqualifikationen voraussetzen.

### 4.7 Buchst. k — 5 `RR`, 2 × 0 `RR`

Buchst. k verlangt Informationen zur Prüfung der ordnungsgemäßen Installation und der Betriebsbereitschaft sowie, soweit relevant, zu Wartung und Reinigung, Verbrauchskomponenten, Kalibrierung und zu Risiken bei Installation, Kalibrierung und Wartung.

| Atom | Ergebnis |
| --- | --- |
| ordnungsgemäße Installation | `K1`, regulär |
| sichere und zweckbestimmungsgemäße Betriebsbereitschaft | `K2`, regulär |
| präventive und regelmäßige Instandhaltung | `K3`, conditional („soweit relevant") |
| vorbereitende Reinigung/Desinfektion | 0 `RR` — OUT_OF_SCOPE (Abschnitt 5) |
| Verbrauchskomponenten und Austausch | 0 `RR` — OUT_OF_SCOPE (Abschnitt 5) |
| erforderliche Kalibrierung | `K4`, conditional (Kalibrierung erforderlich) |
| Verfahren zur Beseitigung von Risiken für Installations-, Kalibrierungs- und Wartungspersonal | `K5`, conditional |

Software-Wartung, Installation, Konfiguration und gegebenenfalls Kalibrierung besitzen einen horizontalen Bezug zu Medizinproduktesoftware; Reinigung, Desinfektion und Verbrauchsmaterial dagegen nicht.

### 4.8 Buchst. s — 5 `RR`, 3 × 0 `RR`

Buchst. s verlangt zunächst allgemeine Information über Warnungen, Vorsichtsmaßnahmen, Kontraindikationen, Maßnahmen und Nutzungsbeschränkungen; soweit relevant soll diese Information auch ermöglichen, den Patienten zu unterrichten. Anschließend folgen sechs spezielle, jeweils „soweit angemessen" / `where appropriate` zu berücksichtigende Fallgruppen.

| Atom | Ergebnis |
| --- | --- |
| allgemeine Sicherheits-, Warn- und Beschränkungsinformation | `S1`, regulär |
| Information zur Unterrichtung des Patienten | `S2`, conditional |
| Fehlfunktion bzw. sicherheitsrelevante Leistungsänderung | `S3`, conditional |
| vorhersehbare äußere Einflüsse bzw. Umgebungsbedingungen | `S4`, conditional |
| Interferenzrisiken bei diagnostischen oder therapeutischen Verfahren | `S5`, conditional |
| Verabreichung von Arzneimitteln, Geweben, Zellen oder biologischen Stoffen | 0 `RR` — OUT_OF_SCOPE |
| integrierter Arzneistoff bzw. biologisches Material | 0 `RR` — OUT_OF_SCOPE |
| CMR-, endokrinschädliche oder sensibilisierende Materialien | 0 `RR` — OUT_OF_SCOPE |

`S3` ist unmittelbar für Medizinproduktesoftware relevant. `S4` und `S5` bleiben conditional im Korpus, weil externe Betriebsbedingungen bzw. die Einbindung in diagnostische oder therapeutische Systemumgebungen bei Medizinproduktesoftware sicherheitsrelevant sein können; die Beispiele im Rechtsakt beschränken den Tatbestand nicht auf physische Stand-alone-Hardware.

### 4.9 Buchst. ab — 3 `RR`

Der Buchstabe gilt ausdrücklich für programmierbare elektronische Systeme einschließlich Software sowie für Software, die selbst Medizinprodukt ist. Die Gebrauchsanweisung muss Mindestanforderungen zu Hardware (`AB1`), IT-Netzmerkmalen (`AB2`) und IT-Sicherheitsmaßnahmen einschließlich Schutz vor unbefugtem Zugriff (`AB3`) enthalten, soweit diese zum bestimmungsgemäßen Betrieb der Software erforderlich sind. Der Schutz vor unbefugtem Zugriff wird **nicht** als vierte `RR` abgespalten, weil er ausdrücklich eingeschlossener Bestandteil der IT-Sicherheitsmaßnahmen ist. Alle drei regulär; Software-Scope unmittelbar gegeben.

---

## 5. 0-`RR`-Entscheidungen

| Nr. | Fundstelle | Potenzielles Atom | Behandlung | Begründung |
| --- | --- | --- | --- | --- |
| 1 | Nr. 23.4 Buchst. k | vorbereitende Reinigung/Desinfektion | 0 `RR` — OUT_OF_SCOPE | für eigenständige KI-basierte Medizinproduktesoftware kein horizontaler systematischer Beitrag; physische Hygiene- bzw. Aufbereitungspflicht |
| 2 | Nr. 23.4 Buchst. k | Verbrauchskomponenten und deren Austausch | 0 `RR` — OUT_OF_SCOPE | primär physischer Produkt- bzw. Verbrauchsmaterialgegenstand |
| 3 | Nr. 23.4 Buchst. s | Beschränkungen/Inkompatibilitäten bei verabreichten Arzneimitteln, Geweben, Zellen oder biologischen Stoffen | 0 `RR` — OUT_OF_SCOPE | Produktkonstellation mit stofflicher Verabreichung, kein horizontaler Gegenstand für Medizinproduktesoftware |
| 4 | Nr. 23.4 Buchst. s | Warnungen/Beschränkungen zu integriertem Arzneistoff bzw. biologischem Material | 0 `RR` — OUT_OF_SCOPE | primär stofflich-kombiniertes Medizinprodukt |
| 5 | Nr. 23.4 Buchst. s | Vorsichtsmaßnahmen zu CMR-, endokrinschädlichen oder sensibilisierenden Materialien | 0 `RR` — OUT_OF_SCOPE | Material- bzw. Stoffrisiken ohne systematischen Beitrag für eigenständige Medizinproduktesoftware |

Die Out-of-Scope-Einordnung ist keine Aussage über regulatorische Irrelevanz für Produkte mit entsprechenden physischen oder stofflichen Eigenschaften. **Zählung:** 30 `RR` + 5 0-`RR` = 35 geprüfte potenzielle Einheiten.

---

## 6. Theme, Lebenszyklus und Conditionality

**Theme:** Die ausschließliche Zuordnung zu `Transparenz` ist kein Taxonomieautomatismus. Entscheidend ist, dass jeder final erhaltene Sollzustand unmittelbar die Bereitstellung eines bestimmten Informationsinhalts verlangt. Materielle Risikobeherrschung, Schulungsdurchführung, Wartung, Cybersecurity-Implementierung oder Usability Engineering werden damit nicht selbst vorgeschrieben; bei `AB1` bis `AB3` ist der unmittelbare normative Gegenstand die Information in der Gebrauchsanweisung, nicht die Implementierung der IT-Sicherheitsmaßnahmen.

**Lebenszyklus:** Alle 30 Kandidaten tragen Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung. Es handelt sich durchgehend um Inhalte der Gebrauchsanweisung: Der geforderte Informationszustand wird erstellt bzw. gestaltet, muss beim Inverkehrbringen bzw. bei der Nutzung bereitstehen und ist bei relevanten Änderungen aufrechtzuerhalten. Eine Phase `Verifikation und Validierung` wird nicht allein aufgrund späterer Nachweisbarkeit vergeben. Alle Werte stammen aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 3.

**Conditionality:** 9 regulär, 21 conditional. Die jeweiligen Bedingungen („soweit zutreffend", „gegebenenfalls", „soweit relevant", „soweit angemessen", Vorliegen des Gegenstands) stehen im Requirement Text. Kein Outer Conditional: Nr. 23.4 ist ohne Coverage-Trigger freigegeben. Kein neues Katalogfeld.

---

## 7. Kandidatenübersicht

| Kandidat | `RR` | Primary | Einordnung / Trigger / Modalität | Software-Scope |
| --- | --- | --- | --- | --- |
| `M23_4-B1` | `RR-266` | `SRC-001#Anh.I/Nr.23.4/Buchst.b` | regulär | IN |
| `M23_4-B2` | `RR-267` | `SRC-001#Anh.I/Nr.23.4/Buchst.b` | conditional: Indikationen einschlägig | IN |
| `M23_4-B3` | `RR-268` | `SRC-001#Anh.I/Nr.23.4/Buchst.b` | conditional | IN |
| `M23_4-B4` | `RR-269` | `SRC-001#Anh.I/Nr.23.4/Buchst.b` | conditional | IN |
| `M23_4-B5` | `RR-270` | `SRC-001#Anh.I/Nr.23.4/Buchst.b` | conditional | IN |
| `M23_4-E1` | `RR-271` | `SRC-001#Anh.I/Nr.23.4/Buchst.e` | regulär | IN |
| `M23_4-F1` | `RR-272` | `SRC-001#Anh.I/Nr.23.4/Buchst.f` | conditional: Prüfung der Eignung einschlägig | IN |
| `M23_4-F2` | `RR-273` | `SRC-001#Anh.I/Nr.23.4/Buchst.f` | conditional: korrespondierende Software auszuwählen | IN |
| `M23_4-F3` | `RR-274` | `SRC-001#Anh.I/Nr.23.4/Buchst.f` | conditional: Zubehörauswahl einschlägig | IN |
| `M23_4-G1` | `RR-275` | `SRC-001#Anh.I/Nr.23.4/Buchst.g` | conditional: Restrisiko vorhanden | IN |
| `M23_4-G2` | `RR-276` | `SRC-001#Anh.I/Nr.23.4/Buchst.g` | conditional | IN |
| `M23_4-G3` | `RR-277` | `SRC-001#Anh.I/Nr.23.4/Buchst.g` | conditional | IN |
| `M23_4-G4` | `RR-278` | `SRC-001#Anh.I/Nr.23.4/Buchst.g` | conditional: Patienteninformation erforderlich | IN |
| `M23_4-H1` | `RR-279` | `SRC-001#Anh.I/Nr.23.4/Buchst.h` | regulär; Genauigkeitsbeispiel kein eigenes Atom | IN |
| `M23_4-J1` | `RR-280` | `SRC-001#Anh.I/Nr.23.4/Buchst.j` | conditional | IN |
| `M23_4-J2` | `RR-281` | `SRC-001#Anh.I/Nr.23.4/Buchst.j` | conditional | IN |
| `M23_4-J3` | `RR-282` | `SRC-001#Anh.I/Nr.23.4/Buchst.j` | conditional | IN |
| `M23_4-K1` | `RR-283` | `SRC-001#Anh.I/Nr.23.4/Buchst.k` | regulär | IN |
| `M23_4-K2` | `RR-284` | `SRC-001#Anh.I/Nr.23.4/Buchst.k` | regulär | IN |
| `M23_4-K3` | `RR-285` | `SRC-001#Anh.I/Nr.23.4/Buchst.k` | conditional: Instandhaltung relevant | IN |
| `M23_4-K4` | `RR-286` | `SRC-001#Anh.I/Nr.23.4/Buchst.k` | conditional: Kalibrierung erforderlich | IN |
| `M23_4-K5` | `RR-287` | `SRC-001#Anh.I/Nr.23.4/Buchst.k` | conditional | IN |
| `M23_4-S1` | `RR-288` | `SRC-001#Anh.I/Nr.23.4/Buchst.s` | regulär | IN |
| `M23_4-S2` | `RR-289` | `SRC-001#Anh.I/Nr.23.4/Buchst.s` | conditional: Patientenunterrichtung relevant | IN |
| `M23_4-S3` | `RR-290` | `SRC-001#Anh.I/Nr.23.4/Buchst.s` | conditional | IN |
| `M23_4-S4` | `RR-291` | `SRC-001#Anh.I/Nr.23.4/Buchst.s` | conditional | IN, soweit MDSW/System betroffen |
| `M23_4-S5` | `RR-292` | `SRC-001#Anh.I/Nr.23.4/Buchst.s` | conditional | IN, soweit systemisch relevant |
| `M23_4-AB1` | `RR-293` | `SRC-001#Anh.I/Nr.23.4/Buchst.ab` | regulär | unmittelbar IN |
| `M23_4-AB2` | `RR-294` | `SRC-001#Anh.I/Nr.23.4/Buchst.ab` | regulär | unmittelbar IN |
| `M23_4-AB3` | `RR-295` | `SRC-001#Anh.I/Nr.23.4/Buchst.ab` | regulär; Schutz vor unbefugtem Zugriff = eingeschlossene Konkretisierung | unmittelbar IN |

---

## 8. Deduplizierung

**Vollständige Deduplizierungen: 0.** Keine bestehende `RR` wird geändert. Es wurde keine Vollprüfung aller bestehenden `RR` durchgeführt; dokumentiert sind die in der Research-Adjudikation final festgestellten Beziehungen. `RR`-IDs in Klammern sind die Katalogzuordnung der in der Adjudikation mit Titel bezeichneten Anforderungen.

| Kandidat | Bestehende Anforderung | Ergebnis | Begründung |
| --- | --- | --- | --- |
| `B3` | `G2` und `S1` innerhalb Nr. 23.4 | PARTIAL_OVERLAP | alle betreffen Kontraindikationen, aber `B3` verlangt deren klare Spezifikation im Zweckbestimmungskontext, `G2` deren Angabe im Risiko- bzw. Nebenwirkungskontext und `S1` allgemeine sicherheitsbezogene Information |
| `E1` | Nr.-23.1-Anforderung „Relevante Leistungsinformationen" (`RR-186`) | PARTIAL_OVERLAP | Nr. 23.1 verlangt allgemein relevante Leistungsinformation; Nr. 23.4 Buchst. e bestimmt konkret die Leistungsmerkmale als Inhalt der Gebrauchsanweisung |
| `G1` | Restrisikoinformation (`RR-162`) und Nr.-23.1-Anforderung zur Aufnahme mitzuteilender Restrisiken (`RR-201`) | PARTIAL_OVERLAP | gleicher Sachbereich, aber unterschiedliche konkrete Informationssollzustände; die dokumentierte Beziehung zwischen `RR-201` und `RR-162` war ebenfalls nur partiell |
| `G2` bis `G4` | Sicherheitsinformationen (`RR-160`) und Nr.-23.1-Anforderung „Relevante Sicherheitsinformationen" (`RR-185`) | PARTIAL_OVERLAP | Nr. 23.4 Buchst. g konkretisiert spezifische Inhalte der Gebrauchsanweisung; die allgemeineren Informationspflichten bleiben unabhängig statusfähig |
| `H1` | Nr.-23.1-Anforderung „Relevante Leistungsinformationen" (`RR-186`) | PARTIAL_OVERLAP | nutzerseitig benötigte technische Spezifikationen können Leistungsinformation sein, sind aber nicht mit dem allgemeinen Leistungsinformations-Sollzustand identisch |
| `J2` | Anwenderschulung aus Anhang I Nr. 4 (`RR-161`) | DISTINCT | `J2` verlangt Information darüber, welche Schulung erforderlich ist; die Nr.-4-Pflicht betrifft die tatsächliche Schulung als Risikokontrollmaßnahme |
| `K5` | Sicherheitsinformationen (`RR-160`) | PARTIAL_OVERLAP | `K5` spezifiziert Verfahren zum Ausschluss von Risiken bei Installation, Kalibrierung und Wartung; `RR-160` ist allgemeiner |
| `S1` bis `S5` | `RR-160`, `RR-162` sowie die einschlägigen Nr.-23.1-Sicherheits- und Restrisikoinformations-Anforderungen (`RR-185`, `RR-201`) | PARTIAL_OVERLAP | Nr. 23.4 Buchst. s spezifiziert konkrete Warn-, Vorsichts- und Patienteninformationsinhalte, ohne die allgemeineren Pflichten zu ersetzen |
| `AB1` | `SRC-009#Art.5/Nr.7` — Hardwareanforderungen für die Anzeige einer eIFU (`RR-233`) | DISTINCT | `SRC-009` betrifft Hardware zum Anzeigen der elektronischen Gebrauchsanweisung; `AB1` Hardware zum bestimmungsgemäßen Betrieb der Medizinproduktesoftware selbst |
| `AB3` | `SRC-009#Art.4/Abs.1` — Manipulations- und Sicherheitsrisiken der eIFU | DISTINCT | `SRC-009` verlangt eine eIFU-bezogene Risikobewertung; `AB3` Information über Mindest-IT-Sicherheitsmaßnahmen des Medizinproduktesoftwaresystems |

**Verhältnis zu `SRC-009` (alle 30 Kandidaten):** Im eIFU-Fall verlangt `SRC-009#Art.6/Abs.5`, dass die elektronische Gebrauchsanweisung mindestens denselben Informationsgehalt wie die Papierfassung besitzt. Das ist **keine** Deduplizierung eines Nr.-23.4-Inhalts: `SRC-009` regelt Medium bzw. Inhaltsparität der elektronischen Gebrauchsanweisung, Nr. 23.4 bestimmt, welche materiellen Informationen die Gebrauchsanweisung enthalten muss. Verhältnis: PARTIAL_OVERLAP auf Transport- und Vollständigkeitsebene.

**Verhältnis zu `RR-200`:** keine Duplizierung. `RR-200` betrifft die Zulässigkeit der nicht papiergebundenen Gebrauchsanweisung im Durchführungsrahmen; die Nr.-23.4-Kandidaten betreffen deren materiellen Informationsinhalt. `RR-200` bleibt unverändert.

---

## 9. Source Dependencies

**Neue externe Source Dependency: keine.**

1. Bei elektronischer Gebrauchsanweisung gilt zusätzlich das bereits registrierte `SRC-009`-Regime; das ist keine neue Quelle und ändert den materiellen Inhalt der MDR-`RR` nicht.
2. Buchst. ab besitzt eine starke MDR-interne Beziehung zu den materiellen Software- und IT-Sicherheitsanforderungen insbesondere aus Anhang I Nr. 17.4. Diese Fundstelle wird nicht importiert und ist keine externe Source Dependency; sie bleibt außerhalb des initialen Gap-Coverage ([COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 9.2).
3. Produktbezogene Leistungs-, Zubehör-, Kalibrierungs- oder Schulungsinformationen benötigen später konkrete Produktevidenz, aber keine zusätzliche normative Quelle für die Extraktion.

---

## 10. Nicht geprüfte Bereiche

| Bereich | Behandlung |
| --- | --- |
| übrige Buchstaben von `SRC-001#Anh.I/Nr.23.4` | nicht aktiviert, nicht geprüft, nicht extrahiert |
| `SRC-001#Anh.I/Nr.23.2`, `Nr.23.3` | nicht Teil der Coverage |
| `SRC-001#Anh.I/Nr.17.4` | außerhalb des initialen Gap-Coverage; nicht importiert |
| Normen und Kandidaten des [Standards-Landscape-Audits](../01-research/MEDICAL_DEVICE_STANDARDS_LANDSCAPE_AUDIT.md) | keine Inhalte verwendet |

---

## 11. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 und [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 reichen aus; keine Änderung erforderlich. Die bestehenden Regeln für `0 / 1 / n`, Split-Test, Conditionality, Scope und primären normativen Gegenstand wurden angewandt: Split nur bei unabhängig abweichendem Erfüllungsstatus und jeweils vollständiger Compliance-Aussage. Kein neues Katalogfeld.

---

## 12. Kandidaten

Für alle 30 Kandidaten gilt: Theme `Transparenz`; Lifecycle Entwicklung und Realisierung · Inverkehrbringen, Inbetriebnahme und Betrieb · Änderung und Wartung; Supplementary keine; `uncertainty` null; Katalogstatus `aktiv`.

### M23_4-B1 — Angabe der Zweckbestimmung

- **Title EN:** Specification of the Intended Purpose
- **DE:** Der Hersteller muss sicherstellen, dass die Gebrauchsanweisung die Zweckbestimmung des Produkts eindeutig angibt.
- **EN:** The manufacturer shall ensure that the instructions for use clearly specify the intended purpose of the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.b`
- **Einordnung:** regulär
- **Katalog:** `RR-266`

### M23_4-B2 — Angabe der Indikationen

- **Title EN:** Specification of Indications
- **DE:** Soweit dies für das Produkt zutrifft, muss der Hersteller sicherstellen, dass die Gebrauchsanweisung die Indikationen eindeutig angibt.
- **EN:** Where appropriate for the device, the manufacturer shall ensure that the instructions for use clearly specify the indications.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.b`
- **Einordnung:** conditional: Indikationen einschlägig
- **Katalog:** `RR-267`

### M23_4-B3 — Angabe der Kontraindikationen im Zweckbestimmungskontext

- **Title EN:** Specification of Contra-Indications within the Intended-Purpose Context
- **DE:** Soweit dies für das Produkt zutrifft, muss der Hersteller sicherstellen, dass die Gebrauchsanweisung die Kontraindikationen im Zusammenhang mit der Zweckbestimmung eindeutig angibt.
- **EN:** Where appropriate for the device, the manufacturer shall ensure that the instructions for use clearly specify the contra-indications in the context of the intended purpose.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.b`
- **Einordnung:** conditional
- **Katalog:** `RR-268`

### M23_4-B4 — Angabe der Patientenzielgruppe

- **Title EN:** Specification of Patient Target Groups
- **DE:** Soweit dies für das Produkt zutrifft, muss der Hersteller sicherstellen, dass die Gebrauchsanweisung die Patientenzielgruppe oder Patientenzielgruppen eindeutig angibt.
- **EN:** Where appropriate for the device, the manufacturer shall ensure that the instructions for use clearly specify the patient target group or groups.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.b`
- **Einordnung:** conditional
- **Katalog:** `RR-269`

### M23_4-B5 — Angabe der vorgesehenen Anwender

- **Title EN:** Specification of Intended Users
- **DE:** Soweit dies für das Produkt zutrifft, muss der Hersteller sicherstellen, dass die Gebrauchsanweisung die vorgesehenen Anwender eindeutig angibt.
- **EN:** Where appropriate for the device, the manufacturer shall ensure that the instructions for use clearly specify the intended users.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.b`
- **Einordnung:** conditional
- **Katalog:** `RR-270`

### M23_4-E1 — Angabe der Leistungsmerkmale

- **Title EN:** Provision of Performance Characteristics
- **DE:** Der Hersteller muss sicherstellen, dass die Gebrauchsanweisung die Leistungsmerkmale des Produkts enthält.
- **EN:** The manufacturer shall ensure that the instructions for use contain the performance characteristics of the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.e`
- **Einordnung:** regulär
- **Katalog:** `RR-271`

### M23_4-F1 — Information zur Prüfung der Produkteignung

- **Title EN:** Information for Verification of Device Suitability
- **DE:** Soweit zutreffend, muss der Hersteller in der Gebrauchsanweisung die Informationen bereitstellen, anhand deren ein Angehöriger der Gesundheitsberufe überprüfen kann, ob das Produkt geeignet ist.
- **EN:** Where applicable, the manufacturer shall provide in the instructions for use the information enabling a healthcare professional to verify whether the device is suitable.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.f`
- **Einordnung:** conditional: Prüfung der Eignung einschlägig
- **Katalog:** `RR-272`

### M23_4-F2 — Information zur Auswahl korrespondierender Software

- **Title EN:** Information for Selection of Corresponding Software
- **DE:** Soweit zutreffend, muss der Hersteller in der Gebrauchsanweisung die Informationen bereitstellen, anhand deren ein Angehöriger der Gesundheitsberufe die zu dem Produkt passende Software auswählen kann.
- **EN:** Where applicable, the manufacturer shall provide in the instructions for use the information enabling a healthcare professional to select the software corresponding to the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.f`
- **Einordnung:** conditional: korrespondierende Software auszuwählen
- **Katalog:** `RR-273`

### M23_4-F3 — Information zur Auswahl korrespondierender Zubehörteile

- **Title EN:** Information for Selection of Corresponding Accessories
- **DE:** Soweit zutreffend, muss der Hersteller in der Gebrauchsanweisung die Informationen bereitstellen, anhand deren ein Angehöriger der Gesundheitsberufe die zu dem Produkt passenden Zubehörteile auswählen kann.
- **EN:** Where applicable, the manufacturer shall provide in the instructions for use the information enabling a healthcare professional to select the accessories corresponding to the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.f`
- **Einordnung:** conditional: Zubehörauswahl einschlägig
- **Katalog:** `RR-274`

### M23_4-G1 — Information über Restrisiken

- **Title EN:** Information on Residual Risks
- **DE:** Soweit Restrisiken bestehen, muss der Hersteller sicherstellen, dass diese in der Gebrauchsanweisung angegeben werden.
- **EN:** Where residual risks exist, the manufacturer shall ensure that they are stated in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.g`
- **Einordnung:** conditional: Restrisiko vorhanden
- **Katalog:** `RR-275`

### M23_4-G2 — Information über Kontraindikationen

- **Title EN:** Information on Contra-Indications
- **DE:** Soweit Kontraindikationen bestehen, muss der Hersteller sicherstellen, dass diese in der Gebrauchsanweisung angegeben werden.
- **EN:** Where contra-indications exist, the manufacturer shall ensure that they are stated in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.g`
- **Einordnung:** conditional
- **Katalog:** `RR-276`

### M23_4-G3 — Information über unerwünschte Nebenwirkungen

- **Title EN:** Information on Undesirable Side-Effects
- **DE:** Soweit unerwünschte Nebenwirkungen bestehen, muss der Hersteller sicherstellen, dass diese in der Gebrauchsanweisung angegeben werden.
- **EN:** Where undesirable side-effects exist, the manufacturer shall ensure that they are stated in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.g`
- **Einordnung:** conditional
- **Katalog:** `RR-277`

### M23_4-G4 — Patienteninformation zu Risiken, Kontraindikationen und Nebenwirkungen

- **Title EN:** Patient Information on Risks, Contra-Indications and Side-Effects
- **DE:** Soweit im Zusammenhang mit Restrisiken, Kontraindikationen oder unerwünschten Nebenwirkungen Informationen an den Patienten zu vermitteln sind, muss der Hersteller diese Informationen in die Gebrauchsanweisung aufnehmen.
- **EN:** Where information concerning residual risks, contra-indications or undesirable side-effects is to be conveyed to the patient, the manufacturer shall include that patient information in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.g`
- **Einordnung:** conditional: Patienteninformation erforderlich
- **Katalog:** `RR-278`

### M23_4-H1 — Spezifikationen für die ordnungsgemäße Verwendung

- **Title EN:** Specifications Required for Appropriate Use
- **DE:** Der Hersteller muss sicherstellen, dass die Gebrauchsanweisung die Spezifikationen enthält, die der Anwender für die ordnungsgemäße Verwendung des Produkts benötigt; bei Produkten mit Messfunktion ist die einschlägige Genauigkeitsangabe als möglicher Bestandteil zu berücksichtigen.
- **EN:** The manufacturer shall ensure that the instructions for use contain the specifications required by the user to use the device appropriately, including the relevant accuracy information where applicable to a device with a measuring function.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.h`
- **Einordnung:** regulär; Genauigkeitsbeispiel kein eigenes Atom
- **Katalog:** `RR-279`

### M23_4-J1 — Information über erforderliche besondere Einrichtungen

- **Title EN:** Information on Required Special Facilities
- **DE:** Soweit für die Verwendung des Produkts besondere Einrichtungen erforderlich sind, muss der Hersteller diese Anforderungen in der Gebrauchsanweisung angeben.
- **EN:** Where special facilities are required for use of the device, the manufacturer shall specify those requirements in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.j`
- **Einordnung:** conditional
- **Katalog:** `RR-280`

### M23_4-J2 — Information über erforderliche besondere Schulungen

- **Title EN:** Information on Required Special Training
- **DE:** Soweit für die Verwendung des Produkts besondere Schulungen erforderlich sind, muss der Hersteller diese Anforderungen in der Gebrauchsanweisung angeben.
- **EN:** Where special training is required for use of the device, the manufacturer shall specify those requirements in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.j`
- **Einordnung:** conditional
- **Katalog:** `RR-281`

### M23_4-J3 — Information über erforderliche besondere Qualifikationen

- **Title EN:** Information on Required Particular Qualifications
- **DE:** Soweit für den Produktanwender oder andere beteiligte Personen besondere Qualifikationen erforderlich sind, muss der Hersteller diese Anforderungen in der Gebrauchsanweisung angeben.
- **EN:** Where particular qualifications are required of the device user or other persons involved, the manufacturer shall specify those requirements in the instructions for use.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.j`
- **Einordnung:** conditional
- **Katalog:** `RR-282`

### M23_4-K1 — Information zur Prüfung der ordnungsgemäßen Installation

- **Title EN:** Information for Verification of Proper Installation
- **DE:** Der Hersteller muss in der Gebrauchsanweisung die Informationen bereitstellen, anhand deren überprüft werden kann, ob das Produkt ordnungsgemäß installiert wurde.
- **EN:** The manufacturer shall provide in the instructions for use the information needed to verify whether the device has been properly installed.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.k`
- **Einordnung:** regulär
- **Katalog:** `RR-283`

### M23_4-K2 — Information zur Prüfung der sicheren und bestimmungsgemäßen Betriebsbereitschaft

- **Title EN:** Information for Verification of Safe and Intended Readiness for Operation
- **DE:** Der Hersteller muss in der Gebrauchsanweisung die Informationen bereitstellen, anhand deren überprüft werden kann, ob das Produkt für einen sicheren und vom Hersteller beabsichtigten Betrieb bereit ist.
- **EN:** The manufacturer shall provide in the instructions for use the information needed to verify whether the device is ready to perform safely and as intended by the manufacturer.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.k`
- **Einordnung:** regulär
- **Katalog:** `RR-284`

### M23_4-K3 — Information zu präventiver und regelmäßiger Instandhaltung

- **Title EN:** Information on Preventive and Regular Maintenance
- **DE:** Soweit relevant, muss der Hersteller in der Gebrauchsanweisung Art und Häufigkeit der erforderlichen präventiven und regelmäßigen Instandhaltungsmaßnahmen angeben.
- **EN:** Where relevant, the manufacturer shall specify in the instructions for use the nature and frequency of required preventive and regular maintenance.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.k`
- **Einordnung:** conditional: Instandhaltung relevant
- **Katalog:** `RR-285`

### M23_4-K4 — Information zu erforderlicher Kalibrierung

- **Title EN:** Information on Necessary Calibration
- **DE:** Soweit für das Produkt eine Kalibrierung erforderlich ist, muss der Hersteller in der Gebrauchsanweisung die Informationen bereitstellen, die erforderlich sind, damit das Produkt während seiner vorgesehenen Lebensdauer ordnungsgemäß und sicher betrieben werden kann.
- **EN:** Where calibration is necessary, the manufacturer shall provide in the instructions for use the calibration information required to ensure proper and safe operation of the device throughout its intended lifetime.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.k`
- **Einordnung:** conditional: Kalibrierung erforderlich
- **Katalog:** `RR-286`

### M23_4-K5 — Verfahren zur Beseitigung von Risiken bei Installation, Kalibrierung oder Wartung

- **Title EN:** Methods for Eliminating Risks during Installation, Calibration or Servicing
- **DE:** Soweit bei Installation, Kalibrierung oder Wartung des Produkts Risiken für die beteiligten Personen auftreten können, muss der Hersteller in der Gebrauchsanweisung Verfahren angeben, mit denen diese Risiken beseitigt werden können.
- **EN:** Where persons involved in installing, calibrating or servicing the device may encounter risks, the manufacturer shall specify in the instructions for use methods for eliminating those risks.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.k`
- **Einordnung:** conditional
- **Katalog:** `RR-287`

### M23_4-S1 — Allgemeine Sicherheits-, Warn- und Nutzungsbeschränkungsinformation

- **Title EN:** General Safety, Warning and Use-Limitation Information
- **DE:** Der Hersteller muss in der Gebrauchsanweisung Informationen bereitstellen, anhand deren Anwender und/oder Patienten über einschlägige Warnungen, Vorsichtsmaßnahmen, Kontraindikationen, zu ergreifende Maßnahmen und Nutzungsbeschränkungen des Produkts informiert werden können.
- **EN:** The manufacturer shall provide in the instructions for use information enabling the user and/or patient to be informed of relevant warnings, precautions, contra-indications, measures to be taken and limitations of use concerning the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.s`
- **Einordnung:** regulär
- **Katalog:** `RR-288`

### M23_4-S2 — Information zur Unterrichtung des Patienten durch den Anwender

- **Title EN:** Information Enabling the User to Brief the Patient
- **DE:** Soweit relevant, muss der Hersteller in der Gebrauchsanweisung ausreichende Informationen bereitstellen, damit der Anwender den Patienten über Warnungen, Vorsichtsmaßnahmen, Kontraindikationen, erforderliche Maßnahmen und Nutzungsbeschränkungen des Produkts unterrichten kann.
- **EN:** Where relevant, the manufacturer shall provide sufficient information in the instructions for use to enable the user to brief the patient on warnings, precautions, contra-indications, measures to be taken and limitations of use concerning the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.s`
- **Einordnung:** conditional: Patientenunterrichtung relevant
- **Katalog:** `RR-289`

### M23_4-S3 — Information bei Fehlfunktion oder sicherheitsrelevanter Leistungsänderung

- **Title EN:** Information for Malfunction or Safety-Relevant Performance Changes
- **DE:** Soweit angemessen, muss die Gebrauchsanweisung Warnungen, Vorsichtsmaßnahmen und/oder erforderliche Maßnahmen für den Fall enthalten, dass eine Fehlfunktion oder eine Änderung der Produktleistung die Sicherheit beeinträchtigen kann.
- **EN:** Where appropriate, the instructions for use shall contain warnings, precautions and/or measures to be taken in the event of a device malfunction or a change in performance that may affect safety.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.s`
- **Einordnung:** conditional
- **Katalog:** `RR-290`

### M23_4-S4 — Information zu vorhersehbaren äußeren Einflüssen und Umgebungsbedingungen

- **Title EN:** Information on Foreseeable External Influences and Environmental Conditions
- **DE:** Soweit angemessen, muss die Gebrauchsanweisung Warnungen, Vorsichtsmaßnahmen und/oder erforderliche Maßnahmen hinsichtlich vernünftigerweise vorhersehbarer äußerer Einflüsse oder Umgebungsbedingungen enthalten, die die sichere Verwendung des Produkts beeinflussen können.
- **EN:** Where appropriate, the instructions for use shall contain warnings, precautions and/or measures concerning reasonably foreseeable external influences or environmental conditions that may affect safe use of the device.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.s`
- **Einordnung:** conditional
- **Katalog:** `RR-291`

### M23_4-S5 — Information zu Interferenzrisiken bei diagnostischen oder therapeutischen Verfahren

- **Title EN:** Information on Interference Risks during Diagnostic or Therapeutic Procedures
- **DE:** Soweit angemessen, muss die Gebrauchsanweisung Warnungen, Vorsichtsmaßnahmen und/oder erforderliche Maßnahmen zu Interferenzrisiken enthalten, die durch die vernünftigerweise vorhersehbare Anwesenheit des Produkts bei diagnostischen Untersuchungen, Bewertungen, therapeutischen Behandlungen oder anderen Verfahren entstehen können.
- **EN:** Where appropriate, the instructions for use shall contain warnings, precautions and/or measures concerning interference risks arising from the reasonably foreseeable presence of the device during diagnostic investigations, evaluations, therapeutic treatment or other procedures.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.s`
- **Einordnung:** conditional
- **Katalog:** `RR-292`

### M23_4-AB1 — Hardware-Mindestanforderungen für den bestimmungsgemäßen Softwarebetrieb

- **Title EN:** Minimum Hardware Requirements for Intended Software Operation
- **DE:** Bei Medizinproduktesoftware muss der Hersteller in der Gebrauchsanweisung die Mindestanforderungen an die Hardware angeben, die für den bestimmungsgemäßen Betrieb der Software erforderlich sind.
- **EN:** For medical device software, the manufacturer shall specify in the instructions for use the minimum hardware requirements necessary to run the software as intended.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.ab`
- **Einordnung:** regulär
- **Katalog:** `RR-293`

### M23_4-AB2 — Mindestanforderungen an IT-Netzmerkmale

- **Title EN:** Minimum Requirements for IT Network Characteristics
- **DE:** Bei Medizinproduktesoftware muss der Hersteller in der Gebrauchsanweisung die Mindestanforderungen an die Merkmale der IT-Netze angeben, die für den bestimmungsgemäßen Betrieb der Software erforderlich sind.
- **EN:** For medical device software, the manufacturer shall specify in the instructions for use the minimum requirements concerning IT network characteristics necessary to run the software as intended.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.ab`
- **Einordnung:** regulär
- **Katalog:** `RR-294`

### M23_4-AB3 — Mindestanforderungen an IT-Sicherheitsmaßnahmen

- **Title EN:** Minimum Requirements for IT Security Measures
- **DE:** Bei Medizinproduktesoftware muss der Hersteller in der Gebrauchsanweisung die Mindestanforderungen an die IT-Sicherheitsmaßnahmen angeben, die für den bestimmungsgemäßen Betrieb der Software erforderlich sind, einschließlich des erforderlichen Schutzes vor unbefugtem Zugriff.
- **EN:** For medical device software, the manufacturer shall specify in the instructions for use the minimum requirements concerning IT security measures necessary to run the software as intended, including the required protection against unauthorised access.
- **Primary:** `SRC-001#Anh.I/Nr.23.4/Buchst.ab`
- **Einordnung:** regulär; Schutz vor unbefugtem Zugriff = eingeschlossene Konkretisierung
- **Katalog:** `RR-295`

---

## 13. Quellenfundstelle

| Bezug | URL |
| --- | --- |
| `SRC-001`, konsolidierte Fassung 19.07.2026 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02017R0745-20260719 |

---

## 14. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der systematischen Extraktion von `SRC-001#Anh.I/Nr.23.4`, ausschließlich Buchst. b, e, f, g, h, j, k, s und ab (keine vollständige Extraktion von Nr. 23.4). 35 potenzielle Einheiten; 30 finale Gap-`RR`-Kandidaten, davon 9 regulär und 21 conditional; 5 0-`RR`-Entscheidungen (OUT_OF_SCOPE). Theme 30 × Transparenz; Lebenszyklus je Entwicklung und Realisierung, Inverkehrbringen, Inbetriebnahme und Betrieb sowie Änderung und Wartung. 0 vollständige Deduplizierungen; `RR-200` und alle bestehenden `RR` unverändert. 0 unresolved. |
