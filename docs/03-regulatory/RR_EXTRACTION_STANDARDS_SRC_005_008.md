# Systematische RR-Extraktion — Normen SRC-005 bis SRC-008

Version 1.1 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quellen | `SRC-005` ISO 13485:2016, `SRC-006` ISO 14971:2019, `SRC-007` IEC 62304:2006+AMD1:2015, `SRC-008` IEC 62366-1:2015+AMD1:2020 |
| Quellenebene | C (Normen) nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 4 |
| Ergebnis | 594 eingefrorene Normkandidaten → **582 neue `RR`** (`RR-378` bis `RR-959`) |
| Maschinenlesbare Zuordnung | [RR_STANDARDS_MAPPING_SRC_005_008.yaml](RR_STANDARDS_MAPPING_SRC_005_008.yaml) Version 1.1 |
| Katalog | [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.25, redaktionell präzisiert in Version 0.26 (Abschnitt 6.1) |
| Applicability | [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.4 |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.48, Abschnitte 10.37 und 10.38 |

Grundlage ist die abgeschlossene Research-Adjudikation aus Block 3 (Einzeladjudikation je Norm, Atomisierungs-QC für `SRC-005`, normübergreifende Deduplizierung). Die Adjudikation wurde **unverändert** übernommen: keine erneute Normextraktion, keine neue regulatorische Interpretation, keine erneute Deduplizierung. Temp-IDs (`ISO13485-RR-NNN`, `ISO14971-RR-NNN`, `IEC62304-RR-NNN`, `IEC62366-RR-NNN`, `NORM-MERGE-NN`) sind ausschließlich Evidenzkennungen; permanente IDs werden nur in [RR_CATALOG.yaml](RR_CATALOG.yaml) vergeben.

**Kein Normvolltext im Repository.** Dieses Dokument und die Zuordnungsdatei enthalten ausschließlich wissenschaftlich erforderliche Metadaten, kontrollierte Paraphrasen, Lokatoren sowie Coverage- und Evidenzangaben. Weder die lizenzierten Normvolltexte noch das Research-Handoff-Dokument sind Bestandteil des Repositorys; das Handoff ist kein Lizenzersatz.

---

## 2. Quellen und autorisierte Arbeitsfassungen

Die `SRC`-IDs bezeichnen weiterhin die in [SOURCES.md](SOURCES.md) registrierten Normen. Adjudiziert wurde jeweils auf Grundlage der im Projekt autorisiert vorliegenden deutschen Übernahme; die englischen Requirement Texte sind kontrollierte Paraphrasen des deutschen Volltexts und keine wörtlichen Zitate einer englischen Originalausgabe.

| Quelle | Autorisierte Arbeitsfassung | Provenienzhinweis laut Adjudikation | Offener Punkt |
| --- | --- | --- | --- |
| `SRC-005` | DIN EN ISO 13485:2016-08 (deutsche Fassung EN ISO 13485:2016) | Anforderungskörper ISO 13485:2016; ausschließlich der ISO-2016-Anforderungstext verwendet | `OPEN_SOURCE_PACKAGE_CHECK` (Berichtigung, Abschnitt 2.1) |
| `SRC-006` | DIN EN ISO 14971:2020-07 (deutsche Fassung EN ISO 14971:2019) | ISO 14971:2019 ohne Abänderung als EN ISO 14971:2019 übernommen; keine normativen Verweisungen | keiner |
| `SRC-007` | DIN EN 62304 (VDE 0750-101):2016-10 | EN-Übernahme von IEC 62304:2006 und A1:2015 ohne Änderung; Corrigendum 2008 eingearbeitet; ISO 14971 als normative Verweisung | keiner; die originale IEC-CSV-Datei liegt **nicht** vor und wird nicht als Arbeitsquelle behauptet |
| `SRC-008` | DIN EN 62366-1 (VDE 0750-241-1):2021-08 | Anforderungskörper IEC 62366-1:2015 + COR1:2016 + A1:2020; CENELEC-AC:2015 eingearbeitet; ISO 14971:2019 als einzige normative Verweisung | keiner; die originale IEC-CSV-Datei liegt **nicht** vor und wird nicht als Arbeitsquelle behauptet |

### 2.1 `OPEN_SOURCE_PACKAGE_CHECK` für `SRC-005`

Die Arbeitsfassung weist darauf hin, dass zu dieser DIN-Ausgabe eine oder mehrere Berichtigungen erschienen sind; sie nennt weder Nummer noch Datum. Ein Berichtigungstext liegt im autorisierten Projektbestand nicht vor. Eine Änderung des Anforderungskörpers ist daher **nicht feststellbar**; eine Bezeichnung der Berichtigung wird nicht erfunden.

- `RR`-Freeze der 209 `SRC-005`-Kandidaten: **nicht blockiert**; kein Requirement-unresolved.
- Finaler Source-/Evidence-Freeze für `SRC-005`: **offen**, bis der angekündigte Berichtigungstext beschafft und geprüft ist. Ändert er eine normative Klausel, genügt ein gezielter Delta-Audit der betroffenen Klauseln.

**Provenienzhinweis `SRC-006`:** Die Arbeitsdatei DIN EN ISO 14971:2020-07 ist laut Adjudikation mit dem nationalen Nachfolgedokument DIN EN ISO 14971:2022-04 gekennzeichnet. Maßgeblich bleibt der ISO-14971:2019-Anforderungskörper (`SRC-006`); daraus entsteht weder ein Requirement-unresolved noch ein offener Source-Package-Punkt. Für die Zitierung ist lediglich die verwendete nationale Hüllfassung (2020-07) anzugeben.

### 2.2 Geprüfter Normumfang und Einordnung nicht extrahierter Bereiche

Zusammenfassung der adjudizierten Einordnung; es wurde nichts neu bewertet.

| Quelle | Normativ extrahiert (`INCLUDE_RR`) | `CROSSWALK_ONLY` bzw. Routing | `OUT_OF_SCOPE` | `DEFINITION_ONLY` / `INFORMATIVE` | Normative Verweisungen |
| --- | --- | --- | --- | --- | --- |
| `SRC-005` | Abschnitte 4.1 bis 8.5.3 | Abschnitt 1 (Verantwortung für ausgegliederte Prozesse, Ausschluss der Entwicklungslenkung – im MDSW-Kern keine generelle Freistellung –, Begründung nicht anwendbarer Anforderungen), Abschnitt 2 (ISO 9000:2015 ohne Import), physische Einzelpflichten aus 7.5.1 und Messmitteldetails aus 7.6 | vertrauliche Gesundheitsangaben (4.2.5), hygiene-, kontaminations-, sterilitäts-, verpackungs- und implantatspezifische Pflichten (6.4.1(a), 6.4.2, 7.5.2, 7.5.5, 7.5.7, 7.5.8 Rücksendesatz, 7.5.9.2, 7.5.11(a)/(b), 8.2.6 letzter Satz) | Abschnitt 3; Vorworte, Einleitung 0.1–0.5, Anmerkungen, Anhänge A, B, ZA, ZB, ZC, Literaturhinweise | ISO 9000:2015 (nicht importiert); kein Verweis auf IEC 62304 |
| `SRC-006` | Abschnitte 4.1 bis 10.4 | Abschnitt 1, Strukturliste 4.1, Planungs-Chapeau 4.4, Routing aus Abschnitt 6, Permissionen aus 7.4 und 8, Konformitätsprüfsätze | klinische Einzelfallentscheidung, Geschäftsrisiken (Abschnitt 1) | Abschnitt 3; Anmerkungen, Anhänge A bis C; ISO/TR 24971 nur informativ | keine |
| `SRC-007` | Abschnitte 4.1 bis 9.8 | 1.3, 1.4, Abschnitt 2 (Abhängigkeit zu ISO 14971), Klassenkriterien 4.3, **4.3/g (bis zur Klassifizierung Klasse-C-Anforderungen; als Applicability-Regel abgebildet, Abschnitt 8.5)**, 4.4.1 (Legacy-Route als Alternative), 5.7.4 erster Satz, 7.3.2, Anhang ZA | Validierung und Freigabe des Gesamtprodukts (Scope) | Abschnitt 3; Vorworte, Einleitung, Anmerkungen, Anhänge A bis D, ZZ | ISO 14971 → `SRC-006` |
| `SRC-008` | Abschnitte 4.1.1 bis 5.9 und Anhang C (C.2.1–C.2.5) | Abschnitt 1, Abschnitt 2 (Abhängigkeit zu ISO 14971), 4.1.2, 4.3, 5.10 (Route 5.1–5.9 oder Anhang C), C.1, C.2.1 (Wiederverwendung `IEC62366-RR-011` bis `017`), C.2.2 (Weiterleitung), Anhang ZA | Usability ohne Sicherheitsbezug; Bewertung/Reduzierung von Risiken aus anormalem Gebrauch | Abschnitt 3; Einleitung, Anmerkungen, Beispiele, Anhänge A, B, D, E, Literaturhinweise | ISO 14971:2019 → `SRC-006`; ISO 13485 und IEC 62304 keine normativen Verweisungen |

---

## 3. Eingefrorener Kandidatenbestand

| Quelle | Adjudizierte Kandidaten | Anmerkung |
| --- | --- | --- |
| `SRC-005` | **209** | 172 Kandidaten der Erstadjudikation; im Atomisierungs-QC wurden 30 Kandidaten in 67 Teilkandidaten (`NNN-A`, `NNN-B`, …) zerlegt: 142 unverändert + 67 = 209. Ein zerlegter Ausgangskandidat und seine Teilkandidaten werden nie gemeinsam gezählt. |
| `SRC-006` | **107** | |
| `SRC-007` | **185** | Sicherheitsklassen-Partition: ALL 2, PRE 5, A/B/C 103, nur B/C 48, nur C 9, Legacy 18 |
| `SRC-008` | **93** | Clause 4 gemeinsame Basis 10, reguläre Route 5.1–5.9 72, UOUP-spezifisch Anhang C 11 |
| **Gesamt** | **594** | Requirement-unresolved: **0** |

Die Themenzuordnung folgt den Zeilen der Adjudikation. Für `SRC-005` sind die zeilenbasierten Summen verbindlich (Erstadjudikation 120 / 39 / 13 = 172, final 137 `Qualitäts- und Risikomanagement` / 57 `Software-Lebenszyklus` / 15 `Post-Market-Monitoring` = 209); abweichende Summenangaben der Research-Übersichten wurden auf dieser Grundlage korrigiert.

---

## 4. Normübergreifende Deduplizierung

| Klasse | Ausgangskandidaten | Resultierende neue `RR` |
| --- | --- | --- |
| `EXISTING_RR_SUPPORT` | 1 | 0 |
| `CROSS_NORM_MERGE` | 15 | 6 |
| `NEW_UNIQUE_RR` | 576 | 576 |
| `CROSSWALK_ONLY` | 2 | 0 |
| unresolved | 0 | — |
| **Gesamt** | **594** | **582** |

Kontrolle: 1 + 15 + 576 + 2 = 594; 6 + 576 = 582. Die geringe Deduplizierungsquote ist methodisch beabsichtigt: Allgemeine QMS- und Risikomanagementpflichten wurden nicht mit software-, UOUP-, Legacy-, SOUP-, V&V- oder artefaktspezifischen Anforderungen zusammengezogen, wenn unterschiedliche Erfüllungsstatus möglich bleiben.

### 4.1 Bezug zu bestehenden `RR`

| Kandidat | Entscheidung | Behandlung im Repository |
| --- | --- | --- |
| `ISO14971-RR-064` (`SRC-006#Abschnitt 7.1`) | `EXISTING_RR_SUPPORT` → `RR-157` | `SOURCE_SUPPORT`-Beziehung in der Zuordnungsdatei; `RR-157` einschließlich Primary Source unverändert |
| `ISO14971-RR-021` (`SRC-006#Abschnitt 4.4`) | `CROSSWALK_ONLY` → `RR-145` und `RR-146` | je eine `SOURCE_SUPPORT`-Beziehung; der kombinierte Kandidat würde die bestehende Atomisierung zusammenführen; `RR-145` und `RR-146` unverändert |
| `IEC62304-RR-002` (`SRC-007#Abschnitt 4.2`) | `CROSSWALK_ONLY` → `RR-594` | `NORMATIVE_DEPENDENCY` von `SRC-007#Abschnitt 4.2` zu `RR-594` (aus `ISO14971-RR-002`, Risikomanagementprozess); kein zweiter Gap-Sollzustand |

Keine weitere Einheit wurde gegen `RR-001` bis `RR-377` vollständig dedupliziert. `RR-001` bis `RR-377` sind in Text, Titel, Quellen und ID unverändert.

### 4.2 Merge-Gruppen

| Gruppe | `RR` | Kandidaten | Primary | Supplementary |
| --- | --- | --- | --- | --- |
| `NORM-MERGE-01` Risikobeherrschungsmaßnahmen bestimmen | `RR-378` | `ISO14971-RR-063`, `IEC62304-RR-148` | `SRC-006#Abschnitt 7.1` | `SRC-007#Abschnitt 7.2.1` |
| `NORM-MERGE-02` Risikobeherrschungsmaßnahmen dokumentieren | `RR-379` | `ISO14971-RR-065`, `IEC62304-RR-149` | `SRC-006#Abschnitt 7.1` | `SRC-007#Abschnitt 7.2.1` |
| `NORM-MERGE-03` Implementierung verifizieren | `RR-380` | `ISO14971-RR-068`, `IEC62304-RR-153`, `IEC62366-RR-089` | `SRC-006#Abschnitt 7.2` | `SRC-007#Abschnitt 7.3.1`, `SRC-008#Anhang C/C.2.4` |
| `NORM-MERGE-04` Verifizierung dokumentieren | `RR-381` | `ISO14971-RR-069`, `IEC62304-RR-154`, `IEC62366-RR-091` | `SRC-006#Abschnitt 7.2` | `SRC-007#Abschnitt 7.3.1`, `SRC-008#Anhang C/C.2.4` |
| `NORM-MERGE-05` Restrisiko (erneut) bewerten | `RR-382` | `ISO14971-RR-072`, `IEC62366-RR-082`, `IEC62366-RR-092` | `SRC-006#Abschnitt 7.3` | `SRC-008#Abschnitt 5.9`, `SRC-008#Anhang C/C.2.5` |
| `NORM-MERGE-06` Ergebnis der Restrisikobewertung dokumentieren | `RR-383` | `ISO14971-RR-073`, `IEC62366-RR-093` | `SRC-006#Abschnitt 7.3` | `SRC-008#Anhang C/C.2.5` |

Requirement Texte DE/EN der Merge-`RR` sind unverändert aus der Adjudikation übernommen. Die unterstützenden Normfundstellen stehen als `sources.supplementary`, weil sie nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8 Umfang und Bedingung des gemeinsamen Sollzustands (Sicherheitsklasse, UOUP-Route, Ablagemodalität) tragen; so bleiben alle beteiligten Quellen am `RR` selbst rückverfolgbar. Die source-spezifischen Bedingungen stehen vollständig in `local_not_modelled` der Merge-`RR` (Abschnitt 8.7). `IEC62366-RR-090` bleibt nach der Adjudikation `NEW_UNIQUE_RR`.

---

## 5. ID-Vergabe

Deterministische Reihenfolge ohne Lücken:

| Bereich | Inhalt | Anzahl |
| --- | --- | --- |
| `RR-378` bis `RR-383` | `NORM-MERGE-01` bis `NORM-MERGE-06` | 6 |
| `RR-384` bis `RR-592` | `SRC-005` in der finalen Post-Split-Reihenfolge (Ausgangsnummer aufsteigend, Teilkandidaten `A`, `B`, … an der Stelle ihres Ausgangskandidaten) | 209 |
| `RR-593` bis `RR-691` | `SRC-006` `NEW_UNIQUE_RR` aufsteigend (`001`–`020`, `022`–`062`, `066`–`067`, `070`–`071`, `074`–`107`) | 99 |
| `RR-692` bis `RR-871` | `SRC-007` `NEW_UNIQUE_RR` aufsteigend (`001`, `003`–`147`, `150`–`152`, `155`–`185`) | 180 |
| `RR-872` bis `RR-959` | `SRC-008` `NEW_UNIQUE_RR` aufsteigend (`001`–`081`, `083`–`088`, `090`) | 88 |
| **Gesamt** | | **582** |

Die vollständige Zuordnung jeder Temp-ID steht in Abschnitt 11 und maschinenlesbar in [RR_STANDARDS_MAPPING_SRC_005_008.yaml](RR_STANDARDS_MAPPING_SRC_005_008.yaml).

---

## 6. Katalogintegration

- **Lokatoren:** `SRC-00X#` + adjudizierter Lokator; ausschließlich `Clause` → `Abschnitt` und `Annex` → `Anhang` ersetzt, alle Untergliederungen und Suffixe unverändert (z. B. `SRC-007#Abschnitt 4.3/a`, `SRC-005#Abschnitt 4.1.3(a)`, `SRC-008#Anhang C/C.2.1`).
- **Requirement Text:** adjudizierte DE/EN-Paraphrase unverändert, mit grammatisch integriertem Adressaten nach Katalogkonvention („… muss …“ / „… shall …“). Adressaten: `H` Der Hersteller / The manufacturer; `O` Die Organisation / The organization; `OL` Die oberste Leitung / Top management; `O/OL` Die Organisation bzw. die oberste Leitung / The organization or top management; `H/OL` Der Hersteller bzw. die oberste Leitung / The manufacturer or top management; verantwortliche Leitung / The responsible management; `RM-P` das mit Risikomanagementaufgaben betraute Personal / personnel entrusted with risk-management tasks. Es wurden keine neuen Rollen eingeführt.
- **Grammatische Sonderfälle:** Einleitende Nebensätze („Wenn …“, „Falls …“, „Where …“, „When …“, „For …“, „After …“, „Before …“, „If …“) werden nach dem Modalverb eingebettet („Der Hersteller muss, wenn …, …“; „The manufacturer shall, where …, …“). Bei `ISO13485-RR-035` (Verpflichtung der obersten Leitung), `ISO14971-RR-018` und `ISO14971-RR-019` (Adressat `RM-P`) ist der Adressat Satzsubjekt bzw. Bezugsperson; die Sätze wurden ohne inhaltliche Änderung umgestellt.
- **Titel:** Das Schema verlangt einen Titel. Er ist der adjudizierte Sollgegenstand ohne Adressat (deutsche Infinitiv- bzw. englische Imperativkonstruktion ohne Schlusspunkt); bei den Merge-`RR` die Gruppenüberschrift. Es wurden keine Inhalte ergänzt.
- **Bedingungen:** Bedingungen werden nicht in den Requirement Text gezogen; sie stehen ausschließlich in [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) (Abschnitt 8) und in Abschnitt 11.
- **Feldwerte:** `status` `aktiv`, `uncertainty` `null`, `replaces` / `replaced_by` leer, `sources.supplementary` leer außer bei den Merge-`RR`. Kein neues Schemafeld.
- **Kontextabhängige Paraphrasen:** 15 adjudizierte Paraphrasen begannen mit einem Rückverweis; sie wurden in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.26 redaktionell präzisiert (Abschnitt 6.1).

### 6.1 Selbstständigkeit der Requirement Texte (Katalogversion 0.26)

Kriterium: Jede `RR` muss als einzelner Gap-Sollzustand ohne vorherige `RR` verständlich und bewertbar sein. Geprüft wurde jeder der 15 Fälle gegen seinen Temp-Kandidaten, seinen Lokator und die unmittelbar vorangehende `RR` desselben Lokators. In allen 15 Fällen machte der Rückverweis den Gegenstand ohne Kontext unklar; eingesetzt wurde ausschließlich der Antezedent aus dieser vorangehenden `RR`. Titel wurden entsprechend angepasst, weil sie den Sollgegenstand wiedergeben (Abschnitt 6). Keine neue Pflicht, keine Änderung von Bedingung, Atomisierung, Lokator, Theme oder Lebenszyklusphasen (redaktionelle Änderung nach [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3, gleiche ID).

| `RR` | Temp-ID | Rückverweis vorher | Eingesetzter Antezedent (DE) | Quelle des Antezedenten | EN |
| --- | --- | --- | --- | --- | --- |
| `RR-521` | `ISO13485-RR-114-B` | „solche Software“ | Computersoftware in Produktion/Dienstleistung | `RR-520` | angepasst |
| `RR-535` | `ISO13485-RR-125-B` | „solche Software“ | Computersoftware für Überwachung/Messung | `RR-534` | angepasst |
| `RR-638` | `ISO14971-RR-047` | „diese sicherheitsbezogenen Merkmale“ | die identifizierten qualitativen und quantitativen sicherheitsbezogenen Merkmale | `RR-637` | angepasst |
| `RR-642` | `ISO14971-RR-051` | „diese Gefährdungen“ | die identifizierten bekannten und vorhersehbaren Gefährdungen | `RR-641` | angepasst |
| `RR-644` | `ISO14971-RR-053` | „daraus resultierende“ | aus vernünftigerweise vorhersehbaren Ereignisfolgen/-kombinationen resultierende | `RR-643` | angepasst |
| `RR-645` | `ISO14971-RR-054` | „daraus resultierende“ | wie `RR-644` | `RR-643` | angepasst |
| `RR-675` | `ISO14971-RR-091` | „dieses Informationssystem“ | das System zur aktiven Sammlung und Überprüfung relevanter Produktions-/Post-Production-Informationen | `RR-674` | angepasst |
| `RR-676` | `ISO14971-RR-092` | „dieses Informationssystem“ | wie `RR-675` | `RR-674` | angepasst |
| `RR-711` | `IEC62304-RR-021` | „diesen Lückenschließungsplan“ | den Plan zur Erzeugung identifizierter fehlender Ergebnisse | `RR-710` | bereits explizit, unverändert |
| `RR-759` | `IEC62304-RR-069` | „diese Schnittstellenarchitektur“ | die Architektur für interne und externe Softwareschnittstellen | `RR-758` | angepasst |
| `RR-827` | `IEC62304-RR-137` | „solche Änderungsanforderungen“ | Änderungsanforderungen an freigegebener Software | `RR-826` | bereits explizit, unverändert |
| `RR-832` | `IEC62304-RR-142` | „diese erforderlichen Entwicklungsaktivitäten“ | die wegen einer Änderung zu wiederholenden Clause-5-Aktivitäten | `RR-831` | angepasst |
| `RR-894` | `IEC62366-RR-023` | „dabei“ | bei der Ermittlung benutzungsbezogener Gefährdungen und Gefährdungssituationen | `RR-893` | angepasst |
| `RR-941` | `IEC62366-RR-070` | „diese Trainingsmöglichkeit“ | die Trainingsmöglichkeit für den sicheren Gebrauch | `RR-940` | angepasst |
| `RR-949` | `IEC62366-RR-078` | „andernfalls“ | wenn keine neuen Use Errors, Gefährdungen, Gefährdungssituationen oder Szenarien erkannt wurden | `RR-948`; entspricht der unverändert adjudizierten Bedingung „keine neuen Befunde im vorgenannten Zweig“ | angepasst |

Regressionstest: `tools/test_validate_standards_mapping.py` (`test_new_rr_texts_are_self_contained`) prüft, dass kein Titel und kein Requirement Text der neuen `RR` unmittelbar nach dem Adressaten mit einem solchen Rückverweis beginnt.

---

## 7. Themen, Lebenszyklus und Quellenbeteiligung

| Theme | Neue `RR` |
| --- | --- |
| Qualitäts- und Risikomanagement | **265** |
| Software-Lebenszyklus | **197** |
| Gebrauchstauglichkeit | **79** |
| Post-Market-Monitoring | **39** |
| Transparenz | **2** |
| Data Governance, Menschliche Aufsicht, Robustheit | **0** |
| **Gesamt** | **582** |

Je Quelle (ohne Merge-`RR`): `SRC-005` 137 / 57 / 15 (QRM / SLZ / PMM); `SRC-006` 84 QRM, 13 PMM, 2 Transparenz; `SRC-007` 140 SLZ, 30 QRM, 9 PMM, 1 Gebrauchstauglichkeit; `SRC-008` 78 Gebrauchstauglichkeit, 8 QRM, 2 PMM; Merge-`RR` 6 QRM.

Lebenszyklus-Kürzel wurden auf das kontrollierte Vokabular abgebildet (`P` Planung und Konzeption, `D` Entwicklung und Realisierung, `V` Verifikation und Validierung, `C` Konformitätsbewertung, `B` Inverkehrbringen, Inbetriebnahme und Betrieb, `PM` Post-Market-Überwachung, `M` Änderung und Wartung; `ALL` alle sieben Phasen) und in Vokabularreihenfolge gespeichert.

Quellenbeteiligung (Mehrfachzählung bei Merge-`RR`): `SRC-005` **209**, `SRC-006` **105** (99 + 6 Merge-Primary), `SRC-007` **184** (180 + 4 Merge-Supplementary), `SRC-008` **92** (88 + 4 Merge-Supplementary).

---

## 8. Applicability

Die Anwendbarkeit wird in [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.3 nach der bestehenden Modellierungsregel aus [RR_APPLICABILITY_MAPPING.md](RR_APPLICABILITY_MAPPING.md) Abschnitt 2 abgebildet. Keine Bedingung wurde verworfen; Anforderungstexte werden nicht ausgewertet. Was nicht deterministisch entscheidbar ist, bleibt fail-closed `APPLICABILITY_UNRESOLVED`. Requirement-unresolved bleibt davon getrennt 0.

### 8.1 Übergeordneter Bereich

Je Norm ein Block (`NORM_SRC_005_QMS`, `NORM_SRC_006_RISK_MANAGEMENT` einschließlich der Merge-`RR`, `NORM_SRC_007_SOFTWARE_LIFECYCLE`, `NORM_SRC_008_USABILITY`). Scope ist das **bestehende kanonische** Prädikat `MDR_MDSW`; es wurde **kein** neues Normen- oder MDSW-Gate eingeführt. Begründung der Wiederverwendung: Der Demonstrator betrachtet die Normen ausschließlich als Gap-Quellen für MDR-Medizinproduktesoftware. `MDR_MDSW` schaltet nach [DECISION_LOGIC_SRC_004_MDSW_QUALIFICATION_CLASSIFICATION.md](DECISION_LOGIC_SRC_004_MDSW_QUALIFICATION_CLASSIFICATION.md) Abschnitt 11 genau diesen RegScoutX-Gap-Korpus frei; `NOT_MDSW` bzw. `OUT_OF_SCOPE_IVDR` bedeuten dort „keine Gap-Auswertung im derzeitigen RegScoutX-Scope“, Sonderroute und Prüfbedarf lassen den Bereich ungeklärt. `NOT_APPLICABLE` mit `SCOPE_INACTIVE` ist deshalb eine Aussage über den Scope des Demonstrators, **keine** Aussage über die normative Anwendbarkeit einer Norm außerhalb dieses Scopes (etwa für IVD-Software).

### 8.2 ISO-13485-Ausschlussregel (Abschnitte 6 bis 8)

Nach der Adjudikation unterliegen die Anforderungen der Abschnitte 6 bis 8 von `SRC-005` der Applicability-Regel aus Abschnitt 1: Ist eine Anforderung aufgrund der Tätigkeiten der Organisation oder der Art des Produkts nicht anwendbar, kann sie mit Begründung ausgeschlossen werden. Diese globale Bedingung ist in den Zeilen nicht wiederholt. Modellierung: Eingabe `iso13485_clause1_exclusion_claimed`, Prädikat `ISO13485_NO_CLAUSE1_EXCLUSION` bei allen 159 `SRC-005`-`RR` der Abschnitte 6 bis 8. Keine Ausschlüsse → erfüllt; Ausschlüsse in Anspruch genommen → `UNKNOWN` (`unknown_values`), weil offen bleibt, welche Anforderung betroffen ist. Damit führt ein beanspruchter Ausschluss nie ungeprüft zu `NOT_APPLICABLE`.

### 8.3 Weitere Bedingungen `SRC-005`

Als faktische Eingabe modelliert werden nur die adjudizierten Bedingungen, die die Organisation ohne rechtliche Wertung mit Ja/Nein angeben kann: QMS-Software eingesetzt (`qms_software_used`, 4 `RR`), Outsourcing (`outsourced_processes`), Beschaffung (`purchasing_performed`), „entsprechende Software eingesetzt“ getrennt nach Lokator in Produktion/Dienstleistungserbringung (Abschnitt 7.5.6, `production_service_software_used`) und Überwachung/Messung (Abschnitt 7.6, `monitoring_measurement_software_used`) sowie Kundeneigentum (`customer_property_provided`). Enthält eine Bedingung zusätzlich einen Wertungs- oder Relevanzanteil („Prozess ausgelagert und konformitätsrelevant“, „Beschaffung relevant“), wird der faktische Teil modelliert und die vollständige Bedingung zusätzlich in `local_not_modelled` geführt. Ereignisbedingungen (z. B. Entwicklungs-, Prozess-, Dokument- oder QMS-Änderung, Nichtkonformität, Nacharbeit, Reklamation), Angemessenheits- und Relevanzvorbehalte sowie regulatorische Pflichtauslöser bleiben nach der bestehenden Modellierungsregel nicht modelliert.

### 8.4 Bedingungen `SRC-006`

Die 32 bedingten `SRC-006`-`RR` (z. B. „soweit zutreffend“, „Risiko nicht akzeptabel“, „Maßnahme implementiert“, „Information sicherheitsrelevant“, „je Medizinprodukt“) sind Ereignis-, Ergebnis-, Relevanz- oder Bezugsbedingungen des Risikomanagementprozesses und bleiben vollständig in `local_not_modelled`. 67 `SRC-006`-`RR` sind regulär.

### 8.5 IEC 62304: Sicherheitsklasse, Route und lokale Auslöser

- `software_safety_class` (A, B, C, noch nicht klassifiziert): Prädikate `IEC62304_CLASS_ABC`, `IEC62304_CLASS_BC`, `IEC62304_CLASS_C`. „Noch nicht klassifiziert“ wird nach der adjudizierten Routing-Regel `SRC-007#Abschnitt 4.3/g` (bis zur Klassifizierung gelten die Klasse-C-Anforderungen) wie Klasse C behandelt. In [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.3 ergab dieser Wert noch `UNKNOWN`; die Korrektur erfolgte im Abschluss-Audit (Abschnitt 12).
- `iec62304_route` (reguläre Lebenszyklusprozesse bzw. Legacy-Route nach Abschnitt 4.4): Die 18 Legacy-Kandidaten gelten nur auf der Legacy-Route (`IEC62304_LEGACY_ROUTE`). Die klassengebundenen `RR` gelten auf der regulären Route; auf der Legacy-Route ergeben sie `UNKNOWN`, weil nach der Adjudikation erst die Lückenanalyse nach 4.4.3/4.4.4 bestimmt, welche regulären Ergebnisse nachzuholen sind.
- `ALL` (`RR-692`) und die fünf vorgelagerten Klassifizierungsregeln `PRE` sind regulär.
- Lokale Auslöser: SOUP (`soup_used`), Änderung (`software_change`), Problembericht bzw. identifiziertes Problem (`software_problem_reported`). „SOUP-Trigger“ (SOUP als mögliche Ursache), „soweit angemessen“, „lokale Vorschrift“, „softwareimplementierte RM“, „Testverifizierung“, „Bedarf festgestellt“, „Lücken vorhanden“ und „conditional“ bleiben (zusätzlich) in `local_not_modelled`.

### 8.6 IEC 62366-1: Route und lokale Auslöser

- `iec62366_ui_route`: reguläre Route, UOUP ohne geänderte Teile, UOUP mit geänderten Teilen. Die Route folgt aus dem Lokator laut Adjudikation: Abschnitt 4 gemeinsame Basis (ohne Routenbedingung), Abschnitt 5 reguläre Route (`IEC62366_REGULAR_ROUTE`), Anhang C UOUP (`IEC62366_UOUP_ROUTE`). Die Use-Specification-Atome `IEC62366-RR-011` bis `017` gelten nach C.2.1 auf beiden Routen und sind daher ohne Routenbedingung. Werden Teile einer UOUP geändert, fallen nur diese Teile in die reguläre Route; deshalb aktiviert „UOUP mit geänderten Teilen“ beide Routen.
- Lokale Auslöser: Usability-Test vorgesehen bzw. durchgeführt (`usability_test_planned`), Training für sicheren Gebrauch erforderlich (`training_required_for_safe_use`), Sicherheitsinformation als Risikobeherrschungsmaßnahme (`safety_information_as_risk_control`). Verweise „wie NNN“ sind auf die Bedingung des referenzierten Kandidaten aufgelöst. Befund-, Zweig- und Relevanzbedingungen bleiben in `local_not_modelled`.

### 8.7 Merge-`RR`

Alle sechs Merge-`RR` sind bedingt; die source-spezifischen Bedingungen (ISO-14971-Pfad, IEC-62304-Klasse B/C, IEC-62366-1-Route und Reassessment-Trigger) stehen vollständig in `local_not_modelled`, sodass die Deduplizierung keine Bedingung abschwächt.

### 8.8 Ergebnis

| Bereich | `RR` | regulär | bedingt, vollständig modelliert | bedingt mit nicht (vollständig) modellierter Bedingung |
| --- | --- | --- | --- | --- |
| Merge-`RR` | 6 | 0 | 0 | 6 |
| `SRC-005` | 209 | 33 | 89 | 87 |
| `SRC-006` | 99 | 67 | 0 | 32 |
| `SRC-007` | 180 | 6 | 147 | 27 |
| `SRC-008` | 88 | 14 | 60 | 14 |
| **Gesamt** | **582** | **120** | **296** | **166** |

Neue Applicability-Eingaben: 16; neue Prädikate: 20; neue Blöcke: 4. Die Auswertung ist in `tests/test_standards_applicability.py` geprüft.

---

## 9. Traceability und Abhängigkeiten

- Jede neue `RR` ist über `sources.primary` auf genau einen Normlokator rückführbar; die Merge-`RR` tragen zusätzlich alle beteiligten Normlokatoren.
- Die Zuordnungsdatei führt `SOURCE_SUPPORT` (`RR-157`, `RR-145`, `RR-146` ← `SRC-006`) und `NORMATIVE_DEPENDENCY` (`SRC-007#Abschnitt 4.2` → `RR-594`; `SRC-007` → `SRC-006`; `SRC-008` → `SRC-006`). Die Abhängigkeiten ändern keine Primary Source.
- `tools/validate_standards_mapping.py` prüft Vollständigkeit und Eindeutigkeit der Zuordnung, Kandidatenzahl je Quelle, Merge-Gruppen, Lokatoren und Beziehungen; `tools/traceability.py` führt die Beziehungen als Verknüpfungen und prüft ihre Verweisintegrität ([TRACEABILITY_MODEL.md](../05-traceability/TRACEABILITY_MODEL.md)).

---

## 10. Unsicherheiten und offene Punkte

1. `SRC-005` `OPEN_SOURCE_PACKAGE_CHECK` (Abschnitt 2.1): blockiert den finalen Evidence-Freeze, nicht den `RR`-Freeze.
2. `SRC-007` und `SRC-008`: Arbeitsgrundlage ist die deutsche EN-Übernahme, nicht die in [SOURCES.md](SOURCES.md) als Normnummer geführte IEC-CSV. Nach der Adjudikation ist der Anforderungskörper identisch übernommen; ein Abgleich mit der originalen IEC-CSV wurde nicht durchgeführt.
3. Englische Requirement Texte sind kontrollierte Übersetzungen der deutschen Arbeitsfassungen.
4. Die 15 kontextabhängigen Paraphrasen sind seit Katalogversion 0.26 selbstständig formuliert (Abschnitt 6.1); kein offener Punkt.
5. 166 neue `RR` bleiben bei aktivem Block wegen nicht (vollständig) modellierter Bedingung fail-closed `APPLICABILITY_UNRESOLVED`; das ist beabsichtigt und keine Requirement-Unsicherheit.

---

## 11. Vollständige Zuordnung Temp-ID → `RR`

Bedingung und Adressat wie adjudiziert (Legende Abschnitt 6 und 8). `—` bzw. `–` = keine lokale Bedingung.

### 11.1 SRC-005 — ISO 13485:2016 (209 Kandidaten)

| Temp-ID | Lokator | Adressat | Bedingung laut Adjudikation | Entscheidung | RR |
| --- | --- | --- | --- | --- | --- |
| `ISO13485-RR-001` | `SRC-005#Abschnitt 4.1.1` | O | – | `NEW_UNIQUE_RR` | `RR-384` |
| `ISO13485-RR-002` | `SRC-005#Abschnitt 4.1.1` | O | – | `NEW_UNIQUE_RR` | `RR-385` |
| `ISO13485-RR-003` | `SRC-005#Abschnitt 4.1.1` | O | Dokumentationspflicht besteht | `NEW_UNIQUE_RR` | `RR-386` |
| `ISO13485-RR-004` | `SRC-005#Abschnitt 4.1.1` | O | – | `NEW_UNIQUE_RR` | `RR-387` |
| `ISO13485-RR-005` | `SRC-005#Abschnitt 4.1.2(a)` | O | – | `NEW_UNIQUE_RR` | `RR-388` |
| `ISO13485-RR-006` | `SRC-005#Abschnitt 4.1.2(b)` | O | – | `NEW_UNIQUE_RR` | `RR-389` |
| `ISO13485-RR-007` | `SRC-005#Abschnitt 4.1.2(c)` | O | – | `NEW_UNIQUE_RR` | `RR-390` |
| `ISO13485-RR-008` | `SRC-005#Abschnitt 4.1.3(a)` | O | – | `NEW_UNIQUE_RR` | `RR-391` |
| `ISO13485-RR-009` | `SRC-005#Abschnitt 4.1.3(b)` | O | – | `NEW_UNIQUE_RR` | `RR-392` |
| `ISO13485-RR-010` | `SRC-005#Abschnitt 4.1.3(c)` | O | – | `NEW_UNIQUE_RR` | `RR-393` |
| `ISO13485-RR-011` | `SRC-005#Abschnitt 4.1.3(d)` | O | Messung/Analyse soweit angemessen | `NEW_UNIQUE_RR` | `RR-394` |
| `ISO13485-RR-012` | `SRC-005#Abschnitt 4.1.3(e)` | O | – | `NEW_UNIQUE_RR` | `RR-395` |
| `ISO13485-RR-013` | `SRC-005#Abschnitt 4.1.4` | O | – | `NEW_UNIQUE_RR` | `RR-396` |
| `ISO13485-RR-014` | `SRC-005#Abschnitt 4.1.4(a)–(b)` | O | Prozessänderung | `NEW_UNIQUE_RR` | `RR-397` |
| `ISO13485-RR-015` | `SRC-005#Abschnitt 4.1.4(c)` | O | Prozessänderung | `NEW_UNIQUE_RR` | `RR-398` |
| `ISO13485-RR-016` | `SRC-005#Abschnitt 4.1.5` | O | Prozess ausgelagert und konformitätsrelevant | `NEW_UNIQUE_RR` | `RR-399` |
| `ISO13485-RR-017` | `SRC-005#Abschnitt 4.1.5` | O | Outsourcing | `NEW_UNIQUE_RR` | `RR-400` |
| `ISO13485-RR-018` | `SRC-005#Abschnitt 4.1.5` | O | Outsourcing | `NEW_UNIQUE_RR` | `RR-401` |
| `ISO13485-RR-019` | `SRC-005#Abschnitt 4.1.5` | O | Outsourcing | `NEW_UNIQUE_RR` | `RR-402` |
| `ISO13485-RR-020` | `SRC-005#Abschnitt 4.1.6` | O | QMS-Software eingesetzt | `NEW_UNIQUE_RR` | `RR-403` |
| `ISO13485-RR-021` | `SRC-005#Abschnitt 4.1.6` | O | QMS-Software eingesetzt | `NEW_UNIQUE_RR` | `RR-404` |
| `ISO13485-RR-022` | `SRC-005#Abschnitt 4.1.6` | O | relevante Änderung + angemessen | `NEW_UNIQUE_RR` | `RR-405` |
| `ISO13485-RR-023` | `SRC-005#Abschnitt 4.1.6` | O | QMS-Software eingesetzt | `NEW_UNIQUE_RR` | `RR-406` |
| `ISO13485-RR-024` | `SRC-005#Abschnitt 4.1.6` | O | QMS-Software eingesetzt | `NEW_UNIQUE_RR` | `RR-407` |
| `ISO13485-RR-025` | `SRC-005#Abschnitt 4.2.1` | O | – | `NEW_UNIQUE_RR` | `RR-408` |
| `ISO13485-RR-026` | `SRC-005#Abschnitt 4.2.2` | O | – | `NEW_UNIQUE_RR` | `RR-409` |
| `ISO13485-RR-027` | `SRC-005#Abschnitt 4.2.3` | O | je Produkttyp/-gruppe | `NEW_UNIQUE_RR` | `RR-410` |
| `ISO13485-RR-028` | `SRC-005#Abschnitt 4.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-411` |
| `ISO13485-RR-029` | `SRC-005#Abschnitt 4.2.4` | O | Dokumentänderung | `NEW_UNIQUE_RR` | `RR-412` |
| `ISO13485-RR-030` | `SRC-005#Abschnitt 4.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-413` |
| `ISO13485-RR-031` | `SRC-005#Abschnitt 4.2.5` | O | – | `NEW_UNIQUE_RR` | `RR-414` |
| `ISO13485-RR-032` | `SRC-005#Abschnitt 4.2.5` | O | – | `NEW_UNIQUE_RR` | `RR-415` |
| `ISO13485-RR-033` | `SRC-005#Abschnitt 4.2.5` | O | – | `NEW_UNIQUE_RR` | `RR-416` |
| `ISO13485-RR-034` | `SRC-005#Abschnitt 4.2.5` | O | längere regulatorische Frist geht vor | `NEW_UNIQUE_RR` | `RR-417` |
| `ISO13485-RR-035` | `SRC-005#Abschnitt 5.1` | OL | – | `NEW_UNIQUE_RR` | `RR-418` |
| `ISO13485-RR-036` | `SRC-005#Abschnitt 5.2` | OL | – | `NEW_UNIQUE_RR` | `RR-419` |
| `ISO13485-RR-037` | `SRC-005#Abschnitt 5.3` | OL | – | `NEW_UNIQUE_RR` | `RR-420` |
| `ISO13485-RR-038` | `SRC-005#Abschnitt 5.4.1` | OL | – | `NEW_UNIQUE_RR` | `RR-421` |
| `ISO13485-RR-039` | `SRC-005#Abschnitt 5.4.2(a)` | OL | – | `NEW_UNIQUE_RR` | `RR-422` |
| `ISO13485-RR-040` | `SRC-005#Abschnitt 5.4.2(b)` | OL | QMS-Änderung | `NEW_UNIQUE_RR` | `RR-423` |
| `ISO13485-RR-041` | `SRC-005#Abschnitt 5.5.1` | OL | – | `NEW_UNIQUE_RR` | `RR-424` |
| `ISO13485-RR-042` | `SRC-005#Abschnitt 5.5.1` | OL | – | `NEW_UNIQUE_RR` | `RR-425` |
| `ISO13485-RR-043` | `SRC-005#Abschnitt 5.5.2` | OL | – | `NEW_UNIQUE_RR` | `RR-426` |
| `ISO13485-RR-044-A` | `SRC-005#Abschnitt 5.5.3` | OL | – | `NEW_UNIQUE_RR` | `RR-427` |
| `ISO13485-RR-044-B` | `SRC-005#Abschnitt 5.5.3` | OL | – | `NEW_UNIQUE_RR` | `RR-428` |
| `ISO13485-RR-045` | `SRC-005#Abschnitt 5.6.1` | O | – | `NEW_UNIQUE_RR` | `RR-429` |
| `ISO13485-RR-046-A` | `SRC-005#Abschnitt 5.6.1` | OL | – | `NEW_UNIQUE_RR` | `RR-430` |
| `ISO13485-RR-046-B` | `SRC-005#Abschnitt 5.6.1` | OL | – | `NEW_UNIQUE_RR` | `RR-431` |
| `ISO13485-RR-047` | `SRC-005#Abschnitt 5.6.2` | O/OL | – | `NEW_UNIQUE_RR` | `RR-432` |
| `ISO13485-RR-048` | `SRC-005#Abschnitt 5.6.3` | O/OL | – | `NEW_UNIQUE_RR` | `RR-433` |
| `ISO13485-RR-049` | `SRC-005#Abschnitt 6.1` | O | – | `NEW_UNIQUE_RR` | `RR-434` |
| `ISO13485-RR-050` | `SRC-005#Abschnitt 6.2` | O | – | `NEW_UNIQUE_RR` | `RR-435` |
| `ISO13485-RR-051` | `SRC-005#Abschnitt 6.2` | O | – | `NEW_UNIQUE_RR` | `RR-436` |
| `ISO13485-RR-052` | `SRC-005#Abschnitt 6.2(a)–(e)` | O | – | `NEW_UNIQUE_RR` | `RR-437` |
| `ISO13485-RR-053` | `SRC-005#Abschnitt 6.3` | O | soweit angemessen | `NEW_UNIQUE_RR` | `RR-438` |
| `ISO13485-RR-054-A` | `SRC-005#Abschnitt 6.3` | O | Wartung bzw. Unterlassung kann Produktqualität beeinflussen | `NEW_UNIQUE_RR` | `RR-439` |
| `ISO13485-RR-054-B` | `SRC-005#Abschnitt 6.3` | O | Wartung bzw. Unterlassung kann Produktqualität beeinflussen | `NEW_UNIQUE_RR` | `RR-440` |
| `ISO13485-RR-055-A` | `SRC-005#Abschnitt 6.4.1` | O | soweit Arbeitsumgebung produktqualitätsrelevant | `NEW_UNIQUE_RR` | `RR-441` |
| `ISO13485-RR-055-B` | `SRC-005#Abschnitt 6.4.1` | O | soweit Arbeitsumgebung produktqualitätsrelevant | `NEW_UNIQUE_RR` | `RR-442` |
| `ISO13485-RR-056` | `SRC-005#Abschnitt 7.1` | O | – | `NEW_UNIQUE_RR` | `RR-443` |
| `ISO13485-RR-057-A` | `SRC-005#Abschnitt 7.1` | O | – | `NEW_UNIQUE_RR` | `RR-444` |
| `ISO13485-RR-057-B` | `SRC-005#Abschnitt 7.1` | O | – | `NEW_UNIQUE_RR` | `RR-445` |
| `ISO13485-RR-058` | `SRC-005#Abschnitt 7.1(a)–(d)` | O | soweit angemessen | `NEW_UNIQUE_RR` | `RR-446` |
| `ISO13485-RR-059` | `SRC-005#Abschnitt 7.2.1` | O | einzelne Kategorien soweit einschlägig | `NEW_UNIQUE_RR` | `RR-447` |
| `ISO13485-RR-060-A` | `SRC-005#Abschnitt 7.2.2` | O | – | `NEW_UNIQUE_RR` | `RR-448` |
| `ISO13485-RR-060-B` | `SRC-005#Abschnitt 7.2.2` | O | – | `NEW_UNIQUE_RR` | `RR-449` |
| `ISO13485-RR-061` | `SRC-005#Abschnitt 7.2.2` | O | keine schriftlichen Kundenanforderungen | `NEW_UNIQUE_RR` | `RR-450` |
| `ISO13485-RR-062-A` | `SRC-005#Abschnitt 7.2.2` | O | Anforderungsänderung | `NEW_UNIQUE_RR` | `RR-451` |
| `ISO13485-RR-062-B` | `SRC-005#Abschnitt 7.2.2` | O | Anforderungsänderung | `NEW_UNIQUE_RR` | `RR-452` |
| `ISO13485-RR-063` | `SRC-005#Abschnitt 7.2.3` | O | – | `NEW_UNIQUE_RR` | `RR-453` |
| `ISO13485-RR-064` | `SRC-005#Abschnitt 7.2.3` | O | regulatorischer Kommunikationsanlass | `NEW_UNIQUE_RR` | `RR-454` |
| `ISO13485-RR-065` | `SRC-005#Abschnitt 7.3.1` | O | – | `NEW_UNIQUE_RR` | `RR-455` |
| `ISO13485-RR-066` | `SRC-005#Abschnitt 7.3.2` | O | – | `NEW_UNIQUE_RR` | `RR-456` |
| `ISO13485-RR-067` | `SRC-005#Abschnitt 7.3.2(a)–(f)` | O | Aktualisierung soweit angemessen | `NEW_UNIQUE_RR` | `RR-457` |
| `ISO13485-RR-068-A` | `SRC-005#Abschnitt 7.3.3` | O | – | `NEW_UNIQUE_RR` | `RR-458` |
| `ISO13485-RR-068-B` | `SRC-005#Abschnitt 7.3.3` | O | – | `NEW_UNIQUE_RR` | `RR-459` |
| `ISO13485-RR-069` | `SRC-005#Abschnitt 7.3.3(a)–(e)` | O | frühere Designs soweit angemessen | `NEW_UNIQUE_RR` | `RR-460` |
| `ISO13485-RR-070-A` | `SRC-005#Abschnitt 7.3.3` | O | – | `NEW_UNIQUE_RR` | `RR-461` |
| `ISO13485-RR-070-B` | `SRC-005#Abschnitt 7.3.3` | O | – | `NEW_UNIQUE_RR` | `RR-462` |
| `ISO13485-RR-071` | `SRC-005#Abschnitt 7.3.3` | O | – | `NEW_UNIQUE_RR` | `RR-463` |
| `ISO13485-RR-072` | `SRC-005#Abschnitt 7.3.4(a)–(d)` | O | – | `NEW_UNIQUE_RR` | `RR-464` |
| `ISO13485-RR-073-A` | `SRC-005#Abschnitt 7.3.4` | O | – | `NEW_UNIQUE_RR` | `RR-465` |
| `ISO13485-RR-073-B` | `SRC-005#Abschnitt 7.3.4` | O | – | `NEW_UNIQUE_RR` | `RR-466` |
| `ISO13485-RR-073-C` | `SRC-005#Abschnitt 7.3.4` | O | – | `NEW_UNIQUE_RR` | `RR-467` |
| `ISO13485-RR-074` | `SRC-005#Abschnitt 7.3.5` | O | geeignete Entwicklungsphasen | `NEW_UNIQUE_RR` | `RR-468` |
| `ISO13485-RR-075-A` | `SRC-005#Abschnitt 7.3.5` | O | – | `NEW_UNIQUE_RR` | `RR-469` |
| `ISO13485-RR-075-B` | `SRC-005#Abschnitt 7.3.5` | O | – | `NEW_UNIQUE_RR` | `RR-470` |
| `ISO13485-RR-076` | `SRC-005#Abschnitt 7.3.6` | O | – | `NEW_UNIQUE_RR` | `RR-471` |
| `ISO13485-RR-077` | `SRC-005#Abschnitt 7.3.6` | O | Statistik soweit angemessen | `NEW_UNIQUE_RR` | `RR-472` |
| `ISO13485-RR-078` | `SRC-005#Abschnitt 7.3.6` | O | Schnittstelle laut Zweckbestimmung erforderlich | `NEW_UNIQUE_RR` | `RR-473` |
| `ISO13485-RR-079` | `SRC-005#Abschnitt 7.3.6` | O | – | `NEW_UNIQUE_RR` | `RR-474` |
| `ISO13485-RR-080` | `SRC-005#Abschnitt 7.3.7` | O | – | `NEW_UNIQUE_RR` | `RR-475` |
| `ISO13485-RR-081` | `SRC-005#Abschnitt 7.3.7` | O | Statistik soweit angemessen | `NEW_UNIQUE_RR` | `RR-476` |
| `ISO13485-RR-082-A` | `SRC-005#Abschnitt 7.3.7` | O | – | `NEW_UNIQUE_RR` | `RR-477` |
| `ISO13485-RR-082-B` | `SRC-005#Abschnitt 7.3.7` | O | – | `NEW_UNIQUE_RR` | `RR-478` |
| `ISO13485-RR-083` | `SRC-005#Abschnitt 7.3.7` | O | soweit regulatorisch einschlägig | `NEW_UNIQUE_RR` | `RR-479` |
| `ISO13485-RR-084` | `SRC-005#Abschnitt 7.3.7` | O | Schnittstelle laut Zweckbestimmung | `NEW_UNIQUE_RR` | `RR-480` |
| `ISO13485-RR-085-A` | `SRC-005#Abschnitt 7.3.7` | O | – | `NEW_UNIQUE_RR` | `RR-481` |
| `ISO13485-RR-085-B` | `SRC-005#Abschnitt 7.3.7` | O | – | `NEW_UNIQUE_RR` | `RR-482` |
| `ISO13485-RR-086-A` | `SRC-005#Abschnitt 7.3.8` | O | – | `NEW_UNIQUE_RR` | `RR-483` |
| `ISO13485-RR-086-B` | `SRC-005#Abschnitt 7.3.8` | O | – | `NEW_UNIQUE_RR` | `RR-484` |
| `ISO13485-RR-086-C` | `SRC-005#Abschnitt 7.3.8` | O | – | `NEW_UNIQUE_RR` | `RR-485` |
| `ISO13485-RR-087` | `SRC-005#Abschnitt 7.3.8` | O | – | `NEW_UNIQUE_RR` | `RR-486` |
| `ISO13485-RR-088` | `SRC-005#Abschnitt 7.3.9` | O | – | `NEW_UNIQUE_RR` | `RR-487` |
| `ISO13485-RR-089` | `SRC-005#Abschnitt 7.3.9` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-488` |
| `ISO13485-RR-090-A` | `SRC-005#Abschnitt 7.3.9` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-489` |
| `ISO13485-RR-090-B` | `SRC-005#Abschnitt 7.3.9(a)` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-490` |
| `ISO13485-RR-090-C` | `SRC-005#Abschnitt 7.3.9(b)` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-491` |
| `ISO13485-RR-090-D` | `SRC-005#Abschnitt 7.3.9(c)` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-492` |
| `ISO13485-RR-090-E` | `SRC-005#Abschnitt 7.3.9(d)` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-493` |
| `ISO13485-RR-091` | `SRC-005#Abschnitt 7.3.9` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-494` |
| `ISO13485-RR-092` | `SRC-005#Abschnitt 7.3.9` | O | Entwicklungsänderung | `NEW_UNIQUE_RR` | `RR-495` |
| `ISO13485-RR-093` | `SRC-005#Abschnitt 7.3.10` | O | je Typ/Gruppe | `NEW_UNIQUE_RR` | `RR-496` |
| `ISO13485-RR-094` | `SRC-005#Abschnitt 7.4.1` | O | Beschaffung relevant | `NEW_UNIQUE_RR` | `RR-497` |
| `ISO13485-RR-095` | `SRC-005#Abschnitt 7.4.1` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-498` |
| `ISO13485-RR-096-A` | `SRC-005#Abschnitt 7.4.1` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-499` |
| `ISO13485-RR-096-B` | `SRC-005#Abschnitt 7.4.1` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-500` |
| `ISO13485-RR-096-C` | `SRC-005#Abschnitt 7.4.1` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-501` |
| `ISO13485-RR-097` | `SRC-005#Abschnitt 7.4.1` | O | Lieferantennichtkonformität | `NEW_UNIQUE_RR` | `RR-502` |
| `ISO13485-RR-098` | `SRC-005#Abschnitt 7.4.1` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-503` |
| `ISO13485-RR-099` | `SRC-005#Abschnitt 7.4.2` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-504` |
| `ISO13485-RR-100` | `SRC-005#Abschnitt 7.4.2` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-505` |
| `ISO13485-RR-101` | `SRC-005#Abschnitt 7.4.2` | O | Änderung kann Eignung beeinflussen | `NEW_UNIQUE_RR` | `RR-506` |
| `ISO13485-RR-102` | `SRC-005#Abschnitt 7.4.2` | O | soweit Traceability erforderlich | `NEW_UNIQUE_RR` | `RR-507` |
| `ISO13485-RR-103` | `SRC-005#Abschnitt 7.4.3` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-508` |
| `ISO13485-RR-104` | `SRC-005#Abschnitt 7.4.3` | O | Lieferantenänderung | `NEW_UNIQUE_RR` | `RR-509` |
| `ISO13485-RR-105` | `SRC-005#Abschnitt 7.4.3` | O | Verifizierung beim Lieferanten vorgesehen | `NEW_UNIQUE_RR` | `RR-510` |
| `ISO13485-RR-106` | `SRC-005#Abschnitt 7.4.3` | O | Beschaffung | `NEW_UNIQUE_RR` | `RR-511` |
| `ISO13485-RR-107` | `SRC-005#Abschnitt 7.5.1` | O | soweit auf MDSW-Prozesse anwendbar | `NEW_UNIQUE_RR` | `RR-512` |
| `ISO13485-RR-108-A` | `SRC-005#Abschnitt 7.5.3` | O | Installation für MDSW einschlägig | `NEW_UNIQUE_RR` | `RR-513` |
| `ISO13485-RR-108-B` | `SRC-005#Abschnitt 7.5.3` | O | Installation für MDSW einschlägig | `NEW_UNIQUE_RR` | `RR-514` |
| `ISO13485-RR-109` | `SRC-005#Abschnitt 7.5.4` | O | Instandhaltung vorgeschrieben | `NEW_UNIQUE_RR` | `RR-515` |
| `ISO13485-RR-110` | `SRC-005#Abschnitt 7.5.4` | O | Serviceaufzeichnungen vorhanden | `NEW_UNIQUE_RR` | `RR-516` |
| `ISO13485-RR-111` | `SRC-005#Abschnitt 7.5.4` | O | Instandhaltung | `NEW_UNIQUE_RR` | `RR-517` |
| `ISO13485-RR-112` | `SRC-005#Abschnitt 7.5.6` | O | Tatbestand 7.5.6 erfüllt | `NEW_UNIQUE_RR` | `RR-518` |
| `ISO13485-RR-113` | `SRC-005#Abschnitt 7.5.6` | O | validierungspflichtiger Prozess | `NEW_UNIQUE_RR` | `RR-519` |
| `ISO13485-RR-114-A` | `SRC-005#Abschnitt 7.5.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-520` |
| `ISO13485-RR-114-B` | `SRC-005#Abschnitt 7.5.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-521` |
| `ISO13485-RR-115` | `SRC-005#Abschnitt 7.5.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-522` |
| `ISO13485-RR-116` | `SRC-005#Abschnitt 7.5.6` | O | Validierung durchgeführt | `NEW_UNIQUE_RR` | `RR-523` |
| `ISO13485-RR-117-A` | `SRC-005#Abschnitt 7.5.8` | O | – | `NEW_UNIQUE_RR` | `RR-524` |
| `ISO13485-RR-117-B` | `SRC-005#Abschnitt 7.5.8` | O | – | `NEW_UNIQUE_RR` | `RR-525` |
| `ISO13485-RR-118` | `SRC-005#Abschnitt 7.5.8` | O | – | `NEW_UNIQUE_RR` | `RR-526` |
| `ISO13485-RR-119` | `SRC-005#Abschnitt 7.5.8` | O | regulatorische UDI-Pflicht | `NEW_UNIQUE_RR` | `RR-527` |
| `ISO13485-RR-120` | `SRC-005#Abschnitt 7.5.9.1` | O | – | `NEW_UNIQUE_RR` | `RR-528` |
| `ISO13485-RR-121-A` | `SRC-005#Abschnitt 7.5.10` | O | Kundeneigentum bereitgestellt | `NEW_UNIQUE_RR` | `RR-529` |
| `ISO13485-RR-121-B` | `SRC-005#Abschnitt 7.5.10` | O | Kundeneigentum bereitgestellt | `NEW_UNIQUE_RR` | `RR-530` |
| `ISO13485-RR-122` | `SRC-005#Abschnitt 7.5.11` | O | soweit für MDSW relevant | `NEW_UNIQUE_RR` | `RR-531` |
| `ISO13485-RR-123` | `SRC-005#Abschnitt 7.6` | O | – | `NEW_UNIQUE_RR` | `RR-532` |
| `ISO13485-RR-124` | `SRC-005#Abschnitt 7.6` | O | – | `NEW_UNIQUE_RR` | `RR-533` |
| `ISO13485-RR-125-A` | `SRC-005#Abschnitt 7.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-534` |
| `ISO13485-RR-125-B` | `SRC-005#Abschnitt 7.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-535` |
| `ISO13485-RR-126` | `SRC-005#Abschnitt 7.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-536` |
| `ISO13485-RR-127` | `SRC-005#Abschnitt 7.6` | O | entsprechende Software eingesetzt | `NEW_UNIQUE_RR` | `RR-537` |
| `ISO13485-RR-128` | `SRC-005#Abschnitt 8.1` | O | – | `NEW_UNIQUE_RR` | `RR-538` |
| `ISO13485-RR-129-A` | `SRC-005#Abschnitt 8.2.1` | O | – | `NEW_UNIQUE_RR` | `RR-539` |
| `ISO13485-RR-129-B` | `SRC-005#Abschnitt 8.2.1` | O | – | `NEW_UNIQUE_RR` | `RR-540` |
| `ISO13485-RR-130` | `SRC-005#Abschnitt 8.2.1` | O | – | `NEW_UNIQUE_RR` | `RR-541` |
| `ISO13485-RR-131` | `SRC-005#Abschnitt 8.2.1` | O | entsprechende Information relevant | `NEW_UNIQUE_RR` | `RR-542` |
| `ISO13485-RR-132` | `SRC-005#Abschnitt 8.2.1` | O | regulatorische Pflicht besteht | `NEW_UNIQUE_RR` | `RR-543` |
| `ISO13485-RR-133` | `SRC-005#Abschnitt 8.2.2` | O | – | `NEW_UNIQUE_RR` | `RR-544` |
| `ISO13485-RR-134-A` | `SRC-005#Abschnitt 8.2.2` | O | jeweiliger Fall tritt ein | `NEW_UNIQUE_RR` | `RR-545` |
| `ISO13485-RR-134-B` | `SRC-005#Abschnitt 8.2.2` | O | jeweiliger Fall tritt ein | `NEW_UNIQUE_RR` | `RR-546` |
| `ISO13485-RR-135` | `SRC-005#Abschnitt 8.2.2` | O |  | `NEW_UNIQUE_RR` | `RR-547` |
| `ISO13485-RR-136` | `SRC-005#Abschnitt 8.2.2` | O | – | `NEW_UNIQUE_RR` | `RR-548` |
| `ISO13485-RR-137` | `SRC-005#Abschnitt 8.2.3` | O | regulatorische Meldepflicht | `NEW_UNIQUE_RR` | `RR-549` |
| `ISO13485-RR-138` | `SRC-005#Abschnitt 8.2.3` | O | Meldung/Verfahren einschlägig | `NEW_UNIQUE_RR` | `RR-550` |
| `ISO13485-RR-139` | `SRC-005#Abschnitt 8.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-551` |
| `ISO13485-RR-140` | `SRC-005#Abschnitt 8.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-552` |
| `ISO13485-RR-141-A` | `SRC-005#Abschnitt 8.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-553` |
| `ISO13485-RR-141-B` | `SRC-005#Abschnitt 8.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-554` |
| `ISO13485-RR-142` | `SRC-005#Abschnitt 8.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-555` |
| `ISO13485-RR-143` | `SRC-005#Abschnitt 8.2.4` | O | – | `NEW_UNIQUE_RR` | `RR-556` |
| `ISO13485-RR-144-A` | `SRC-005#Abschnitt 8.2.4` | verantwortliche Leitung | Audit-Nichtkonformität | `NEW_UNIQUE_RR` | `RR-557` |
| `ISO13485-RR-144-B` | `SRC-005#Abschnitt 8.2.4` | verantwortliche Leitung | Audit-Nichtkonformität | `NEW_UNIQUE_RR` | `RR-558` |
| `ISO13485-RR-145` | `SRC-005#Abschnitt 8.2.5` | O | – | `NEW_UNIQUE_RR` | `RR-559` |
| `ISO13485-RR-146` | `SRC-005#Abschnitt 8.2.5` | O | Ergebnis nicht erreicht | `NEW_UNIQUE_RR` | `RR-560` |
| `ISO13485-RR-147` | `SRC-005#Abschnitt 8.2.6` | O | – | `NEW_UNIQUE_RR` | `RR-561` |
| `ISO13485-RR-148-A` | `SRC-005#Abschnitt 8.2.6` | O | – | `NEW_UNIQUE_RR` | `RR-562` |
| `ISO13485-RR-148-B` | `SRC-005#Abschnitt 8.2.6` | O | – | `NEW_UNIQUE_RR` | `RR-563` |
| `ISO13485-RR-148-C` | `SRC-005#Abschnitt 8.2.6` | O | – | `NEW_UNIQUE_RR` | `RR-564` |
| `ISO13485-RR-149` | `SRC-005#Abschnitt 8.2.6` | O | – | `NEW_UNIQUE_RR` | `RR-565` |
| `ISO13485-RR-150` | `SRC-005#Abschnitt 8.3.1` | O | Nichtkonformität | `NEW_UNIQUE_RR` | `RR-566` |
| `ISO13485-RR-151` | `SRC-005#Abschnitt 8.3.1` | O | – | `NEW_UNIQUE_RR` | `RR-567` |
| `ISO13485-RR-152-A` | `SRC-005#Abschnitt 8.3.1` | O | Nichtkonformität | `NEW_UNIQUE_RR` | `RR-568` |
| `ISO13485-RR-152-B` | `SRC-005#Abschnitt 8.3.1` | O | Nichtkonformität | `NEW_UNIQUE_RR` | `RR-569` |
| `ISO13485-RR-153` | `SRC-005#Abschnitt 8.3.1` | O | Nichtkonformität | `NEW_UNIQUE_RR` | `RR-570` |
| `ISO13485-RR-154` | `SRC-005#Abschnitt 8.3.2` | O | NC vor Auslieferung | `NEW_UNIQUE_RR` | `RR-571` |
| `ISO13485-RR-155-A` | `SRC-005#Abschnitt 8.3.2` | O | Sonderfreigabe gewählt | `NEW_UNIQUE_RR` | `RR-572` |
| `ISO13485-RR-155-B` | `SRC-005#Abschnitt 8.3.2` | O | Sonderfreigabe gewählt | `NEW_UNIQUE_RR` | `RR-573` |
| `ISO13485-RR-156` | `SRC-005#Abschnitt 8.3.3` | O | post-delivery NC | `NEW_UNIQUE_RR` | `RR-574` |
| `ISO13485-RR-157` | `SRC-005#Abschnitt 8.3.3` | O | Maßnahmenempfehlung einschlägig | `NEW_UNIQUE_RR` | `RR-575` |
| `ISO13485-RR-158` | `SRC-005#Abschnitt 8.3.3` | O | entsprechender Fall | `NEW_UNIQUE_RR` | `RR-576` |
| `ISO13485-RR-159-A` | `SRC-005#Abschnitt 8.3.4` | O | Nacharbeit | `NEW_UNIQUE_RR` | `RR-577` |
| `ISO13485-RR-159-B` | `SRC-005#Abschnitt 8.3.4` | O | Nacharbeit | `NEW_UNIQUE_RR` | `RR-578` |
| `ISO13485-RR-160` | `SRC-005#Abschnitt 8.3.4` | O | Nacharbeit | `NEW_UNIQUE_RR` | `RR-579` |
| `ISO13485-RR-161` | `SRC-005#Abschnitt 8.3.4` | O | Nacharbeit | `NEW_UNIQUE_RR` | `RR-580` |
| `ISO13485-RR-162` | `SRC-005#Abschnitt 8.4` | O | – | `NEW_UNIQUE_RR` | `RR-581` |
| `ISO13485-RR-163` | `SRC-005#Abschnitt 8.4` | O | Serviceberichte soweit angemessen | `NEW_UNIQUE_RR` | `RR-582` |
| `ISO13485-RR-164` | `SRC-005#Abschnitt 8.4` | O | entsprechendes Analyseergebnis | `NEW_UNIQUE_RR` | `RR-583` |
| `ISO13485-RR-165` | `SRC-005#Abschnitt 8.4` | O | – | `NEW_UNIQUE_RR` | `RR-584` |
| `ISO13485-RR-166-A` | `SRC-005#Abschnitt 8.5.1` | O | erforderliche Verbesserung | `NEW_UNIQUE_RR` | `RR-585` |
| `ISO13485-RR-166-B` | `SRC-005#Abschnitt 8.5.1` | O | erforderliche Verbesserung | `NEW_UNIQUE_RR` | `RR-586` |
| `ISO13485-RR-167` | `SRC-005#Abschnitt 8.5.2` | O | bestehende NC | `NEW_UNIQUE_RR` | `RR-587` |
| `ISO13485-RR-168` | `SRC-005#Abschnitt 8.5.2(a)–(f)` | O | – | `NEW_UNIQUE_RR` | `RR-588` |
| `ISO13485-RR-169` | `SRC-005#Abschnitt 8.5.2` | O | Korrekturmaßnahme | `NEW_UNIQUE_RR` | `RR-589` |
| `ISO13485-RR-170` | `SRC-005#Abschnitt 8.5.3` | O | potentielle NC | `NEW_UNIQUE_RR` | `RR-590` |
| `ISO13485-RR-171` | `SRC-005#Abschnitt 8.5.3(a)–(e)` | O | – | `NEW_UNIQUE_RR` | `RR-591` |
| `ISO13485-RR-172` | `SRC-005#Abschnitt 8.5.3` | O | Vorbeugungsmaßnahme | `NEW_UNIQUE_RR` | `RR-592` |

### 11.2 SRC-006 — ISO 14971:2019 (107 Kandidaten)

| Temp-ID | Lokator | Adressat | Bedingung laut Adjudikation | Entscheidung | RR |
| --- | --- | --- | --- | --- | --- |
| `ISO14971-RR-001` | `SRC-006#Abschnitt 4.1` | H | – | `NEW_UNIQUE_RR` | `RR-593` |
| `ISO14971-RR-002` | `SRC-006#Abschnitt 4.1` | H | – | `NEW_UNIQUE_RR` | `RR-594` |
| `ISO14971-RR-003` | `SRC-006#Abschnitt 4.1` | H | – | `NEW_UNIQUE_RR` | `RR-595` |
| `ISO14971-RR-004` | `SRC-006#Abschnitt 4.1` | H | – | `NEW_UNIQUE_RR` | `RR-596` |
| `ISO14971-RR-005` | `SRC-006#Abschnitt 4.1(a)` | H | – | `NEW_UNIQUE_RR` | `RR-597` |
| `ISO14971-RR-006` | `SRC-006#Abschnitt 4.1(b)` | H | – | `NEW_UNIQUE_RR` | `RR-598` |
| `ISO14971-RR-007` | `SRC-006#Abschnitt 4.1(b)` | H | – | `NEW_UNIQUE_RR` | `RR-599` |
| `ISO14971-RR-008` | `SRC-006#Abschnitt 4.1(c)` | H | – | `NEW_UNIQUE_RR` | `RR-600` |
| `ISO14971-RR-009` | `SRC-006#Abschnitt 4.1(d)` | H | – | `NEW_UNIQUE_RR` | `RR-601` |
| `ISO14971-RR-010` | `SRC-006#Abschnitt 4.1` | H | – | `NEW_UNIQUE_RR` | `RR-602` |
| `ISO14971-RR-011` | `SRC-006#Abschnitt 4.1` | H | dokumentierter Produktrealisierungsprozess vorhanden | `NEW_UNIQUE_RR` | `RR-603` |
| `ISO14971-RR-012` | `SRC-006#Abschnitt 4.2` | OL | – | `NEW_UNIQUE_RR` | `RR-604` |
| `ISO14971-RR-013` | `SRC-006#Abschnitt 4.2` | OL | – | `NEW_UNIQUE_RR` | `RR-605` |
| `ISO14971-RR-014` | `SRC-006#Abschnitt 4.2` | OL | – | `NEW_UNIQUE_RR` | `RR-606` |
| `ISO14971-RR-015` | `SRC-006#Abschnitt 4.2` | OL | – | `NEW_UNIQUE_RR` | `RR-607` |
| `ISO14971-RR-016` | `SRC-006#Abschnitt 4.2` | OL | – | `NEW_UNIQUE_RR` | `RR-608` |
| `ISO14971-RR-017` | `SRC-006#Abschnitt 4.2` | OL | Review durchgeführt | `NEW_UNIQUE_RR` | `RR-609` |
| `ISO14971-RR-018` | `SRC-006#Abschnitt 4.3` | RM-P | – | `NEW_UNIQUE_RR` | `RR-610` |
| `ISO14971-RR-019` | `SRC-006#Abschnitt 4.3` | RM-P | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-611` |
| `ISO14971-RR-020` | `SRC-006#Abschnitt 4.3` | H | – | `NEW_UNIQUE_RR` | `RR-612` |
| `ISO14971-RR-021` | `SRC-006#Abschnitt 4.4` | H | je Medizinprodukt | `CROSSWALK_ONLY` | `RR-145`, `RR-146` |
| `ISO14971-RR-022` | `SRC-006#Abschnitt 4.4` | H | – | `NEW_UNIQUE_RR` | `RR-613` |
| `ISO14971-RR-023` | `SRC-006#Abschnitt 4.4(a)` | H | – | `NEW_UNIQUE_RR` | `RR-614` |
| `ISO14971-RR-024` | `SRC-006#Abschnitt 4.4(b)` | H | – | `NEW_UNIQUE_RR` | `RR-615` |
| `ISO14971-RR-025` | `SRC-006#Abschnitt 4.4(c)` | H | – | `NEW_UNIQUE_RR` | `RR-616` |
| `ISO14971-RR-026` | `SRC-006#Abschnitt 4.4(d)` | H | – | `NEW_UNIQUE_RR` | `RR-617` |
| `ISO14971-RR-027` | `SRC-006#Abschnitt 4.4(e)` | H | – | `NEW_UNIQUE_RR` | `RR-618` |
| `ISO14971-RR-028` | `SRC-006#Abschnitt 4.4(e)` | H | – | `NEW_UNIQUE_RR` | `RR-619` |
| `ISO14971-RR-029` | `SRC-006#Abschnitt 4.4(f)` | H | – | `NEW_UNIQUE_RR` | `RR-620` |
| `ISO14971-RR-030` | `SRC-006#Abschnitt 4.4(f)` | H | – | `NEW_UNIQUE_RR` | `RR-621` |
| `ISO14971-RR-031` | `SRC-006#Abschnitt 4.4(g)` | H | – | `NEW_UNIQUE_RR` | `RR-622` |
| `ISO14971-RR-032` | `SRC-006#Abschnitt 4.4(g)` | H | – | `NEW_UNIQUE_RR` | `RR-623` |
| `ISO14971-RR-033` | `SRC-006#Abschnitt 4.4` | H | Plan geändert | `NEW_UNIQUE_RR` | `RR-624` |
| `ISO14971-RR-034` | `SRC-006#Abschnitt 4.5` | H | je Medizinprodukt | `NEW_UNIQUE_RR` | `RR-625` |
| `ISO14971-RR-035` | `SRC-006#Abschnitt 4.5` | H | – | `NEW_UNIQUE_RR` | `RR-626` |
| `ISO14971-RR-036` | `SRC-006#Abschnitt 4.5` | H | jede identifizierte Gefährdung | `NEW_UNIQUE_RR` | `RR-627` |
| `ISO14971-RR-037` | `SRC-006#Abschnitt 5.1` | H | je Medizinprodukt | `NEW_UNIQUE_RR` | `RR-628` |
| `ISO14971-RR-038` | `SRC-006#Abschnitt 5.1` | H | – | `NEW_UNIQUE_RR` | `RR-629` |
| `ISO14971-RR-039` | `SRC-006#Abschnitt 5.1` | H | – | `NEW_UNIQUE_RR` | `RR-630` |
| `ISO14971-RR-040` | `SRC-006#Abschnitt 5.1(a)` | H | – | `NEW_UNIQUE_RR` | `RR-631` |
| `ISO14971-RR-041` | `SRC-006#Abschnitt 5.1(b)` | H | – | `NEW_UNIQUE_RR` | `RR-632` |
| `ISO14971-RR-042` | `SRC-006#Abschnitt 5.1(c)` | H | – | `NEW_UNIQUE_RR` | `RR-633` |
| `ISO14971-RR-043` | `SRC-006#Abschnitt 5.2` | H | – | `NEW_UNIQUE_RR` | `RR-634` |
| `ISO14971-RR-044` | `SRC-006#Abschnitt 5.2` | H | – | `NEW_UNIQUE_RR` | `RR-635` |
| `ISO14971-RR-045` | `SRC-006#Abschnitt 5.2` | H | – | `NEW_UNIQUE_RR` | `RR-636` |
| `ISO14971-RR-046` | `SRC-006#Abschnitt 5.3` | H | – | `NEW_UNIQUE_RR` | `RR-637` |
| `ISO14971-RR-047` | `SRC-006#Abschnitt 5.3` | H | – | `NEW_UNIQUE_RR` | `RR-638` |
| `ISO14971-RR-048` | `SRC-006#Abschnitt 5.3` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-639` |
| `ISO14971-RR-049` | `SRC-006#Abschnitt 5.3` | H | – | `NEW_UNIQUE_RR` | `RR-640` |
| `ISO14971-RR-050` | `SRC-006#Abschnitt 5.4` | H | – | `NEW_UNIQUE_RR` | `RR-641` |
| `ISO14971-RR-051` | `SRC-006#Abschnitt 5.4` | H | – | `NEW_UNIQUE_RR` | `RR-642` |
| `ISO14971-RR-052` | `SRC-006#Abschnitt 5.4` | H | jede identifizierte Gefährdung | `NEW_UNIQUE_RR` | `RR-643` |
| `ISO14971-RR-053` | `SRC-006#Abschnitt 5.4` | H | – | `NEW_UNIQUE_RR` | `RR-644` |
| `ISO14971-RR-054` | `SRC-006#Abschnitt 5.4` | H | – | `NEW_UNIQUE_RR` | `RR-645` |
| `ISO14971-RR-055` | `SRC-006#Abschnitt 5.4` | H | – | `NEW_UNIQUE_RR` | `RR-646` |
| `ISO14971-RR-056` | `SRC-006#Abschnitt 5.5` | H | – | `NEW_UNIQUE_RR` | `RR-647` |
| `ISO14971-RR-057` | `SRC-006#Abschnitt 5.5` | H | Wahrscheinlichkeit nicht abschätzbar | `NEW_UNIQUE_RR` | `RR-648` |
| `ISO14971-RR-058` | `SRC-006#Abschnitt 5.5` | H | – | `NEW_UNIQUE_RR` | `RR-649` |
| `ISO14971-RR-059` | `SRC-006#Abschnitt 5.5` | H | – | `NEW_UNIQUE_RR` | `RR-650` |
| `ISO14971-RR-060` | `SRC-006#Abschnitt 6` | H | – | `NEW_UNIQUE_RR` | `RR-651` |
| `ISO14971-RR-061` | `SRC-006#Abschnitt 6` | H | Risiko akzeptabel | `NEW_UNIQUE_RR` | `RR-652` |
| `ISO14971-RR-062` | `SRC-006#Abschnitt 6` | H | – | `NEW_UNIQUE_RR` | `RR-653` |
| `ISO14971-RR-063` | `SRC-006#Abschnitt 7.1` | H | Risiko nicht akzeptabel | `CROSS_NORM_MERGE (NORM-MERGE-01)` | `RR-378` |
| `ISO14971-RR-064` | `SRC-006#Abschnitt 7.1(a)–(c)` | H | Risikobeherrschung erforderlich | `EXISTING_RR_SUPPORT` | `RR-157` |
| `ISO14971-RR-065` | `SRC-006#Abschnitt 7.1` | H | – | `CROSS_NORM_MERGE (NORM-MERGE-02)` | `RR-379` |
| `ISO14971-RR-066` | `SRC-006#Abschnitt 7.1` | H | weitere Risikominderung nicht realisierbar | `NEW_UNIQUE_RR` | `RR-654` |
| `ISO14971-RR-067` | `SRC-006#Abschnitt 7.2` | H | – | `NEW_UNIQUE_RR` | `RR-655` |
| `ISO14971-RR-068` | `SRC-006#Abschnitt 7.2` | H | – | `CROSS_NORM_MERGE (NORM-MERGE-03)` | `RR-380` |
| `ISO14971-RR-069` | `SRC-006#Abschnitt 7.2` | H | – | `CROSS_NORM_MERGE (NORM-MERGE-04)` | `RR-381` |
| `ISO14971-RR-070` | `SRC-006#Abschnitt 7.2` | H | – | `NEW_UNIQUE_RR` | `RR-656` |
| `ISO14971-RR-071` | `SRC-006#Abschnitt 7.2` | H | – | `NEW_UNIQUE_RR` | `RR-657` |
| `ISO14971-RR-072` | `SRC-006#Abschnitt 7.3` | H | Maßnahmen implementiert | `CROSS_NORM_MERGE (NORM-MERGE-05)` | `RR-382` |
| `ISO14971-RR-073` | `SRC-006#Abschnitt 7.3` | H | – | `CROSS_NORM_MERGE (NORM-MERGE-06)` | `RR-383` |
| `ISO14971-RR-074` | `SRC-006#Abschnitt 7.3` | H | Restrisiko nicht akzeptabel | `NEW_UNIQUE_RR` | `RR-658` |
| `ISO14971-RR-075` | `SRC-006#Abschnitt 7.4` | H | Nutzen-Risiko-Analyse durchgeführt | `NEW_UNIQUE_RR` | `RR-659` |
| `ISO14971-RR-076` | `SRC-006#Abschnitt 7.5` | H | Maßnahme implementiert | `NEW_UNIQUE_RR` | `RR-660` |
| `ISO14971-RR-077` | `SRC-006#Abschnitt 7.5` | H | neues/erhöhtes Risiko | `NEW_UNIQUE_RR` | `RR-661` |
| `ISO14971-RR-078` | `SRC-006#Abschnitt 7.5` | H | – | `NEW_UNIQUE_RR` | `RR-662` |
| `ISO14971-RR-079` | `SRC-006#Abschnitt 7.6` | H | – | `NEW_UNIQUE_RR` | `RR-663` |
| `ISO14971-RR-080` | `SRC-006#Abschnitt 7.6` | H | – | `NEW_UNIQUE_RR` | `RR-664` |
| `ISO14971-RR-081` | `SRC-006#Abschnitt 8` | H | alle Maßnahmen implementiert/verifiziert | `NEW_UNIQUE_RR` | `RR-665` |
| `ISO14971-RR-082` | `SRC-006#Abschnitt 8` | H | Gesamt-Restrisiko vertretbar | `NEW_UNIQUE_RR` | `RR-666` |
| `ISO14971-RR-083` | `SRC-006#Abschnitt 8` | H | Gesamt-Restrisiko vertretbar | `NEW_UNIQUE_RR` | `RR-667` |
| `ISO14971-RR-084` | `SRC-006#Abschnitt 8` | H | – | `NEW_UNIQUE_RR` | `RR-668` |
| `ISO14971-RR-085` | `SRC-006#Abschnitt 9` | H | vor kommerzieller Freigabe | `NEW_UNIQUE_RR` | `RR-669` |
| `ISO14971-RR-086` | `SRC-006#Abschnitt 9` | H | Review durchgeführt | `NEW_UNIQUE_RR` | `RR-670` |
| `ISO14971-RR-087` | `SRC-006#Abschnitt 9` | H | – | `NEW_UNIQUE_RR` | `RR-671` |
| `ISO14971-RR-088` | `SRC-006#Abschnitt 9` | H | – | `NEW_UNIQUE_RR` | `RR-672` |
| `ISO14971-RR-089` | `SRC-006#Abschnitt 9` | H | – | `NEW_UNIQUE_RR` | `RR-673` |
| `ISO14971-RR-090` | `SRC-006#Abschnitt 10.1` | H | – | `NEW_UNIQUE_RR` | `RR-674` |
| `ISO14971-RR-091` | `SRC-006#Abschnitt 10.1` | H | – | `NEW_UNIQUE_RR` | `RR-675` |
| `ISO14971-RR-092` | `SRC-006#Abschnitt 10.1` | H | – | `NEW_UNIQUE_RR` | `RR-676` |
| `ISO14971-RR-093` | `SRC-006#Abschnitt 10.1` | H | – | `NEW_UNIQUE_RR` | `RR-677` |
| `ISO14971-RR-094` | `SRC-006#Abschnitt 10.2(a)` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-678` |
| `ISO14971-RR-095` | `SRC-006#Abschnitt 10.2(b)` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-679` |
| `ISO14971-RR-096` | `SRC-006#Abschnitt 10.2(c)` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-680` |
| `ISO14971-RR-097` | `SRC-006#Abschnitt 10.2(d)` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-681` |
| `ISO14971-RR-098` | `SRC-006#Abschnitt 10.2(e)` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-682` |
| `ISO14971-RR-099` | `SRC-006#Abschnitt 10.2(f)` | H | soweit zutreffend | `NEW_UNIQUE_RR` | `RR-683` |
| `ISO14971-RR-100` | `SRC-006#Abschnitt 10.2` | H | – | `NEW_UNIQUE_RR` | `RR-684` |
| `ISO14971-RR-101` | `SRC-006#Abschnitt 10.3` | H | – | `NEW_UNIQUE_RR` | `RR-685` |
| `ISO14971-RR-102` | `SRC-006#Abschnitt 10.3` | H | – | `NEW_UNIQUE_RR` | `RR-686` |
| `ISO14971-RR-103` | `SRC-006#Abschnitt 10.4(1)` | H | Information sicherheitsrelevant | `NEW_UNIQUE_RR` | `RR-687` |
| `ISO14971-RR-104` | `SRC-006#Abschnitt 10.4(1)` | H | Restrisiko nicht mehr akzeptabel | `NEW_UNIQUE_RR` | `RR-688` |
| `ISO14971-RR-105` | `SRC-006#Abschnitt 10.4(1)` | H | Clause-10.4-Pfad aktiv | `NEW_UNIQUE_RR` | `RR-689` |
| `ISO14971-RR-106` | `SRC-006#Abschnitt 10.4(2)` | H | Information sicherheitsrelevant | `NEW_UNIQUE_RR` | `RR-690` |
| `ISO14971-RR-107` | `SRC-006#Abschnitt 10.4(2)` | H/OL | Clause-10.4-Pfad aktiv | `NEW_UNIQUE_RR` | `RR-691` |

### 11.3 SRC-007 — IEC 62304:2006+AMD1:2015 (185 Kandidaten)

| Temp-ID | Lokator | Adressat | Bedingung laut Adjudikation | Entscheidung | RR |
| --- | --- | --- | --- | --- | --- |
| `IEC62304-RR-001` | `SRC-007#Abschnitt 4.1` | H | ALL | `NEW_UNIQUE_RR` | `RR-692` |
| `IEC62304-RR-002` | `SRC-007#Abschnitt 4.2` | H | ALL | `CROSSWALK_ONLY` | `RR-594` |
| `IEC62304-RR-003` | `SRC-007#Abschnitt 4.3/a` | H | PRE | `NEW_UNIQUE_RR` | `RR-693` |
| `IEC62304-RR-004` | `SRC-007#Abschnitt 4.3/c` | H | PRE | `NEW_UNIQUE_RR` | `RR-694` |
| `IEC62304-RR-005` | `SRC-007#Abschnitt 4.3/d` | H | PRE | `NEW_UNIQUE_RR` | `RR-695` |
| `IEC62304-RR-006` | `SRC-007#Abschnitt 4.3/e` | H | PRE | `NEW_UNIQUE_RR` | `RR-696` |
| `IEC62304-RR-007` | `SRC-007#Abschnitt 4.3/f` | H | PRE | `NEW_UNIQUE_RR` | `RR-697` |
| `IEC62304-RR-008` | `SRC-007#Abschnitt 4.4.2/a` | H | LEG | `NEW_UNIQUE_RR` | `RR-698` |
| `IEC62304-RR-009` | `SRC-007#Abschnitt 4.4.2/b` | H | LEG | `NEW_UNIQUE_RR` | `RR-699` |
| `IEC62304-RR-010` | `SRC-007#Abschnitt 4.4.2/b` | H | LEG | `NEW_UNIQUE_RR` | `RR-700` |
| `IEC62304-RR-011` | `SRC-007#Abschnitt 4.4.2/b` | H | LEG | `NEW_UNIQUE_RR` | `RR-701` |
| `IEC62304-RR-012` | `SRC-007#Abschnitt 4.4.2/b` | H | LEG | `NEW_UNIQUE_RR` | `RR-702` |
| `IEC62304-RR-013` | `SRC-007#Abschnitt 4.4.2/b` | H | LEG | `NEW_UNIQUE_RR` | `RR-703` |
| `IEC62304-RR-014` | `SRC-007#Abschnitt 4.4.3` | H | LEG | `NEW_UNIQUE_RR` | `RR-704` |
| `IEC62304-RR-015` | `SRC-007#Abschnitt 4.4.3/a` | H | LEG | `NEW_UNIQUE_RR` | `RR-705` |
| `IEC62304-RR-016` | `SRC-007#Abschnitt 4.4.3/b` | H | LEG; Lücken vorhanden | `NEW_UNIQUE_RR` | `RR-706` |
| `IEC62304-RR-017` | `SRC-007#Abschnitt 4.4.3/c` | H | LEG | `NEW_UNIQUE_RR` | `RR-707` |
| `IEC62304-RR-018` | `SRC-007#Abschnitt 4.4.3/c` | H | LEG | `NEW_UNIQUE_RR` | `RR-708` |
| `IEC62304-RR-019` | `SRC-007#Abschnitt 4.4.3/c` | H | LEG | `NEW_UNIQUE_RR` | `RR-709` |
| `IEC62304-RR-020` | `SRC-007#Abschnitt 4.4.4/a` | H | LEG | `NEW_UNIQUE_RR` | `RR-710` |
| `IEC62304-RR-021` | `SRC-007#Abschnitt 4.4.4/a` | H | LEG | `NEW_UNIQUE_RR` | `RR-711` |
| `IEC62304-RR-022` | `SRC-007#Abschnitt 4.4.4/b` | H | LEG | `NEW_UNIQUE_RR` | `RR-712` |
| `IEC62304-RR-023` | `SRC-007#Abschnitt 4.4.4/c` | H | LEG; Änderung | `NEW_UNIQUE_RR` | `RR-713` |
| `IEC62304-RR-024` | `SRC-007#Abschnitt 4.4.5` | H | LEG | `NEW_UNIQUE_RR` | `RR-714` |
| `IEC62304-RR-025` | `SRC-007#Abschnitt 4.4.5` | H | LEG | `NEW_UNIQUE_RR` | `RR-715` |
| `IEC62304-RR-026` | `SRC-007#Abschnitt 5.1.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-716` |
| `IEC62304-RR-027` | `SRC-007#Abschnitt 5.1.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-717` |
| `IEC62304-RR-028` | `SRC-007#Abschnitt 5.1.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-718` |
| `IEC62304-RR-029` | `SRC-007#Abschnitt 5.1.1/a` | H | ABC | `NEW_UNIQUE_RR` | `RR-719` |
| `IEC62304-RR-030` | `SRC-007#Abschnitt 5.1.1/b` | H | ABC | `NEW_UNIQUE_RR` | `RR-720` |
| `IEC62304-RR-031` | `SRC-007#Abschnitt 5.1.1/c` | H | ABC | `NEW_UNIQUE_RR` | `RR-721` |
| `IEC62304-RR-032` | `SRC-007#Abschnitt 5.1.1/d` | H | ABC | `NEW_UNIQUE_RR` | `RR-722` |
| `IEC62304-RR-033` | `SRC-007#Abschnitt 5.1.1/e` | H | ABC | `NEW_UNIQUE_RR` | `RR-723` |
| `IEC62304-RR-034` | `SRC-007#Abschnitt 5.1.2` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-724` |
| `IEC62304-RR-035` | `SRC-007#Abschnitt 5.1.3/a` | H | ABC | `NEW_UNIQUE_RR` | `RR-725` |
| `IEC62304-RR-036` | `SRC-007#Abschnitt 5.1.3/b` | H | ABC | `NEW_UNIQUE_RR` | `RR-726` |
| `IEC62304-RR-037` | `SRC-007#Abschnitt 5.1.4` | H | C | `NEW_UNIQUE_RR` | `RR-727` |
| `IEC62304-RR-038` | `SRC-007#Abschnitt 5.1.5` | H | BC | `NEW_UNIQUE_RR` | `RR-728` |
| `IEC62304-RR-039` | `SRC-007#Abschnitt 5.1.6` | H | ABC | `NEW_UNIQUE_RR` | `RR-729` |
| `IEC62304-RR-040` | `SRC-007#Abschnitt 5.1.7` | H | ABC | `NEW_UNIQUE_RR` | `RR-730` |
| `IEC62304-RR-041` | `SRC-007#Abschnitt 5.1.8` | H | ABC | `NEW_UNIQUE_RR` | `RR-731` |
| `IEC62304-RR-042` | `SRC-007#Abschnitt 5.1.9` | H | ABC | `NEW_UNIQUE_RR` | `RR-732` |
| `IEC62304-RR-043` | `SRC-007#Abschnitt 5.1.10` | H | BC | `NEW_UNIQUE_RR` | `RR-733` |
| `IEC62304-RR-044` | `SRC-007#Abschnitt 5.1.11` | H | BC | `NEW_UNIQUE_RR` | `RR-734` |
| `IEC62304-RR-045` | `SRC-007#Abschnitt 5.1.12` | H | BC | `NEW_UNIQUE_RR` | `RR-735` |
| `IEC62304-RR-046` | `SRC-007#Abschnitt 5.2.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-736` |
| `IEC62304-RR-047` | `SRC-007#Abschnitt 5.2.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-737` |
| `IEC62304-RR-048` | `SRC-007#Abschnitt 5.2.2/a` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-738` |
| `IEC62304-RR-049` | `SRC-007#Abschnitt 5.2.2/b` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-739` |
| `IEC62304-RR-050` | `SRC-007#Abschnitt 5.2.2/c` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-740` |
| `IEC62304-RR-051` | `SRC-007#Abschnitt 5.2.2/d` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-741` |
| `IEC62304-RR-052` | `SRC-007#Abschnitt 5.2.2/e` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-742` |
| `IEC62304-RR-053` | `SRC-007#Abschnitt 5.2.2/f` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-743` |
| `IEC62304-RR-054` | `SRC-007#Abschnitt 5.2.2/g` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-744` |
| `IEC62304-RR-055` | `SRC-007#Abschnitt 5.2.2/h` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-745` |
| `IEC62304-RR-056` | `SRC-007#Abschnitt 5.2.2/i` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-746` |
| `IEC62304-RR-057` | `SRC-007#Abschnitt 5.2.2/j` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-747` |
| `IEC62304-RR-058` | `SRC-007#Abschnitt 5.2.2/k` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-748` |
| `IEC62304-RR-059` | `SRC-007#Abschnitt 5.2.2/l` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-749` |
| `IEC62304-RR-060` | `SRC-007#Abschnitt 5.2.3` | H | BC | `NEW_UNIQUE_RR` | `RR-750` |
| `IEC62304-RR-061` | `SRC-007#Abschnitt 5.2.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-751` |
| `IEC62304-RR-062` | `SRC-007#Abschnitt 5.2.4` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-752` |
| `IEC62304-RR-063` | `SRC-007#Abschnitt 5.2.5` | H | ABC | `NEW_UNIQUE_RR` | `RR-753` |
| `IEC62304-RR-064` | `SRC-007#Abschnitt 5.2.5` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-754` |
| `IEC62304-RR-065` | `SRC-007#Abschnitt 5.2.6` | H | ABC | `NEW_UNIQUE_RR` | `RR-755` |
| `IEC62304-RR-066` | `SRC-007#Abschnitt 5.2.6` | H | ABC | `NEW_UNIQUE_RR` | `RR-756` |
| `IEC62304-RR-067` | `SRC-007#Abschnitt 5.3.1` | H | BC | `NEW_UNIQUE_RR` | `RR-757` |
| `IEC62304-RR-068` | `SRC-007#Abschnitt 5.3.2` | H | BC | `NEW_UNIQUE_RR` | `RR-758` |
| `IEC62304-RR-069` | `SRC-007#Abschnitt 5.3.2` | H | BC | `NEW_UNIQUE_RR` | `RR-759` |
| `IEC62304-RR-070` | `SRC-007#Abschnitt 5.3.3` | H | BC; SOUP | `NEW_UNIQUE_RR` | `RR-760` |
| `IEC62304-RR-071` | `SRC-007#Abschnitt 5.3.4` | H | BC; SOUP | `NEW_UNIQUE_RR` | `RR-761` |
| `IEC62304-RR-072` | `SRC-007#Abschnitt 5.3.5` | H | C | `NEW_UNIQUE_RR` | `RR-762` |
| `IEC62304-RR-073` | `SRC-007#Abschnitt 5.3.5` | H | C | `NEW_UNIQUE_RR` | `RR-763` |
| `IEC62304-RR-074` | `SRC-007#Abschnitt 5.3.6` | H | BC | `NEW_UNIQUE_RR` | `RR-764` |
| `IEC62304-RR-075` | `SRC-007#Abschnitt 5.3.6` | H | BC | `NEW_UNIQUE_RR` | `RR-765` |
| `IEC62304-RR-076` | `SRC-007#Abschnitt 5.4.1` | H | BC | `NEW_UNIQUE_RR` | `RR-766` |
| `IEC62304-RR-077` | `SRC-007#Abschnitt 5.4.2` | H | C | `NEW_UNIQUE_RR` | `RR-767` |
| `IEC62304-RR-078` | `SRC-007#Abschnitt 5.4.2` | H | C | `NEW_UNIQUE_RR` | `RR-768` |
| `IEC62304-RR-079` | `SRC-007#Abschnitt 5.4.3` | H | C | `NEW_UNIQUE_RR` | `RR-769` |
| `IEC62304-RR-080` | `SRC-007#Abschnitt 5.4.4` | H | C | `NEW_UNIQUE_RR` | `RR-770` |
| `IEC62304-RR-081` | `SRC-007#Abschnitt 5.4.4` | H | C | `NEW_UNIQUE_RR` | `RR-771` |
| `IEC62304-RR-082` | `SRC-007#Abschnitt 5.5.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-772` |
| `IEC62304-RR-083` | `SRC-007#Abschnitt 5.5.2` | H | BC | `NEW_UNIQUE_RR` | `RR-773` |
| `IEC62304-RR-084` | `SRC-007#Abschnitt 5.5.2` | H | BC; Testverifizierung | `NEW_UNIQUE_RR` | `RR-774` |
| `IEC62304-RR-085` | `SRC-007#Abschnitt 5.5.3` | H | BC | `NEW_UNIQUE_RR` | `RR-775` |
| `IEC62304-RR-086` | `SRC-007#Abschnitt 5.5.3` | H | BC | `NEW_UNIQUE_RR` | `RR-776` |
| `IEC62304-RR-087` | `SRC-007#Abschnitt 5.5.4` | H | C; conditional | `NEW_UNIQUE_RR` | `RR-777` |
| `IEC62304-RR-088` | `SRC-007#Abschnitt 5.5.5` | H | BC | `NEW_UNIQUE_RR` | `RR-778` |
| `IEC62304-RR-089` | `SRC-007#Abschnitt 5.5.5` | H | BC | `NEW_UNIQUE_RR` | `RR-779` |
| `IEC62304-RR-090` | `SRC-007#Abschnitt 5.6.1` | H | BC | `NEW_UNIQUE_RR` | `RR-780` |
| `IEC62304-RR-091` | `SRC-007#Abschnitt 5.6.2` | H | BC | `NEW_UNIQUE_RR` | `RR-781` |
| `IEC62304-RR-092` | `SRC-007#Abschnitt 5.6.2` | H | BC | `NEW_UNIQUE_RR` | `RR-782` |
| `IEC62304-RR-093` | `SRC-007#Abschnitt 5.6.3` | H | BC | `NEW_UNIQUE_RR` | `RR-783` |
| `IEC62304-RR-094` | `SRC-007#Abschnitt 5.6.3` | H | BC | `NEW_UNIQUE_RR` | `RR-784` |
| `IEC62304-RR-095` | `SRC-007#Abschnitt 5.6.4` | H | BC | `NEW_UNIQUE_RR` | `RR-785` |
| `IEC62304-RR-096` | `SRC-007#Abschnitt 5.6.5` | H | BC | `NEW_UNIQUE_RR` | `RR-786` |
| `IEC62304-RR-097` | `SRC-007#Abschnitt 5.6.6` | H | BC | `NEW_UNIQUE_RR` | `RR-787` |
| `IEC62304-RR-098` | `SRC-007#Abschnitt 5.6.7` | H | BC | `NEW_UNIQUE_RR` | `RR-788` |
| `IEC62304-RR-099` | `SRC-007#Abschnitt 5.6.8` | H | BC | `NEW_UNIQUE_RR` | `RR-789` |
| `IEC62304-RR-100` | `SRC-007#Abschnitt 5.7.1/a` | H | ABC | `NEW_UNIQUE_RR` | `RR-790` |
| `IEC62304-RR-101` | `SRC-007#Abschnitt 5.7.1/a` | H | ABC | `NEW_UNIQUE_RR` | `RR-791` |
| `IEC62304-RR-102` | `SRC-007#Abschnitt 5.7.1/b` | H | ABC | `NEW_UNIQUE_RR` | `RR-792` |
| `IEC62304-RR-103` | `SRC-007#Abschnitt 5.7.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-793` |
| `IEC62304-RR-104` | `SRC-007#Abschnitt 5.7.3/a` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-794` |
| `IEC62304-RR-105` | `SRC-007#Abschnitt 5.7.3/b` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-795` |
| `IEC62304-RR-106` | `SRC-007#Abschnitt 5.7.3/c` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-796` |
| `IEC62304-RR-107` | `SRC-007#Abschnitt 5.7.4/a` | H | ABC | `NEW_UNIQUE_RR` | `RR-797` |
| `IEC62304-RR-108` | `SRC-007#Abschnitt 5.7.4/b` | H | ABC | `NEW_UNIQUE_RR` | `RR-798` |
| `IEC62304-RR-109` | `SRC-007#Abschnitt 5.7.4/c` | H | ABC | `NEW_UNIQUE_RR` | `RR-799` |
| `IEC62304-RR-110` | `SRC-007#Abschnitt 5.7.5` | H | ABC | `NEW_UNIQUE_RR` | `RR-800` |
| `IEC62304-RR-111` | `SRC-007#Abschnitt 5.8.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-801` |
| `IEC62304-RR-112` | `SRC-007#Abschnitt 5.8.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-802` |
| `IEC62304-RR-113` | `SRC-007#Abschnitt 5.8.3` | H | BC | `NEW_UNIQUE_RR` | `RR-803` |
| `IEC62304-RR-114` | `SRC-007#Abschnitt 5.8.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-804` |
| `IEC62304-RR-115` | `SRC-007#Abschnitt 5.8.5` | H | BC | `NEW_UNIQUE_RR` | `RR-805` |
| `IEC62304-RR-116` | `SRC-007#Abschnitt 5.8.6` | H | BC | `NEW_UNIQUE_RR` | `RR-806` |
| `IEC62304-RR-117` | `SRC-007#Abschnitt 5.8.6` | H | BC | `NEW_UNIQUE_RR` | `RR-807` |
| `IEC62304-RR-118` | `SRC-007#Abschnitt 5.8.7` | H | ABC | `NEW_UNIQUE_RR` | `RR-808` |
| `IEC62304-RR-119` | `SRC-007#Abschnitt 5.8.8` | H | ABC | `NEW_UNIQUE_RR` | `RR-809` |
| `IEC62304-RR-120` | `SRC-007#Abschnitt 6.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-810` |
| `IEC62304-RR-121` | `SRC-007#Abschnitt 6.1/a` | H | ABC | `NEW_UNIQUE_RR` | `RR-811` |
| `IEC62304-RR-122` | `SRC-007#Abschnitt 6.1/b` | H | ABC | `NEW_UNIQUE_RR` | `RR-812` |
| `IEC62304-RR-123` | `SRC-007#Abschnitt 6.1/c` | H | ABC | `NEW_UNIQUE_RR` | `RR-813` |
| `IEC62304-RR-124` | `SRC-007#Abschnitt 6.1/d` | H | ABC | `NEW_UNIQUE_RR` | `RR-814` |
| `IEC62304-RR-125` | `SRC-007#Abschnitt 6.1/e` | H | ABC | `NEW_UNIQUE_RR` | `RR-815` |
| `IEC62304-RR-126` | `SRC-007#Abschnitt 6.1/f` | H | ABC; SOUP | `NEW_UNIQUE_RR` | `RR-816` |
| `IEC62304-RR-127` | `SRC-007#Abschnitt 6.2.1.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-817` |
| `IEC62304-RR-128` | `SRC-007#Abschnitt 6.2.1.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-818` |
| `IEC62304-RR-129` | `SRC-007#Abschnitt 6.2.1.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-819` |
| `IEC62304-RR-130` | `SRC-007#Abschnitt 6.2.1.2` | H | ABC; Problem identifiziert | `NEW_UNIQUE_RR` | `RR-820` |
| `IEC62304-RR-131` | `SRC-007#Abschnitt 6.2.1.2` | H | ABC; Problembericht | `NEW_UNIQUE_RR` | `RR-821` |
| `IEC62304-RR-132` | `SRC-007#Abschnitt 6.2.1.3` | H | ABC | `NEW_UNIQUE_RR` | `RR-822` |
| `IEC62304-RR-133` | `SRC-007#Abschnitt 6.2.1.3` | H | ABC | `NEW_UNIQUE_RR` | `RR-823` |
| `IEC62304-RR-134` | `SRC-007#Abschnitt 6.2.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-824` |
| `IEC62304-RR-135` | `SRC-007#Abschnitt 6.2.3` | H | ABC | `NEW_UNIQUE_RR` | `RR-825` |
| `IEC62304-RR-136` | `SRC-007#Abschnitt 6.2.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-826` |
| `IEC62304-RR-137` | `SRC-007#Abschnitt 6.2.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-827` |
| `IEC62304-RR-138` | `SRC-007#Abschnitt 6.2.5` | H | ABC | `NEW_UNIQUE_RR` | `RR-828` |
| `IEC62304-RR-139` | `SRC-007#Abschnitt 6.2.5` | H | ABC; lokale Vorschrift | `NEW_UNIQUE_RR` | `RR-829` |
| `IEC62304-RR-140` | `SRC-007#Abschnitt 6.2.5` | H | ABC; lokale Vorschrift | `NEW_UNIQUE_RR` | `RR-830` |
| `IEC62304-RR-141` | `SRC-007#Abschnitt 6.3.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-831` |
| `IEC62304-RR-142` | `SRC-007#Abschnitt 6.3.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-832` |
| `IEC62304-RR-143` | `SRC-007#Abschnitt 6.3.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-833` |
| `IEC62304-RR-144` | `SRC-007#Abschnitt 7.1.1` | H | BC | `NEW_UNIQUE_RR` | `RR-834` |
| `IEC62304-RR-145` | `SRC-007#Abschnitt 7.1.2` | H | BC | `NEW_UNIQUE_RR` | `RR-835` |
| `IEC62304-RR-146` | `SRC-007#Abschnitt 7.1.3` | H | BC; SOUP-Trigger | `NEW_UNIQUE_RR` | `RR-836` |
| `IEC62304-RR-147` | `SRC-007#Abschnitt 7.1.4` | H | BC | `NEW_UNIQUE_RR` | `RR-837` |
| `IEC62304-RR-148` | `SRC-007#Abschnitt 7.2.1` | H | BC | `CROSS_NORM_MERGE (NORM-MERGE-01)` | `RR-378` |
| `IEC62304-RR-149` | `SRC-007#Abschnitt 7.2.1` | H | BC | `CROSS_NORM_MERGE (NORM-MERGE-02)` | `RR-379` |
| `IEC62304-RR-150` | `SRC-007#Abschnitt 7.2.2/a` | H | BC; softwareimplementierte RM | `NEW_UNIQUE_RR` | `RR-838` |
| `IEC62304-RR-151` | `SRC-007#Abschnitt 7.2.2/b` | H | BC; softwareimplementierte RM | `NEW_UNIQUE_RR` | `RR-839` |
| `IEC62304-RR-152` | `SRC-007#Abschnitt 7.2.2/c` | H | BC | `NEW_UNIQUE_RR` | `RR-840` |
| `IEC62304-RR-153` | `SRC-007#Abschnitt 7.3.1` | H | BC | `CROSS_NORM_MERGE (NORM-MERGE-03)` | `RR-380` |
| `IEC62304-RR-154` | `SRC-007#Abschnitt 7.3.1` | H | BC | `CROSS_NORM_MERGE (NORM-MERGE-04)` | `RR-381` |
| `IEC62304-RR-155` | `SRC-007#Abschnitt 7.3.1` | H | BC | `NEW_UNIQUE_RR` | `RR-841` |
| `IEC62304-RR-156` | `SRC-007#Abschnitt 7.3.3` | H | BC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-842` |
| `IEC62304-RR-157` | `SRC-007#Abschnitt 7.4.1/a` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-843` |
| `IEC62304-RR-158` | `SRC-007#Abschnitt 7.4.1/b` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-844` |
| `IEC62304-RR-159` | `SRC-007#Abschnitt 7.4.2` | H | BC; Änderung | `NEW_UNIQUE_RR` | `RR-845` |
| `IEC62304-RR-160` | `SRC-007#Abschnitt 7.4.3` | H | BC; Bedarf festgestellt | `NEW_UNIQUE_RR` | `RR-846` |
| `IEC62304-RR-161` | `SRC-007#Abschnitt 8.1.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-847` |
| `IEC62304-RR-162` | `SRC-007#Abschnitt 8.1.1` | H | ABC | `NEW_UNIQUE_RR` | `RR-848` |
| `IEC62304-RR-163` | `SRC-007#Abschnitt 8.1.2` | H | ABC; SOUP | `NEW_UNIQUE_RR` | `RR-849` |
| `IEC62304-RR-164` | `SRC-007#Abschnitt 8.1.3` | H | ABC | `NEW_UNIQUE_RR` | `RR-850` |
| `IEC62304-RR-165` | `SRC-007#Abschnitt 8.2.1` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-851` |
| `IEC62304-RR-166` | `SRC-007#Abschnitt 8.2.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-852` |
| `IEC62304-RR-167` | `SRC-007#Abschnitt 8.2.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-853` |
| `IEC62304-RR-168` | `SRC-007#Abschnitt 8.2.2` | H | ABC | `NEW_UNIQUE_RR` | `RR-854` |
| `IEC62304-RR-169` | `SRC-007#Abschnitt 8.2.3` | H | ABC | `NEW_UNIQUE_RR` | `RR-855` |
| `IEC62304-RR-170` | `SRC-007#Abschnitt 8.2.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-856` |
| `IEC62304-RR-171` | `SRC-007#Abschnitt 8.3` | H | ABC | `NEW_UNIQUE_RR` | `RR-857` |
| `IEC62304-RR-172` | `SRC-007#Abschnitt 9.1` | H | ABC; Problem | `NEW_UNIQUE_RR` | `RR-858` |
| `IEC62304-RR-173` | `SRC-007#Abschnitt 9.1` | H | ABC; Problembericht | `NEW_UNIQUE_RR` | `RR-859` |
| `IEC62304-RR-174` | `SRC-007#Abschnitt 9.2/a` | H | ABC; Problembericht | `NEW_UNIQUE_RR` | `RR-860` |
| `IEC62304-RR-175` | `SRC-007#Abschnitt 9.2/b` | H | ABC; Problembericht | `NEW_UNIQUE_RR` | `RR-861` |
| `IEC62304-RR-176` | `SRC-007#Abschnitt 9.2/c` | H | ABC; Problembericht | `NEW_UNIQUE_RR` | `RR-862` |
| `IEC62304-RR-177` | `SRC-007#Abschnitt 9.2/d` | H | ABC; Problembericht | `NEW_UNIQUE_RR` | `RR-863` |
| `IEC62304-RR-178` | `SRC-007#Abschnitt 9.3` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-864` |
| `IEC62304-RR-179` | `SRC-007#Abschnitt 9.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-865` |
| `IEC62304-RR-180` | `SRC-007#Abschnitt 9.4` | H | ABC | `NEW_UNIQUE_RR` | `RR-866` |
| `IEC62304-RR-181` | `SRC-007#Abschnitt 9.5` | H | ABC | `NEW_UNIQUE_RR` | `RR-867` |
| `IEC62304-RR-182` | `SRC-007#Abschnitt 9.5` | H | ABC; soweit angemessen | `NEW_UNIQUE_RR` | `RR-868` |
| `IEC62304-RR-183` | `SRC-007#Abschnitt 9.6` | H | ABC | `NEW_UNIQUE_RR` | `RR-869` |
| `IEC62304-RR-184` | `SRC-007#Abschnitt 9.7` | H | ABC | `NEW_UNIQUE_RR` | `RR-870` |
| `IEC62304-RR-185` | `SRC-007#Abschnitt 9.8` | H | ABC; Änderung | `NEW_UNIQUE_RR` | `RR-871` |

### 11.4 SRC-008 — IEC 62366-1:2015+AMD1:2020 (93 Kandidaten)

| Temp-ID | Lokator | Adressat | Bedingung laut Adjudikation | Entscheidung | RR |
| --- | --- | --- | --- | --- | --- |
| `IEC62366-RR-001` | `SRC-008#Abschnitt 4.1.1` | H | — | `NEW_UNIQUE_RR` | `RR-872` |
| `IEC62366-RR-002` | `SRC-008#Abschnitt 4.1.1` | H | — | `NEW_UNIQUE_RR` | `RR-873` |
| `IEC62366-RR-003` | `SRC-008#Abschnitt 4.1.1` | H | — | `NEW_UNIQUE_RR` | `RR-874` |
| `IEC62366-RR-004` | `SRC-008#Abschnitt 4.1.1` | H | — | `NEW_UNIQUE_RR` | `RR-875` |
| `IEC62366-RR-005` | `SRC-008#Abschnitt 4.1.1` | H | — | `NEW_UNIQUE_RR` | `RR-876` |
| `IEC62366-RR-006` | `SRC-008#Abschnitt 4.1.1` | H | — | `NEW_UNIQUE_RR` | `RR-877` |
| `IEC62366-RR-007` | `SRC-008#Abschnitt 4.1.1` | H | dokumentierter Produktentwicklungsprozess vorhanden | `NEW_UNIQUE_RR` | `RR-878` |
| `IEC62366-RR-008` | `SRC-008#Abschnitt 4.1.3` | H | Sicherheitsinformation als RM-Maßnahme | `NEW_UNIQUE_RR` | `RR-879` |
| `IEC62366-RR-009` | `SRC-008#Abschnitt 4.1.3` | H | wie 008 | `NEW_UNIQUE_RR` | `RR-880` |
| `IEC62366-RR-010` | `SRC-008#Abschnitt 4.2` | H | — | `NEW_UNIQUE_RR` | `RR-881` |
| `IEC62366-RR-011` | `SRC-008#Abschnitt 5.1` | H | REG; zusätzlich über C.2.1 für UOUP referenziert | `NEW_UNIQUE_RR` | `RR-882` |
| `IEC62366-RR-012` | `SRC-008#Abschnitt 5.1` | H | wie 011 | `NEW_UNIQUE_RR` | `RR-883` |
| `IEC62366-RR-013` | `SRC-008#Abschnitt 5.1` | H | wie 011 | `NEW_UNIQUE_RR` | `RR-884` |
| `IEC62366-RR-014` | `SRC-008#Abschnitt 5.1` | H | wie 011 | `NEW_UNIQUE_RR` | `RR-885` |
| `IEC62366-RR-015` | `SRC-008#Abschnitt 5.1` | H | wie 011 | `NEW_UNIQUE_RR` | `RR-886` |
| `IEC62366-RR-016` | `SRC-008#Abschnitt 5.1` | H | wie 011 | `NEW_UNIQUE_RR` | `RR-887` |
| `IEC62366-RR-017` | `SRC-008#Abschnitt 5.1` | H | wie 011 | `NEW_UNIQUE_RR` | `RR-888` |
| `IEC62366-RR-018` | `SRC-008#Abschnitt 5.2` | H | REG | `NEW_UNIQUE_RR` | `RR-889` |
| `IEC62366-RR-019` | `SRC-008#Abschnitt 5.2` | H | entsprechende produktspezifische Sicherheitsnorm fordert sie | `NEW_UNIQUE_RR` | `RR-890` |
| `IEC62366-RR-020` | `SRC-008#Abschnitt 5.2` | H | REG | `NEW_UNIQUE_RR` | `RR-891` |
| `IEC62366-RR-021` | `SRC-008#Abschnitt 5.2` | H | REG | `NEW_UNIQUE_RR` | `RR-892` |
| `IEC62366-RR-022` | `SRC-008#Abschnitt 5.3` | H | REG | `NEW_UNIQUE_RR` | `RR-893` |
| `IEC62366-RR-023` | `SRC-008#Abschnitt 5.3` | H | ähnliche UI-Information soweit verfügbar | `NEW_UNIQUE_RR` | `RR-894` |
| `IEC62366-RR-024` | `SRC-008#Abschnitt 5.3` | H | REG | `NEW_UNIQUE_RR` | `RR-895` |
| `IEC62366-RR-025` | `SRC-008#Abschnitt 5.4` | H | REG | `NEW_UNIQUE_RR` | `RR-896` |
| `IEC62366-RR-026` | `SRC-008#Abschnitt 5.4` | H | REG | `NEW_UNIQUE_RR` | `RR-897` |
| `IEC62366-RR-027` | `SRC-008#Abschnitt 5.4` | H | REG | `NEW_UNIQUE_RR` | `RR-898` |
| `IEC62366-RR-028` | `SRC-008#Abschnitt 5.5` | H | REG | `NEW_UNIQUE_RR` | `RR-899` |
| `IEC62366-RR-029` | `SRC-008#Abschnitt 5.5` | H | REG | `NEW_UNIQUE_RR` | `RR-900` |
| `IEC62366-RR-030` | `SRC-008#Abschnitt 5.5` | H | REG | `NEW_UNIQUE_RR` | `RR-901` |
| `IEC62366-RR-031` | `SRC-008#Abschnitt 5.5` | H | REG | `NEW_UNIQUE_RR` | `RR-902` |
| `IEC62366-RR-032` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-903` |
| `IEC62366-RR-033` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-904` |
| `IEC62366-RR-034` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-905` |
| `IEC62366-RR-035` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-906` |
| `IEC62366-RR-036` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-907` |
| `IEC62366-RR-037` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-908` |
| `IEC62366-RR-038` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-909` |
| `IEC62366-RR-039` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-910` |
| `IEC62366-RR-040` | `SRC-008#Abschnitt 5.6` | H | REG | `NEW_UNIQUE_RR` | `RR-911` |
| `IEC62366-RR-041` | `SRC-008#Abschnitt 5.7.1` | H | REG | `NEW_UNIQUE_RR` | `RR-912` |
| `IEC62366-RR-042` | `SRC-008#Abschnitt 5.7.1` | H | REG | `NEW_UNIQUE_RR` | `RR-913` |
| `IEC62366-RR-043` | `SRC-008#Abschnitt 5.7.1/a` | H | REG | `NEW_UNIQUE_RR` | `RR-914` |
| `IEC62366-RR-044` | `SRC-008#Abschnitt 5.7.1/a` | H | REG | `NEW_UNIQUE_RR` | `RR-915` |
| `IEC62366-RR-045` | `SRC-008#Abschnitt 5.7.1/b` | H | Usability Test vorgesehen | `NEW_UNIQUE_RR` | `RR-916` |
| `IEC62366-RR-046` | `SRC-008#Abschnitt 5.7.1/b` | H | Usability Test vorgesehen | `NEW_UNIQUE_RR` | `RR-917` |
| `IEC62366-RR-047` | `SRC-008#Abschnitt 5.7.1/b` | H | Usability Test vorgesehen | `NEW_UNIQUE_RR` | `RR-918` |
| `IEC62366-RR-048` | `SRC-008#Abschnitt 5.7.1/b` | H | Usability Test vorgesehen | `NEW_UNIQUE_RR` | `RR-919` |
| `IEC62366-RR-049` | `SRC-008#Abschnitt 5.7.1` | H | REG | `NEW_UNIQUE_RR` | `RR-920` |
| `IEC62366-RR-050` | `SRC-008#Abschnitt 5.7.2/a` | H | REG | `NEW_UNIQUE_RR` | `RR-921` |
| `IEC62366-RR-051` | `SRC-008#Abschnitt 5.7.2/b` | H | REG | `NEW_UNIQUE_RR` | `RR-922` |
| `IEC62366-RR-052` | `SRC-008#Abschnitt 5.7.2/c` | H | REG | `NEW_UNIQUE_RR` | `RR-923` |
| `IEC62366-RR-053` | `SRC-008#Abschnitt 5.7.3/a` | H | REG | `NEW_UNIQUE_RR` | `RR-924` |
| `IEC62366-RR-054` | `SRC-008#Abschnitt 5.7.3/a` | H | REG | `NEW_UNIQUE_RR` | `RR-925` |
| `IEC62366-RR-055` | `SRC-008#Abschnitt 5.7.3/b` | H | REG | `NEW_UNIQUE_RR` | `RR-926` |
| `IEC62366-RR-056` | `SRC-008#Abschnitt 5.7.3/c` | H | Sicherheitsinformationen einschlägig | `NEW_UNIQUE_RR` | `RR-927` |
| `IEC62366-RR-057` | `SRC-008#Abschnitt 5.7.3/d` | H | REG | `NEW_UNIQUE_RR` | `RR-928` |
| `IEC62366-RR-058` | `SRC-008#Abschnitt 5.7.3/d` | H | REG | `NEW_UNIQUE_RR` | `RR-929` |
| `IEC62366-RR-059` | `SRC-008#Abschnitt 5.7.3/e` | H | Usability Test | `NEW_UNIQUE_RR` | `RR-930` |
| `IEC62366-RR-060` | `SRC-008#Abschnitt 5.7.3/e` | H | Usability Test | `NEW_UNIQUE_RR` | `RR-931` |
| `IEC62366-RR-061` | `SRC-008#Abschnitt 5.7.3/e` | H | Usability Test | `NEW_UNIQUE_RR` | `RR-932` |
| `IEC62366-RR-062` | `SRC-008#Abschnitt 5.7.3/e` | H | Usability Test | `NEW_UNIQUE_RR` | `RR-933` |
| `IEC62366-RR-063` | `SRC-008#Abschnitt 5.7.3/e` | H | Usability Test | `NEW_UNIQUE_RR` | `RR-934` |
| `IEC62366-RR-064` | `SRC-008#Abschnitt 5.8` | H | REG | `NEW_UNIQUE_RR` | `RR-935` |
| `IEC62366-RR-065` | `SRC-008#Abschnitt 5.8` | H | REG | `NEW_UNIQUE_RR` | `RR-936` |
| `IEC62366-RR-066` | `SRC-008#Abschnitt 5.8` | H | REG | `NEW_UNIQUE_RR` | `RR-937` |
| `IEC62366-RR-067` | `SRC-008#Abschnitt 5.8` | H | formative Evaluation durchgeführt | `NEW_UNIQUE_RR` | `RR-938` |
| `IEC62366-RR-068` | `SRC-008#Abschnitt 5.8` | H | neuer Befund | `NEW_UNIQUE_RR` | `RR-939` |
| `IEC62366-RR-069` | `SRC-008#Abschnitt 5.8` | H | Training für sicheren Gebrauch erforderlich | `NEW_UNIQUE_RR` | `RR-940` |
| `IEC62366-RR-070` | `SRC-008#Abschnitt 5.8` | H | wie 069 | `NEW_UNIQUE_RR` | `RR-941` |
| `IEC62366-RR-071` | `SRC-008#Abschnitt 5.9` | H | REG | `NEW_UNIQUE_RR` | `RR-942` |
| `IEC62366-RR-072` | `SRC-008#Abschnitt 5.9` | H | Fremd-/Vergleichsdaten genutzt | `NEW_UNIQUE_RR` | `RR-943` |
| `IEC62366-RR-073` | `SRC-008#Abschnitt 5.9` | H | REG | `NEW_UNIQUE_RR` | `RR-944` |
| `IEC62366-RR-074` | `SRC-008#Abschnitt 5.9` | H | REG | `NEW_UNIQUE_RR` | `RR-945` |
| `IEC62366-RR-075` | `SRC-008#Abschnitt 5.9` | H | REG | `NEW_UNIQUE_RR` | `RR-946` |
| `IEC62366-RR-076` | `SRC-008#Abschnitt 5.9` | H | entsprechender sicherheitsrelevanter Befund | `NEW_UNIQUE_RR` | `RR-947` |
| `IEC62366-RR-077` | `SRC-008#Abschnitt 5.9` | H | neuer Befund | `NEW_UNIQUE_RR` | `RR-948` |
| `IEC62366-RR-078` | `SRC-008#Abschnitt 5.9` | H | keine neuen Befunde im vorgenannten Zweig | `NEW_UNIQUE_RR` | `RR-949` |
| `IEC62366-RR-079` | `SRC-008#Abschnitt 5.9` | H | Verbesserung erforderlich/praktikabel | `NEW_UNIQUE_RR` | `RR-950` |
| `IEC62366-RR-080` | `SRC-008#Abschnitt 5.9` | H | entsprechender Zweig | `NEW_UNIQUE_RR` | `RR-951` |
| `IEC62366-RR-081` | `SRC-008#Abschnitt 5.9` | H | wie 080 | `NEW_UNIQUE_RR` | `RR-952` |
| `IEC62366-RR-082` | `SRC-008#Abschnitt 5.9` | H | wie 080 | `CROSS_NORM_MERGE (NORM-MERGE-05)` | `RR-382` |
| `IEC62366-RR-083` | `SRC-008#Anhang C/C.2.1` | H | UOUP | `NEW_UNIQUE_RR` | `RR-953` |
| `IEC62366-RR-084` | `SRC-008#Anhang C/C.2.2` | H | UOUP | `NEW_UNIQUE_RR` | `RR-954` |
| `IEC62366-RR-085` | `SRC-008#Anhang C/C.2.2` | H | UOUP; entsprechender Befund | `NEW_UNIQUE_RR` | `RR-955` |
| `IEC62366-RR-086` | `SRC-008#Anhang C/C.2.3` | H | UOUP | `NEW_UNIQUE_RR` | `RR-956` |
| `IEC62366-RR-087` | `SRC-008#Anhang C/C.2.3` | H | UOUP | `NEW_UNIQUE_RR` | `RR-957` |
| `IEC62366-RR-088` | `SRC-008#Anhang C/C.2.3` | H | UOUP | `NEW_UNIQUE_RR` | `RR-958` |
| `IEC62366-RR-089` | `SRC-008#Anhang C/C.2.4` | H | UOUP | `CROSS_NORM_MERGE (NORM-MERGE-03)` | `RR-380` |
| `IEC62366-RR-090` | `SRC-008#Anhang C/C.2.4` | H | UOUP | `NEW_UNIQUE_RR` | `RR-959` |
| `IEC62366-RR-091` | `SRC-008#Anhang C/C.2.4` | H | UOUP | `CROSS_NORM_MERGE (NORM-MERGE-04)` | `RR-381` |
| `IEC62366-RR-092` | `SRC-008#Anhang C/C.2.5` | H | UOUP | `CROSS_NORM_MERGE (NORM-MERGE-05)` | `RR-382` |
| `IEC62366-RR-093` | `SRC-008#Anhang C/C.2.5` | H | UOUP | `CROSS_NORM_MERGE (NORM-MERGE-06)` | `RR-383` |
---

## 12. Abschließender Cross-Source- und Coverage-Audit

Durchgeführt nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 13 Nr. 8 für `SRC-005` bis `SRC-008` gegen [RR_CATALOG.yaml](RR_CATALOG.yaml) 0.26, [RR_STANDARDS_MAPPING_SRC_005_008.yaml](RR_STANDARDS_MAPPING_SRC_005_008.yaml) 1.1 und [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) 0.4. Reine Konsistenzprüfung, keine erneute fachliche Adjudikation. Ergebnis: **PASS**.

| Prüfbereich | Prüfung | Ergebnis |
| --- | --- | --- |
| A Katalog | `RR-001` bis `RR-959` lückenlos und eindeutig; `RR-378` bis `RR-959` = 582; `RR-001` bis `RR-377` feldweise identisch mit dem Stand vor Block 3 (Commit `3baa54d`) | PASS |
| B Research-Mapping | 594 Temp-Kandidaten eindeutig erklärt; 1 `EXISTING_RR_SUPPORT`, 15 → 6 `CROSS_NORM_MERGE`, 576 `NEW_UNIQUE_RR`, 2 `CROSSWALK_ONLY`; jede neue `RR` genau einmal erzeugt, keine verwaiste Temp-ID, keine Temp-ID im Katalog; Requirement-unresolved 0 (`uncertainty` null, Status `aktiv`) | PASS |
| C Themes | 265 / 197 / 79 / 39 / 2 = 582 | PASS |
| D Quellenbeteiligung | `SRC-005` 209, `SRC-006` 105, `SRC-007` 184, `SRC-008` 92 | PASS |
| E Coverage | normativer Umfang und nicht extrahierte Bereiche dokumentiert (Abschnitt 2.2); normative Abhängigkeiten nur `SRC-007` → `SRC-006` und `SRC-008` → `SRC-006` sowie `SRC-007#Abschnitt 4.2` → `RR-594`; keine lizenzierte Normdatei und kein Handoff im Repository; keine Behauptung einer originalen IEC-CSV als Arbeitsquelle; `OPEN_SOURCE_PACKAGE_CHECK` für `SRC-005` erhalten | PASS |
| F Applicability | alle 582 `RR` zugeordnet (Normblöcke mit `MDR_MDSW`-Scope); jede adjudizierte Bedingung als Prädikat oder `local_not_modelled` erhalten, ISO-13485-Ausschlussregel bei allen 159 `RR` der Abschnitte 6 bis 8; `SCOPE_INACTIVE` als Demonstrator-Scope dokumentiert (Abschnitt 8.1); nicht operationalisierte Bedingungen fail-closed; Requirement-unresolved getrennt von Applicability-unresolved | PASS nach Korrektur (siehe unten) |
| G Traceability | jede neue `RR` mit genau einem Primary-Lokator; Merge-`RR` tragen alle Kandidatenlokatoren; `SOURCE_SUPPORT` und `NORMATIVE_DEPENDENCY` aufgelöst; `tools/traceability.py` ohne Befund | PASS |

**Audit-Befund und Korrektur:** Die adjudizierte Routing-Regel `SRC-007#Abschnitt 4.3/g` war in [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) 0.3 nicht abgebildet (noch nicht klassifizierte Software ergab `UNKNOWN`). Sie ist seit Version 0.4 in den Klassenprädikaten umgesetzt; Counts, Blöcke, Eingaben und Zuordnungen bleiben unverändert.

**Verbleibender Source-Package-Punkt:** ausschließlich `SRC-005` `OPEN_SOURCE_PACKAGE_CHECK` (Abschnitt 2.1). Er blockiert den `RR`-Arbeitsfreeze nicht, sondern nur den finalen Evidence-Freeze von `SRC-005`. Die fehlende originale IEC-CSV für `SRC-007` und `SRC-008` ist kein Requirement-Blocker; die verwendeten DIN-EN-Arbeitsfassungen sind in Abschnitt 2 und in [SOURCES.md](SOURCES.md) transparent dokumentiert.

---

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Integration der adjudizierten Normkandidaten aus `SRC-005` bis `SRC-008` (594 Kandidaten → 582 neue `RR`, `RR-378` bis `RR-959`); Quellen- und Provenienzangaben, Deduplizierungsarithmetik, ID-Vergabe, Katalogintegration, Applicability-Modellierung, Traceability und vollständige Temp-ID-Zuordnung. Kein Normvolltext im Repository. |
| 1.1 | Abschnitt 6.1: 15 kontextabhängige Paraphrasen redaktionell präzisiert (`RR_CATALOG.yaml` 0.26). Abschnitt 2.1 um Provenienzhinweis `SRC-006`, neuer Abschnitt 2.2 (geprüfter Normumfang und nicht extrahierte Bereiche). Abschnitt 8.5: Regel 4.3/g abgebildet. Abschnitt 12: abschließender Cross-Source- und Coverage-Audit PASS; Änderungshistorie wird Abschnitt 13. |
