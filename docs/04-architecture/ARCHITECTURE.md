# Logische Architektur des Demonstrators

Version 1.12 · Status: aktiv

Dieses Dokument beschreibt die **logische**, technologieneutrale Modularchitektur von RegScoutX. Die Entscheidung und ihre Alternativen stehen in ADR-0002 (Entwicklungsarchiv). Die logische Architektur bleibt technologieneutral; Programmiersprache, Persistenz, Bericht und Benutzeroberfläche sind in eigenen ADRs entschieden (ADR-0003 (Entwicklungsarchiv) bis ADR-0007 (Entwicklungsarchiv); Umsetzung in Abschnitt 8).

---

Für `PRESENTATION` und alle sichtbaren Komponenten ist [UI_UX_DESIGN_SYSTEM.md](UI_UX_DESIGN_SYSTEM.md) (Version 1.1, byte-genau übernommen; SHA-256 `794df31d5950fdcb95ac56769fda2d210394ed82241d73a1f91cceb06042417c`) die führende, verbindliche UI/UX- und Frontend-Architekturleitlinie; sie ändert keine fachliche Semantik und keine Abhängigkeitsregel.

## 1. Leitprinzipien

1. **Datengetriebene regulatorische Inhalte.** Quellen (`SRC`), regulatorische Anforderungen (`RR`) und Entscheidungsregeln (`RUL`) werden ausschließlich aus den versionierten Katalogen gelesen und nie in Programm- oder UI-Code nachgebildet.
2. **Deterministische Entscheidungslogik ohne generative KI.** Gleiche Eingaben und gleiche Katalogversionen ergeben gleiche Ergebnisse ([EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitte 3 und 4).
3. **Trennung der Rollen.** `RUL` entscheiden Applicability, Qualification, Classification und Routing; `RR` beschreiben regulatorische Sollanforderungen; `SR` beschreiben Anforderungen an RegScoutX selbst.
4. **Geringe Kopplung, hohe Kohäsion.** Jedes Modul hat genau eine Verantwortung und kommuniziert nur über die in Abschnitt 4 zugelassenen Abhängigkeiten.
5. **Rückverfolgbarkeit als Datenmerkmal.** Jedes Ergebnis trägt die IDs und Katalogversionen, aus denen es entstanden ist ([../05-traceability/TRACEABILITY_MODEL.md](../05-traceability/TRACEABILITY_MODEL.md)).

Die wissenschaftliche Herleitung dieser bereits getroffenen Entscheidungen aus dem Stand der Technik – deterministischer Regelkern, Trennung von Regelkern und Oberfläche, regelgesteuerte adaptive Frageführung, Explainability über den Rule Trace, fail-closed-Verhalten, versionierte Wissensbasis, Traceability, Lebenszyklusbezug und Evidence Mapping – steht in [../01-research/STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) Abschnitt 9. Sie ändert keine Entscheidung.

## 2. Kontext

```text
 Nutzer ──► PRESENTATION ──► APPLICATION_API ──► ASSESSMENT_SERVICE ──► RULE_ENGINE ─┐
                 │                  │                    │               │
                 │                  ├──► APPLICABILITY_ENGINE ──► REQUIREMENT_SERVICE
                 │                  ├──► GAP_ENGINE ──► EVIDENCE_SERVICE │
                 │                  └──► REPORTING                       │
                 └──► I18N                                               ▼
                                       CATALOG_REPOSITORY (SRC, RR, RUL, Ausgabewerte)
 AUDIT_LOG ◄── Ereignisse aller fachlichen Module
 ASSESSMENT_SERVICE ──► ASSESSMENT_REPOSITORY (Schnittstelle) ◄── lokale JSON-Dateipersistenz
```

## 3. Module

Zulässige Architekturmodule:

`CATALOG_REPOSITORY` · `ASSESSMENT_SERVICE` · `ASSESSMENT_REPOSITORY` · `RULE_ENGINE` · `APPLICABILITY_ENGINE` · `REQUIREMENT_SERVICE` · `GAP_ENGINE` · `EVIDENCE_SERVICE` · `REPORTING` · `I18N` · `AUDIT_LOG` · `APPLICATION_API` · `PRESENTATION`

| Modul | Verantwortung | Liest | Erzeugt / verwaltet |
| --- | --- | --- | --- |
| `CATALOG_REPOSITORY` | lädt und validiert `SOURCES`, `RR_CATALOG`, `RUL_CATALOG`, `RR_APPLICABILITY` und `RR_MEASURE_CATALOG` fail-closed; stellt sie schreibgeschützt und mit Version bereit | Katalogdateien | `CatalogVersionSet`, `SourceReference` |
| `ASSESSMENT_SERVICE` | Lebenszyklus einer Bewertung, Produkteingaben, Orchestrierung der Engines | Nutzereingaben, `CatalogVersionSet`, Lesesicht auf `RR` | `Assessment`, `ProductProfile`, `RequirementResult` |
| `RULE_ENGINE` | führt `RUL` deterministisch aus, behandelt Review-Ausgänge, aggregiert Klassen nach `class_order`, protokolliert den Pfad | `RUL_CATALOG`, `ProductProfile` | `RuleExecution`, `DecisionResult` |
| `APPLICABILITY_ENGINE` | bestimmt anwendbare `RR` anhand von Entscheidungsergebnissen und dokumentierten Applicability-Regeln; begründet Nicht-Anwendbarkeit | `DecisionResult`, `RR_CATALOG`, `RUL_CATALOG` | `ApplicableRequirement` |
| `REQUIREMENT_SERVICE` | liefert `RR` mit Texten und Quellenlokatoren | `RR_CATALOG`, `SOURCES` | Lesesicht auf `RR` |
| `GAP_ENGINE` | verwaltet Erfüllungsstatus, Begründung und Gap-Ermittlung | `ApplicableRequirement`, `EvidenceReference`, vorgesehene Maßnahmen als Werte | `GapAssessment`, Gap-Ergebnis je `RR` |
| `EVIDENCE_SERVICE` | verwaltet nutzerseitig angegebene Nachweisreferenzen | Nutzereingaben | `EvidenceReference` |
| `REPORTING` | erzeugt Ergebnisberichte aus einem unveränderlichen Snapshot | alle Ergebnisobjekte, `I18N` | `ReportSnapshot` |
| `I18N` | zentrale DE/EN-Texte der Oberfläche und des Berichts; regulatorische Texte kommen aus den Katalogen | Sprachressourcen, Kataloge | Textauflösung |
| `AUDIT_LOG` | nur anhängendes Ereignisprotokoll | Ereignisse der Module | `AuditEvent` |
| `ASSESSMENT_REPOSITORY` | Speicherschnittstelle für versionierte Bewertungsdokumente mit Anhängeregel; austauschbare Implementierung | Bewertungsdokumente | gespeicherte Revisionen und Audit-Einträge |
| `APPLICATION_API` | lokaler Adapter zwischen Oberfläche und Anwendungseinstieg: übersetzt Anfragen in Aufrufe des `AssessmentApplicationService` und seiner Sichten, Fehler in stabile Codes; Composition Root des lokalen Servers; keine Fachlogik | Anfragen der Oberfläche | JSON-Antworten, Berichtsdateien |
| `PRESENTATION` | Fragebogen, Anzeige, Sprachwahl; enthält keine regulatorische Logik | `APPLICATION_API`, `I18N` | — |

Die Zuordnung der Systemanforderungen zu den Modulen steht ausschließlich im Feld `allocated_modules` von [../02-requirements/SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml).

## 4. Abhängigkeitsregeln

| Modul | darf abhängen von |
| --- | --- |
| `PRESENTATION` | `APPLICATION_API`, `I18N` |
| `APPLICATION_API` | `ASSESSMENT_SERVICE`, `CATALOG_REPOSITORY`, `GAP_ENGINE`, `EVIDENCE_SERVICE`, `REPORTING`, `I18N`, `ASSESSMENT_REPOSITORY` (nur Composition Root: Erzeugung der Persistenzimplementierung) |
| `ASSESSMENT_SERVICE` | `CATALOG_REPOSITORY`, `ASSESSMENT_REPOSITORY`, `RULE_ENGINE`, `APPLICABILITY_ENGINE`, `REQUIREMENT_SERVICE`, `GAP_ENGINE`, `EVIDENCE_SERVICE`, `REPORTING`, `AUDIT_LOG` |
| `RULE_ENGINE` | `CATALOG_REPOSITORY`, `AUDIT_LOG` |
| `APPLICABILITY_ENGINE` | `CATALOG_REPOSITORY`, `REQUIREMENT_SERVICE`, `AUDIT_LOG` |
| `REQUIREMENT_SERVICE` | `CATALOG_REPOSITORY` |
| `GAP_ENGINE` | `EVIDENCE_SERVICE`, `AUDIT_LOG` |
| `EVIDENCE_SERVICE` | `AUDIT_LOG` |
| `REPORTING` | `REQUIREMENT_SERVICE`, `CATALOG_REPOSITORY`, `I18N`, `AUDIT_LOG` |
| `I18N` | `CATALOG_REPOSITORY` |
| `CATALOG_REPOSITORY` | — |
| `AUDIT_LOG` | — |
| `ASSESSMENT_REPOSITORY` | — |

Keine Engine und kein Service hängt von `PRESENTATION` oder `APPLICATION_API` ab. Die Entscheidungsmodule sind damit ohne Oberfläche testbar. `PRESENTATION` (Browser-Oberfläche unter `web/`) erreicht den Kern ausschließlich über die HTTP-Schnittstelle von `APPLICATION_API`; `GAP_ENGINE` und `EVIDENCE_SERVICE` nutzt `APPLICATION_API` nur für Wertobjekte (`GapAssessment`, `GapStatus`, `EvidenceReference`) der Anfragen, nicht für Operationen.

## 5. Ablauf einer Bewertung

1. `ASSESSMENT_SERVICE` legt ein `Assessment` an und fixiert das `CatalogVersionSet` des `CATALOG_REPOSITORY`.
2. `PRESENTATION` erfragt kontrollierte Eingaben; die Fragen und zulässigen Werte stammen aus dem `RUL_CATALOG`.
3. `RULE_ENGINE` führt die Regelpfade ab den Einstiegspunkten aus und erzeugt je Entscheidungsbereich ein `DecisionResult` mit den zugehörigen `RuleExecution`.
4. `APPLICABILITY_ENGINE` bestimmt die `ApplicableRequirement`; Anforderungen ohne belastbar bestätigte Bedingung bleiben `APPLICABILITY_UNRESOLVED`.
5. Der Nutzer bewertet die anwendbaren `RR` und referenziert Nachweise; `GAP_ENGINE` führt `GapAssessment`, `EVIDENCE_SERVICE` die `EvidenceReference`.
6. `REPORTING` friert den Stand als `ReportSnapshot` ein und erzeugt daraus den Bericht.
7. Jeder fachliche Schritt erzeugt ein `AuditEvent`.

## 6. Datenmodell

Das fachliche Datenmodell steht maschinenlesbar in [DATA_MODEL.yaml](DATA_MODEL.yaml) und wird mit `tools/validate_data_model.py` geprüft. Es ist ein konzeptionelles Modell ohne Persistenz- oder Technologieentscheidung. Die wesentlichen Invarianten stehen dort je Entität.

## 7. Bewusst offene Entscheidungen

- Bereitstellung außerhalb des lokalen Demonstrators (Hosting, Mehrbenutzerbetrieb, Store-Auslieferung); Frontend-Stack und Interaktionskonzept sind mit ADR-0007 (Entwicklungsarchiv) und [WEB_APPLICATION.md](WEB_APPLICATION.md) entschieden;
- Gap-Filter-Regeln als `RUL` nach Pfad 1 ([DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 5): Die Anwendbarkeit bedingter `RR` ist stattdessen maschinenlesbar in [RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) abgebildet und wird vom `APPLICABILITY_ENGINE` ausgewertet; nicht modellierte Bedingungen bleiben `APPLICABILITY_UNRESOLVED`.

## 8. Laufzeitumsetzung

Technologie nach ADR-0003 (Entwicklungsarchiv): Python-Paket `regscoutx/` ohne Framework-Abhängigkeit, Tests unter `tests/`.

| Modul | Umsetzung | Stand |
| --- | --- | --- |
| `CATALOG_REPOSITORY` | `regscoutx/catalog_repository.py`; Validierung ausschließlich über `regscoutx/_validation.py` und die Validatoren unter `tools/` | umgesetzt |
| `RULE_ENGINE` | `regscoutx/rule_engine.py`; Domainobjekte in `regscoutx/domain.py`, Domain-Fehler in `regscoutx/errors.py` | umgesetzt |
| `APPLICABILITY_ENGINE` | `regscoutx/applicability_engine.py`; Zuordnung aus `docs/03-regulatory/RR_APPLICABILITY.yaml` über `CATALOG_REPOSITORY`; Herleitung je `RR` über `explain` (SR-042) | umgesetzt |
| `REQUIREMENT_SERVICE` | `regscoutx/requirement_service.py`; Lesesicht je `RR` mit Texten, Quellen, Lebenszyklusphasen (SR-041) und vorgesehenen Maßnahmen (SR-043) | umgesetzt |
| `ASSESSMENT_SERVICE` | `regscoutx/assessment_service.py` (zustandsloser Kern: `Assessment`, `ProductProfile`, `AssessmentInput`, `RRResult`, `AssessmentSummary`, Neuberechnung, Differenzen); `regscoutx/assessment_application.py` (Anwendungseinstieg: Lebenszyklus, Revisionen, Versionsabgleich, Audit, Nachweisoperationen); `regscoutx/assessment_codec.py` (Persistenzschema) | umgesetzt (D2) |
| `ASSESSMENT_REPOSITORY` | `regscoutx/assessment_repository.py` (Schnittstelle, Hülle, Anhängeregel); `regscoutx/json_assessment_repository.py` (lokale JSON-Dateien, ADR-0005 (Entwicklungsarchiv), Format: [PERSISTENCE_FORMAT.md](PERSISTENCE_FORMAT.md)) | umgesetzt (D2) |
| `GAP_ENGINE` | `regscoutx/gap_engine.py`; `GapAssessment`, Ableitung genau eines Gap-Status je `RR` | umgesetzt (D1) |
| `EVIDENCE_SERVICE` | `regscoutx/evidence_service.py`; Prüfung, Register, Hinzufügen, Ändern, Entfernen, Abruf und Filter nach Maßnahme nutzerseitiger `EvidenceReference` | umgesetzt (D2, keine Dokumentablage) |
| `AUDIT_LOG` | `regscoutx/audit_log.py`; nur anhängendes Protokoll je Bewertung, persistiert mit dem Bewertungsdokument | umgesetzt (D2; `REPORT_CREATED` seit D3) |
| `REPORTING` | `regscoutx/report_model.py` (ReportSource, sprachneutrales ReportModel), `report_document.py` (Gliederung und Texte), `report_html.py`, `report_pdf.py` (Renderer), `report_service.py` (Fassade); Konzept: [REPORTING.md](REPORTING.md), Entscheidung: ADR-0006 (Entwicklungsarchiv) | umgesetzt (D3) |
| `I18N` | `regscoutx/i18n.py` mit `regscoutx/resources/i18n/de.json`, `en.json`; Code-Bezeichnungen aus `enum_labels`, Themen und Phasen aus dem Vokabular | umgesetzt für den Bericht (D3) |
| `I18N` (Oberfläche) | dieselben Ressourcen unter dem Präfix `ui.`; Auslieferung als Sprachpaket über `APPLICATION_API` | umgesetzt (D4) |
| `APPLICATION_API` | `regscoutx/web_api.py` (Routen, Fehlercodes), `regscoutx/web_server.py` (lokaler Server, Composition Root); Sichten `regscoutx/questionnaire.py` und `regscoutx/assessment_views.py` gehören zu `ASSESSMENT_SERVICE`; Entscheidung: ADR-0007 (Entwicklungsarchiv) | umgesetzt (D4) |
| `PRESENTATION` | `web/` (React, TypeScript, Vite; Shared Product Core, Domain UI, Experience Profile); Konzept: [WEB_APPLICATION.md](WEB_APPLICATION.md), Leitlinie: [UI_UX_DESIGN_SYSTEM.md](UI_UX_DESIGN_SYSTEM.md) | umgesetzt (D4) |

**Semantik der Engine** (ausschließlich aus [RUL_METHOD.md](../03-regulatory/RUL_METHOD.md) und dem Katalog, keine regulatorischen Inhalte im Code):

- Je Regel genau ein Zweig passend zum Eingabewert; `bool` und Zeichenketten werden nicht vermischt.
- Unbekannte, abgeleitete oder unzulässige Eingaben werden als `InvalidInputError` abgewiesen; fehlt ein entscheidungsnotwendiger Wert, endet der Pfad mit Status `INCOMPLETE` und benennt Regel und Eingabeschlüssel.
- Abgeleitete Eingaben: bei genau einem zulässigen Wert dieser Wert; bei booleschen Werten `true`, wenn auf dem Pfad in derselben Kategorie bereits ein Klassenkandidat oder Review-Ausgang entstanden ist; jede andere Form wird als `UnsupportedDerivationError` abgewiesen.
- Die ausgeführten Regeln werden je Kategorie zu einem `DecisionResult` zusammengefasst. Ein Review-Ausgang ergibt `REVIEW_REQUIRED` ohne Klasse; ohne Review-Ausgang ist die finale MDR-Klasse der strengste Klassenkandidat nach `class_order`.
- Zyklen, ungültige `next`-Verweise und Zweige ohne Ergebnis und Folgeregel werden als Domain-Fehler abgewiesen.
- IDs werden als UUIDv5 aus Einstiegsregel, Eingaben und Katalogversionen gebildet; gleiche Eingaben ergeben gleiche Ergebnisse einschließlich IDs.
- Sichtbare Texte (Fragen, Ausgabebezeichnungen, Review-Ursachen) werden über `CatalogRepository` aus den DE/EN-Feldern des Katalogs aufgelöst; die Engine arbeitet nur mit Codes.
- Datumseingaben (`date`) werden als ISO-Datum an Stichtagen verzweigt (`before`/`on_or_after`); ein Zweig kann zusätzlich eine `date_condition` auf einen Datumseingang tragen. Parallele Rechtswege (AI-Act-Routing, `RUL-043`) werden generisch nach [../03-regulatory/RUL_METHOD.md](../03-regulatory/RUL_METHOD.md) Abschnitt 8.1 aggregiert; `DecisionResult` trägt dann `applicable_from` und `compliance_flags`. Die AI-Act-Regeln laufen ab dem Einstiegspunkt `RUL-027` als eigener Entscheidungsbereich `AI_ACT_APPLICABILITY`.
- Die beiden abgeleiteten Eingaben (`RUL-015`, `RUL-019`) sind technische Graph-Ableitungen; der Nachweis steht in [../03-regulatory/RR_APPLICABILITY_MAPPING.md](../03-regulatory/RR_APPLICABILITY_MAPPING.md) Abschnitt 5.

**Semantik des `APPLICABILITY_ENGINE`:**

- Eingaben sind die `DecisionResult`s des `RULE_ENGINE` (höchstens eines je Bereich) und kontrollierte Applicability-Eingaben aus `RR_APPLICABILITY.yaml`; unbekannte oder unzulässige Eingaben werden als `InvalidInputError` abgewiesen.
- Prädikate sind dreiwertig (`TRUE`, `FALSE`, `UNKNOWN`) und werden nur über Entscheidungsergebnisse mit Status `DECIDED`, über die MDR-Klasse oder über Eingaben bestimmt; `ALL_OF`/`ANY_OF` kombinieren sie, `NOT_MODELLED` ist stets `UNKNOWN`.
- Je `RR` wird zuerst der Block, dann die lokale Bedingung ausgewertet: inaktiver Block `NOT_APPLICABLE`, ungeklärter Block, nicht dokumentierte Einordnung, fehlende Eingabe, nicht modellierte Bedingung oder fehlende Zuordnung `APPLICABILITY_UNRESOLVED`.
- Für referenzierte, aber nicht ausgewertete Bereiche (z. B. `AI_ACT_APPLICABILITY` ohne Ausführung von `RUL-027`) entsteht ein `DecisionResult` mit Status `NOT_EVALUATED`, auf das die betroffenen `RR` über `determined_by` verweisen.
- Ein `false_if`-Eintrag kann einen eigenen Begründungscode tragen (z. B. `SCOPE_NOT_YET_APPLICABLE`, `SCOPE_LEGACY_TRANSITION`), damit der zeitliche bzw. Übergangsgrund einer Nicht-Aktivierung erhalten bleibt.
- Anforderungstexte werden nicht gelesen; das Ergebnis ist unabhängig von `requirement_text` (geprüft in `tests/test_applicability_engine.py`).
- `explain` stellt je `RR` Anwendbarkeit, Begründungscode, Block, Prädikate, Eingaben, herangezogene Entscheidungsergebnisse mit ihren `RUL` und die Quellenlokatoren aus der bestehenden Trace-Struktur zusammen; es findet keine neue Bewertung statt.

**Semantik von `ASSESSMENT_SERVICE` und `GAP_ENGINE`** (Entscheidung: ADR-0004 (Entwicklungsarchiv)):

- Ein `Assessment` fixiert das `CatalogVersionSet` und enthält Produktprofil, Erfüllungsbewertungen (`GapAssessment`), Nachweisreferenzen, Regelläufe, Entscheidungsergebnisse, genau ein `RRResult` je `RR` und Summen. Das Ergebnisschema ist [DATA_MODEL.yaml](DATA_MODEL.yaml); `schema_version` ist dessen Version im `CatalogVersionSet`.
- Das `ProductProfile` ist flach. Jeder Schlüssel ist eine Applicability-Eingabe oder gehört zu genau einem Einstiegspunkt (Schlüsselmenge aller von dort erreichbaren, nicht abgeleiteten Regeln); ein Einstiegspunkt wird ausgewertet, wenn das Profil mindestens einen seiner Schlüssel enthält, sonst bleibt der Bereich `NOT_EVALUATED`. Unbekannte Schlüssel werden abgewiesen.
- `RRResult` konsumiert unverändert: Katalogtexte DE/EN, Themencluster und Lebenszyklusphasen mit Vokabularbezeichnungen (SR-041) sowie vorgesehene Maßnahmen und Nachweisarten (SR-043) über `REQUIREMENT_SERVICE`; `ApplicableRequirement` und `ApplicabilityEngine.explain` (SR-042); das Gap-Ergebnis der `GAP_ENGINE`. Die Herleitung ist damit Eingabe → Prädikat → `RUL`/Entscheidung → Anwendbarkeit → `RR` → Gap-Status mit eigenem, nicht-regulatorischem `gap_reason`.
- Ableitungstabelle des Gap-Status (einzige Stelle im Code: `gap_engine._derive`):

| Anwendbarkeit | Erfüllungsbewertung | Nachweisreferenz | `gap_result` | `gap_reason` | Gap |
| --- | --- | --- | --- | --- | --- |
| `NOT_APPLICABLE` | beliebig (dann `INACTIVE`) | — | `NOT_APPLICABLE` | `RR_NOT_APPLICABLE` | nein |
| `APPLICABILITY_UNRESOLVED` | beliebig (dann `INACTIVE`) | — | `APPLICABILITY_UNRESOLVED` | `RR_APPLICABILITY_UNRESOLVED` | nein |
| `APPLICABLE` | keine | — | `NOT_ASSESSED` | `NO_ANSWER` | nein |
| `APPLICABLE` | `NOT_ASSESSED` | beliebig | `NOT_ASSESSED` | `ANSWER_NOT_ASSESSED` | nein |
| `APPLICABLE` | `NOT_FULFILLED` | beliebig | `NOT_FULFILLED` | `ANSWER_NOT_FULFILLED` | ja |
| `APPLICABLE` | `FULFILLED` / `PARTIALLY_FULFILLED` | vorhanden | `FULFILLED` / `PARTIALLY_FULFILLED` | `ANSWER_WITH_EVIDENCE` | nur bei teilweise |
| `APPLICABLE` | `FULFILLED` / `PARTIALLY_FULFILLED` | fehlt | `EVIDENCE_REVIEW_REQUIRED` | `ANSWER_WITHOUT_EVIDENCE` | ja (Nachweislücke, SR-015) |
| `APPLICABLE` | beliebig, aber `stale` (`REACTIVATED_REVIEW_REQUIRED`, seit D2) | nicht berücksichtigt | `NOT_ASSESSED` | `ANSWER_REVIEW_REQUIRED` | nein |

- Erfüllungsstatus entstehen nur aus einer `GapAssessment` (SR-013); `NOT_APPLICABLE` ist nicht setzbar; `FULFILLED`, `PARTIALLY_FULFILLED` und `NOT_FULFILLED` verlangen eine nicht leere Begründung (SR-014), deren Inhalt nie ausgewertet wird. Eine vorhandene Nachweisreferenz belegt keine Erfüllung; eine fehlende ist nie `NOT_FULFILLED`.
- Drei getrennte Nachweisbegriffe: vorgesehene Maßnahme und Nachweisart aus `RR_MEASURE` (`RRResult.measure`, bei `REVIEW_REQUIRED` genau dieser Status ohne Maßnahme), nutzerseitige `EvidenceReference` (`RRResult.gap.evidence`) und Projektevidenz `EV-NNN` (nur unter `docs/09-evidence/`). Ein `measure_key` muss eine vorgesehene Maßnahme jeder `RR` sein, die die Referenz nutzt; je Maßnahme wird ausgewiesen, ob eine Referenz mit diesem `measure_key` vorliegt.
- Neuberechnung (SR-040): `recalculate` ersetzt das Profil bzw. ergänzt Bewertungen und Referenzen und wertet vollständig neu aus; das Ergebnis ist identisch mit einer frischen Auswertung desselben Eingabestands. Bewertungen nicht anwendbarer `RR` bleiben als `INACTIVE` erhalten und werden bei erneuter Anwendbarkeit `REACTIVATED_REVIEW_REQUIRED` (seit D2, siehe unten); `AssessmentChange` weist geänderte Eingaben sowie de- und reaktivierte Bewertungen aus, `AUDIT_LOG` die Ereignisse. Abweichende Katalogversionen (SR-037) und nicht im Zustand `DRAFT` befindliche Bewertungen werden abgewiesen; bei jedem Fehler bleibt die Ausgangsbewertung unverändert.
- Fail-closed: strukturell ungültige Kataloge (auch eine fehlende oder unzulässige `RR_MEASURE`-Zuordnung) ergeben einen harten Fehler ohne Teilergebnis; fachlich nicht entscheidbare Anwendbarkeit ergibt `APPLICABILITY_UNRESOLVED`; fehlende Bewertung `NOT_ASSESSED`.
- Reproduzierbarkeit: `Assessment.fingerprint` ist SHA-256 über die kanonische fachliche Form; Assessment-ID, Zeitpunkte (`created_at`, `assessed_at`, Audit), Sprache, Zustand und `AssessmentChange` gehen nicht ein.
- Sichtbare Bezeichnungen der Ausgabecodes stehen zentral in `enum_labels` von [DATA_MODEL.yaml](DATA_MODEL.yaml); der Kern liefert nur Codes und Katalogtexte.

**Anwendungseinstieg und Persistenz** (Entscheidung: ADR-0005 (Entwicklungsarchiv)):

- `AssessmentApplicationService` ist der einzige Zugang späterer Adapter: anlegen, öffnen, Versionen prüfen, Profil ändern, Erfüllungsbewertung setzen/bestätigen, Nachweisreferenz hinzufügen/ändern/entfernen/zuordnen, neu berechnen, abschließen, wieder öffnen, mit aktuellem Katalogstand neu bewerten, Revisionen und Audit lesen. Er hängt nur von der Schnittstelle `AssessmentRepository` ab; die Implementierung wird von außen übergeben.
- Revisionen: nur die letzte Revision ist änderbar und nur im Zustand `DRAFT`; jede Änderung wertet vollständig neu aus und legt die Vorher/Nachher-Differenz (`AssessmentChange`: Eingaben, Anwendbarkeit, Gap-Status, de-/reaktivierte Bewertungen, Nachweisreferenzen) in der Revision und zusammengefasst im Audit ab. `finalise` setzt `FINALISED` (nicht bei offenen Bestätigungen); `reopen` erzeugt eine neue `DRAFT`-Revision; gespeicherte Revisionen bleiben unverändert (Anhängeregel im Repository).
- Versionsabgleich beim Öffnen (SR-037): `MATCH` stellt die Auswertung aus den gespeicherten Eingaben wieder her und prüft Fingerprint und Ergebnissicht gegen den gespeicherten Stand (Abweichung fail-closed). `MISMATCH` und `INCOMPLETE_VERSION_INFO` liefern nur den gespeicherten, katalogunabhängigen Stand und protokollieren `CATALOG_VERSION_MISMATCH_DETECTED`; Schreiboperationen werden abgewiesen. Nur bei `MISMATCH` erzeugt `rebase` bewusst eine neue Revision gegen die aktuellen Kataloge; Entscheidungen werden nicht migriert, sondern neu bestimmt.
- Wieder anwendbare Bewertungen: Das System markiert eine Bewertung als `stale`, sobald ihre `RR` nicht anwendbar ist. Wird die `RR` wieder anwendbar, ist die Bewertung `REACTIVATED_REVIEW_REQUIRED`, fließt nicht ein (`NOT_ASSESSED`/`ANSWER_REVIEW_REQUIRED`) und wird erst durch `confirm_gap_assessment` oder eine neue Bewertung wieder `ACTIVE`.
- Audit: jede Operation erzeugt Ereignisse mit Revision, fortlaufender Nummer, Zeitpunkt (Metadatum), betroffener Kennung und strukturierten Codes; Begründungen, Dokumenttitel und -kennungen werden nicht protokolliert.

**Reporting und Sprachausgabe** (Entscheidung: ADR-0006 (Entwicklungsarchiv), Konzept: [REPORTING.md](REPORTING.md)):

- `AssessmentApplicationService.create_report` bzw. `report_model` bilden aus einer gespeicherten Revision eine `ReportSource`; bei `MATCH` wird die Revision vorher gegen eine Neuauswertung geprüft. `REPORTING` baut daraus das sprachneutrale, unveränderliche `ReportModel` (`ReportSnapshot`), `ReportComposer` das formatneutrale Dokument mit allen sichtbaren Texten, die Renderer HTML bzw. PDF. Nichts wird neu berechnet.
- Katalogtexte nur bei `MATCH`; historische Stände zeigen Codes und einen Hinweis. `content_hash` ist unabhängig von Format und Zeitpunkt. Nach Erfolg `REPORT_CREATED` im Audit; Renderer-Fehler werden als `ReportGenerationError` gemeldet und ändern weder Bewertung noch Audit (SR-036).
- Renderer importieren nur Dokumentblöcke; ReportLab nur in `report_pdf.py` (statisch geprüft in `tests/test_architecture.py`).

**Web-Anwendung und Anwendungs-API** (Entscheidung: ADR-0007 (Entwicklungsarchiv), Konzept: [WEB_APPLICATION.md](WEB_APPLICATION.md)):

- Der adaptive Fragebogen (`questionnaire.py`) leitet Fragen, Folgefragen mit Auslöser (Regel, Frage, Antwort), zulässige Werte mit Folge je Wert (Ergebnis, Prüfpunkt, Folgeregel), Stichtage von Datumsfragen, Segmentstatus und nicht mehr verwendete Angaben ausschließlich aus RUL-Katalog, Applicability-Zuordnung und gespeicherter Auswertung ab. Applicability-Eingaben werden gefragt, sobald eine Anforderung ein Prädikat mit dieser Eingabe auswertet; der Grund nennt die betroffenen Blöcke mit Anzahl.
- Die Sichten (`assessment_views.py`) verdichten gespeicherte Ergebnisse und das D3-`ReportModel` zu Regulatory Spine, Blockzuständen, Anforderungsdetail mit Herleitung und Compliance-Matrix (Themencluster × Lebenszyklusphase); sie entscheiden nichts neu.
- Lesende Zugriffe (`read`) protokollieren nichts; nur das bewusste Öffnen (`open`) protokolliert eine Versionsabweichung, nur die Berichtsdatei `REPORT_CREATED`. Lesen verändert weder Fingerprint noch Audit (geprüft in `tests/test_web_application.py`).
- Der Server bindet ausschließlich an localhost, prüft den Host-Header (DNS-Rebinding), weist seitenfremde Anfragen (`Sec-Fetch-Site`) ab, verlangt für schreibende Anfragen den Header `X-RegScoutX-Request: 1` und JSON bis 1 MB, setzt eine strikte Content-Security-Policy ohne Inline-Skripte und -Stile und gibt statische Dateien pfadsicher aus. Keine CORS-Freigabe, keine Protokollierung von Inhalten, keine externen Verbindungen.

**Gemeinsamer Domain-Kern:** `regscoutx/domain.py`, `regscoutx/errors.py` und die Validierungsbrücke `regscoutx/_validation.py` sind modulübergreifend nutzbar. Der Namensraum der deterministischen IDs (`ID_NAMESPACE`) liegt im Domain-Kern, damit `APPLICABILITY_ENGINE` nicht von `RULE_ENGINE` abhängt; aus demselben Grund liegen `ApplicableRequirement`, `Applicability`, `EvaluatedPredicate` und `TriState` dort, damit `GAP_ENGINE` sie ohne Abhängigkeit vom `APPLICABILITY_ENGINE` liest. Die Abhängigkeitsregeln aus Abschnitt 4 und die Zyklenfreiheit werden in `tests/test_architecture.py` statisch geprüft.

## 9. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der logischen Modularchitektur: Leitprinzipien, elf Module mit Verantwortungen, Abhängigkeitsregeln, Ablauf einer Bewertung, Verweis auf das fachliche Datenmodell und bewusst offene Entscheidungen. |
| 1.1 | Abschnitt 8 ergänzt: Laufzeitumsetzung von `CATALOG_REPOSITORY` und `RULE_ENGINE` nach ADR-0003 und Semantik der Engine; Programmiersprache aus Abschnitt 7 durch ADR-0003 entschieden. |
| 1.2 | Abschnitt 8 um `APPLICABILITY_ENGINE` und dessen Semantik ergänzt; Statuscode `APPLICABILITY_UNRESOLVED` statt `UNDETERMINED`. |
| 1.3 | Abschnitt 8: Datumseingaben, `date_condition`, Aggregation paralleler Routen, `applicable_from`/`compliance_flags` und Begründungscodes für zeitliche bzw. Übergangs-Nicht-Aktivierung ergänzt (AI-Act-Routing `RUL-027` bis `RUL-043`). |
| 1.4 | Abschnitt 1: Verweis auf die wissenschaftliche Herleitung der bestehenden Entscheidungen aus dem Stand der Technik; Abschnitt 7: Grundlage des offenen Interaktionskonzepts benannt. Keine Architekturänderung. |
| 1.5 | Abschnitt 8: `REQUIREMENT_SERVICE` teilweise umgesetzt, `explain` des `APPLICABILITY_ENGINE`, gemeinsamer Domain-Kern mit `ID_NAMESPACE` (Abhängigkeit `APPLICABILITY_ENGINE` → `RULE_ENGINE` entfernt) und statische Prüfung der Abhängigkeitsregeln. Keine Änderung der Module oder Abhängigkeitsregeln. |
| 1.6 | Abschnitt 3: `CATALOG_REPOSITORY` lädt zusätzlich `RR_APPLICABILITY` und `RR_MEASURE_CATALOG`; deren Versionen sind Teil des `CatalogVersionSet` (DATA_MODEL 0.5). Keine Änderung an Modulen oder Abhängigkeiten. |
| 1.7 | Demonstrator D1: `ASSESSMENT_SERVICE`, `GAP_ENGINE`, `EVIDENCE_SERVICE` und `AUDIT_LOG` umgesetzt; Abschnitt 4: `ASSESSMENT_SERVICE` darf zusätzlich `CATALOG_REPOSITORY` und `REQUIREMENT_SERVICE` nutzen (ADR-0004 (Entwicklungsarchiv)); Abschnitt 8: Semantik und Ableitungstabelle des Gap-Status, Neuberechnung, Fingerprint; Applicability-Domainobjekte im gemeinsamen Kern. |
| 1.8 | Demonstrator D2: Modul `ASSESSMENT_REPOSITORY` (Schnittstelle und lokale JSON-Dateipersistenz, ADR-0005 (Entwicklungsarchiv)); `ASSESSMENT_SERVICE` darf davon abhängen; Anwendungseinstieg mit Revisionen, Versionsabgleich und Audit; Lebenszyklus wieder anwendbarer Bewertungen; offene Entscheidung „Persistenz“ aus Abschnitt 7 geschlossen. |
| 1.9 | Verweis auf die führende UI/UX-Leitlinie [UI_UX_DESIGN_SYSTEM.md](UI_UX_DESIGN_SYSTEM.md) (Version 1.1); keine Änderung an Modulen, Abhängigkeiten oder Semantik. |
| 1.10 | Demonstrator D3: `REPORTING` und `I18N` umgesetzt (ADR-0006 (Entwicklungsarchiv), [REPORTING.md](REPORTING.md)); offene Entscheidung „Berichtsformat“ geschlossen; keine Änderung der Abhängigkeitsregeln. |
| 1.11 | Demonstrator D4: Modul `APPLICATION_API` (lokaler HTTP-Adapter und Composition Root, ADR-0007 (Entwicklungsarchiv)); `PRESENTATION` hängt nur noch von `APPLICATION_API` und `I18N` ab; Fragebogen und Sichten als Teil von `ASSESSMENT_SERVICE`; SHA-256 der UI/UX-Leitlinie 1.1 dokumentiert; offene Entscheidung „Frontend-Stack und Interaktionskonzept“ geschlossen. |
| 1.12 | Einleitung und Abschnitt 7 an den umgesetzten Stand angeglichen (Technologie in ADR-0003 bis ADR-0007; Anwendbarkeit bedingter `RR` über `RR_APPLICABILITY`); Stand von `AUDIT_LOG` in Abschnitt 8 berichtigt. Keine Änderung an Modulen, Abhängigkeiten oder Semantik. |
