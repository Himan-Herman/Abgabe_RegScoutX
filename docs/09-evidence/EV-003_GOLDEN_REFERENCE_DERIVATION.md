# EV-003 — Herleitung der Referenzfälle TC-036 bis TC-039

Version 1.0 · Status: aktiv · Datum: 27.09.2026

| Merkmal | Angabe |
| --- | --- |
| Evidenztyp | manuelle Referenzadjudikation (Review) |
| Bezug | TC-036, TC-037, TC-038, TC-039 ([TC_CATALOG.yaml](../07-testing/TC_CATALOG.yaml)) |
| Katalogstände | RR_CATALOG 0.26 · RUL_CATALOG 0.2 · RR_APPLICABILITY 0.4 · SR_CATALOG 0.3 · DATA_MODEL 0.4 · RR_MEASURE 0.1 |
| Grundlage | Regelzweige in [RUL_CATALOG.yaml](../03-regulatory/RUL_CATALOG.yaml), Aggregationsregel nach [RUL_METHOD.md](../03-regulatory/RUL_METHOD.md) Abschnitt 8.1, Blöcke/Prädikate/Zuordnungen in [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml), Auswertungssemantik nach [ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md) Abschnitt 8 |

Die Soll-Ergebnisse wurden **vor** dem ersten Lauf des Referenztests aus dem eingefrorenen Regel- und Zuordnungsstand hergeleitet und in `golden_case` des Testfallkatalogs eingetragen. Sie wurden nicht aus einem Laufzeitergebnis kopiert. Der anschließende automatisierte Abgleich (`tests/test_golden_cases.py`, dokumentiert in EV-001) ergab für alle vier Fälle Übereinstimmung; nach dem Lauf wurde kein Soll-Wert geändert.

**Referenzstruktur:** Vollständige Soll-Mengen über alle 959 `RR` nur dort, wo sie aus dem Scope zwingend folgen (TC-037, TC-039). Für TC-036 und TC-038 sind vollständig festgelegt: Regelpfade, Entscheidungsergebnisse, der Zustand aller 16 Applicability-Blöcke, die Summen scope-bedingt nicht anwendbarer bzw. ungeklärter `RR` und eine begründete Teilmenge entscheidungskritischer `RR`. Die übrigen lokal bedingten `RR` dieser Fälle sind **nicht** einzeln manuell adjudiziert; eine vollständige Einzelreferenz wird nicht behauptet.

---

## TC-036 — KI-Symptomchecker, MDR Klasse IIa, AI-Act-Hochrisiko

**Regelpfad RUL-001:** RUL-001 `is_software=true` → RUL-002 `special_route=NONE` → RUL-003 `BEYOND_BASIC` → RUL-004 `individual_patient_benefit=true` → RUL-005 `own_medical_purpose=true` (Ergebnis `MDSW`) → RUL-006 `ivdr_information_purpose=false` (Ergebnis `MDR_MDSW`) → RUL-009 `NONE` → RUL-010 `true` → RUL-011 `false` → RUL-012 `false` (Kandidat IIa) → RUL-016 `false` → RUL-017 `false` → RUL-018 `false` → RUL-019 (abgeleitet: Kandidat auf dem Pfad, daher `true`) → RUL-020 `false` (Ergebnis `FINAL_MDR_CLASS`). Strengster Kandidat: IIa.

**Regelpfad RUL-027:** RUL-027 `YES` → RUL-028 `PRODUCT_MANUFACTURER` → RUL-029 `NONE` → RUL-030 `AI_SYSTEM_IS_PRODUCT` → RUL-032 `YES` → RUL-033 `NO` → RUL-034 Bewertungsdatum 2028-09-01 ≥ 2028-08-02 → RUL-035 Inverkehrbringen 2028-09-01 ≥ 2028-08-02 (`ART6_1_HIGH_RISK`, anwendbar ab 2028-08-02) → RUL-038 `NONE` (`ART6_2_ROUTE_FALSE`) → RUL-043 (abgeleitet: erster zulässiger Wert der Vorrangfolge, der als `aggregates_to` auftritt: `AI_ACT_HIGH_RISK`), `applicable_from` 2028-08-02.

**Blöcke:** `MDR_MDSW` wahr. Aktiv: `AI_ACT_HIGH_RISK`, `MDR_MDSW_CORE`, `MDR_LAY_USE` (Laienanwendung), `MDR_ART86` (IIa ∈ IIa/IIb/III), `MDR_ART86_IIA`, `MDR_ART86_OUTSIDE_ABS2` (IIa/IIb und nicht implantierbar), vier Normblöcke. Inaktiv: `SRC009_*` (keine eIFU), `MDR_ART85` (nicht Klasse I), `MDR_ART86_IIB_III`, `MDR_ART86_ABS2` (weder III noch implantierbar). Scope-bedingt nicht anwendbar: 1 + 59 + 1 + 7 + 1 + 1 = **70**; ungeklärt: 0.

**Entscheidungskritische `RR`:** reguläre `RR` aktiver Blöcke `APPLICABLE`/`SCOPE_ACTIVE` (RR-116, RR-064, RR-384, RR-593; bedingte ohne lokale Prädikate RR-174, RR-360, RR-376); inaktive Blöcke `NOT_APPLICABLE`/`SCOPE_INACTIVE` (RR-353, RR-370, RR-240); nicht dokumentierte AI-Einordnung RR-001 `CONDITIONALITY_NOT_DOCUMENTED`; lokale Normbedingungen: RR-443 (keine Ausschlüsse), RR-403 (QMS-Software), RR-728 (Klasse B ∈ B/C, reguläre Route), RR-760 (zusätzlich SOUP), RR-889 (reguläre UE-Route), RR-930 (Usability-Test) erfüllt; RR-727 (nur C), RR-698 (Legacy), RR-954 (UOUP) nicht erfüllt; RR-378 (Merge) und RR-678 („soweit zutreffend“) `LOCAL_CONDITION_NOT_MODELLED`.

## TC-037 — Wellness-App ohne medizinische Zweckbestimmung und ohne KI

RUL-001 bis RUL-005 mit `own_medical_purpose=false` → `NOT_MDSW`; RUL-027 `NO` → `AI_ACT_NOT_APPLICABLE`. `MDR_MDSW` ist über `false_if QUALIFICATION NOT_MDSW` falsch; jeder MDR-, SRC-009- und Normblock enthält `MDR_MDSW` im Scope, die UND-Verknüpfung ist damit falsch. `AI_ACT_HIGH_RISK_SYSTEM` ist über `false_if AI_ACT_NOT_APPLICABLE` falsch. Folge: alle 16 Blöcke inaktiv, **alle 959 `RR` `NOT_APPLICABLE` mit `SCOPE_INACTIVE`** (kein `reason_code` an den `false_if`-Einträgen).

## TC-038 — MDSW Klasse I ohne KI, Legacy-Route, geänderte UOUP-Teile, ISO-13485-Ausschlüsse

**Regelpfad RUL-001:** bis RUL-006 wie TC-036 → RUL-009 `NONE` → RUL-010 `false` → RUL-013 `false` → RUL-015 (abgeleitet, einziger zulässiger Wert `true`: Kandidat I) → RUL-016 bis RUL-018 `false` → RUL-019 (abgeleitet `true`) → RUL-020 `false` → `FINAL_MDR_CLASS` I. RUL-027 `NO`.

**Blöcke:** aktiv `MDR_MDSW_CORE`, `SRC009_EIFU_REPLACEMENT` (eIFU anstelle Papier), `MDR_ART85`, vier Normblöcke; ungeklärt `SRC009_ART3_1_PATH` (nicht modelliertes Prädikat, übrige Teile wahr); alle übrigen inaktiv. Scope-bedingt nicht anwendbar: 115 + 9 + 1 + 12 + 1 + 2 + 1 + 2 = **143**; ungeklärt: **1**.

**Entscheidungskritische `RR`:** RR-353 (Art. 85) anwendbar; RR-360 und RR-064 scope-inaktiv; RR-205 `SCOPE_UNRESOLVED`; IEC 62304: RR-698 (Legacy) anwendbar, RR-693 (vorgelagerte Klassifizierung) regulär anwendbar, RR-716 (A/B/C) ungeklärt, weil die reguläre Route auf der Legacy-Route `UNKNOWN` ist, RR-728 (B/C) nicht anwendbar, weil Klasse A die Konjunktion falsch macht; IEC 62366-1: RR-889 und RR-954 anwendbar (geänderte UOUP-Teile aktivieren beide Routen), RR-930 nicht anwendbar (kein Usability-Test); ISO 13485: RR-384 regulär anwendbar, RR-443 ungeklärt (beanspruchter Ausschluss), RR-403 nicht anwendbar (keine QMS-Software).

## TC-039 — unvollständige Eingaben, fail-closed

RUL-001 bis RUL-004 beantwortet, `own_medical_purpose` fehlt → `QUALIFICATION` `INCOMPLETE` mit fehlender Eingabe an RUL-005; `BOUNDARY` und `CLASSIFICATION` nicht bewertet. RUL-027 `UNCLEAR` → `AI_ACT_APPLICABILITY_REVIEW_REQUIRED`. Ohne Applicability-Profil sind `MDR_MDSW`, alle Klassen- und Profilprädikate `UNKNOWN`; kein Prädikat ist falsch. Folge: alle 16 Blöcke ungeklärt, **alle 959 `RR` `APPLICABILITY_UNRESOLVED` mit `SCOPE_UNRESOLVED`**; keine `RR` wird als anwendbar oder nicht anwendbar geführt.

---

## Bewertung

Die vier Referenzfälle sind aus dem eingefrorenen Projektstand nachvollziehbar hergeleitet und für die Evaluation in Block 6 verwendbar. Grenze: TC-036 und TC-038 enthalten keine vollständige Einzelreferenz aller lokal bedingten `RR`.
