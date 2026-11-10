# Traceability-Modell

Version 1.13 · Status: aktiv

**Hinweis zum Abgabestand:** Das Beispiel mit `RUL-027` bis `RUL-043` in Abschnitt 2 beschreibt den evaluierten Regelkatalog 0.2 mit Anwendbarkeitszuordnung 0.4. Der mitgelieferte Demonstrator verwendet Regelkatalog 0.3 und Anwendbarkeitszuordnung 0.5. Die Ergänzung ist in [EV-019](../09-evidence/EV-019_ANNEX_III_TRANSITION_FIX.md) dokumentiert. Die Traceability-Matrix lässt sich für den Abgabestand aus den enthaltenen Katalogen ableiten.

Dieses Dokument legt fest, wie die Traceability-Kette aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 5 technisch geführt und ausgewertet wird. Die dortigen Grundregeln — Pfad 1 `SRC → RR → (SR) → RUL → TC → EV`, Pfad 2 `SRC → RUL → TC → EV`, Verweise nur aufwärts zum Vorgänger — gelten unverändert und werden hier nicht wiederholt.

---

## 1. Grundsatz: keine manuell gepflegte Matrix als Wahrheitsquelle

- Die Verknüpfungen stehen ausschließlich in den führenden Katalogen, jeweils am Nachfolger. Es gibt **keine** zweite, manuell gepflegte Matrix.
- Die Traceability-Matrix ist eine **abgeleitete Ansicht**. Sie wird bei Bedarf mit `tools/traceability.py` aus den Katalogen erzeugt und nicht versioniert, damit sie nicht von den Katalogen abweichen kann.
- Die Verweisintegrität wird automatisiert geprüft; ein Verweis auf eine nicht vergebene ID ist ein Fehler.

## 2. Entwurfszeit-Verknüpfungen

| Von | Verknüpfungsart | Nach | Feld | Führende Datei |
| --- | --- | --- | --- | --- |
| `RR` | `RR_SOURCE_PRIMARY` / `RR_SOURCE_SUPPLEMENTARY` | `SRC`-Lokator | `sources.primary` / `sources.supplementary` | [RR_CATALOG.yaml](../03-regulatory/RR_CATALOG.yaml) |
| `RUL` | `PRIMARY_LEGAL_ANCHOR` | `SRC`-Lokator (Ebene A) | `primary_legal_anchor` | [RUL_CATALOG.yaml](../03-regulatory/RUL_CATALOG.yaml) |
| `RUL` | `GUIDANCE_ANCHOR` | `SRC`-Lokator (Ebene B) | `guidance_anchor` | [RUL_CATALOG.yaml](../03-regulatory/RUL_CATALOG.yaml) |
| `RUL` | `DEPENDS_ON` | vorgelagerte `RUL` | `dependencies` | [RUL_CATALOG.yaml](../03-regulatory/RUL_CATALOG.yaml) |
| `RUL` | `PRODUCES` | Ausgabewert (`RUL_OUTPUT`) | `branches.result` / `branches.review` | [RUL_CATALOG.yaml](../03-regulatory/RUL_CATALOG.yaml) |
| `SR` | `DERIVED_FROM` | Exposé-Abschnitt, Design Implication (`STATE_OF_THE_ART.md#DI-NNN`), `RR` oder `SRC`-Lokator | `derived_from` | [SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml) |
| `SR` | `ALLOCATED_TO` | Architekturmodul | `allocated_modules` | [SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml) |
| `TC` | `VERIFIES` / `TC_VERIFIES_SR` / `TC_COVERS_RR` | `RUL` / `SR` / `RR` bzw. Block (`BLOCK:<name>`) | `verifies_rul` / `verifies_sr` / `covers_rr` | [TC_CATALOG.yaml](../07-testing/TC_CATALOG.yaml) |
| `EV` | `EV_OF_TC` | `TC` | `test_cases` | [EV_INDEX.yaml](../09-evidence/EV_INDEX.yaml) |
| `RR` | `RR_MEASURE` | vorgesehene Maßnahme (`MEASURE:<key>`) | `requirements.<RR>.measures` | [RR_MEASURE_CATALOG.yaml](../03-regulatory/RR_MEASURE_CATALOG.yaml) |
| Maßnahme | `MEASURE_EVIDENCE_TYPE` | vorgesehene Nachweisart (`EVIDENCE_TYPE:<key>`) | `measures.<key>.evidence_types` | [RR_MEASURE_CATALOG.yaml](../03-regulatory/RR_MEASURE_CATALOG.yaml) |
| `RR` | `APPLICABILITY_BLOCK` / `LOCAL_CONDITION` | Block bzw. Prädikat | `block` / `local` | [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) |
| Block | `BLOCK_SCOPE` | Prädikat | `scope` | [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) |
| Prädikat | `PREDICATE_PART` / `DECISION_OUTCOME` / `PROFILE_INPUT` | Prädikat, RUL-Ausgabe bzw. Applicability-Eingabe | `of` / `true_if`, `false_if` / `input` | [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) |
| Prädikat | `CONDITION_SOURCE` | Evidenzdatei | `source_of_condition` | [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) |
| Prädikat | `MISSING_PRIMARY_LAW` | `SRC`-Lokator (fehlender Primärrechtsknoten) | `missing_primary_law` | [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) |
| `RR` | `SOURCE_SUPPORT` | `SRC`-Lokator einer Norm, die eine bestehende `RR` stützt, ohne deren Primary Source zu ändern | `relations[].rr` / `locator` | [RR_STANDARDS_MAPPING_SRC_005_008.yaml](../03-regulatory/RR_STANDARDS_MAPPING_SRC_005_008.yaml) |
| `SRC` bzw. `SRC`-Lokator | `NORMATIVE_DEPENDENCY` | `RR` bzw. `SRC` (normative Verweisung einer Norm) | `relations[].from` / `to` | [RR_STANDARDS_MAPPING_SRC_005_008.yaml](../03-regulatory/RR_STANDARDS_MAPPING_SRC_005_008.yaml) |

Damit ist jede Anwendbarkeitsentscheidung rückverfolgbar: `RR` ← Zuordnung ← Prädikat bzw. Eingabe ← RUL-Ausgabe/`DecisionResult` ← erzeugende `RUL` (`PRODUCES`) ← `SRC`-Anker der `RUL` bzw. Evidenzdatei; für den AI-Act-Block `RR-001` bis `RR-115` ← `AI_ACT_HIGH_RISK` ← `RUL-027` bis `RUL-043` ← `SRC-002`. Für die Norm-`RR` `RR-378` bis `RR-959` gilt: `RR` ← Normlokator (`sources.primary`, bei Merge-`RR` zusätzlich `sources.supplementary`) ← Temp-ID der Normadjudikation ([RR_STANDARDS_MAPPING_SRC_005_008.yaml](../03-regulatory/RR_STANDARDS_MAPPING_SRC_005_008.yaml)); Stützungen bestehender `RR` und normative Abhängigkeiten (IEC 62304 bzw. IEC 62366-1 → ISO 14971) ändern keine Primary Source.

`TC` und `EV` sind seit Version 1.5 vergeben ([TC_CATALOG.yaml](../07-testing/TC_CATALOG.yaml), [EV_INDEX.yaml](../09-evidence/EV_INDEX.yaml); Strategie in TEST_STRATEGY.md (Entwicklungsarchiv; nicht im Abgabepaket)). Die lokalen Kennungen T01 bis T15 bleiben Datenvarianten, die `TC-001` bis `TC-006` über `data_refs` referenzieren; `VERIFIES` wird ausschließlich aus dem TC-Katalog gebildet, damit keine doppelten Verknüpfungen entstehen. Die abgeleitete Matrix (`tools/traceability.py --markdown`) führt je `RR` Quelle, Lebenszyklusphasen, vorgesehene Maßnahme mit Mapping-Status, Nachweisart und prüfende `TC` und damit die Kette Anforderung → Quelle → Lebenszyklusphase → Maßnahme → Nachweisdokument nach [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 4.

## 3. Bewusst nicht erzwungene Verknüpfungen

Die Rollen der Artefakte sind verschieden; es wird keine künstliche lineare Kette gebildet:

- **`RUL` (Pfad 2) → `RR`:** Die Qualifikations-, Abgrenzungs- und Klassifikationsregeln verweisen direkt auf `SRC`, weil keine sachgerechte Gap-`RR` formulierbar ist. Welche `RR` eine Entscheidung aktiviert, ist keine Entwurfszeit-Verknüpfung, sondern ein Ergebnis zur Laufzeit (Abschnitt 4). Gap-Filter-Regeln nach Pfad 1 sind im Katalog nicht angelegt: Die Anwendbarkeit bedingter `RR` ist über [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) (Block, lokale Bedingung, Prädikat) abgebildet, die Gap-Ableitung liegt in `GAP_ENGINE` ([ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md) Abschnitt 8); künftige Gap-Filter-Regeln würden die `RR` referenzieren, deren Anwendbarkeit sie bestimmen.
- **`SR` → `RR`:** `RR` richten sich an Medizinproduktehersteller, nicht an RegScoutX. Sie sind für die `SR` Verarbeitungsgegenstand. Eine `SR` referenziert eine `RR` nur, wenn sie aus deren Inhalt als Anforderung an RegScoutX folgt; in `SR_CATALOG.yaml` trifft das bis Version 0.6 auf keine `SR` zu.
- **`SR` → `RUL`:** Die Konvention lässt `SR` nur auf Exposé, `RR` oder `SRC` verweisen. `SR` fordern die Ausführung der Regeln; die Regeln sind Daten dieser Ausführung.

## 4. Laufzeit-Traceability einer Bewertung

Zur Laufzeit wird Rückverfolgbarkeit über die Entitäten des Datenmodells [../04-architecture/DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml) hergestellt:

```text
ReportSnapshot ─► CatalogVersionSet (SOURCES, RR_CATALOG, RUL_CATALOG, DATA_MODEL, RR_APPLICABILITY, RR_MEASURE)
      │
      ├─► DecisionResult ─► RuleExecution ─► RUL ─► SRC (Primärrecht, Guidance)
      │
      └─► RequirementResult ─► ApplicableRequirement ─► RR ─► SRC
                │                      └─► determined_by ─► DecisionResult
                ├─► RR_MEASURE (vorgesehene Maßnahme, Nachweisart)
                └─► GapAssessment (Nutzerangabe, an RR gebunden)
                          └─► EvidenceReference (Nutzerangabe) ─► measure_key ─► RR_MEASURE ─► RR
```

Damit ist jedes Berichtsergebnis — Klasse, Anwendbarkeit, Status, Gap — über Regelpfad bzw. Anforderung bis zur Quelle und zur verwendeten Katalogversion rückverfolgbar. Seit Demonstrator D1 setzt der `ASSESSMENT_SERVICE` diese Kette je `RR` als `RRResult` zur Laufzeit zusammen ([ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md) Abschnitt 8); der Gap-Status trägt einen eigenen, nicht-regulatorischen `gap_reason`. Seit D2 ist jeder Stand eine gespeicherte Revision mit eigenem `CatalogVersionSet`, Fingerprint und Differenz zum Vorgänger; das Audit-Protokoll verweist je Ereignis auf Revision und Kennung (PERSISTENCE_FORMAT.md (Entwicklungsarchiv; nicht im Abgabepaket)). Seit D3 entsteht jeder Bericht aus genau einer Revision (`ReportSnapshot` mit `content_hash`); `REPORT_CREATED` verknüpft Revision, Sprache, Format und Inhaltshash, sodass ein Berichtsartefakt über den Hash seiner Revision und deren Katalogversionen zugeordnet werden kann (REPORTING.md (Entwicklungsarchiv; nicht im Abgabepaket)). Die Herleitung der Anwendbarkeit (Begründungscode, Block, Prädikate, Eingaben, herangezogene `RUL`) wird nach SR-042 aus `ApplicableRequirement` ausgewiesen, der Lebenszykluskontext nach SR-041 aus `lifecycle_phases` der `RR`. Seit D4 macht die Web-Oberfläche diese Kette je `RR` als Decision Trace sichtbar (Eingabe → Bedingung → `RUL`/Entscheidung → Anwendbarkeit → `RR` → Gap-Status → Maßnahme → Nachweis) und nennt je Frage ihren Auslöser (Einstieg, auslösende `RUL` mit Frage und Antwort, oder auswertende Anwendbarkeitsbereiche); alle Werte stammen aus der gespeicherten Revision über die Anwendungs-API ([WEB_APPLICATION.md](../04-architecture/WEB_APPLICATION.md)). Die Web-Abnahmeszenarien `TC-055` bis `TC-060` verweisen zusätzlich auf Browser-Spezifikationen unter `web/e2e/`; `VERIFIES` bleibt ausschließlich aus dem TC-Katalog gebildet.

**Vorgesehene Maßnahmen (SR-043):** Die Kette `RR → vorgesehene Maßnahme (RR_MEASURE) → Nachweis` ist im Datenmodell angelegt ([DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml) Version 0.4). Der versionierte Maßnahmenkatalog ist seit Version 1.5 als [RR_MEASURE_CATALOG.yaml](../03-regulatory/RR_MEASURE_CATALOG.yaml) angelegt und in Abschnitt 2 sowie in `tools/traceability.py` verknüpft. Die Maßnahmen sind generisch und wiederverwendbar; eine Zuordnung verbindet jeweils genau eine `RR` mit einer Maßnahme und deren vorgesehener Nachweisart. Ein `measure_key` einer `EvidenceReference` ist nur gültig, wenn die Maßnahme der `RR` des zugehörigen `GapAssessment` zugeordnet ist. Seit `RR_MEASURE_CATALOG.yaml` 0.2 ist die Kette für alle 959 `RR` belegt: Quelle → Lebenszyklusphase → vorgesehene Maßnahme → vorgesehene Nachweisart (intended evidence artifact); jede Zuordnung trägt ihre Mapping-Basis (`SOURCE_EXPLICIT` bzw. `PROJECT_DERIVED`), die die abgeleitete Matrix ausweist ([RR_MEASURE_METHOD.md](../03-regulatory/RR_MEASURE_METHOD.md)). Vorgesehene Nachweisart, tatsächliche Nachweisreferenz der Bewertung und Projektevidenz `EV` bleiben getrennt. Die Evaluationskette (Abschnitt 4a) ist an Version 0.1 gebunden.

## 4a. Evaluationskette der Fallstudie (Block 6)

Die Evaluation fügt keine neue Entwurfszeit-Verknüpfungsart hinzu. Sie verbindet bestehende Artefakte in einer eigenen, dateibasierten Kette:

```text
CASE_STUDY.md (Annahmen) ─► TC-036 golden_case (EV-003) ─► REFERENCE_ASSESSMENT.yaml (SHA-256, EV-011)
      │                                                              │
      └─► Systemlauf über die Anwendungs-API (evaluation/, R1/R2) ◄──┘ Vergleich je RR
                │
                ├─► results/R*/system_output.json, metrics.json ─► EVALUATION_RESULTS.md
                ├─► Bericht (content_hash, PDF DE/EN in 09-evidence/evaluation/)
                └─► EV-012 bis EV-016 ─► TC-061 (Regressionstest der berichteten Kennzahlen)
```

Die Referenz verweist je `RR` auf den Begründungscode, den Anwendbarkeitsblock und die herangezogene Referenzregel (`RB-0` bis `RB-9`) und ist dadurch über `RR_APPLICABILITY.yaml` bis zu `RUL` und `SRC` rückverfolgbar. Die Zirkularitätsprüfung (`tools/validate_reference_assessment.py`) stellt sicher, dass das Ableitungswerkzeug keinen Code und keine Laufzeitausgabe des Demonstrators verwendet und die eingefrorene Datei unverändert ist. Die Stichprobe der Nachvollziehbarkeit (T1–T11) prüft die Laufzeitkette aus Abschnitt 4 für 11 `RR` einschließlich Bericht ([EVALUATION_METHOD.md](../08-evaluation/EVALUATION_METHOD.md) Abschnitt 5.4).

## 5. Werkzeug

```
.venv/bin/python tools/traceability.py            # Integritätsprüfung und Zusammenfassung
.venv/bin/python tools/traceability.py --markdown # abgeleitete Matrixansicht auf stdout
```

Die Prüfung bestätigt ausschließlich formale Verweisintegrität, nicht die fachliche Richtigkeit einer Verknüpfung.

## 6. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Katalog-basierte Traceability ohne manuell gepflegte Matrix, Entwurfszeit-Verknüpfungsarten, bewusst nicht erzwungene Verknüpfungen, Laufzeit-Traceability über das Datenmodell, Werkzeug zur Integritätsprüfung und Matrixerzeugung. |
| 1.1 | Verknüpfungsarten der RR-Applicability-Zuordnung ergänzt (Block, lokale Bedingung, Prädikat, RUL-Ausgabe, Eingabe, Evidenz, fehlender Primärrechtsknoten). |
| 1.2 | Verknüpfungsart `PRODUCES` (`RUL` → Ausgabewert) ergänzt; Kette des AI-Act-Blocks bis `SRC-002` beschrieben. |
| 1.3 | Verknüpfungsarten `SOURCE_SUPPORT` und `NORMATIVE_DEPENDENCY` aus der Zuordnung der Normkandidaten `SRC-005` bis `SRC-008` ergänzt; Kette der Norm-`RR` beschrieben. |
| 1.4 | `DERIVED_FROM` einer `SR` um Design Implications (`STATE_OF_THE_ART.md#DI-NNN`) erweitert; Laufzeitkette um vorgesehene Maßnahme (`RR_MEASURE`) nach SR-043 ergänzt; Herleitung der Anwendbarkeit (SR-042) und Lebenszykluskontext (SR-041) benannt. |
| 1.5 | `TC`- und `EV`-Verknüpfungen (`VERIFIES`, `TC_VERIFIES_SR`, `TC_COVERS_RR`, `EV_OF_TC`) aus TC-Katalog und Evidenzindex statt aus den lokalen T-Fällen; Maßnahmenkatalog mit `RR_MEASURE` und `MEASURE_EVIDENCE_TYPE`; abgeleitete Matrix um Lebenszyklusphase, Maßnahme, Nachweisart und prüfende `TC` erweitert. |
| 1.6 | Laufzeitkette: `CatalogVersionSet` führt zusätzlich die Versionen von `RR_APPLICABILITY` und `RR_MEASURE` (DATA_MODEL 0.5). |
| 1.7 | Laufzeitkette: `RequirementResult` verbindet `ApplicableRequirement`, `RR_MEASURE` und die an die `RR` gebundene `GapAssessment` (DATA_MODEL 0.6); Umsetzung durch den `ASSESSMENT_SERVICE`. |
| 1.8 | Laufzeit-Traceability über gespeicherte Revisionen und Audit-Ereignisse (D2). |
| 1.9 | Laufzeitkette Revision → ReportSnapshot → Berichtsartefakt über `content_hash` und `REPORT_CREATED` (D3). |
| 1.10 | Sichtbare Laufzeitkette in der Web-Oberfläche (Decision Trace, Auslöser je Frage) und Browser-Verweise der Web-Abnahmeszenarien (D4); keine neue Verknüpfungsart. |
| 1.11 | Evaluationskette der Fallstudie (Block 6): Fallstudie → Referenz (EV-011) → Systemlauf → Metriken → EV-012 bis EV-016 → TC-061; keine neue Verknüpfungsart. |
| 1.12 | Abschnitt 3 an den umgesetzten Stand angeglichen: Pfad 1 ohne Gap-Filter-`RUL`, Anwendbarkeit bedingter `RR` über `RR_APPLICABILITY`, `SR → RR` bis `SR_CATALOG` 0.6. Keine neue Verknüpfungsart. |
| 1.13 | Abschnitt 4: vollständige Kette Quelle → Lebenszyklusphase → Maßnahme → Nachweisart für alle 959 `RR` mit Mapping-Basis (`RR_MEASURE` 0.2); Matrix und Zusammenfassung von `tools/traceability.py` um Mapping-Basis und Kettenvollständigkeit ergänzt. Keine neue Verknüpfungsart. |
