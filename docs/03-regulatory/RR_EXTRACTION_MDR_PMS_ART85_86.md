# Systematische RR-Extraktion — SRC-001 klassenspezifischer PMS-Berichtsblock: Art. 85 und Art. 86

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereiche | `SRC-001#Art.85` (Klasse-I-Zweig), `SRC-001#Art.86` (Klasse-IIa/IIb/III-Zweig) |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Ergänzungsbereich, Priorität `Ergänzend, conditional`; Trigger Klasse I bzw. Klasse IIa, IIb oder III |
| Expected Theme | Post-Market-Monitoring (Ex-ante-Erwartung) |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.39 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Grundlage ist die abgeschlossene Research-Adjudikation zu Art. 85 und Art. 86. Die Temp-IDs `M85-A` bis `M86-R` sind ausschließlich Evidenzkennungen; permanente IDs werden nur in [RR_CATALOG.yaml](RR_CATALOG.yaml) vergeben. Titel, Requirement Texte, Locators, Trigger und Modalitäten sind unverändert aus der Research-Adjudikation übernommen; die Texte sind kontrollierte normative Paraphrasen.

**Quellentreue:** Maßgeblich ist ausschließlich `02017R0745-20260719`. Recherchelinks der Adjudikation auf den Basisrechtsakt werden nicht als maßgebliche Evidenz übernommen.

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Geprüfte potenzielle Einheiten | **28** |
| Finale `RR` | **25** |
| davon regulär | 0 |
| davon conditional | 25 |
| 0-`RR` | 3 |
| Unresolved | 0 |
| Vollständige Deduplizierungen | 0 |

| Quellenbereich | `RR` | 0-`RR` | IDs |
| --- | --- | --- | --- |
| Art. 85 | 7 | 0 | `RR-353` bis `RR-359` |
| Art. 86 | 18 | 3 | `RR-360` bis `RR-377` |
| **Gesamt** | **25** | **3** | |

**Theme:** 25 × `Post-Market-Monitoring`. **Lebenszyklus:** 25 × `Post-Market-Überwachung`.

Reine Trigger und Ausnahmen werden nicht als eigene potenzielle Einheit gezählt; gesondert adjudizierte Modalitäts- und Institutionsteile sind als 0-`RR` geführt.

---

## 3. Source Verification

**PASS.** Verbindliche Arbeitsfassung ist die MDR, konsolidierte Fassung 19.07.2026. Art. 85 und 86 sind im geltenden Rechtsstand als PMS-Bericht für Klasse I bzw. regelmäßig aktualisierter Bericht über die Sicherheit (PSUR) für die Klassen IIa, IIb und III strukturiert. DE/EN: keine für Atomisierung oder Conditionality materielle Divergenz.

---

## 4. Art. 85 — 7 `RR`

Art. 85 gilt ausschließlich für Produkte der Klasse I. Dieser Klassenbezug ist Outer Applicability und keine eigene `RR`. Der Artikel verlangt einen PMS-Bericht, bestimmte Berichtsinhalte, die Aktualisierung bei Bedarf und die Bereitstellung für die zuständige Behörde auf Ersuchen (`M85-A` bis `M85-G`).

- **Ergebnisse und Schlussfolgerungen getrennt** (`M85-B`, `M85-C`): Ein Bericht kann Analyseergebnisse korrekt zusammenfassen, daraus gezogene Schlussfolgerungen aber unvollständig wiedergeben; beide bilden selbständig verständliche Berichtsanforderungen.
- **Begründung und Beschreibung getrennt** (`M85-D`, `M85-E`): Eine Maßnahme kann beschrieben sein, ohne ihre Begründung darzustellen, und umgekehrt.

---

## 5. Art. 86 — 18 `RR`, 3 × 0 `RR`

Art. 86 Abs. 1 gilt für Produkte der Klassen IIa, IIb und III. Er verlangt einen PSUR mit definiertem Inhalt, klassenspezifischer Aktualisierung und dokumentarischer Einordnung. Abs. 2 und 3 legen unterschiedliche Übermittlungs- bzw. Bereitstellungswege fest.

### 5.1 Abs. 1

| Bestandteil | Ergebnis |
| --- | --- |
| Erstellung eines PSUR | `M86-A` |
| „für jedes Produkt und gegebenenfalls jede Kategorie/Gruppe" | 0 `RR` — Umfangs-/Granularitätsmodalität von `M86-A` |
| Zusammenfassung der Analyseergebnisse / -schlussfolgerungen | `M86-B`, `M86-C` |
| Begründung / Beschreibung ergriffener Präventiv- und Korrekturmaßnahmen | `M86-D`, `M86-E` |
| Schlussfolgerungen der Nutzen-Risiko-Abwägung | `M86-F` |
| wichtigste PMCF-Ergebnisse | `M86-G` |
| Gesamtabsatzmenge | `M86-H` |
| Schätzung von Größe und weiteren Merkmalen der Anwender- bzw. Patientenpopulation | `M86-I` |
| Nutzungshäufigkeit, soweit praktikabel | `M86-J` |
| mindestens jährliche Aktualisierung für Klasse IIb und III | `M86-K` |
| Aktualisierung bei Bedarf für Klasse IIa | `M86-L` |
| Aktualisierung mindestens alle zwei Jahre für Klasse IIa | `M86-M` |
| PSUR als Teil der technischen Dokumentation bei Nicht-Sonderanfertigungen | `M86-N` |
| PSUR in der Dokumentation nach Anhang XIII bei Sonderanfertigungen | `M86-O` |

**IIa-Aktualisierung getrennt** (`M86-L`, `M86-M`): Ein Hersteller kann den PSUR spätestens alle zwei Jahre aktualisieren, aber einen früher entstandenen Aktualisierungsbedarf nicht rechtzeitig umsetzen; umgekehrt können bedarfsbezogene Aktualisierungen erfolgen, während die maximale Zweijahresfrist überschritten wird.

**Technische Dokumentation nicht doppelt atomisiert:** Die identische Pflicht für Klasse IIa einerseits und IIb/III andererseits ergibt einen gemeinsamen Sollzustand für alle Art.-86-Klassen (`M86-N`) mit der ausdrücklichen Sonderanfertigungs-Ausnahme; die Sonderanfertigungsroute ist `M86-O`.

### 5.2 Abs. 2

Für Produkte der Klasse III oder implantierbare Produkte übermittelt der Hersteller den PSUR über das elektronische System nach Art. 92 an die nach Art. 52 beteiligte Benannte Stelle (`M86-P`; elektronische Übermittlung als verpflichtende Modalität). Prüfung und Eintragung der Bewertung durch die Benannte Stelle (Satz 2) sowie die anschließende Zugänglichkeit für Behörden (Satz 3) sind 0 `RR` (Abschnitt 6).

### 5.3 Abs. 3

Für Art.-86-Produkte, die nicht unter Abs. 2 fallen: PSUR der beteiligten Benannten Stelle verfügbar machen (`M86-Q`) und der zuständigen Behörde auf Ersuchen verfügbar machen (`M86-R`).

---

## 6. 0-`RR`-Entscheidungen

| Nr. | Fundstelle | Bestandteil | Behandlung |
| --- | --- | --- | --- |
| 1 | `SRC-001#Art.86/Abs.1` | „für jedes Produkt und gegebenenfalls jede Kategorie/Gruppe" als eigenständige Pflicht | 0 `RR` — Umfangs-/Granularitätsmodalität von `M86-A` |
| 2 | `SRC-001#Art.86/Abs.2/Satz.2` | Benannte Stelle prüft den PSUR und trägt ihre Bewertung in das elektronische System ein | 0 `RR` — institutionelle Pflicht, kein Hersteller-Gap |
| 3 | `SRC-001#Art.86/Abs.2/Satz.3` | PSUR und Bewertung der Benannten Stelle werden Behörden über das System zugänglich | 0 `RR` — kein eigenständiger Hersteller-Sollzustand |

Klassenbezüge, „soweit praktikabel", „wenn erforderlich", die Sonderanfertigungs-Ausnahme und Behördenanforderungen werden nicht zusätzlich als 0-`RR` gezählt; sie bleiben Trigger bzw. Modalitäten der jeweiligen `RR`. **Zählung:** 25 `RR` + 3 0-`RR` = 28.

---

## 7. Theme, Lebenszyklus und Conditionality

**Theme:** 25 × `Post-Market-Monitoring`.

**Lebenszyklus:** 25 × `Post-Market-Überwachung`; alle übrigen Phasen 0. Die Beteiligung einer Benannten Stelle in Art. 86 Abs. 2 macht die Herstellerpflicht nicht automatisch zur Phase `Konformitätsbewertung`: Normativer Gegenstand ist die nach dem Inverkehrbringen erfolgende PSUR-Übermittlung.

**Conditionality (0 regulär / 25 conditional):** Art. 85 gilt nur für Klasse I, Art. 86 nur für die Klassen IIa, IIb und III bzw. definierte Untergruppen. Jede extrahierte `RR` besitzt damit eine echte produktklassenabhängige Outer Applicability; lokale Bedingungen wie „wenn erforderlich", „soweit praktikabel", Sonderanfertigung oder Behördenanforderung kommen als Inner Trigger hinzu. Kein neues Katalogfeld; die Bedingungen stehen im Requirement Text.

| Klassenzweig | Kandidaten |
| --- | --- |
| Klasse I | `M85-A` bis `M85-G` |
| Klasse IIa, IIb oder III | `M86-A` bis `M86-J`, `M86-N`, `M86-O` |
| Klasse IIb oder III | `M86-K` |
| Klasse IIa | `M86-L`, `M86-M` |
| Klasse III oder implantierbares Art.-86-Produkt | `M86-P` |
| Art.-86-Produkt außerhalb Abs. 2 | `M86-Q`, `M86-R` |

---

## 8. Kandidatenübersicht

| Kandidat | `RR` | Primary | Outer Trigger | Inner Trigger / Modalität |
| --- | --- | --- | --- | --- |
| `M85-A` | `RR-353` | `SRC-001#Art.85/Satz.1` | Produkt Klasse I | — |
| `M85-B` | `RR-354` | `SRC-001#Art.85/Satz.1` | Klasse I | — |
| `M85-C` | `RR-355` | `SRC-001#Art.85/Satz.1` | Klasse I | — |
| `M85-D` | `RR-356` | `SRC-001#Art.85/Satz.1` | Klasse I | Maßnahmen wurden ergriffen |
| `M85-E` | `RR-357` | `SRC-001#Art.85/Satz.1` | Klasse I | Maßnahmen wurden ergriffen |
| `M85-F` | `RR-358` | `SRC-001#Art.85/Satz.2` | Klasse I | Aktualisierungsbedarf |
| `M85-G` | `RR-359` | `SRC-001#Art.85/Satz.2` | Klasse I | zuständige Behörde fordert Bericht an |
| `M86-A` | `RR-360` | `SRC-001#Art.86/Abs.1` | Klasse IIa, IIb oder III | Kategorie/Gruppe = Umfangsmodalität |
| `M86-B` | `RR-361` | `SRC-001#Art.86/Abs.1` | IIa/IIb/III | — |
| `M86-C` | `RR-362` | `SRC-001#Art.86/Abs.1` | IIa/IIb/III | — |
| `M86-D` | `RR-363` | `SRC-001#Art.86/Abs.1` | IIa/IIb/III | Maßnahmen wurden ergriffen |
| `M86-E` | `RR-364` | `SRC-001#Art.86/Abs.1` | IIa/IIb/III | Maßnahmen wurden ergriffen |
| `M86-F` | `RR-365` | `SRC-001#Art.86/Abs.1/Buchst.a` | IIa/IIb/III | — |
| `M86-G` | `RR-366` | `SRC-001#Art.86/Abs.1/Buchst.b` | IIa/IIb/III | kein zusätzlicher Trigger aus Art.86 |
| `M86-H` | `RR-367` | `SRC-001#Art.86/Abs.1/Buchst.c` | IIa/IIb/III | — |
| `M86-I` | `RR-368` | `SRC-001#Art.86/Abs.1/Buchst.c` | IIa/IIb/III | — |
| `M86-J` | `RR-369` | `SRC-001#Art.86/Abs.1/Buchst.c` | IIa/IIb/III | Nutzungshäufigkeit bestimmbar/praktikabel |
| `M86-K` | `RR-370` | `SRC-001#Art.86/Abs.1` | Klasse IIb oder III | — |
| `M86-L` | `RR-371` | `SRC-001#Art.86/Abs.1` | Klasse IIa | Aktualisierungsbedarf |
| `M86-M` | `RR-372` | `SRC-001#Art.86/Abs.1` | Klasse IIa | — |
| `M86-N` | `RR-373` | `SRC-001#Art.86/Abs.1` | IIa/IIb/III | Ausnahme: Sonderanfertigung |
| `M86-O` | `RR-374` | `SRC-001#Art.86/Abs.1` | IIa/IIb/III + Sonderanfertigung | alternative Dokumentationsroute |
| `M86-P` | `RR-375` | `SRC-001#Art.86/Abs.2/Satz.1` | Klasse III ODER implantierbares Art.-86-Produkt | elektronische Übermittlung ist verpflichtende Modalität |
| `M86-Q` | `RR-376` | `SRC-001#Art.86/Abs.3` | Art.-86-Produkt außerhalb Abs.2 | — |
| `M86-R` | `RR-377` | `SRC-001#Art.86/Abs.3` | Art.-86-Produkt außerhalb Abs.2 | zuständige Behörde fordert PSUR an |

---

## 9. Deduplizierung gegen `RR-296` bis `RR-352`

**Vollständige Deduplizierungen: 0.** Keine bestehende `RR` wird geändert.

| Neue Kandidaten | Bestehende `RR` | Ergebnis | Begründung |
| --- | --- | --- | --- |
| `M85-B`, `M85-C`, `M86-B`, `M86-C` | `RR-306` Analyse von PMS-Daten; `RR-307` Ziehen notwendiger Schlussfolgerungen | PARTIAL_OVERLAP | bestehende `RR` verlangen Analyse bzw. Schlussfolgerungsbildung; Art. 85/86 verlangen deren Darstellung in einem regulatorischen Bericht |
| `M85-D`, `M85-E`, `M86-D`, `M86-E` | `RR-308`, `RR-309`, `RR-318`, `RR-326` | PARTIAL_OVERLAP | bestehende `RR` betreffen Ermittlung bzw. Durchführung von Maßnahmen; die neuen `RR` Begründung bzw. Beschreibung dieser Maßnahmen im Bericht |
| `M86-F` | `RR-311` Aktualisierung der Nutzen-Risiko-Abwägung | PARTIAL_OVERLAP | `RR-311` verlangt die Aktualisierung selbst; `M86-F` die Darstellung ihrer Schlussfolgerungen im PSUR |
| `M86-G` | `RR-352` PMCF-Plan oder Nichtanwendbarkeitsbegründung | DISTINCT | Planung bzw. Nichtanwendbarkeit von PMCF gegenüber Darstellung der tatsächlich vorliegenden PMCF-Ergebnisse |
| `M85-F`, `M86-K`, `M86-L`, `M86-M` | `RR-301` Aktualisierung des PMS-Systems | DISTINCT | Aktualisierung des Systems gegenüber Aktualisierung eines Berichts |
| `M86-N`, `M86-O` | `RR-325` Aktualisierung der technischen Dokumentation | PARTIAL_OVERLAP | allgemeine PMS-bedingte Aktualisierung der technischen Dokumentation gegenüber ausdrücklicher Zuordnung des PSUR zu einem bestimmten Dokumentationssatz |
| `M85-G`, `M86-P`, `M86-Q`, `M86-R` | `RR-347` PMS-Kommunikationsverfahren | DISTINCT | `RR-347` verlangt einen PMS-Plan mit Kommunikationsverfahren; Art. 85/86 verlangen die tatsächliche Bereitstellung bzw. Übermittlung des fertigen Berichts |
| sämtliche Art.-86-Kandidaten | `RR-348` Bezugnahme des PMS-Plans auf Verfahren nach Art. 86 | DISTINCT | `RR-348` verlangt nur, dass der PMS-Plan auf entsprechende Verfahren verweist; Art. 86 normiert die materiellen Berichtspflichten selbst |

---

## 10. Source Dependencies

**Externe Source Dependency: NEIN.** Die erforderlichen normativen Verknüpfungen liegen innerhalb von `SRC-001`: Art. 85/86 → Art. 84 (Herkunft der PMS-Daten); Art. 86 → PMCF; Art. 86 Abs. 1 → Anhänge II, III und XIII; Art. 86 Abs. 2 → Art. 52 und Art. 92. Für `M86-P` ist keine externe eIFU- oder andere Rechtsquelle erforderlich: Art. 86 Abs. 2 verlangt selbst die Übermittlung über das elektronische System nach Art. 92.

---

## 11. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 und [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 reichen aus; keine Änderung erforderlich. Kein neues Katalogfeld.

---

## 12. Kandidaten

Für alle 25 Kandidaten gilt: Theme `Post-Market-Monitoring`; Lifecycle `Post-Market-Überwachung`; conditional; Supplementary keine; `uncertainty` null; Katalogstatus `aktiv`; Software-Scope: in Scope.

### M85-A — Erstellung des PMS-Berichts

- **Title EN:** Preparation of the Post-Market Surveillance Report
- **DE:** Für ein Produkt der Klasse I muss der Hersteller einen Bericht über die Überwachung nach dem Inverkehrbringen erstellen.
- **EN:** For a class I device, the manufacturer shall prepare a post-market surveillance report.
- **Primary:** `SRC-001#Art.85/Satz.1`
- **Outer Trigger:** Produkt Klasse I
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-353`

### M85-B — Zusammenfassung der PMS-Analyseergebnisse

- **Title EN:** Summary of PMS Analysis Results
- **DE:** Für ein Produkt der Klasse I muss der Hersteller im PMS-Bericht die Ergebnisse der Analysen der aufgrund des PMS-Plans nach Artikel 84 gesammelten PMS-Daten zusammenfassen.
- **EN:** For a class I device, the manufacturer shall summarise in the PMS report the results of the analyses of PMS data gathered pursuant to the post-market surveillance plan referred to in Article 84.
- **Primary:** `SRC-001#Art.85/Satz.1`
- **Outer Trigger:** Klasse I
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-354`

### M85-C — Zusammenfassung der PMS-Analyseschlussfolgerungen

- **Title EN:** Summary of PMS Analysis Conclusions
- **DE:** Für ein Produkt der Klasse I muss der Hersteller im PMS-Bericht die Schlussfolgerungen aus den Analysen der aufgrund des PMS-Plans nach Artikel 84 gesammelten PMS-Daten zusammenfassen.
- **EN:** For a class I device, the manufacturer shall summarise in the PMS report the conclusions of the analyses of PMS data gathered pursuant to the post-market surveillance plan referred to in Article 84.
- **Primary:** `SRC-001#Art.85/Satz.1`
- **Outer Trigger:** Klasse I
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-355`

### M85-D — Begründung ergriffener Präventiv- und Korrekturmaßnahmen

- **Title EN:** Rationale for Preventive and Corrective Actions Taken
- **DE:** Für ein Produkt der Klasse I muss der Hersteller im PMS-Bericht die Begründung für etwaige ergriffene Präventiv- und Korrekturmaßnahmen darlegen.
- **EN:** For a class I device, the manufacturer shall include in the PMS report the rationale for any preventive and corrective actions taken.
- **Primary:** `SRC-001#Art.85/Satz.1`
- **Outer Trigger:** Klasse I
- **Inner Trigger / Modalität:** Maßnahmen wurden ergriffen
- **Katalog:** `RR-356`

### M85-E — Beschreibung ergriffener Präventiv- und Korrekturmaßnahmen

- **Title EN:** Description of Preventive and Corrective Actions Taken
- **DE:** Für ein Produkt der Klasse I muss der Hersteller im PMS-Bericht etwaige ergriffene Präventiv- und Korrekturmaßnahmen beschreiben.
- **EN:** For a class I device, the manufacturer shall describe in the PMS report any preventive and corrective actions taken.
- **Primary:** `SRC-001#Art.85/Satz.1`
- **Outer Trigger:** Klasse I
- **Inner Trigger / Modalität:** Maßnahmen wurden ergriffen
- **Katalog:** `RR-357`

### M85-F — Bedarfsbezogene Aktualisierung des PMS-Berichts

- **Title EN:** Updating the PMS Report When Necessary
- **DE:** Für ein Produkt der Klasse I muss der Hersteller den PMS-Bericht aktualisieren, wenn dies erforderlich ist.
- **EN:** For a class I device, the manufacturer shall update the PMS report when necessary.
- **Primary:** `SRC-001#Art.85/Satz.2`
- **Outer Trigger:** Klasse I
- **Inner Trigger / Modalität:** Aktualisierungsbedarf
- **Katalog:** `RR-358`

### M85-G — Bereitstellung des PMS-Berichts für die zuständige Behörde

- **Title EN:** Availability of the PMS Report to the Competent Authority
- **DE:** Für ein Produkt der Klasse I muss der Hersteller den PMS-Bericht der zuständigen Behörde auf Ersuchen zur Verfügung stellen.
- **EN:** For a class I device, the manufacturer shall make the PMS report available to the competent authority upon request.
- **Primary:** `SRC-001#Art.85/Satz.2`
- **Outer Trigger:** Klasse I
- **Inner Trigger / Modalität:** zuständige Behörde fordert Bericht an
- **Katalog:** `RR-359`

### M86-A — Erstellung des PSUR

- **Title EN:** Preparation of the PSUR
- **DE:** Für ein Produkt der Klasse IIa, IIb oder III muss der Hersteller einen regelmäßig aktualisierten Bericht über die Sicherheit für jedes Produkt und, soweit relevant, für jede Produktkategorie oder Produktgruppe erstellen.
- **EN:** For a class IIa, IIb or III device, the manufacturer shall prepare a periodic safety update report for each device and, where relevant, for each category or group of devices.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** Klasse IIa, IIb oder III
- **Inner Trigger / Modalität:** Kategorie/Gruppe = Umfangsmodalität
- **Katalog:** `RR-360`

### M86-B — Zusammenfassung der PMS-Analyseergebnisse im PSUR

- **Title EN:** Summary of PMS Analysis Results in the PSUR
- **DE:** Der Hersteller muss im PSUR die Ergebnisse der Analysen der aufgrund des PMS-Plans nach Artikel 84 gesammelten PMS-Daten zusammenfassen.
- **EN:** The manufacturer shall summarise in the PSUR the results of the analyses of PMS data gathered pursuant to the post-market surveillance plan referred to in Article 84.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-361`

### M86-C — Zusammenfassung der PMS-Analyseschlussfolgerungen im PSUR

- **Title EN:** Summary of PMS Analysis Conclusions in the PSUR
- **DE:** Der Hersteller muss im PSUR die Schlussfolgerungen aus den Analysen der aufgrund des PMS-Plans nach Artikel 84 gesammelten PMS-Daten zusammenfassen.
- **EN:** The manufacturer shall summarise in the PSUR the conclusions of the analyses of PMS data gathered pursuant to the post-market surveillance plan referred to in Article 84.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-362`

### M86-D — Begründung ergriffener Präventiv- und Korrekturmaßnahmen im PSUR

- **Title EN:** Rationale for Preventive and Corrective Actions in the PSUR
- **DE:** Der Hersteller muss im PSUR die Begründung für etwaige ergriffene Präventiv- und Korrekturmaßnahmen darlegen.
- **EN:** The manufacturer shall include in the PSUR the rationale for any preventive and corrective actions taken.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** Maßnahmen wurden ergriffen
- **Katalog:** `RR-363`

### M86-E — Beschreibung ergriffener Präventiv- und Korrekturmaßnahmen im PSUR

- **Title EN:** Description of Preventive and Corrective Actions in the PSUR
- **DE:** Der Hersteller muss im PSUR etwaige ergriffene Präventiv- und Korrekturmaßnahmen beschreiben.
- **EN:** The manufacturer shall describe in the PSUR any preventive and corrective actions taken.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** Maßnahmen wurden ergriffen
- **Katalog:** `RR-364`

### M86-F — Schlussfolgerungen der Nutzen-Risiko-Abwägung im PSUR

- **Title EN:** Benefit-Risk Conclusions in the PSUR
- **DE:** Der Hersteller muss während der gesamten Lebensdauer des Produkts im PSUR die Schlussfolgerungen aus der Nutzen-Risiko-Abwägung aufführen.
- **EN:** Throughout the lifetime of the device, the manufacturer shall set out in the PSUR the conclusions of the benefit-risk determination.
- **Primary:** `SRC-001#Art.86/Abs.1/Buchst.a`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-365`

### M86-G — Wichtigste PMCF-Ergebnisse im PSUR

- **Title EN:** Main PMCF Findings in the PSUR
- **DE:** Der Hersteller muss während der gesamten Lebensdauer des Produkts im PSUR die wichtigsten Ergebnisse der klinischen Nachbeobachtung nach dem Inverkehrbringen aufführen.
- **EN:** Throughout the lifetime of the device, the manufacturer shall set out in the PSUR the main findings of the PMCF.
- **Primary:** `SRC-001#Art.86/Abs.1/Buchst.b`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** kein zusätzlicher Trigger aus Art.86
- **Katalog:** `RR-366`

### M86-H — Gesamtabsatzmenge im PSUR

- **Title EN:** Device Sales Volume in the PSUR
- **DE:** Der Hersteller muss während der gesamten Lebensdauer des Produkts im PSUR die Gesamtabsatzmenge des Produkts angeben.
- **EN:** Throughout the lifetime of the device, the manufacturer shall set out in the PSUR the volume of sales of the device.
- **Primary:** `SRC-001#Art.86/Abs.1/Buchst.c`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-367`

### M86-I — Schätzung der Anwender-/Patientenpopulation im PSUR

- **Title EN:** Estimate of the Device-Using Population in the PSUR
- **DE:** Der Hersteller muss während der gesamten Lebensdauer des Produkts im PSUR eine Schätzung der Anzahl und weiterer Merkmale der Personen angeben, bei denen das Produkt zur Anwendung kommt.
- **EN:** Throughout the lifetime of the device, the manufacturer shall set out in the PSUR an estimate of the size and other characteristics of the population using the device.
- **Primary:** `SRC-001#Art.86/Abs.1/Buchst.c`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-368`

### M86-J — Nutzungshäufigkeit im PSUR

- **Title EN:** Device Usage Frequency in the PSUR
- **DE:** Soweit dies praktikabel ist, muss der Hersteller während der gesamten Lebensdauer des Produkts im PSUR die Häufigkeit der Produktverwendung angeben.
- **EN:** Where practicable, throughout the lifetime of the device the manufacturer shall set out in the PSUR the frequency of use of the device.
- **Primary:** `SRC-001#Art.86/Abs.1/Buchst.c`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** Nutzungshäufigkeit bestimmbar/praktikabel
- **Katalog:** `RR-369`

### M86-K — Mindestens jährliche PSUR-Aktualisierung für Klasse IIb und III

- **Title EN:** At Least Annual PSUR Update for Class IIb and III
- **DE:** Für Produkte der Klassen IIb und III muss der Hersteller den PSUR mindestens einmal jährlich aktualisieren.
- **EN:** For class IIb and class III devices, the manufacturer shall update the PSUR at least annually.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** Klasse IIb oder III
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-370`

### M86-L — Bedarfsbezogene PSUR-Aktualisierung für Klasse IIa

- **Title EN:** Needs-Based PSUR Update for Class IIa
- **DE:** Für ein Produkt der Klasse IIa muss der Hersteller den PSUR aktualisieren, wenn dies erforderlich ist.
- **EN:** For a class IIa device, the manufacturer shall update the PSUR when necessary.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** Klasse IIa
- **Inner Trigger / Modalität:** Aktualisierungsbedarf
- **Katalog:** `RR-371`

### M86-M — Mindestens zweijährliche PSUR-Aktualisierung für Klasse IIa

- **Title EN:** At Least Biennial PSUR Update for Class IIa
- **DE:** Für ein Produkt der Klasse IIa muss der Hersteller den PSUR mindestens alle zwei Jahre aktualisieren.
- **EN:** For a class IIa device, the manufacturer shall update the PSUR at least every two years.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** Klasse IIa
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-372`

### M86-N — PSUR als Bestandteil der technischen Dokumentation

- **Title EN:** PSUR as Part of the Technical Documentation
- **DE:** Für ein Produkt der Klasse IIa, IIb oder III, das keine Sonderanfertigung ist, muss der Hersteller sicherstellen, dass der PSUR Bestandteil der technischen Dokumentation gemäß den Anhängen II und III ist.
- **EN:** For a class IIa, IIb or III device other than a custom-made device, the manufacturer shall ensure that the PSUR forms part of the technical documentation specified in Annexes II and III.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** IIa/IIb/III
- **Inner Trigger / Modalität:** Ausnahme: Sonderanfertigung
- **Katalog:** `RR-373`

### M86-O — PSUR-Dokumentation bei Sonderanfertigungen

- **Title EN:** PSUR Documentation for Custom-Made Devices
- **DE:** Handelt es sich bei einem unter Artikel 86 fallenden Produkt um eine Sonderanfertigung, muss der Hersteller sicherstellen, dass der PSUR Bestandteil der Dokumentation gemäß Anhang XIII Abschnitt 2 ist.
- **EN:** Where a device falling under Article 86 is custom-made, the manufacturer shall ensure that the PSUR forms part of the documentation referred to in Section 2 of Annex XIII.
- **Primary:** `SRC-001#Art.86/Abs.1`
- **Outer Trigger:** IIa/IIb/III + Sonderanfertigung
- **Inner Trigger / Modalität:** alternative Dokumentationsroute
- **Katalog:** `RR-374`

### M86-P — Elektronische PSUR-Übermittlung an die Benannte Stelle

- **Title EN:** Electronic Submission of the PSUR to the Notified Body
- **DE:** Für ein Produkt der Klasse III oder ein implantierbares Produkt muss der Hersteller den PSUR über das elektronische System nach Artikel 92 an die gemäß Artikel 52 an der Konformitätsbewertung beteiligte Benannte Stelle übermitteln.
- **EN:** For a class III device or an implantable device, the manufacturer shall submit the PSUR through the electronic system referred to in Article 92 to the notified body involved in the conformity assessment pursuant to Article 52.
- **Primary:** `SRC-001#Art.86/Abs.2/Satz.1`
- **Outer Trigger:** Klasse III ODER implantierbares Art.-86-Produkt
- **Inner Trigger / Modalität:** elektronische Übermittlung ist verpflichtende Modalität
- **Katalog:** `RR-375`

### M86-Q — Bereithaltung des PSUR für die Benannte Stelle

- **Title EN:** Availability of the PSUR to the Notified Body
- **DE:** Für ein unter Artikel 86 fallendes Produkt, das nicht von Artikel 86 Absatz 2 erfasst wird, muss der Hersteller den PSUR der an der Konformitätsbewertung beteiligten Benannten Stelle zur Verfügung stellen.
- **EN:** For a device falling under Article 86 that is not referred to in Article 86(2), the manufacturer shall make the PSUR available to the notified body involved in the conformity assessment.
- **Primary:** `SRC-001#Art.86/Abs.3`
- **Outer Trigger:** Art.-86-Produkt außerhalb Abs.2
- **Inner Trigger / Modalität:** —
- **Katalog:** `RR-376`

### M86-R — Bereithaltung des PSUR für zuständige Behörden

- **Title EN:** Availability of the PSUR to Competent Authorities
- **DE:** Für ein unter Artikel 86 fallendes Produkt, das nicht von Artikel 86 Absatz 2 erfasst wird, muss der Hersteller den PSUR einer zuständigen Behörde auf Ersuchen zur Verfügung stellen.
- **EN:** For a device falling under Article 86 that is not referred to in Article 86(2), the manufacturer shall make the PSUR available to competent authorities upon request.
- **Primary:** `SRC-001#Art.86/Abs.3`
- **Outer Trigger:** Art.-86-Produkt außerhalb Abs.2
- **Inner Trigger / Modalität:** zuständige Behörde fordert PSUR an
- **Katalog:** `RR-377`

---

## 13. Quellenfundstelle

| Bezug | URL |
| --- | --- |
| `SRC-001`, konsolidierte Fassung 19.07.2026 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02017R0745-20260719 |

---

## 14. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der systematischen Extraktion des klassenspezifischen MDR-PMS-Berichtsblocks `SRC-001#Art.85` und `SRC-001#Art.86`. 28 potenzielle Einheiten; 25 finale Gap-`RR`-Kandidaten (Art. 85: 7, Art. 86: 18), alle conditional; 3 0-`RR`-Entscheidungen. Theme 25 × Post-Market-Monitoring, Lifecycle 25 × Post-Market-Überwachung. Abgleich gegen `RR-296` bis `RR-352`: 0 vollständige Deduplizierungen; bestehende `RR` unverändert. Keine externe Source Dependency. 0 unresolved. |
