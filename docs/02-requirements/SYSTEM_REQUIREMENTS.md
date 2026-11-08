# Systemanforderungen (SR) des Demonstrators

Version 1.3 · Status: aktiv

Dieses Dokument legt fest, wie Systemanforderungen (`SR`) an RegScoutX selbst formuliert, abgeleitet, geprüft und versioniert werden. ID-, Status-, Lebenszyklus- und Traceability-Grundregeln stehen ausschließlich in [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) und werden hier nicht wiederholt.

---

## 1. Gegenstand und Abgrenzung

- Eine `SR` beschreibt eine Anforderung an den Demonstrator RegScoutX: Funktion, Datenbehandlung oder Qualitätseigenschaft.
- Eine `SR` ist **keine** regulatorische Anforderung. `RR` beschreiben Sollanforderungen an den Hersteller eines Medizinprodukts; sie sind für RegScoutX **Daten**, die verarbeitet, angezeigt und bewertet werden. `RR` werden deshalb nicht 1:1 in `SR` übertragen.
- Eine `SR` ist **keine** Entscheidungsregel. `RUL` entscheiden Applicability, Qualification, Classification und Routing; `SR` fordern, dass und wie RegScoutX solche Regeln ausführt.
- `SR` sind lösungsneutral formuliert, soweit das die Prüfbarkeit nicht beeinträchtigt. Technologieentscheidungen für den Demonstrator sind nicht Gegenstand dieser Version.

## 2. Führende Vergabestelle und Format

Führende Vergabestelle und Single Source of Truth für `SR` ist:

`docs/02-requirements/SR_CATALOG.yaml`

Das Format ist YAML, aus denselben Gründen wie für den Anforderungskatalog ([RR_EXTRACTION_METHOD.md](../03-regulatory/RR_EXTRACTION_METHOD.md) Abschnitt 10.2).

## 3. Ableitung

Zulässige Herkunft einer `SR` nach [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 5 ist ein Abschnitt aus [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md), eine `RR`, ein `SRC`-Lokator oder eine Design Implication aus dem Stand der Technik (`STATE_OF_THE_ART.md#DI-NNN`).

Für den Katalog gilt:

- Alle `SR` sind aus dem genehmigten Exposé abgeleitet, insbesondere aus Zielstellung und Bewertungskriterien (Abschnitt 3), erwartetem Ergebnis (Abschnitt 4) und geplanter Evaluation (Abschnitt 5).
- Qualitätsanforderungen, die das Exposé nicht ausdrücklich nennt (Zweisprachigkeit, Security/Privacy by Design, Wartbarkeit), sind technische Erweiterungen im Sinne des Exposé-Abschnitts „Status und Zweck dieses Dokuments“ und stützen sich zusätzlich auf die Projektvorgaben in [AGENTS.md](../../AGENTS.md). Die Begründung steht jeweils im Feld `rationale`.
- Keine `SR` ist aus einer einzelnen `RR` abgeleitet: Die `RR` richten sich an Medizinproduktehersteller, nicht an RegScoutX. `RR` und `RUL` sind für die `SR` Verarbeitungsgegenstand, keine Traceability-Vorgänger.
- Die im Exposé vorgesehene Ableitung aus dem Stand der Technik ist in [STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) Abschnitt 8 dokumentiert: Die zwölf Design Implications sind gegen die `SR` und die Architektur abgeglichen. Die vier dabei identifizierten Ergänzungen sind seit Katalogversion 0.3 als SR-040 bis SR-043 aufgenommen; SR-001 bis SR-039 blieben unverändert. Änderungen folgen [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3.
- Fachliteratur erhält keine `SRC`-ID; `SRC` bezeichnet ausschließlich regulatorische Quellen. Eine aus dem Stand der Technik abgeleitete `SR` verweist in `derived_from` auf den Exposé-Abschnitt und auf die Design Implication (`STATE_OF_THE_ART.md#DI-NNN`); der Validator prüft, dass die Design Implication existiert.

## 4. Kontrollierte Werte

Die folgenden Wertelisten sind führend; der Validator liest sie aus diesem Abschnitt.

Zulässige SR-Gruppen:

`QUALIFICATION_CLASSIFICATION` · `APPLICABILITY` · `GAP_ANALYSIS` · `EVIDENCE` · `TRACEABILITY` · `REPORTING` · `I18N` · `NON_FUNCTIONAL`

Zulässige Verifikationsmethoden:

`TEST` · `INSPECTION` · `ANALYSIS` · `DEMONSTRATION`

| Wert | Bedeutung |
| --- | --- |
| `QUALIFICATION_CLASSIFICATION` | Produkteingaben, Ausführung der Entscheidungsregeln, Qualifikation, MDR/IVDR-Abgrenzung, MDR-Klassifikation, AI-Act-Applicability |
| `APPLICABILITY` | Aktivierung anwendbarer `RR` |
| `GAP_ANALYSIS` | Erfüllungsstatus und Gap-Ermittlung |
| `EVIDENCE` | Nachweisreferenzen |
| `TRACEABILITY` | Rückverfolgbarkeit von Ergebnissen bis zur Quelle |
| `REPORTING` | Ergebnisbericht |
| `I18N` | Zweisprachigkeit DE/EN |
| `NON_FUNCTIONAL` | Security/Privacy, Audit, Versionierung, Fehlerbehandlung, Modularität, Testbarkeit, Wartbarkeit |
| `TEST` | automatisierter oder manueller Test mit Soll-Ergebnis |
| `INSPECTION` | Prüfung von Code, Daten oder Dokumentation gegen das Kriterium |
| `ANALYSIS` | strukturierte Analyse, z. B. von Abhängigkeiten |
| `DEMONSTRATION` | Vorführung der Funktion am Demonstrator |

Die Architekturmodule für `allocated_modules` sind in [../04-architecture/ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md) Abschnitt 3 festgelegt.

## 5. Pflichtstruktur je `SR`

| Feld | Inhalt |
| --- | --- |
| `id` | `SR-NNN`; unveränderlich, fortlaufend, semantikfrei |
| `status` | Artefaktstatus aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3 |
| `group` | genau eine SR-Gruppe aus Abschnitt 4 |
| `title.de` / `title.en` | Titel |
| `statement.de` / `statement.en` | Beschreibung als genau eine prüfbare Anforderung („Das System muss …“) |
| `acceptance_criterion.de` / `acceptance_criterion.en` | beobachtbares Abnahmekriterium |
| `verification_method` | genau eine Verifikationsmethode aus Abschnitt 4 |
| `derived_from` | Herkunft: mindestens ein Verweis `EXPOSE_SCOPE.md#<abschnitt>`, `STATE_OF_THE_ART.md#DI-NNN`, eine `RR`-ID oder ein `SRC`-Lokator |
| `allocated_modules` | mindestens ein Architekturmodul |
| `rationale` | Begründung |
| `replaces` / `replaced_by` | Ersetzungsbeziehungen analog zu `RR` |

Das Pflichtfeld „Version“ nach [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 6 wird über die Katalogversion erfüllt; inhaltlich wesentliche Änderungen erzeugen nach Abschnitt 3 der Konvention eine neue ID, sodass eine zusätzliche Elementversion keinen Informationsgewinn hätte.

## 6. Qualitätskriterien

- **Atomar:** genau eine prüfbare Anforderung je `SR`.
- **Prüfbar:** jedes Abnahmekriterium ist beobachtbar und einer Verifikationsmethode zugeordnet.
- **Eindeutig:** kontrollierte Begriffe aus [../04-architecture/DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml) statt freier Umschreibung.
- **Begrenzt:** nur so viele `SR`, wie für eine vollständig rückverfolgbare Demonstrator-Architektur nötig sind; keine kommerziellen Ziele.

## 7. Versionierung und Prüfung

- `SR_CATALOG.yaml` führt eine Katalogversion im Format `MAJOR.MINOR` mit Startwert `0.1` und eine `change_history`.
- Die formale Prüfung erfolgt mit `tools/validate_sr_catalog.py` auf der Werkzeugbasis aus [ADR-0001](../decisions/0001-rr-catalog-validation-tooling.md). Ein erfolgreicher Lauf belegt ausschließlich formale Konsistenz.

## 8. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Gegenstand und Abgrenzung von `SR` gegenüber `RR` und `RUL`, Vergabestelle `SR_CATALOG.yaml`, Ableitungsregeln, kontrollierte Werte, Pflichtstruktur, Qualitätskriterien. |
| 1.1 | Abschnitt 3: Ableitung aus dem Stand der Technik durchgeführt und auf [STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) verwiesen; keine `SR` geändert, vier `PROPOSED_SR_GAP` nicht angelegt; Herkunftsangabe für literaturgestützte `SR` ohne `SRC`-ID präzisiert. |
| 1.2 | Abschnitte 3 und 5: Herkunft aus dem Stand der Technik als `STATE_OF_THE_ART.md#DI-NNN` zugelassen; SR-040 bis SR-043 schließen die vier `PROPOSED_SR_GAP`. |
| 1.3 | Ausschließlich redaktionell: Einleitung von Abschnitt 3 ohne irreführende Versionsangabe. |
