# Methode der regelbasierten Entscheidungslogik (RUL)

Version 1.2 · Status: aktiv

Diese Methode legt fest, wie Entscheidungsregeln (`RUL`) für die Applicability-, Qualifikations-, Klassifikations- und Routing-Logik von RegScoutX formuliert, verankert, versioniert und geprüft werden. Sie ergänzt [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) und wiederholt deren ID-, Status-, Lebenszyklus-, Lokator- und Traceability-Regeln nicht. [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) bleibt ausschließlich für regulatorische Anforderungen (`RR`) maßgeblich; es entsteht keine Parallelmethodik.

---

## 1. Gegenstand und Abgrenzung

Eine `RUL` ist hier ausschließlich eine **regelbasierte, reproduzierbare Applicability-, Qualification-, Classification- oder Routing-Regel**. Sie bestimmt, welcher regulatorische Pfad, welche Einordnung oder welche Klasse sich aus kontrollierten Eingaben ergibt.

Eine `RUL` ist **keine** regulatorische Anforderung:

- Sie hat keinen Erfüllungsstatus und erzeugt keinen Gap.
- Sie darf nicht verwendet werden, um eine extrahierbare Compliance-/Gap-Anforderung zu umgehen (Schutzregel nach [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 5).
- Die hier geregelten `RUL` folgen dem Traceability-Pfad 2 (`SRC → RUL → TC → EV`) mit direktem, verifiziertem `SRC`-Lokator. `RUL` der späteren Gap-Logik (Pfad 1, `SRC → RR → RUL`) sind nicht Gegenstand von Version 1.0 dieser Methode.

## 2. Führende Vergabestelle und Format

Führende Vergabestelle und Single Source of Truth für `RUL` ist:

`docs/03-regulatory/RUL_CATALOG.yaml`

`RUL`-IDs werden ausschließlich dort vergeben. Alle anderen Dokumente referenzieren sie nur.

Das Format ist **YAML**, aus denselben Gründen wie für den Anforderungskatalog ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 10.2): menschenlesbar, im Diff reviewbar, maschinenlesbar, native Listen und verschachtelte DE/EN-Texte. Die Entscheidung ist begrenzt und reversibel und wird deshalb hier und nicht als eigener ADR geführt.

## 3. Kontrollierte Werte

Die folgenden Wertelisten sind führend; der Validator liest sie aus diesem Abschnitt.

Zulässige Kategorien:

`QUALIFICATION` · `BOUNDARY` · `CLASSIFICATION` · `MODULES` · `CHANGE_REASSESSMENT` · `AI_ACT_APPLICABILITY`

Zulässige Eingabetypen:

`boolean` · `enum` · `derived` · `date`

Zulässige Guidance-Rollen:

`INTERPRETATIVE` · `CLARIFIES` · `CROSSWALK`

Zulässige Ausgabetypen:

`RESULT` · `CLASS_CANDIDATE` · `REVIEW`

Zulässige Basis-Kennzeichnungen:

`GUIDANCE_INTERPRETATION`

| Wert | Bedeutung |
| --- | --- |
| `QUALIFICATION` | Ist die Software durch die Medizinprodukteverordnungen erfasst bzw. MDSW? |
| `BOUNDARY` | Abgrenzung MDR/IVDR für festgestellte MDSW |
| `CLASSIFICATION` | MDR-Klassifikation einschließlich Aggregation nach Anhang VIII Abschnitt 3.5 |
| `MODULES` | Qualifikations- und Klassifikationslogik modularer Software |
| `CHANGE_REASSESSMENT` | Auslöser einer erneuten Prüfung von Qualifikation und Klassifikation |
| `AI_ACT_APPLICABILITY` | Anwendbarkeit des AI Act und Hochrisiko-Routing nach Art. 6 |
| `boolean` | Ja/Nein-Eingabe; `allowed_values` ist `[true, false]` |
| `enum` | Auswahl aus einer geschlossenen Werteliste |
| `derived` | Eingabe wird nicht erfragt, sondern ergibt sich deterministisch aus dem bisherigen Regelpfad nach Abschnitt 8.1; die Ableitung ist in `decision_logic` beschrieben |
| `date` | ISO-Datum (`JJJJ-MM-TT`); `allowed_values` enthält nur zusätzlich zulässige Kennwerte (z. B. `UNKNOWN`), ggf. leer |
| `INTERPRETATIVE` | Die Guidance operationalisiert oder legt Primärrecht für Software aus. |
| `CLARIFIES` | Die Guidance bestätigt oder erläutert Primärrecht ohne zusätzliche Operationalisierung. |
| `CROSSWALK` | Die Guidance verknüpft Begriffe oder Pfade zweier Rechtsakte. |
| `RESULT` | Einordnungsergebnis eines Pfads (Zwischen- oder Endergebnis) |
| `CLASS_CANDIDATE` | Klassenkandidat einer einzelnen Klassifizierungsregel; **keine** finale Klasse |
| `REVIEW` | kontrollierter Review-Ausgang; **keine** automatische Entscheidung |
| `GUIDANCE_INTERPRETATION` | Der Zweig operationalisiert eine Guidance-Auslegung, die über den Wortlaut des Primärrechts hinausgeht; er muss als solche erkennbar bleiben. |

Die konkreten Ausgabewerte (`outputs`) mit DE/EN-Bezeichnung stehen im Katalog selbst.

## 4. Pflichtstruktur je `RUL`

Die Mindestfelder aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 6 (ID, Regelzweck, Eingangsgrößen, Bedingung, Ergebnis, Grundlage, Status) werden durch folgende Felder abgebildet:

| Feld | Inhalt |
| --- | --- |
| `id` | `RUL-NNN`; unveränderlich, fortlaufend, semantikfrei |
| `status` | Artefaktstatus aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3 |
| `category` | genau eine Kategorie aus Abschnitt 3 |
| `title.de` / `title.en` | Regelzweck als kurzer Titel |
| `question.de` / `question.en` | regulatorisch verständliche Nutzerfrage; bei `derived` ein Hinweis, dass keine Nutzerfrage gestellt wird |
| `input_key` | stabiler maschinenlesbarer Eingabeschlüssel |
| `input_type` | Eingabetyp aus Abschnitt 3 |
| `allowed_values` | geschlossene Liste zulässiger Werte |
| `value_labels` | bei `enum`: DE/EN-Bezeichnung je Wert; sonst `null` |
| `decision_logic` | präzise Beschreibung von Bedingung und Ergebnis |
| `branches` | je zulässigem Wert genau ein Zweig mit `when` sowie `result` und/oder `next`; optional `review` mit `review_cause.de` / `review_cause.en` und `basis`. Bei `date` genau zwei Datumszweige `when: {before: D}` und `when: {on_or_after: D}` mit demselben Stichtag D. Ein Zweig kann zusätzlich eine `date_condition` (`input_key` eines Datumseingangs und `before` bzw. `on_or_after`) tragen; dann gibt es für denselben `when`-Wert genau zwei komplementäre Zweige. |
| `primary_legal_anchor` | Liste mit mindestens einem präzisen Lokator einer Ebene-A-Quelle |
| `guidance_anchor` | Liste mit 0..n Lokatoren einer Ebene-B-Quelle; leer nur, wenn für die Regel keine adjudizierte Guidance vorliegt |
| `guidance_detail` | präzisierende Angabe innerhalb der Guidance-Fundstelle (z. B. Figure, Decision step) oder `null` |
| `guidance_role` | Guidance-Rolle aus Abschnitt 3; `null` bei leerem `guidance_anchor` |
| `rationale` | Begründung der Regel |
| `dependencies` | Liste der vorgelagerten `RUL`-IDs |
| `replaces` / `replaced_by` | Ersetzungsbeziehungen analog zu `RR` |

Die Felder `title_de`, `title_en`, `question_de` und `question_en` werden als verschachtelte Felder `title.de` usw. geführt, wie im Anforderungskatalog.

Auf Katalogebene werden zusätzlich geführt: `version`, `entry_points`, `class_order`, `outputs`, `flags`, `rules` und `change_history`. Ausgabewerte (`outputs`) können optional `aggregates_to` (Zielzustand für die Routenaggregation nach Abschnitt 8.1), `applicable_from` (ISO-Datum, ab dem der zugrunde liegende Rechtsweg anwendbar ist) und `flags` (Routing-/Compliance-Hinweise aus `flags`, jeweils mit Ebene-A-Anker) tragen. Ein Hinweis ist keine Anforderung und kein Erfüllungsstatus.

## 5. Rechtshierarchie

1. **Primary Law > Guidance Interpretation.** Jede `RUL` trägt einen `primary_legal_anchor` und, soweit adjudizierte Guidance vorliegt, getrennt davon einen `guidance_anchor`.
2. `primary_legal_anchor` darf ausschließlich Lokatoren von Quellen der Ebene A nach [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 4 enthalten; `guidance_anchor` ausschließlich Lokatoren von Quellen der Ebene B. Eine `RUL` nur mit Guidance-Anker ist unzulässig.
3. Guidance darf keine Rechtsfolge erzeugen, die im Primärrecht nicht verankert ist. Wo ein Zweig eine Guidance-Auslegung operationalisiert, die über den Wortlaut hinausgeht, trägt er `basis: GUIDANCE_INTERPRETATION`.
4. Beispiele aus Guidance validieren den Regelbaum als Testfälle, sind aber keine allgemeinen Rechtsregeln.

## 6. Determinismus

- Gleiche Eingaben führen zu gleichen Ausgaben.
- Jeder zulässige Eingabewert einer `RUL` hat genau einen Zweig; es gibt keine überlappenden oder fehlenden Zweige. Datumszweige teilen den Wertebereich lückenlos an einem Stichtag (`before` < D ≤ `on_or_after`).
- Keine freie Texteingabe als Entscheidungsgrundlage und **kein freies LLM-Urteil** innerhalb der Regelverarbeitung.
- Der Regelgraph ist azyklisch; jede aktive `RUL` ist von einem Einstiegspunkt (`entry_points`) aus erreichbar. Ersetzte oder zurückgezogene Regeln bleiben als Herkunftsnachweis im Katalog, sind aber weder ausführbare Einstiegspunkte noch zulässige Ziele aktiver Regeln.

## 7. Unzureichende Evidenz und Review-Ausgänge

- Fehlt eine Eingabe oder liegt sie außerhalb von `allowed_values`, erzeugt die `RUL` kein Ergebnis; die Auswertung endet an dieser Regel ohne Entscheidung. Es wird nicht geraten.
- Wo die Evidenz eine automatische Entscheidung nicht trägt, führt die Regel in einen kontrollierten Review-Ausgang (Ausgabetyp `REVIEW`), insbesondere:
  - `BOUNDARY_REVIEW_REQUIRED` — die MDR/IVDR-Abgrenzung ist mit den verfügbaren Eingaben nicht belastbar entscheidbar;
  - `ADDITIONAL_CLASSIFICATION_REVIEW_REQUIRED` — eine möglicherweise anwendbare Klassifizierungsregel ist im horizontalen RegScoutX-Kernbaum nicht vollständig modelliert.
- Ein Review-Ausgang ist **keine** Entscheidung und keine Klasse. Er trägt eine dokumentierte Ursache (`review_cause`).

## 8. Klassifikation

- Einzelne Klassifizierungsregeln liefern **Klassenkandidaten**, keine finale Klasse.
- Mehrere anwendbare Regeln oder Unterregeln überschreiben sich nicht gegenseitig. Die finale Klasse ist nach `SRC-001#Anh.VIII/Kap.II/Abschn.3.5` die strengste belastbar ermittelte Klasse; die Rangfolge steht in `class_order`.
- Ist eine möglicherweise anwendbare MDR-Regel nicht vollständig modelliert — insbesondere Rules 9 und 10 oder andere hardware- bzw. produktspezifische Regeln bei Hardware- oder Kombinationskonstellationen —, wird **keine** scheinbar endgültige Klasse ausgegeben, sondern `ADDITIONAL_CLASSIFICATION_REVIEW_REQUIRED` mit dokumentierter Ursache. Ein auf dem Pfad gesetzter Review-Ausgang wird bis zur Aggregation mitgeführt und verhindert dort eine finale Klasse.

### 8.1 Abgeleitete Eingaben und parallele Routen

Abgeleitete Eingaben werden ausschließlich nach drei typbasierten Regeln bestimmt; jede andere Form wird abgewiesen:

1. genau ein zulässiger Wert: dieser Wert;
2. boolesch: `true`, wenn auf dem Pfad in derselben Kategorie bereits ein Klassenkandidat oder Review-Ausgang entstanden ist;
3. Aufzählung: der erste zulässige Wert in Katalogreihenfolge, der als `aggregates_to` eines auf dem Pfad in derselben Kategorie erzeugten Ergebnisses auftritt.

Regel 3 bildet parallele, alternative Rechtswege ab: Jede Route liefert ein Routenergebnis mit `aggregates_to`; die Reihenfolge der `allowed_values` der Aggregationsregel ist die dokumentierte Vorrangfolge. `applicable_from` des Gesamtergebnisses ist das früheste `applicable_from` der Routenergebnisse, die auf den gewählten Zustand aggregieren. Hinweise (`flags`) aller Ergebnisse auf dem Pfad werden mitgeführt.

## 9. Änderung einer `RUL`

Es gelten unverändert die Lebenszyklusregeln aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3:

- Redaktionelle Änderung oder Präzisierung ohne Bedeutungsänderung derselben Regel: gleiche ID, Eintrag in `change_history`.
- Inhaltlich wesentliche Änderung (geänderte Entscheidung, geänderter Geltungsbereich, geänderter Anker): neue ID; die bisherige `RUL` erhält den Status `ersetzt` und `replaced_by`, die neue `replaces`.
- Neue eigenständige Regel: neue ID.
- Entfall: Status `zurückgezogen` mit Begründung; keine Löschung.

## 10. Versionierung und Prüfung

- `RUL_CATALOG.yaml` führt eine Katalogversion im Format `MAJOR.MINOR` mit Startwert `0.1` und eine `change_history`. Testfälle und Evidenzen nennen die Katalogversion, gegen die sie erzeugt wurden.
- Die formale Prüfung erfolgt mit `tools/validate_rul_catalog.py` auf der Werkzeugbasis aus ADR-0001 (Entwicklungsarchiv). Ein erfolgreicher Lauf belegt ausschließlich formale und strukturelle Konsistenz, nicht regulatorische Richtigkeit.
- Regelbasierte Testfälle werden unter `docs/07-testing/` geführt. Permanente `TC`-IDs werden erst mit einer eigenen Vergabestelle für `TC` vergeben.

## 11. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Gegenstand und Abgrenzung von `RUL`, führende Vergabestelle `RUL_CATALOG.yaml` im YAML-Format, kontrollierte Werte, Pflichtstruktur, Rechtshierarchie mit getrennten Primary- und Guidance-Ankern, Determinismus, Review-Ausgänge bei unzureichender Evidenz, Klassifikationsaggregation nach Anhang VIII Abschnitt 3.5, Änderungsregeln nach `DOCUMENTATION_CONVENTIONS.md` Abschnitt 3. |
| 1.1 | Kategorie `AI_ACT_APPLICABILITY` und Eingabetyp `date` ergänzt; Datumszweige und `date_condition`; `guidance_anchor` 0..n, leer nur ohne adjudizierte Guidance; Ausgabeattribute `aggregates_to`, `applicable_from`, `flags` und Katalogfeld `flags`; Abschnitt 8.1 zu abgeleiteten Eingaben und Aggregation paralleler Routen. Semantik von `RUL-001` bis `RUL-026` unverändert. |
| 1.2 | Lebenszyklus bei der Ausführung präzisiert: nur aktive Regeln sind ausführbar und müssen im aktiven Graphen erreichbar sein; ersetzte Regeln und ihre wechselseitigen Ersetzungsbeziehungen bleiben erhalten. Anhang-III-Korrektur in RUL_CATALOG 0.3; keine neue Auswertungssemantik. |
