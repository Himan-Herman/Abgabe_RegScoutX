# Entscheidungslogik-Nachweis — SRC-002 (AI Act): Anwendbarkeit und Hochrisiko-Routing

Version 1.1 · Status: aktiv · Fortschreibung: 04.11.2026

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-002` — AI Act, konsolidierte Fassung `CELEX 02024R1689-20260727`, Stand 27.07.2026, einschließlich Verordnung (EU) 2026/1744 |
| Grundlage | finale Rechercheunterlagen A (Art. 2, Art. 3 Nr. 1, Art. 6 Abs. 1 und 1a–1c, Anhang I Abschnitt A Nr. 11, Art. 111 Abs. 2, Art. 113), B (Art. 6 Abs. 2, Anhang III) und C (Art. 6 Abs. 3 und 4, Art. 49 Abs. 2) |
| Ergebnisartefakt | [RUL_CATALOG.yaml](RUL_CATALOG.yaml) Version 0.3, 20 aktive AI-Act-Regeln (`RUL-027` bis `RUL-047` ohne ersetzte `RUL-039`), nach [RUL_METHOD.md](RUL_METHOD.md) Version 1.2 |
| Anwendbarkeit der `RR` | [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.5, Block `AI_ACT_HIGH_RISK` (`RR-001` bis `RR-115`) |
| Neue `RR` | keine |

Die Erstfassung 1.0 übernahm vorhandene Rechercheergebnisse ohne neue Recherche oder Adjudikation. Der begrenzte Quellenabgleich zur Korrektur 1.1 ist in Abschnitt 6 offengelegt. `SRC-003` wird nicht operationalisiert; die dort als überholt gekennzeichneten Aussagen zu Art. 6 und zu den Anwendungsterminen ([CROSSWALK_SRC_003_MDR_AI_ACT.md](CROSSWALK_SRC_003_MDR_AI_ACT.md) Abschnitt 9) sind durch den hier verwendeten Primärrechtsstand ersetzt. Primary Legal Anchor aller neuen `RUL` ist ausschließlich `SRC-002`; Guidance-Anker werden nicht geführt, weil für diese Regeln keine Guidance adjudiziert ist.

## 2. Source Verification

**PASS** (Inputs A bis C). Die MDR steht in Anhang I Abschnitt A Nr. 11; Art. 6 Abs. 1a bis 1c wurden durch die Verordnung (EU) 2026/1744 eingefügt; Art. 113 Buchst. c unterscheidet die Anwendungstermine für Anhang-III-Systeme (02.12.2027) und Anhang-I-Systeme (02.08.2028).

## 3. Anwendungsbereich (RUL-027 bis RUL-029)

| `RUL` | Research | Frage | Ergebnis | Primary |
| --- | --- | --- | --- | --- |
| `RUL-027` | AIA-R01 | KI-System nach Art. 3 Nr. 1? | NO → `AI_ACT_NOT_APPLICABLE`; UNCLEAR → `AI_ACT_APPLICABILITY_REVIEW_REQUIRED` | `SRC-002#Art.3/Nr.1` |
| `RUL-028` | AIA-R02 | Anknüpfungspunkt nach Art. 2 Abs. 1? | NONE → nicht anwendbar; UNCLEAR → Prüfung | `SRC-002#Art.2/Abs.1` |
| `RUL-029` | AIA-R03 | Ausnahme nach Art. 2? | eindeutige Ausnahme → nicht anwendbar; OTHER_REVIEW → Prüfung | `SRC-002#Art.2/Abs.3`, `Abs.6`, `Abs.8` |

## 4. Art.-6(1)-Produktroute (RUL-030 bis RUL-033)

Die beiden Bedingungen des Art. 6 Abs. 1 sind kumulativ: das KI-System ist selbst ein Produkt nach Anhang-I-Recht oder Sicherheitsbauteil eines solchen Produkts **und** für das Produkt ist eine Dritt-Konformitätsbewertung erforderlich.

| `RUL` | Research | Inhalt | Primary |
| --- | --- | --- | --- |
| `RUL-030` | AIA-R04 | Produkt selbst → `RUL-032`; Bestandteil → `RUL-031`; weder noch → Route negativ; unklar → Route ungeklärt | `SRC-002#Art.6/Abs.1/Buchst.a`, `SRC-002#Anh.I/Abschn.A/Nr.11` |
| `RUL-031` | AIA-R05 | Sicherheitsbauteil nach Abs. 1a/1b; Abs. 1b geht Abs. 1a vor | `SRC-002#Art.6/Abs.1a`, `SRC-002#Art.6/Abs.1b` |
| `RUL-032` | AIA-R06 | Dritt-Konformitätsbewertung erforderlich? | `SRC-002#Art.6/Abs.1/Buchst.b` |
| `RUL-033` | AIA-R07 | Drittprüfung ausschließlich wegen anderer als Gesundheits-/Sicherheitsrisiken → Buchst. b nicht erfüllt | `SRC-002#Art.6/Abs.1c` |

Ist das KI-System selbst das MDR-Produkt, ist Art. 6 Abs. 1 Buchst. a über die Produktalternative erfüllt; Abs. 1a/1b bestimmen nur, wann ein KI-System als Sicherheitsbauteil gilt.

**Kodierung von AIA-R05:** Die Adjudikation beschreibt eine Entscheidungstabelle über drei Merkmale (ausschließlich nicht sicherheitsbezogen, Gefährdung bei Ausfall, Sicherheitsbauteil). `RUL-031` kodiert sie verlustfrei als eine kontrollierte Eingabe mit Vorrang von Abs. 1b: Gefährdung bei Ausfall → weiter; ausschließlich nicht sicherheitsbezogen ohne Gefährdung → Route negativ; sonstiges Sicherheitsbauteil → weiter; kein Sicherheitsbauteil → Route negativ (die Bauteilalternative des Buchst. a ist dann nicht erfüllt); unklar → ungeklärt.

## 5. Zeitliche Anwendbarkeit und Übergang für Art.-6(1)-Systeme (RUL-034 bis RUL-037)

| `RUL` | Research | Inhalt | Primary |
| --- | --- | --- | --- |
| `RUL-034` | AIA-R08 | Bewertungsdatum vor 02.08.2028 → Art.-6(1)-Route noch nicht anwendbar | `SRC-002#Art.113/Buchst.c/Ziff.ii` |
| `RUL-035` | AIA-R09 | Inverkehrbringen bzw. Inbetriebnahme ab 02.08.2028 → Hochrisiko wirksam; davor → `RUL-036`; unbekannt → ungeklärt | `SRC-002#Art.111/Abs.2` |
| `RUL-036` | AIA-R10 | signifikante Konzeptionsänderung ab 02.08.2028 → Hochrisiko; nein → `RUL-037` | `SRC-002#Art.111/Abs.2/Satz.1` |
| `RUL-037` | AIA-R11 | Nutzung durch Behörden: nein → Übergang; ja und Bewertungsdatum vor 02.08.2030 → Übergang mit Frist 02.08.2030; ja und ab 02.08.2030 → Hochrisiko | `SRC-002#Art.111/Abs.2/Satz.2` |

`AI_ACT_NOT_YET_APPLICABLE` betrifft ausschließlich den Hochrisiko-Anforderungsblock, nicht den gesamten AI Act. `AI_ACT_HIGH_RISK_LEGACY_TRANSITION` bleibt ein eigener Zustand und wird weder mit „nicht hochriskant“ noch mit „noch nicht anwendbar“ vermischt.

## 6. Art.-6(2)-Route und Anhang III

Art. 6 Abs. 2 ist ein **alternativer** Hochrisiko-Weg; die Route wird deshalb nach jedem Ergebnis der Art.-6(1)-Route geprüft.

| Wert von `annex_iii_use_case` | Anhang-III-Fundstelle |
| --- | --- |
| `REMOTE_BIOMETRIC_IDENTIFICATION` (nicht bloße 1:1-Verifizierung) | `SRC-002#Anh.III/Nr.1/Buchst.a` |
| `SENSITIVE_BIOMETRIC_CATEGORISATION` | `SRC-002#Anh.III/Nr.1/Buchst.b` |
| `EMOTION_RECOGNITION` | `SRC-002#Anh.III/Nr.1/Buchst.c` |
| `PUBLIC_HEALTHCARE_ELIGIBILITY` | `SRC-002#Anh.III/Nr.5/Buchst.a` |
| `HEALTH_INSURANCE_RISK_PRICING` | `SRC-002#Anh.III/Nr.5/Buchst.c` |
| `EMERGENCY_CALL_CLASSIFICATION`, `EMERGENCY_SERVICE_DISPATCH_PRIORITY`, `EMERGENCY_HEALTHCARE_TRIAGE` | `SRC-002#Anh.III/Nr.5/Buchst.d` |

Konkreter Treffer → Art.-6(3)-Prüfung (`RUL-040`); `NONE` → Route negativ; `OTHER_ANNEX_III_POSSIBLE` und `UNCLEAR` → Route ungeklärt. Anhang III Nr. 2, 3, 4, 5 Buchst. b, 6, 7 und 8 sind keine Kernfragen des MDSW-Baums; ein möglicher dualer Einsatzzweck wird über `OTHER_ANNEX_III_POSSIBLE` nicht pauschal verneint.

In Version 0.2 prüfte `RUL-039` nur den Anwendungsbeginn; die Übergangsprüfung fehlte (R01-4.6-F01). Diese Fassung bleibt für R1/R2 eingefroren. Seit Version 0.3 ist `RUL-039` durch `RUL-044` ersetzt; die fachliche Entscheidung wird vor dem wirksamen Hochrisiko-Ausgang um `RUL-045` bis `RUL-047` ergänzt.

| `RUL` | Prüfung | Ergebnis | Primary |
| --- | --- | --- | --- |
| `RUL-044` | Bewertungsdatum | vor 02.12.2027 → noch nicht anwendbar; ab diesem Datum → `RUL-045` | `SRC-002#Art.113/Buchst.c/Ziff.i` |
| `RUL-045` | Inverkehrbringen bzw. Inbetriebnahme | vor 02.12.2027 → `RUL-046`; ab diesem Datum → Hochrisiko wirksam; unbekannt → Prüfung | `SRC-002#Art.111/Abs.2` |
| `RUL-046` | signifikante Konzeptionsänderung seit 02.12.2027 | ja → Hochrisiko wirksam; nein → `RUL-047`; unklar → Prüfung | `SRC-002#Art.111/Abs.2/Satz.1` |
| `RUL-047` | Bestimmung zur Behördennutzung | nein → Übergang; ja und vor 02.08.2030 → Übergang mit Frist; ja und ab 02.08.2030 → Hochrisiko wirksam; unklar → Prüfung | `SRC-002#Art.111/Abs.2/Satz.2` |

Für `RUL-046` gilt ein eigener Eingabeschlüssel `annex_iii_significant_design_change_after_application_date`. Die unveränderte Produktroute verwendet `significant_design_change_after_application_date` zum Stichtag 02.08.2028. Eine Änderung zwischen den beiden Stichtagen darf nicht mit derselben Ja/Nein-Angabe für beide Zeiträume gleichgesetzt werden. Das Inverkehrbringensdatum und die Behördenbestimmung bleiben gemeinsame Produktmerkmale. Die Frageführung zeigt bei gemeinsamen Eingabeschlüsseln Text und Stichtag der tatsächlich erreichten Regel.

Fehlende entscheidungsnotwendige Angaben beenden die Auswertung als `INCOMPLETE`; ausdrücklich unklare Angaben führen zu `AI_ACT_APPLICABILITY_REVIEW_REQUIRED`. Ein bestätigter Übergang ergibt `AI_ACT_HIGH_RISK_LEGACY_TRANSITION`; damit bleiben die 115 AI-Act-Anforderungen blockseitig `NOT_APPLICABLE` mit `SCOPE_LEGACY_TRANSITION`. Eine wirksame parallele Produktroute kann den Block weiterhin aktivieren. Die unveränderte Aggregation in Abschnitt 9 entscheidet über das Gesamtergebnis.

Die Korrektur übernimmt die bereits dokumentierte Übergangssemantik in den eingefrorenen Quellenfassungen; sie aktualisiert weder das Quellenregister noch die Anwendungstermine. Die früheren Source-Verification-Angaben dokumentieren die Erstfassung. Beim gezielten Abgleich am 04.11.2026 waren amtlich indexierte EN-Passagen zu Art. 111 Abs. 2 und den Fristen zugänglich; direkte EUR-Lex-DE-/PDF-Aufrufe scheiterten an der JavaScript-Schranke. Kein neuer vollständiger DE/EN-Rechtsabgleich und keine unabhängige regulatorische Validierung werden behauptet. Gezielte Regression und Grenzen: [EV-019](../09-evidence/EV-019_ANNEX_III_TRANSITION_FIX.md).

## 7. Art. 6 Abs. 3 (RUL-040 bis RUL-042)

| `RUL` | Eingabe | Ergebnis | Primary |
| --- | --- | --- | --- |
| `RUL-040` | `profiling_natural_persons` | YES → Ausnahme ausgeschlossen, Hochrisiko-Kandidat; NO → `RUL-041`; UNCLEAR → ungeklärt | `SRC-002#Art.6/Abs.3` |
| `RUL-041` | `art6_3_derogation_condition` | Bedingung a–d → `RUL-042`; NONE → Hochrisiko-Kandidat; UNCLEAR → ungeklärt | `SRC-002#Art.6/Abs.3/Buchst.a` bis `Buchst.d` |
| `RUL-042` | `significant_risk_health_safety_fundamental_rights` | YES → Hochrisiko-Kandidat; NO → `ART6_3_NON_HIGH_RISK`; UNCLEAR → ungeklärt | `SRC-002#Art.6/Abs.3`, `SRC-002#Art.6/Abs.4` |

Die Ausnahme greift nur kumulativ: mindestens eine Bedingung a–d **und** belastbar kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte. Eine Bedingung a–d allein führt nie zu Nicht-Hochrisiko. Die Buchstaben a–d gehören zum zweiten Unterabsatz von Art. 6 Abs. 3; die Lokatoren sind die engsten nach der Projektkonvention zulässigen Fundstellen.

## 8. Art. 6 Abs. 4 und Art. 49 Abs. 2

Bei `ART6_3_NON_HIGH_RISK` trägt das `DecisionResult` den Hinweis `ART6_4_SELF_ASSESSMENT_OBLIGATIONS_APPLY` (Anker `SRC-002#Art.6/Abs.4`, `SRC-002#Art.49/Abs.2`): Bewertung vor dem Inverkehrbringen oder der Inbetriebnahme dokumentieren, Registrierung nach Art. 49 Abs. 2 in der EU-Datenbank nach Art. 71, Dokumentation auf Verlangen der zuständigen nationalen Behörden vorlegen. Der Hinweis ist ein Routing-/Compliance-Hinweis, **keine** `RR` und **kein** Erfüllungsstatus; Art. 6 Abs. 4 ist nicht Bestandteil des Gap-`RR`-Korpus.

## 9. Kombiniertes Routing und Endzustände (RUL-043)

```text
RUL-027 → RUL-028 → RUL-029 ──(nicht anwendbar / Prüfung)──► Endzustand
                         │
                         ▼
            Art.-6(1)-Route RUL-030 … RUL-037 → Routenergebnis ART6_1_*
                         │
                         ▼
            Art.-6(2)/(3)-Route RUL-038, RUL-040 … RUL-042, RUL-044 … RUL-047 → Routenergebnis ART6_2_* bzw. ART6_3_NON_HIGH_RISK
                         │
                         ▼
            RUL-043: HIGH_RISK = wirksame Art.-6(1)-Route ODER wirksame Art.-6(2)-Route
```

`RUL-043` kombiniert ausschließlich die Routenergebnisse über die generische Aggregation nach [RUL_METHOD.md](RUL_METHOD.md) Abschnitt 8.1. Vorrangfolge: `AI_ACT_HIGH_RISK` › `AI_ACT_APPLICABILITY_REVIEW_REQUIRED` › `AI_ACT_HIGH_RISK_LEGACY_TRANSITION` › `AI_ACT_NOT_YET_APPLICABLE` › `AI_ACT_APPLICABLE_NOT_HIGH_RISK`.

- Ein wirksamer Hochrisiko-Weg genügt; ein positives Art.-6(1)-Ergebnis wird durch Art. 6 Abs. 3 nicht aufgehoben.
- `AI_ACT_APPLICABLE_NOT_HIGH_RISK` nur, wenn beide Routen negativ sind oder die Art.-6(3)-Ausnahme festgestellt ist und keine Route ungeklärt ist — nie aus einer negativen Art.-6(1)-Route allein.
- Treffen beide Wege zu, ist `applicable_from` der früheste Anwendungsbeginn der wirksamen Wege (z. B. 02.12.2027 vor 02.08.2028).
- Die Einordnung von Übergang vor „noch nicht anwendbar“ bei gleichzeitigem Auftreten beider Zustände ist eine Operationalisierung ohne eigene Rechtsfolge: Beide Zustände aktivieren den Hochrisiko-Block derzeit nicht.

| Endzustand | `RR-001` bis `RR-115` |
| --- | --- |
| `AI_ACT_NOT_APPLICABLE` | `NOT_APPLICABLE` |
| `AI_ACT_APPLICABLE_NOT_HIGH_RISK` | `NOT_APPLICABLE` |
| `AI_ACT_NOT_YET_APPLICABLE` | derzeit `NOT_APPLICABLE`, Begründungscode `SCOPE_NOT_YET_APPLICABLE` |
| `AI_ACT_HIGH_RISK_LEGACY_TRANSITION` | keine pauschale Aktivierung: `NOT_APPLICABLE`, Begründungscode `SCOPE_LEGACY_TRANSITION` |
| `AI_ACT_HIGH_RISK` | Block aktiv; danach lokale Applicability nach [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) |
| `AI_ACT_APPLICABILITY_REVIEW_REQUIRED` bzw. nicht ausgeführt | `APPLICABILITY_UNRESOLVED` |

## 10. Art. 2 Abs. 13

Art. 2 Abs. 13 erlaubt künftig die Begrenzung bestimmter Pflichten aus Art. 9 bis 15 und 17 bis 25 für Art.-6(1)-Systeme durch delegierte Rechtsakte. Im Quellenstand 27.07.2026 besteht kein konkretes Begrenzungsprofil:

`art2_13_limitation_profile = NONE`

Es werden keine `RR` aus Gründen des Art. 2 Abs. 13 unterdrückt; eine `RUL` ist erst erforderlich, wenn ein konkreter delegierter Rechtsakt operationalisiert werden kann.

## 11. Zuordnung der Research-Kandidaten

| Research | `RUL` |
| --- | --- |
| AIA-R01 bis AIA-R11 | `RUL-027` bis `RUL-037` |
| AIA-R12 (Anhang-III-Anwendungsfall) | `RUL-038` |
| AIA-R13 (Anwendungsbeginn Art. 6 Abs. 2) | `RUL-039` (historisch), seit 0.3 `RUL-044` |
| Art. 6 Abs. 3 Profiling, Bedingung, erhebliches Risiko | `RUL-040` bis `RUL-042` |
| kombiniertes Art.-6-Routing | `RUL-043` |

In Version 0.2: 17 neue `RUL`; `RUL-001` bis `RUL-026` unverändert. Die Research bezeichnete eine mögliche Art.-2(13)-Filterregel ebenfalls als „AIA-R12“; sie wird nach Abschnitt 10 nicht als `RUL` angelegt.

## 12. Nachweis

Die Kernpfade werden in `tests/test_ai_act_applicability.py` über den `RULE_ENGINE` und den `APPLICABILITY_ENGINE` geprüft. Source-level Unresolveds: 0.

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: AI-Act-Anwendungsbereich, Art.-6(1)-Produktroute mit Abs. 1a–1c, zeitliche Anwendbarkeit und Übergang nach Art. 111 Abs. 2 und Art. 113, Art.-6(2)-Route mit Anhang III, Art.-6(3)-Ausnahme, Art.-6(4)-Hinweis, kombiniertes Routing, Art.-2(13)-Baseline; `RUL-027` bis `RUL-043`; keine neue `RR`. |
| 1.1 | Gezielte technische Behebung R01-4.6-F01: Anhang-III-Übergangskette RUL-044 bis RUL-047, ersetzte RUL-039, getrennte Änderungsangaben und aktuelle Bindungen. R1/R2 und Quellenstand unverändert; keine neue Fallstudienevaluation. |
