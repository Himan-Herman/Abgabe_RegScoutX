# Fallstudie: KI-gestützter Symptomchecker

Version 1.0 · Status: eingefroren (Phase A, vor dem Evaluationslauf) · Stand: 28.09.2026

Diese Fallstudie ist das Hauptfallbeispiel der Evaluation (Block 6). Sie beruht auf dem manuell adjudizierten Referenzfall **TC-036** ([TC_CATALOG.yaml](../07-testing/TC_CATALOG.yaml), Herleitung [EV-003](../09-evidence/EV-003_GOLDEN_REFERENCE_DERIVATION.md)), wie ihn das Exposé vorsieht ([EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md)). Die Fallstudie ist ein **konstruierter Evaluationsfall** und beschreibt kein reales Produkt. Sie trifft keine regulatorische Aussage über reale Produkte; die Einordnung ergibt sich ausschließlich aus dem eingefrorenen Regelmodell (Katalogstände siehe [EVALUATION_METHOD.md](EVALUATION_METHOD.md) Abschnitt 1).

---

## 1. Kurzbeschreibung

Eine eigenständige Software, die Laien anhand eingegebener Beschwerden Hinweise auf mögliche Ursachen und auf die Dringlichkeit einer ärztlichen Abklärung gibt. Die Hinweise werden von einem Modell des maschinellen Lernens erzeugt. Das Produkt wird vom Hersteller unter eigenem Namen in der EU in Verkehr gebracht.

## 2. Annahmen

Jede Eigenschaft ist entweder eine **Profilangabe** (unverändert aus TC-036, geht in die regelbasierte Auswertung ein) oder eine **beschreibende Annahme** (nur zur Einordnung der Fallstudie, ohne Einfluss auf die Auswertung, weil das Regelmodell sie nicht abfragt). Weitere Eigenschaften werden nicht unterstellt.

| Nr. | Merkmal | Annahme | Art | Profilschlüssel (Wert) |
| --- | --- | --- | --- | --- |
| A-01 | Zweckbestimmung (Intended Purpose) | Software zur Unterstützung von Laien bei der Einschätzung eingegebener Beschwerden: Hinweise auf mögliche Ursachen und Dringlichkeit einer ärztlichen Abklärung; keine Therapieempfehlung | beschreibend; teilweise abgebildet | `own_medical_purpose` (ja), `provides_information_for_diagnostic_or_therapeutic_decisions` (ja) |
| A-02 | Zielnutzer | Laien (Patientinnen und Patienten selbst) | Profil | `lay_use` (ja) |
| A-03 | Patientengruppe | Erwachsene mit akuten Beschwerden, die nicht als Notfall erkennbar sind | beschreibend | — |
| A-04 | Einsatzumgebung | häusliche Umgebung, Nutzung auf eigenem Endgerät | beschreibend | — |
| A-05 | Grundlegende Funktionsweise | Software verarbeitet Eingabedaten über reine Speicherung/Übermittlung hinaus zum Nutzen einzelner Personen; keine Steuerung oder Beeinflussung eines Hardware-Medizinprodukts; kein Zubehör, kein Anhang-XVI-Produkt | Profil | `is_software` (ja), `data_action_type` (`BEYOND_BASIC`), `individual_patient_benefit` (ja), `special_route` (`NONE`), `drives_or_influences_device` (`NONE`) |
| A-06 | KI-Funktion | Modell des maschinellen Lernens erzeugt die Hinweise; das System erfüllt die Definition eines KI-Systems | Profil; Modellart beschreibend | `ai_system_status` (`YES`) |
| A-07 | MDR-Produktstatus | Medizinproduktesoftware im Anwendungsbereich der MDR; keine IVD-Informationszwecke | Profil | `ivdr_information_purpose` (nein) |
| A-08 | Klassifikationsannahmen | Entscheidungen auf Grundlage der Informationen können weder Tod bzw. irreversible Verschlechterung noch schwerwiegende Verschlechterung bzw. chirurgischen Eingriff verursachen; keine Kontrazeption/STI, keine aktive Therapie mit Diagnosefunktion, keine Steuerung von Stoffabgabe, keine weiteren nicht abgefragten Regeln | Profil | `decision_impact_death_or_irreversible_deterioration` (nein), `decision_impact_serious_deterioration_or_surgery` (nein), `used_for_contraception_or_sti_prevention` (nein), `therapeutic_with_integrated_diagnostic_function` (nein), `drives_substance_administration_or_removal_device` (nein), `further_unmodelled_rule_possibly_applicable` (nein) |
| A-09 | AI-Act-Kontext | Anknüpfung über den Produkthersteller; keine Art.-2-Ausnahme; das KI-System ist selbst das MDR-Produkt; Dritt-Konformitätsbewertung erforderlich, nicht nur wegen anderer als Gesundheits- und Sicherheitsrisiken; kein Anhang-III-Anwendungsfall | Profil | `scope_nexus` (`PRODUCT_MANUFACTURER`), `scope_exclusion` (`NONE`), `annex_i_product_relation` (`AI_SYSTEM_IS_PRODUCT`), `third_party_ca_required` (`YES`), `third_party_ca_only_non_health_safety` (`NO`), `annex_iii_use_case` (`NONE`) |
| A-10 | Bewertungs- und Inverkehrbringensdatum | hypothetisches Szenario am 01.09.2028 (nach dem Stichtag für Art.-6(1)-Systeme); gewählt, damit die Hochrisiko-Pflichten im Modell wirksam sind | Profil (Szenarioannahme) | `assessment_date` (2028-09-01), `market_or_service_date` (2028-09-01) |
| A-11 | IEC-62304-Profil | Software-Sicherheitsklasse B; reguläre Lebenszyklusprozesse; SOUP enthalten; keine Softwareänderung und kein Problembericht zum Bewertungszeitpunkt | Profil | `software_safety_class` (`B`), `iec62304_route` (`REGULAR_LIFECYCLE`), `soup_used` (ja), `software_change` (nein), `software_problem_reported` (nein) |
| A-12 | IEC-62366-1-Route | reguläre Route; Usability-Test vorgesehen; kein Training für den sicheren Gebrauch erforderlich; Sicherheitsinformation als Risikobeherrschungsmaßnahme | Profil | `iec62366_ui_route` (`REGULAR_ROUTE`), `usability_test_planned` (ja), `training_required_for_safe_use` (nein), `safety_information_as_risk_control` (ja) |
| A-13 | ISO-13485-/ISO-14971-Profil | keine Ausschlüsse nach ISO 13485 Abschnitt 1; Software im QMS eingesetzt; keine Auslagerung; Beschaffung findet statt; Risikomanagement nach ISO 14971 ohne weitere Profileingaben | Profil | `iso13485_clause1_exclusion_claimed` (nein), `qms_software_used` (ja), `outsourced_processes` (nein), `purchasing_performed` (ja) |
| A-14 | eIFU und weitere MDR-Bedingungen | keine elektronische Gebrauchsanweisung; kein Prüfprodukt, keine Sonderanfertigung, nicht implantierbar | Profil | `eifu_provision` (`NO_EIFU`), `investigational_device` (nein), `custom_made_device` (nein), `implantable_device` (nein) |
| A-15 | Bewusst offene Angaben | nicht festgelegt (wie im adjudizierten Referenzfall): Website des Herstellers, eingebautes Anzeigesystem, eIFU auf Speichermedium, Verfallsdatum, Symbol-/Farbverwendung, harmonisierte Norm bzw. GS für Symbole, Restrisiko, Kalibrierung, Ergebnisinterpretation durch Nutzer, Software in Produktion/Dienstleistung, Software zur Überwachung/Messung, Kundeneigentum | Profil (fehlend) | `manufacturer_has_website`, `built_in_display`, `eifu_on_storage_medium`, `specific_expiry_date`, `symbol_or_colour_used`, `harmonised_standard_or_cs_for_symbols`, `residual_risk_present`, `calibration_required`, `result_interpretation_by_user`, `production_service_software_used`, `monitoring_measurement_software_used`, `customer_property_provided` |
| A-16 | Erfüllungs- und Nachweissituation | bewusst gemischt (Abschnitt 4); ausschließlich strukturierte Erfüllungsangaben und Nachweisreferenzen, keine Ableitung aus Freitext; Nachweisdokumente sind fiktive Kennungen | Szenario | [REFERENCE_ASSESSMENT.yaml](REFERENCE_ASSESSMENT.yaml) `scenario` |

Die offenen Angaben (A-15) sind nicht künstlich erzeugt, sondern übernehmen den Stand des adjudizierten Referenzfalls. Sie führen zu fachlich ungeklärter Anwendbarkeit einzelner Anforderungen und damit zu dem für die Evaluation vorgesehenen `APPLICABILITY_UNRESOLVED`-Fall.

## 3. Erwartete Einordnung nach dem eingefrorenen Regelmodell

Aus TC-036 (manuell adjudiziert, EV-003): Qualifikation `MDSW`; Abgrenzung `MDR_MDSW`; MDR-Klasse IIa über den Pfad der Regel 11 (RUL-010 bis RUL-012, strengster Kandidat IIa); AI Act `AI_ACT_HIGH_RISK` über Art. 6 Abs. 1, anwendbar ab 02.08.2028. Aktive Bereiche: AI-Act-Hochrisiko, MDR-MDSW-Kern, Laienanwendung, Art. 86 (IIa, außerhalb Abs. 2), die vier Normbereiche; inaktiv: eIFU-Bereiche, Art. 85, Art. 86 IIb/III und Abs. 2.

Referenzstatus aller 959 Anforderungen: 542 `APPLICABLE`, 128 `NOT_APPLICABLE`, 289 `APPLICABILITY_UNRESOLVED` ([REFERENCE_ASSESSMENT.yaml](REFERENCE_ASSESSMENT.yaml), Herleitung in [EVALUATION_METHOD.md](EVALUATION_METHOD.md) Abschnitt 2).

## 4. Erfüllungs- und Nachweisszenario

Vor dem Systemlauf festgelegt, strukturiert und ohne Freitextauswertung (Auswahlregel in EVALUATION_METHOD.md Abschnitt 3):

| Szenarioangabe | Anzahl RR | erwarteter Gap-Status |
| --- | --- | --- |
| erfüllt mit Nachweisreferenz | 4 | `FULFILLED` |
| teilweise erfüllt mit Nachweisreferenz | 4 | `PARTIALLY_FULFILLED` |
| nicht erfüllt | 4 | `NOT_FULFILLED` |
| erfüllt bzw. teilweise erfüllt ohne Nachweisreferenz | 4 + 3 | `EVIDENCE_REVIEW_REQUIRED` |
| ausdrücklich nicht bewertet | 3 | `NOT_ASSESSED` |
| ohne Erfüllungsangabe (repräsentative Menge B) | 7 | `NOT_ASSESSED` |
| Erfüllungsangabe an ungeklärter RR | 2 | `APPLICABILITY_UNRESOLVED` |
| Erfüllungsangabe an nicht anwendbarer RR | 1 | `NOT_APPLICABLE` |

Die Anzahlen gelten für die 32 RR des Gap-Referenz-Umfangs (Einzelwerte je RR in REFERENCE_ASSESSMENT.yaml `gap_scope`). Die Nachweisreferenzen verweisen auf fiktive Dokumentkennungen (`CS-DOC-RR-…`); RegScoutX bewertet ihren Inhalt nicht.

## 5. Grenzen der Fallstudie

Einzelner konstruierter Fall; beschreibende Annahmen (A-01, A-03, A-04, Modellart in A-06) haben keinen Einfluss auf das Ergebnis und werden nicht evaluiert; die Datumsangaben sind ein hypothetisches Zukunftsszenario; die Fallstudie ersetzt keine Einzelfallprüfung.

## 6. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung vor dem Evaluationslauf (Phase A, Referenz-Freeze). |
