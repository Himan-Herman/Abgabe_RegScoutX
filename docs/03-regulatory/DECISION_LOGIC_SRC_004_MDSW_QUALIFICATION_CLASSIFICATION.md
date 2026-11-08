# Entscheidungslogik-Nachweis — SRC-004 (MDCG 2019-11 Rev. 1): MDSW-Qualifikation, MDR/IVDR-Abgrenzung und Klassifikation

Version 1.1 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-004` — MDCG 2019-11 Rev. 1, Juni 2025 |
| Quellenrolle | Ebene B, nicht rechtsverbindliche Guidance; Qualification-, Classification- und `RUL`-Quelle (Coverage-Plan Abschnitte 4 und 9.7) |
| Primärrechtsanker | `SRC-001` (MDR, konsolidiert 19.07.2026); für die MDR/IVDR-Abgrenzung `SRC-010#Art.2/Nr.2` (IVDR, konsolidiert 10.01.2025) |
| Ergebnisartefakt | [RUL_CATALOG.yaml](RUL_CATALOG.yaml) Version 0.1 (`RUL-001` bis `RUL-026`) nach [RUL_METHOD.md](RUL_METHOD.md) Version 1.0 |
| Testfälle | [../07-testing/RUL_DECISION_TESTS_SRC_004.yaml](../07-testing/RUL_DECISION_TESTS_SRC_004.yaml) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.43; Bearbeitungsstatus bei Erstellung `in Prüfung`, `abgeschlossen` seit Abschnitt 10.34 |
| `RR`-Katalog | [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.24 — unverändert |

Grundlage ist die fachlich finale SRC-004-Research-Adjudikation. Entscheidungsbäume, Kandidaten, Ergebnisse und Testfälle sind daraus übernommen. Die temporären Kennungen `RQ-*` werden ausschließlich hier und in der Änderungshistorie des Katalogs referenziert; permanente IDs vergibt nur [RUL_CATALOG.yaml](RUL_CATALOG.yaml).

**Keine Guidance als bindendes Recht:** Jede Entscheidungsregel ist an einem Primärrechtsanker verankert. `SRC-004` liefert Interpretation und Entscheidungsstruktur, nie die alleinige rechtsverbindliche Grundlage.

**Lokatorprüfung:** Die verwendeten `SRC-001`-Lokatoren (Art. 1 Abs. 2, Art. 2 Nr. 1, 2 und 12, Anhang XVI, Anhang VIII Kapitel II Abschnitte 3.1, 3.2, 3.3 und 3.5, Kapitel III Abschnitte 6.3 bis 6.5, 7.2 und 7.9) und der `SRC-010`-Lokator wurden am 25.09.2026 gegen die konsolidierten EUR-Lex-Fassungen geprüft; die `SRC-004`-Abschnittsnummern gegen das Inhaltsverzeichnis der Guidance. Die Research-Adjudikation nannte für Module und Änderungen allgemein „Anhang VIII“; hierfür wurden die präzisen Abschnitte 3.1, 3.2 und 3.5 verwendet.

---

## 2. Source Verification und Guidance-Status

**PASS.**

| Merkmal | Befund |
| --- | --- |
| Dokument | `MDCG 2019-11 Rev.1` |
| Titel laut Dokument | Guidance on Qualification and Classification of Software in Regulation (EU) 2017/745 – MDR and Regulation (EU) 2017/746 – IVDR |
| Ursprungsfassung | Oktober 2019 |
| Revision | Rev. 1, Juni 2025; Veröffentlichung 17.06.2025 |
| Umfang | 36 PDF-Seiten |
| Herausgeber | Medical Device Coordination Group (MDCG) |
| Status | nicht rechtsverbindliche Guidance; kein Dokument der Europäischen Kommission, keine offizielle Kommissionsposition; verbindliche Auslegung obliegt dem EuGH |
| Aktualität | Rev. 1 / Juni 2025; auf der offiziellen MDCG-Liste ist keine spätere Revision ausgewiesen |

---

## 3. Qualifikationsbaum (Figure 1)

Figure 1 ist kein Klassifikationsbaum, sondern entscheidet zunächst, ob Software durch MDR/IVDR erfasst wird. Die eigentliche MDSW-Qualifikation beruht auf dem eigenen medizinischen Zweck.

| Schritt | Entscheidungsfrage | Folge | `RUL` |
| --- | --- | --- | --- |
| Step 1 | Ist das Produkt Software im Sinne der Guidance? | JA → Step 2; NEIN → `NOT_COVERED_BY_SRC004` („nicht Software“ bedeutet nicht automatisch „nicht MDR“) | `RUL-001` |
| Step 2 | Anhang-XVI-Produkt, Zubehör oder Software, die ein Medizinprodukt steuert/beeinflusst? | JA → `MEDICAL_DEVICES_REGULATION_SPECIAL_ROUTE`; NEIN → Step 3 | `RUL-002` |
| Step 3 | Datenaktion über Speicherung, Archivierung, Kommunikation, einfache Suche oder verlustfreie Kompression hinaus? | JA → Step 4; NEIN → `NOT_MDSW` | `RUL-003` |
| Step 4 | Zum Nutzen individueller Patientinnen und Patienten? | JA → Step 5; NEIN → `NOT_MDSW` | `RUL-004` |
| Step 5 | Eigener medizinischer Zweck nach der Zweckbestimmung? | JA → `MDSW`, weiter zur Abgrenzung; NEIN → `NOT_MDSW` | `RUL-005` |

Die Softwaredefinition der Guidance (Instruktionssatz, der Eingabedaten verarbeitet und Ausgabedaten erzeugt) ist **Guidance-Interpretation**, keine eigenständige MDR-Definition.

**Medizinischer Zweck:** Maßgeblich sind die medizinischen Zwecke nach `SRC-001#Art.2/Nr.1` auf Grundlage der Zweckbestimmung nach `SRC-001#Art.2/Nr.12`. Die Nutzerfrage fragt nicht „Ist Ihre Software MDSW?“ oder „Wird die Software im Krankenhaus eingesetzt?“, sondern: „Soll die Software selbst einen der in der MDR genannten medizinischen Zwecke erfüllen – z. B. Diagnose, Vorhersage, Überwachung oder Behandlung einer Krankheit?“

**Step-3-Präzisierung:** „Einfache Suche“ wird nicht anhand der verwendeten Technologie bewertet. Eine Suchfunktion, die zur Erreichung eines medizinischen Zwecks beiträgt, ist gerade keine einfache Suche; Speicherung, Kommunikation oder kosmetische Darstellungsänderungen allein reichen nicht. Operationalisiert wird deshalb nicht `uses_NLP = MDSW`, sondern die Funktion der Datenverarbeitung (`RUL-003`, Wert `BEYOND_BASIC`).

---

## 4. MDR/IVDR-Abgrenzung (Figure 2)

Der Abgrenzungsbaum beginnt erst nach festgestellter MDSW.

| Schritt | Entscheidungsfrage | Folge | `RUL` |
| --- | --- | --- | --- |
| D1 | Liefert die MDSW Information im Sinne der IVD-Definition (sechs Kategorien aus IVDR Art. 2 Nr. 2)? | NEIN → `MDR_MDSW`; JA → D2 | `RUL-006` |
| D2 | Beruht die Information ausschließlich auf Daten aus In-vitro-Diagnostika? | JA → `OUT_OF_SCOPE_IVDR`; NEIN → D3 | `RUL-007` |
| D3 | Welche Datenquelle trägt die Zweckbestimmung wesentlich? | `IVD_DOMINANT` → `OUT_OF_SCOPE_IVDR`; `MDR_DOMINANT` → `MDR_MDSW`; `UNCLEAR` → `BOUNDARY_REVIEW_REQUIRED` | `RUL-008` |

Die sechs Kategorien der IVD-Definition: physiologische oder pathologische Prozesse oder Zustände; kongenitale körperliche oder geistige Beeinträchtigungen; Prädisposition für einen Gesundheitszustand oder eine Krankheit; Unbedenklichkeit und Verträglichkeit bei potenziellen Empfängern; voraussichtliche Wirkung einer Behandlung oder Reaktionen darauf; Festlegung oder Überwachung therapeutischer Maßnahmen.

Bei gemischten Daten verlangt `SRC-004` eine **qualitative** Gewichtung der Datenquellen nach ihrem Beitrag zur Zweckbestimmung. Die Guidance gibt bewusst **keinen numerischen Schwellenwert** vor; RegScoutX erfindet keinen. Ist die Gewichtung nicht belastbar möglich, entscheidet die Regel nicht automatisch.

Software, die ausschließlich ein Hardwareprodukt steuert oder beeinflusst, folgt grundsätzlich dem Regulierungsregime des gesteuerten bzw. beeinflussten Produkts (Sonderroute, `RUL-002`).

---

## 5. MDR-Klassifikation

### 5.1 Allgemeine Logik

Nach `MDR_MDSW`:

1. Zweckbestimmung bestimmen.
2. Sämtliche anwendbaren MDR-Durchführungsvorschriften berücksichtigen.
3. Gegebenenfalls Abschnitt 3.3 für steuernde/beeinflussende Software anwenden (`RUL-009`).
4. Regel 11 prüfen (`RUL-010` bis `RUL-015`).
5. Andere einschlägige Regeln prüfen (`RUL-016` bis `RUL-019`).
6. Nach Anhang VIII Abschnitt 3.5 die strengste anwendbare Regel/Unterregel verwenden (`RUL-020`).

**Korrektur aus der Research-Adjudikation:** Eine „Regel 1.9 / höchste anwendbare Klasse“ gehört nicht zur MDR-Logik; Regel 1.9 behandelt `SRC-004` im IVDR-Klassifikationsabschnitt. Für die MDR ist Anhang VIII Kapitel II Abschnitt 3.5 maßgeblich.

`MDR_FINAL_CLASS` = höchste Klasse aus allen aufgrund der Zweckbestimmung anwendbaren MDR-Regeln/Unterregeln — **nicht** „Ergebnis von Regel 11 = automatisch finale Klasse“.

### 5.2 Implementing Rule 3.3

| Fall | Behandlung | Basis |
| --- | --- | --- |
| Nur Steuern/Beeinflussen, kein eigener medizinischer Zweck | Software fällt in dieselbe Klasse wie das gesteuerte bzw. beeinflusste Produkt | `SRC-001#Anh.VIII/Kap.II/Abschn.3.3/Satz.1` |
| Eigener medizinischer Zweck und zusätzlich Steuern/Beeinflussen | Klassifizierung nach eigener Zweckbestimmung; die resultierende Klasse soll nach der Guidance nicht niedriger als die Hardwareklasse sein | `SRC-001#Anh.VIII/Kap.II/Abschn.3.3/Satz.2` + Guidance-Auslegung |

Die Operationalisierung `max(Klasse aus eigener Zweckbestimmung, Klasse des gesteuerten Produkts)` ist **`GUIDANCE_INTERPRETATION`**, kein wörtlicher Primärrechtstext. Da die Hardwareklasse im horizontalen Kernbaum nicht modelliert ist, führen beide Fälle zu `ADDITIONAL_CLASSIFICATION_REVIEW_REQUIRED` statt zu einer scheinbar endgültigen Klasse.

### 5.3 Implementing Rule 3.5

Wenn unter Berücksichtigung der Zweckbestimmung mehrere Regeln oder innerhalb derselben Regel mehrere Unterregeln anwendbar sind, gilt die strengste, sodass das Produkt in die jeweils höchste Klasse eingestuft wird. Klassenkandidaten überschreiben sich nicht gegenseitig; die Aggregation erfolgt ausschließlich in `RUL-020`.

### 5.4 Regel 11a/b/c

Primärrecht: `SRC-001#Anh.VIII/Kap.III/Abschn.6.3/Regel.11` (Unterabsätze 1 bis 3). `SRC-004` teilt Regel 11 in 11a, 11b und 11c.

| Unterregel | Frage | Ergebnis (Kandidat) | `RUL` |
| --- | --- | --- | --- |
| 11a | Informationen für Entscheidungen zu diagnostischen oder therapeutischen Zwecken? | JA → Schweregrad; NEIN → 11b | `RUL-010` |
| 11a | Tod oder irreversible Verschlechterung möglich? | JA → III; NEIN → nächste Stufe | `RUL-011` |
| 11a | Schwerwiegende Verschlechterung oder chirurgischer Eingriff möglich? | JA → IIb; NEIN → IIa | `RUL-012` |
| 11b | Ausschließlich Überwachung physiologischer Prozesse? | JA → Vitalparameter; NEIN → 11c | `RUL-013` |
| 11b | Vitale Parameter, deren Änderung zu unmittelbarer Gefahr führen kann? | JA → IIb; NEIN → IIa | `RUL-014` |
| 11c | Weder 11a noch 11b | I | `RUL-015` |

`SRC-004` konkretisiert die 11a-Eskalation über die Bedeutung der Information und die möglichen Auswirkungen einer auf fehlerhafter Information beruhenden Entscheidung. Monitoring-MDSW liefert häufig Informationen für diagnostische oder therapeutische Entscheidungen und fällt dann bereits unter 11a; 11b ist insbesondere für Software relevant, die nur Monitoringzwecke verfolgt. Die Beispiele vitaler Prozesse (u. a. Atmung, Herzfrequenz, Hirnfunktionen, Blutgase, Blutdruck, Körpertemperatur) sind keine abschließende Positivliste. Das Ergebnis von 11c bleibt ein Klassenkandidat, bis die übrigen Regeln und Abschnitt 3.5 geprüft sind.

### 5.5 Regeln 12, 13, 15 und 22

| Regel | Wann relevant für MDSW | Behandlung | Verhältnis zu Regel 11 | `RUL` |
| --- | --- | --- | --- | --- |
| Regel 12 | Software selbst kann keine Stoffe physisch abgeben oder entfernen; relevant, wenn sie ein entsprechendes Hardwareprodukt steuert oder beeinflusst | Hardware nach Regel 12, Software über Abschnitt 3.3; Review-Ausgang | keine künstliche Regel-12-Klasse für unabhängige Software | `RUL-018` |
| Regel 13 | Auffangregel für sonstige aktive Produkte, wenn keine andere Regel greift | Klasse I | regelmäßig keine Verschärfung gegenüber 11c | `RUL-019` |
| Regel 15 | Software zur Empfängnisverhütung bzw. Verhinderung der Übertragung sexuell übertragbarer Krankheiten | Klasse IIb | kann 11c verdrängen; Abschnitt 3.5 → strengste Klasse | `RUL-016` |
| Regel 22 | aktives therapeutisches Produkt mit integrierter diagnostischer Funktion, die das Patientenmanagement erheblich bestimmt, insbesondere Closed Loop | Klasse III | kann das Regel-11-Ergebnis übersteuern | `RUL-017` |

### 5.6 Regeln 9 und 10

`SRC-004` weist darauf hin, dass für aktive Produkte die Regeln 9, 10, 11, 12, 13, 15 und 22 zu berücksichtigen sein können. Regeln 9 und 10 werden für RegScoutX **nicht** als eigener horizontaler Software-Kernbaum modelliert; bei Hardware- oder Kombinationsprodukten dürfen sie aber nicht ignoriert werden. `RUL-020` fragt deshalb ausdrücklich nach möglicherweise anwendbaren, nicht modellierten Regeln und gibt in diesem Fall `ADDITIONAL_CLASSIFICATION_REVIEW_REQUIRED` mit dokumentierter Ursache aus.

---

## 6. Module

| Schritt | Regel | Ergebnis | `RUL` |
| --- | --- | --- | --- |
| M1 | Besitzt das Modul einen eigenen medizinischen Zweck? | JA → `MDSW_MODULE` (eigenständige Qualifikation und risikobasierte Klassifikation); NEIN → M2 | `RUL-021` |
| M2 | Ist die nicht-medizinische Funktion für den Betrieb der MDSW erforderlich oder kann sie Sicherheit bzw. Leistung beeinflussen? | JA → `NON_MEDICAL_BUT_ASSESSMENT_RELEVANT`; NEIN → `NON_MEDICAL_MODULE_NOT_REGULATED_AS_MDSW` | `RUL-022` |
| M4 | Werden die medizinischen Module gemeinsam als ein integriertes Produkt in Verkehr gebracht? | JA → Zweckbestimmung, Gesamtarchitektur und alle anwendbaren Regeln zusätzlich auf das Gesamtprodukt; NEIN → Klassifizierung nach eigener Zweckbestimmung je Modul | `RUL-023` |

Ein bewertungsrelevantes nicht-medizinisches Modul wird **nicht automatisch MDSW**, ist aber in Beschreibung, Architektur-, Schnittstellen-, Sicherheits-/Leistungs- und Interdependenzbewertung zu berücksichtigen. Bei modularer MDSW müssen insbesondere Produkt- und Modulgrenzen, Schnittstellen, regulatorischer Status der Module, Eingangsdatenwege, Darstellung der Ausgaben, Interdependenzen und Auswirkungen nicht-medizinischer Funktionen auf Sicherheit und Leistung eindeutig bestimmbar sein (M3; dokumentarische Bewertungspflicht, keine eigene `RUL`).

`SRC-004` enthält **keine allgemeine Regel** „Gesamtsoftwareklasse = höchste Modulklasse“. Wird ein integriertes Gesamtprodukt als ein Medizinprodukt in Verkehr gebracht, sind Zweckbestimmung des Gesamtprodukts, anwendbare Regeln und Abschnitt 3.5 maßgeblich.

Die Research-Adjudikation verwendet für M2 in zwei Abschnitten unterschiedliche Ausgabebezeichnungen (`NON_MEDICAL_BUT_ASSESSMENT_RELEVANT` bzw. `ASSESSMENT_RELEVANT_NON_MEDICAL_FUNCTION`) für denselben Ausgang. Der Katalog führt einheitlich `NON_MEDICAL_BUT_ASSESSMENT_RELEVANT` aus der finalen Modullogik.

---

## 7. Change Reassessment

`SRC-004` Abschnitt 8 verlangt eine erneute Bewertung der Auswirkungen von Änderungen auf **Qualifikation und Klassifikation**.

```text
IF change affects
    function
 OR intended_purpose
 OR essential_design
 OR manufacturing_characteristics           → RUL-024
 OR functionality_added_or_modified
 OR module_added_or_modified                → RUL-025
 OR medical_device_combination_changed      → RUL-026
THEN
    REASSESS_QUALIFICATION_CLASSIFICATION
    rerun qualification tree
    rerun MDR/IVDR boundary if relevant
    rerun classification
ELSE
    NO_SRC004_REASSESSMENT_TRIGGER
```

`REASSESS_QUALIFICATION_CLASSIFICATION` bedeutet: erneute Prüfung erforderlich — **nicht** automatische Änderung von Qualifikation oder Klasse. Die wesentliche Änderung (`substantial modification`) nach dem AI Act bleibt davon vollständig getrennt; aus `SRC-004` wird keine AI-Act-Definition abgeleitet.

---

## 8. Zuordnung der temporären Kandidaten

| Research-Kandidat | `RUL` | Kategorie |
| --- | --- | --- |
| `RQ-Q01` bis `RQ-Q05` | `RUL-001` bis `RUL-005` | `QUALIFICATION` |
| `RQ-Q06` bis `RQ-Q08` | `RUL-006` bis `RUL-008` | `BOUNDARY` |
| `RQ-C01` bis `RQ-C12` | `RUL-009` bis `RUL-020` | `CLASSIFICATION` |
| `RQ-M01` bis `RQ-M03` | `RUL-021` bis `RUL-023` | `MODULES` |
| `RQ-CH01` bis `RQ-CH03` | `RUL-024` bis `RUL-026` | `CHANGE_REASSESSMENT` |

26 Kandidaten, 26 `RUL`; keine zusätzliche Regel. Für `RQ-C03`/`RQ-C04` empfahl die Adjudikation ein kontrolliertes Feld statt freier Severity-Interpretation; umgesetzt als zwei kontrollierte Ja/Nein-Eingaben in `RUL-011` und `RUL-012`.

---

## 9. Guidance-Testfälle

Die 15 Testfälle stehen maschinenlesbar in [../07-testing/RUL_DECISION_TESTS_SRC_004.yaml](../07-testing/RUL_DECISION_TESTS_SRC_004.yaml) und werden durch `tools/test_validate_rul_catalog.py` entlang der Katalogzweige nachvollzogen. Die Guidance warnt ausdrücklich davor, ihre Beispiele als allgemeingültige Klassifikationsregeln zu verwenden; sie gelten nur für die jeweils beschriebene Zweckbestimmung und Nutzungssituation. Ein Beispiel validiert den Baum, ist aber keine Rechtsregel.

| Test | Fall | Erwartetes Ergebnis | Beispielfundstelle |
| --- | --- | --- | --- |
| T01 | Labor-Operations-Dashboard | `NOT_MDSW` | Annex II, Figure 1 – Example 1 |
| T02 | reine Telemedizin-Übertragung | `NOT_MDSW` | Annex I, d.1 |
| T03 | Telemedizin mit medizinischem Schwellenwertalarm | `MDSW` | Annex I, d.1 |
| T04 | gemischter ICU-Risikoscore | `MDR_MDSW` | Annex II, Figure 2 – Example 2 |
| T05 | Trisomie-Risikoscore | `OUT_OF_SCOPE_IVDR` | Annex II, Figure 2 – Example 3 |
| T06 | NGS-Krebsanalyse | `OUT_OF_SCOPE_IVDR` | Annex II, Figure 2 – Example 4 |
| T07 | Akut-Schlaganfall-Bilddiagnostik | Klasse III (11a) | Annex IV |
| T08 | Chemotherapie-Ranking BRCA-positiv | Klasse IIa (11a) | Annex IV |
| T09 | kontinuierliche Vitalüberwachung Anästhesie/Intensiv | Klasse IIb (11b) | Annex IV |
| T10 | Routine-/Home-Monitoring physiologischer Prozesse | Klasse IIa (11b) | Annex IV |
| T11 | Fertilitätsstatus zur Unterstützung der Empfängnis | Klasse I (11c) | Annex IV |
| T12 | Kommunikationshilfe bei Kommunikationsstörung | Klasse I (11c) | Annex IV |
| T13 | adaptive kognitive Therapie mit integriertem diagnostischem Feedback | Klasse III (Regel 22) | Annex IV |
| T14 | gleiche kognitive Software, Therapieentscheidung durch Spezialisten | Klasse IIa (11a) | Annex IV |
| T15 | modulares System: Administration und Radiotherapie-Dosisplanung | Administration nicht MDSW; Dosisplanung `MDSW_MODULE`; Schnittstellen dennoch bewerten | Abschnitt 7 |

Wo ein Beispiel einzelne Eingaben nicht festlegt (Negativantworten zu Regeln 12, 15 und 22 in T07 bis T14, Regel-11-Eingaben in T13, Bewertungsrelevanz des Administrationsmoduls in T15), ist dies in der Testdatei als Annahme gekennzeichnet bzw. wird für alle zulässigen Werte geprüft.

---

## 10. Primärrecht vs. Guidance

| Regelungsfrage | Primary Legal Basis | Rolle `SRC-004` |
| --- | --- | --- |
| Medizinprodukt einschließlich Software | `SRC-001#Art.2/Nr.1` | operationalisiert Qualifikation |
| Zweckbestimmung | `SRC-001#Art.2/Nr.12` | erläutert Bedeutung einer klaren Zweckbestimmung |
| Zubehör | `SRC-001#Art.2/Nr.2` | erläutert Software-Zubehör |
| Anhang-XVI-Route | `SRC-001#Art.1/Abs.2`, `SRC-001#Anh.XVI` | integriert in Figure 1 |
| Steuern/Beeinflussen | `SRC-001#Anh.VIII/Kap.II/Abschn.3.3/Satz.1` | erläutert Software-/Hardware-Konstellationen |
| unabhängige Softwareklassifizierung | `SRC-001#Anh.VIII/Kap.II/Abschn.3.3/Satz.2` | erläutert eigene Zweckbestimmung |
| höchste anwendbare Klasse | `SRC-001#Anh.VIII/Kap.II/Abschn.3.5` | bestätigt Anwendung mehrerer Regeln |
| Regel 11 | `SRC-001#Anh.VIII/Kap.III/Abschn.6.3/Regel.11` | zerlegt in 11a/b/c, Interpretation und Beispiele |
| Regeln 12, 13, 15, 22 | `SRC-001#Anh.VIII/Kap.III/Abschn.6.4/Regel.12`, `…/Abschn.6.5/Regel.13`, `…/Abschn.7.2/Regel.15`, `…/Abschn.7.9/Regel.22` | softwarebezogene Auslegung |
| MDR vs. IVDR | `SRC-001#Art.2/Nr.1` + `SRC-010#Art.2/Nr.2` | Figure 2 und qualitative Datenquellengewichtung |
| Module | `SRC-001#Art.2/Nr.1`, `SRC-001#Art.2/Nr.12`, `SRC-001#Anh.VIII/Kap.II/Abschn.3.1`, `…/Abschn.3.5` | detaillierte Guidance-Operationalisierung |
| Änderungen | `SRC-001#Art.2/Nr.1`, `SRC-001#Art.2/Nr.12`, `SRC-001#Anh.VIII/Kap.II/Abschn.3.1`, `…/Abschn.3.2/Satz.1` | definiert Reassessment-Auslöser |

Keine `RUL` stellt `MDCG 2019-11 Rev.1` als alleinige **rechtsverbindliche** Grundlage dar.

---

## 11. Verbindung zum `RR`-Katalog

Nur filterrelevante Beziehungen; eine Gap-Filter-`RUL` wird in Version 0.1 des Katalogs nicht angelegt.

**Qualifikation**

- `MDR_MDSW` → MDR-Gap-Korpus grundsätzlich freischalten; die lokalen `RR`-Trigger bleiben zusätzlich bestehen.
- `NOT_MDSW` → MDSW-spezifische MDR-Gap-Auswertung nicht aktivieren.
- `OUT_OF_SCOPE_IVDR` → für den derzeitigen RegScoutX-Scope keine MDR-Gap-Auswertung; Ausgabe mit Begründung „IVDR-Route“.
- `MEDICAL_DEVICES_REGULATION_SPECIAL_ROUTE` → nicht automatisch als eigenständige MDSW behandeln; dieser Pfad bleibt vom MDSW-Kernpfad getrennt.

**Klassifikation**

- Klasse I → Art.-85-Block `RR-353` bis `RR-359` aktivierbar.
- Klasse IIa, IIb oder III → Art.-86-Block `RR-360` bis `RR-377` aktivierbar. Innerhalb dieses Blocks bleiben die katalogisierten Klassen- und Untergruppenbedingungen maßgeblich: IIa bedarfsbezogene und mindestens zweijährliche Aktualisierung; IIb/III mindestens jährlich; III bzw. einschlägig implantierbar Art.-86-Abs.-2-Pfad; sonstige Art.-86-Produkte Art.-86-Abs.-3-Pfad.

Keine bestehende `RR` muss durch `SRC-004` geändert werden.

**Anschluss an den AI Act:** Nach abgeschlossener MDR-Qualifikation und -Klassifikation wird **separat** die aktuelle High-Risk-Logik aus `SRC-002` geprüft. `SRC-004` erzeugt keine AI-Act-Art.-6-Abs.-1-Regel; `SRC-003` kann später ausschließlich als Interplay-Evidenz dienen.

---

## 12. Neue `RR` aus `SRC-004`

**NEIN — 0 neue `RR`.** Normative `must`-/`shall`-Formulierungen innerhalb der Guidance werden nicht als neue Rechtsanforderungen behandelt. Wo sie MDR- oder IVDR-Recht erläutern, bleibt das jeweilige Primärrecht die normative Basis.

---

## 13. Unresolved und Source Dependencies

**Fachliche Unresolveds auf Quellenebene: 0.**

Explizit behandelt:

1. **Gemischte MDR-/IVDR-Daten:** `substantially driven` besitzt keinen quantitativen Guidance-Schwellenwert; `dominant_data_source = UNCLEAR` führt zu `BOUNDARY_REVIEW_REQUIRED`, nie zu automatischem Raten (`RUL-008`).
2. **IVDR als Primary-Law-Dependency:** SOURCE_DEPENDENCY: JA — ausschließlich für die MDR/IVDR-Abgrenzungslogik. Aufgelöst durch Registrierung von `SRC-010` mit dem einzigen aktiven Quellenbereich `SRC-010#Art.2/Nr.2` ([SOURCES.md](SOURCES.md) Version 1.5; Coverage-Plan Abschnitte 9.10 und 10.34). Keine IVDR-Gap-Extraktion.

Weitere von `SRC-004` genannte Dokumente (etwa MDCG 2021-24, MDCG 2023-4, IMDRF-Dokumente oder IVDR-Klassifikationsguidance) sind für den Kernbaum keine zwingenden Source Dependencies.

**Offene Punkte ohne Blockadewirkung:**

- Die Zitierweise von `SRC-004` (`SRC-004#Abschnitt <Nr.>`) bildet das nicht nummerierte Annex I nicht ab; die Testfälle T02/T03 nennen die Fundstelle deshalb beschreibend.
- Permanente `TC`-IDs für die Testfälle werden erst mit einer eigenen `TC`-Vergabestelle vergeben.

---

## 14. Auswirkungen auf spätere Artefakte

- **`RUL`:** `SRC-004` liefert die Guidance-Schicht für Qualification, MDR/IVDR-Boundary, Classification, Modules und Change Reassessment.
- **Gap-Logik:** Die `RUL` entscheiden vor dem Gap-Katalog insbesondere `MDR_MDSW`, `OUT_OF_SCOPE_IVDR`, `NOT_MDSW` und die MDR-Klasse.
- **Traceability:** Jede `RUL` trägt zwei getrennte Referenzebenen: Primary Legal Anchor und Guidance Interpretation.
- **UI-Fragen:** Fragen erheben regulatorisch konkrete Eingaben (medizinischer Zweck, Datenfunktion, Patientenspezifität, Entscheidungswirkung, physiologisches Monitoring, unmittelbare Gefahr, alternative Regeln), statt Nutzer nach „Regel 11“ oder „MDSW“ zu fragen.
- **Fallstudie:** Sollte mindestens die Pfade `NOT_MDSW`, `MDR_MDSW`, `OUT_OF_SCOPE_IVDR`, Regel-11-Klassen I/IIa/IIb/III sowie Regel 22 abdecken.

**Methodik:** [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) und [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) bleiben unverändert. Das formalisierte Entscheidungsregelmodell ist in [RUL_METHOD.md](RUL_METHOD.md) festgelegt.

---

## 15. Quellenfundstelle

| Bezug | URL |
| --- | --- |
| `SRC-004`, Fundstelle | https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en |
| `SRC-004`, Dokument | https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en |
| `SRC-001`, konsolidierte Fassung 19.07.2026 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02017R0745-20260719 |
| `SRC-010`, konsolidierte Fassung 10.01.2025 | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A02017R0746-20250110 |

---

## 16. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung des Entscheidungslogik-Nachweises zu `SRC-004`: Qualifikationsbaum (Figure 1), MDR/IVDR-Abgrenzung (Figure 2), MDR-Klassifikation mit Regel 11a/b/c, Regeln 12, 13, 15 und 22, Abschnitte 3.3 und 3.5, Hinweis auf Regeln 9/10, Module und Change Reassessment. 26 Kandidaten als `RUL-001` bis `RUL-026` übernommen; 15 Guidance-Testfälle; 0 neue `RR`; Source Dependency IVDR Art. 2 Nr. 2 über `SRC-010` verankert. |
| 1.1 | Ausschließlich redaktionell: Bearbeitungsstatus im Kopf auf den Abschluss nach COVERAGE_PLAN Abschnitt 10.34 fortgeschrieben. Keine inhaltliche Änderung. |
