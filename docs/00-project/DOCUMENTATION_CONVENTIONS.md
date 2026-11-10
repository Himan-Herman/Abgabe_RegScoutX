# Dokumentations- und ID-Konventionen

Version 1.9 · Status: aktiv

Dieses Dokument legt die projektweit verbindlichen Identifikatoren (IDs) und die zugehörigen Pflegeregeln fest. Zweck ist die durchgängige Rückverfolgbarkeit gemäß [EXPOSE_SCOPE.md](EXPOSE_SCOPE.md) (Abschnitt 4: Traceability-Matrix; Abschnitt 3: Reproduzierbarkeit und Nachvollziehbarkeit).

Die Konvention ist bewusst minimal gehalten: Sie legt nur fest, was für Traceability zwingend nötig ist, und nimmt keine inhaltlichen, methodischen oder technischen Entscheidungen vorweg.

## 1. Artefakttypen und ID-Format

| Artefakttyp | Präfix | Format | Beispiel | Vorgesehener Ablageort |
| --- | --- | --- | --- | --- |
| System-/Systemanforderung (wissenschaftlich abgeleitete Anforderung an das Assistenzsystem) | `SR` | `SR-NNN` | `SR-001` | `docs/02-requirements/` |
| Regulatorische Anforderung: atomare Compliance-/Gap-Anforderung, für die ein Erfüllungsstatus grundsätzlich sinnvoll bestimmbar ist | `RR` | `RR-NNN` | `RR-001` | `docs/03-regulatory/` |
| Quelle (Dokument in einer bestimmten Fassung) | `SRC` | `SRC-NNN` | `SRC-001` | `docs/03-regulatory/` |
| Entscheidungsregel: formalisierte Regel der Applicability-, Qualifikations-, Klassifikations- oder Gap-Logik | `RUL` | `RUL-NNN` | `RUL-001` | `docs/03-regulatory/` |
| Testfall | `TC` | `TC-NNN` | `TC-001` | `docs/07-testing/` |
| Evidenz (Nachweisartefakt eines durchgeführten Tests, Reviews oder einer Auswertung) | `EV` | `EV-NNN` | `EV-001` | `docs/09-evidence/` |
| Architecture Decision Record | `ADR` | `ADR-NNNN` | `ADR-0001` | `docs/decisions/` |

Hinweise zum Format:

- `NNN` ist eine dreistellige, führend mit Nullen aufgefüllte laufende Nummer.
- ADR verwendet abweichend vier Stellen, um die bereits in docs/decisions/README.md (Entwicklungsarchiv) festgelegte Dateibenennung `NNNN-kurzer-entscheidungstitel.md` unverändert zu erhalten. Die ID `ADR-0001` entspricht der Datei `0001-...md`.
- Die Präfixe sind englischsprachige Kurzformen, weil sie kurz, kollisionsfrei und in der Fachliteratur zu Requirements Engineering und Traceability gebräuchlich sind. Die Dokumentationssprache bleibt Deutsch.
- Maschinelle Erkennung von IDs erfolgt über das Muster `\b(SR|RR|SRC|RUL|TC|EV|ADR)-\d{3,4}\b`. Die Präfixe `SR` und `SRC` sind dadurch eindeutig unterscheidbar.
- Ablageorte sind vorläufig und folgen der bestehenden Ordnerstruktur unter `docs/`; sie können angepasst werden, ohne dass sich IDs ändern.

## 2. Grundregeln der ID-Vergabe

1. **Semantikfrei.** IDs enthalten keine Themen-, Cluster-, Regelwerks- oder Phasenkürzel (also `RR-001`, nicht `RR-MDR-QMS-001`). Solche Zuordnungen werden ausschließlich als Attribute des Elements geführt.
2. **Unveränderlich.** Eine einmal vergebene ID wird nie geändert, nie neu vergeben und nie wiederverwendet – auch nicht nach Streichung eines Elements.
3. **Fortlaufend.** Nummern werden je Artefakttyp monoton steigend vergeben. Nummernlücken sind zulässig und werden nicht aufgefüllt.
4. **Genau eine Vergabestelle.** Je Artefakttyp existiert genau eine führende Registerdatei (Single Source of Truth). Nur dort werden IDs vergeben; alle anderen Dokumente referenzieren. Für `RR` ist dies [../03-regulatory/RR_CATALOG.yaml](../03-regulatory/RR_CATALOG.yaml), für `SRC` [../03-regulatory/SOURCES.md](../03-regulatory/SOURCES.md), für `RUL` [../03-regulatory/RUL_CATALOG.yaml](../03-regulatory/RUL_CATALOG.yaml), für `SR` [../02-requirements/SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml), für `TC` [../07-testing/TC_CATALOG.yaml](../07-testing/TC_CATALOG.yaml), für `EV` [../09-evidence/EV_INDEX.yaml](../09-evidence/EV_INDEX.yaml).
5. **Keine Version in der ID.** Versionsstände werden auf Dokument-/Katalogebene geführt, nicht im Identifikator.

**Begründung zu Regel 1:** Sprechende IDs (z. B. `RR-QMS-001`) sind zunächst lesbarer, koppeln aber den Identifikator an eine inhaltliche Zuordnung. Ändert sich später die Cluster- oder Regelwerkszuordnung einer Anforderung, wird die ID entweder inhaltlich falsch oder muss umnummeriert werden. Beides verletzt die im Exposé geforderte Reproduzierbarkeit und Rückverfolgbarkeit. Die betrachtete Alternative wurde deshalb verworfen; Lesbarkeit wird stattdessen über Titel und Attribute hergestellt.

## 3. Lebenszyklus und Änderungen

Jedes Element führt einen Status aus folgendem Vokabular:

`Entwurf` · `aktiv` · `ersetzt` · `zurückgezogen`

- **Redaktionelle Änderung** (Formulierung, Tippfehler, Formatierung, ohne Bedeutungsänderung): gleiche ID, Eintrag in der Änderungshistorie der Katalogdatei.
- **Inhaltlich wesentliche Änderung** (geänderte Aussage, geänderter Geltungsbereich, geänderte Quelle): neues Element mit neuer ID. Das alte Element erhält Status `ersetzt` und das Feld `ersetzt durch:`; das neue Element erhält `ersetzt:`.
- **Entfall**: Status `zurückgezogen` mit Begründung. Elemente werden nicht gelöscht, damit frühere Auswertungen nachvollziehbar bleiben.

Katalog- und Registerdateien führen jeweils eine Version (`MAJOR.MINOR`) und eine Änderungshistorie. Auswertungen, Testläufe und Evidenzen nennen immer die Katalogversion, gegen die sie erzeugt wurden.

## 4. Quellen und Fundstellen

- Eine `SRC`-ID bezeichnet ein Dokument **in einer bestimmten Fassung** (Ausgabe-/Revisionsstand, ggf. Datum der konsolidierten Fassung). Eine andere Fassung desselben Regelwerks erhält eine eigene `SRC`-ID, da sonst identische Eingaben je nach Fassung unterschiedliche Ergebnisse liefern könnten.
- Fundstellen (Artikel, Absatz, Anhang, Abschnitt, Kapitel) erhalten **keine eigene ID**, sondern werden als Lokator an die Quelle angehängt. Der Lokator ist hierarchisch aufgebaut:

  `SRC-NNN#<Gliederung>/<Gliederung>/…`

  Der Schrägstrich `/` trennt die Gliederungsebenen und wird von der äußersten zur innersten Ebene gelesen. Für Rechtsakte (MDR, EU AI Act) sind ausschließlich die folgenden Elemente zulässig:

  | Element | Bedeutung | Element | Bedeutung |
  | --- | --- | --- | --- |
  | `Art.` | Artikel | `Nr.` | Nummer |
  | `Abs.` | Absatz | `Anh.` | Anhang |
  | `UAbs.` | Unterabsatz | `Teil.` | Teil |
  | `Satz.` | Satz | `Kap.` | Kapitel |
  | `Buchst.` | Buchstabe | `Abschn.` | Abschnitt |
  | `Ziff.` | Ziffer | `Regel.` | Regel |
  | `ErwG.` | Erwägungsgrund | | |

  Beispiele: `SRC-001#Art.10/Abs.9` · `SRC-001#Anh.VIII/Kap.III/Abschn.6.3/Regel.11` · `SRC-002#Art.113/Abs.3/Buchst.c/Ziff.ii`

  Für Quellen, die keine Rechtsakte sind (Leitlinien, Normen), gilt die jeweils im Quellenregister bei der Quelle hinterlegte Zitierweise.

  Begründung: Der Zuschnitt zitierter Stellen ändert sich während der Anforderungsextraktion häufig. Eigene IDs für Fundstellen würden dadurch instabil, ohne Traceability-Gewinn.
- Jede regulatorische Anforderung (`RR`) referenziert mindestens eine Quelle mit Lokator. Anforderungen ohne belegbare Fundstelle sind unzulässig.
- Unsicherheiten (z. B. strittige Auslegung, noch nicht verifizierte Fundstelle) werden im Feld `Unsicherheit:` ausdrücklich vermerkt, statt als gesicherte Aussage geführt zu werden.

### Abgrenzung zur wissenschaftlichen Zitierweise

Der Lokator ist eine **projektinterne Traceability-Konvention und keine juristische Zitiernorm**. Interne Traceability und wissenschaftlich-juristische Zitierweise werden getrennt geführt:

- Interne `SRC`-Lokatoren werden nicht unverändert als Zitate in der Masterarbeit verwendet.
- Für wissenschaftliche Rechtszitate wird der Rechtsakt über seine normative Identität bzw. seine Amtsblattfundstelle referenziert. Der für die Auswertung herangezogene konsolidierte Rechtsstand wird bei Bedarf transparent angegeben, damit die konsolidierte Fassung nicht wie ein eigenständiger Rechtsakt erscheint.
- Die konkrete formale Zitierweise richtet sich nach den Vorgaben der Hochschule und wird hier nicht festgelegt.

### Verhalten bei späteren Fassungsänderungen

Ändert sich der Rechts- oder Ausgabestand einer Quelle:

1. Für die neue Fassung wird eine **neue `SRC`-ID** vergeben; die bisherige ID bleibt bestehen und behält ihre Bedeutung.
2. Bestehende Referenzen auf die bisherige ID bleiben **unverändert**, damit frühere Auswertungen reproduzierbar bleiben.
3. Anschließend erfolgt eine Change- und Impact-Prüfung entlang der nachgelagerten Traceability-Beziehungen, insbesondere `RR`, `SR`, `RUL`, `TC` und `EV`; betroffene `ADR` sind ebenfalls zu prüfen. Das Ergebnis wird dokumentiert.

Ein zusätzliches Versionsschema am Identifikator (etwa `SRC-NNN@<Datum>`) wird ausdrücklich **nicht** eingeführt; die Fassung steckt bereits in der ID selbst.

## 5. Verknüpfungen und Traceability-Kette

Für regulatorisch begründete Entscheidungs- und Gap-Regeln sind innerhalb **einer** Traceability-Systematik zwei Grundpfade vorgesehen. Sie unterscheiden sich darin, ob eine Regel eine Compliance-/Gap-Anforderung umsetzt oder unmittelbar der vorgelagerten Anwendbarkeits-, Qualifikations- oder Klassifikationslogik dient. Bereits bestehende Herkunftsmöglichkeiten von Systemanforderungen (`SR`) bleiben davon unberührt.

**Pfad 1 – Compliance / Gap** (Regelfall):

```
EXPOSE_SCOPE.md (Abschnitt)
        │
        ▼
      SRC ──► RR ──► RUL ──► TC ──► EV
                │      ▲
                └► SR ─┘
                       ▲
                     ADR (begründet Umsetzungsentscheidungen)
```

Ist eine Systemanforderung zwischengeschaltet, lautet die Kette `SRC → RR → SR → RUL → TC → EV`.

**Pfad 2 – Applicability / Qualifikation / Klassifikation** (eng begrenzter Sonderfall):

```
      SRC ──► RUL ──► TC ──► EV
```

Pfad 2 gilt ausschließlich für Regeln, deren Hauptfunktion in Anwendbarkeit, Qualifikation, Klassifizierung oder regulatorischer Einordnung liegt und für die keine sachgerechte Gap-`RR` formulierbar ist. Die Voraussetzungen und die Schutzregel dazu stehen in den Mindestverknüpfungen unten.

Beide Pfade sind Teil derselben Systematik: Jedes Element referenziert seine Vorgänger, und jeder Pfad endet quellenseitig bei einer `SRC` mit Lokator.

**Umsetzungsstand (Stand Block 6):** Alle `RUL` im Katalog sind Regeln nach Pfad 2 (Qualifikation, Abgrenzung, Klassifikation, AI-Act-Anwendbarkeit). Die Anwendbarkeit der `RR` wird nicht über Gap-Filter-`RUL` nach Pfad 1, sondern maschinenlesbar über [../03-regulatory/RR_APPLICABILITY.yaml](../03-regulatory/RR_APPLICABILITY.yaml) (Block, lokale Bedingung, Prädikat auf `RUL`-Ergebnisse bzw. Eingaben) bestimmt; die Gap-Ableitung liegt im Demonstrator-Kern (`GAP_ENGINE`); `TC` verweisen über `covers_rr` unmittelbar auf `RR` ([../05-traceability/TRACEABILITY_MODEL.md](../05-traceability/TRACEABILITY_MODEL.md)). Pfad 1 bleibt die Konvention für künftige Gap-Filter-Regeln. „Evidenzdatei“ bezeichnet in den regulatorischen Dokumenten die Extraktions- und Adjudikationsnachweise `RR_EXTRACTION_*.md`; sie ist weder eine `EV` noch eine vorgesehene Nachweisart.

**Verbindliche Verknüpfungsrichtung:** Jedes Element referenziert ausschließlich seine Vorgänger (aufwärts, in Richtung Quelle). Die Vorwärtsrichtung (z. B. „welche Tests decken RR-004 ab?") wird aus diesen Angaben abgeleitet und in der Traceability-Matrix dargestellt, aber nicht zusätzlich manuell gepflegt. So kann keine widersprüchliche Doppelpflege entstehen.

Mindestverknüpfungen:

| Element | Muss referenzieren |
| --- | --- |
| `RR` | mindestens eine Quelle mit Lokator (`SRC-NNN#…`) |
| `SR` | mindestens einen Abschnitt aus `EXPOSE_SCOPE.md`, eine `RR`, einen `SRC`-Lokator oder eine belegte Erkenntnis aus dem Stand der Technik als Design Implication (`STATE_OF_THE_ART.md#DI-NNN`) |
| `RUL` | regulär mindestens eine `RR` oder `SR`; ausschließlich im Sonderfall nach Pfad 2 stattdessen mindestens einen verifizierten `SRC`-Lokator (siehe unten) |
| `TC` | mindestens eine `RUL`, `RR` oder `SR` |
| `EV` | genau einen erzeugenden Vorgang, i. d. R. eine `TC`; zusätzlich die verwendete Katalog-/Regelwerksversion |
| `ADR` | die betroffenen `SR`/`RR` sowie ggf. `RUL` |

Verweise auf Abschnitte des Exposés erfolgen als `EXPOSE_SCOPE.md#<abschnitt>`, z. B. `EXPOSE_SCOPE.md#4-erwartetes-ergebnis`.

`SRC` bezeichnet ausschließlich die im Quellenregister geführten regulatorischen Quellen (Rechtsakte, Leitlinien, Normen) in bestimmter Fassung. Wissenschaftliche Fachliteratur und Produktquellen des Stands der Technik erhalten **keine** `SRC`-ID; sie werden mit dokumentinternen Kennungen in [../01-research/STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) geführt. Eine daraus abgeleitete `SR` verweist auf die Design Implication, z. B. `STATE_OF_THE_ART.md#DI-005`. `DI-NNN` ist keine projektweite ID-Klasse.

Eine `EV` bezeichnet ausschließlich einen tatsächlich erzeugten Nachweis dieses Projekts (z. B. Testlauf, Validatorlauf, Review) und verweist auf ein vorhandenes Artefakt; für nur geplante Nachweise wird keine `EV` vergeben. Davon zu unterscheiden sind die vorgesehenen Nachweisarten einer `RR` im Maßnahmenkatalog [../03-regulatory/RR_MEASURE_CATALOG.yaml](../03-regulatory/RR_MEASURE_CATALOG.yaml); sie sind Katalogdaten, keine `EV`. Der Teststatus eines `TC` wird aus den `EV` abgeleitet, die ihn referenzieren.

### Direkter Quellenbezug einer `RUL` (Pfad 2)

Regulär referenziert eine `RUL` mindestens eine `RR` oder `SR`. Nur für reine regulatorische Regeln, deren Hauptfunktion in Anwendbarkeit, Qualifikation, Klassifizierung oder regulatorischer Einordnung liegt und die keine sachgerechte Gap-`RR` darstellen, darf eine `RUL` unmittelbar mindestens einen verifizierten `SRC`-Lokator referenzieren.

**Schutzregel:** Der direkte `SRC → RUL`-Pfad darf **nicht** verwendet werden, um eine extrahierbare Compliance-/Gap-Anforderung zu umgehen. Lässt sich zu einer Fundstelle eine Verpflichtung formulieren, für die ein Erfüllungsstatus sinnvoll bestimmbar ist, ist zwingend eine `RR` anzulegen.

Bei direktem Quellenbezug ist der **präziseste verfügbare Lokator** Pflicht; eine bloße `SRC`-ID ohne Fundstelle genügt nicht.

- Korrekt: `SRC-001#Anh.VIII/Kap.III/Abschn.6.3/Regel.11`
- Unzulässig: eine Angabe der Form `SRC-001@<Datum>#…`. Ein `@VERSION`-Zusatz wird in diesem Projekt nicht verwendet, weil die Fassung bereits durch die `SRC`-ID festgelegt ist.

## 6. Pflichtfelder je Artefakt (Minimum)

| Artefakt | Pflichtfelder |
| --- | --- |
| `SR` | ID, Titel, Beschreibung, Herkunft/Verknüpfung, Status, Version |
| `RR` | ID, Titel, Anforderungstext (sinngemäß, mit Kennzeichnung wörtlicher Zitate), Quelle + Lokator, Themencluster, Lebenszyklusphase, Status |
| `SRC` | ID, Titel, Herausgeber, Fassung/Stand, Fundstellen-Zitierweise, Bezugsnachweis, Status |
| `RUL` | ID, Regelzweck, Eingangsgrößen, Bedingung, Ergebnis, Grundlage (verknüpfte `RR`/`SR`; im Sonderfall nach Pfad 2 stattdessen der direkte `SRC`-Lokator), Status |
| `TC` | ID, Zweck, Vorbedingung, Eingaben, erwartetes Soll-Ergebnis, geprüfte Elemente, Status |
| `EV` | ID, Bezug (`TC`/Review), Datum, Durchführung, Ist-Ergebnis, Bewertung, verwendete Versionsstände |
| `ADR` | ID, Titel, Status, Kontext, Alternativen, Entscheidung, Begründung, Konsequenzen, Verknüpfungen (siehe docs/decisions/README.md (Entwicklungsarchiv)) |

Die im Exposé geforderten Attribute der Traceability-Matrix – Quelle, Lebenszyklusphase, Maßnahme, Nachweisdokument – sind über diese Felder abgedeckt bzw. werden in der Matrix unter `docs/05-traceability/` zusammengeführt.

Für die Pflichtattribute `Themencluster` und `Lebenszyklusphase` einer `RR` sind ausschließlich die Werte aus [../03-regulatory/CONTROLLED_VOCABULARY.md](../03-regulatory/CONTROLLED_VOCABULARY.md) zulässig; dort sind auch die Zuordnungsregeln festgelegt.

Wie eine `RR` aus einer Quellenfundstelle gewonnen und atomisiert wird, ist verbindlich in [../03-regulatory/RR_EXTRACTION_METHOD.md](../03-regulatory/RR_EXTRACTION_METHOD.md) festgelegt; die dortigen Regeln werden hier nicht wiederholt. Wie die Pflichtfelder einer `RUL` im Regelkatalog abgebildet werden, legt [../03-regulatory/RUL_METHOD.md](../03-regulatory/RUL_METHOD.md) fest.

## 7. Dateibenennung

- Dokumente unter `docs/`: `GROSSBUCHSTABEN_MIT_UNTERSTRICH.md` für Rahmendokumente (z. B. `PROJECT_SCOPE.md`), sonst sprechende Kleinschreibung mit Bindestrich.
- ADRs: `NNNN-kurzer-entscheidungstitel.md` (unverändert gemäß bestehender Festlegung).
- Dateinamen enthalten keine IDs von Einzelanforderungen; Einzelelemente werden innerhalb von Katalogdateien geführt.

## 8. Offene Festlegungen

Bewusst noch **nicht** festgelegt (und erst bei Bedarf zu entscheiden, ggf. per ADR):

- Format weiterer, noch nicht definierter Katalog- und Registerartefakte (Markdown-Tabelle, YAML, CSV o. ä.) – hängt von der späteren Verarbeitung im Demonstrator ab. Für den regulatorischen Anforderungskatalog ist das Format bereits festgelegt: YAML in `RR_CATALOG.yaml`, begründet in [../03-regulatory/RR_EXTRACTION_METHOD.md](../03-regulatory/RR_EXTRACTION_METHOD.md) Abschnitt 10. Für den Entscheidungsregelkatalog gilt ebenfalls YAML in `RUL_CATALOG.yaml`, begründet in [../03-regulatory/RUL_METHOD.md](../03-regulatory/RUL_METHOD.md) Abschnitt 2, für den Systemanforderungskatalog YAML in `SR_CATALOG.yaml` nach [../02-requirements/SYSTEM_REQUIREMENTS.md](../02-requirements/SYSTEM_REQUIREMENTS.md) Abschnitt 2. Führende Vergabestelle für `TC` ist [../07-testing/TC_CATALOG.yaml](../07-testing/TC_CATALOG.yaml), für `EV` der Evidenzindex [../09-evidence/EV_INDEX.yaml](../09-evidence/EV_INDEX.yaml), jeweils YAML ([../07-testing/TEST_STRATEGY.md](../07-testing/TEST_STRATEGY.md)).

Festgelegt mit ADR-0002 (Entwicklungsarchiv): Die Traceability-Matrix wird nicht manuell gepflegt, sondern aus den Katalogen abgeleitet; ID-Eindeutigkeit und Verweisintegrität werden werkzeuggestützt geprüft ([../05-traceability/TRACEABILITY_MODEL.md](../05-traceability/TRACEABILITY_MODEL.md)).

## 9. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: ID-Schema, Vergabe- und Lebenszyklusregeln, Verknüpfungsrichtung, Pflichtfelder. |
| 1.1 | Abschnitt 4: hierarchisches Lokator-Schema für Rechtsakte eingeführt (`/` als Trenner, festes Elementvokabular); Abgrenzung des internen Lokators zur wissenschaftlichen Zitierweise sowie Regeln für spätere Fassungsänderungen ergänzt. ID-Bedeutung und Fassungsregel unverändert. |
| 1.2 | Kontrolliertes Themencluster- und Lebenszyklusvokabular referenziert (`CONTROLLED_VOCABULARY.md`) und der entsprechende offene Punkt geschlossen; `RR`/`RUL` gegeneinander abgegrenzt; zwei zulässige Traceability-Pfade dargestellt und der eng begrenzte direkte `SRC → RUL`-Pfad für Applicability-, Qualifikations- und Klassifikationsregeln mit Schutzregel zugelassen. Keine Änderung der `SRC`-Versionierungslogik. |
| 1.3 | Führende RR-Extraktions- und Atomizitätsmethode referenziert (`RR_EXTRACTION_METHOD.md`). Keine Änderung an ID-, `SRC`-, Lokator-, Taxonomie- oder Traceability-Grundlogik. |
| 1.4 | YAML als führendes Format des regulatorischen Anforderungskatalogs festgelegt; `RR_CATALOG.yaml` als Single Source of Truth für `RR` referenziert; offener Punkt zum Katalogformat auf die noch nicht definierten Artefakte eingegrenzt. Keine Änderung an ID-, `SRC`-, Lokator-, Taxonomie-, Atomizitäts- oder Traceability-Grundlogik. |
| 1.5 | `RUL_CATALOG.yaml` als führende Vergabestelle für `RUL` festgelegt und Ablageort von `RUL` auf `docs/03-regulatory/` angepasst (Abschnitt 1 erlaubt die Anpassung vorläufiger Ablageorte ohne ID-Änderung); YAML als Format des Entscheidungsregelkatalogs und `RUL_METHOD.md` als Abbildung der `RUL`-Pflichtfelder referenziert. Keine Änderung an ID-, Status-, Lebenszyklus-, `SRC`-, Lokator- oder Traceability-Grundlogik. |
| 1.6 | `SR_CATALOG.yaml` als führende Vergabestelle für `SR` und YAML als dessen Format referenziert; die offenen Punkte zu Aufbau und Erzeugung der Traceability-Matrix sowie zur werkzeuggestützten Verweisprüfung mit ADR-0002 geschlossen (abgeleitete Matrix, `TRACEABILITY_MODEL.md`). Keine Änderung an ID-, Status-, Lebenszyklus-, `SRC`-, Lokator- oder Traceability-Grundlogik. |
| 1.7 | Abschnitt 5: Herkunft einer `SR` aus dem Stand der Technik als Design Implication (`STATE_OF_THE_ART.md#DI-NNN`) präzisiert; Fachliteratur und Produktquellen erhalten keine `SRC`-ID. `SRC`-Systematik, IDs und Lokatoren unverändert; keine neue projektweite ID-Klasse. |
| 1.8 | Vergabestellen für `TC` (`TC_CATALOG.yaml`) und `EV` (`EV_INDEX.yaml`) festgelegt; `EV` von vorgesehenen Nachweisarten der `RR` (`RR_MEASURE_CATALOG.yaml`) abgegrenzt; Teststatus aus `EV → TC` abgeleitet. Keine Änderung an ID-Format, `SRC`, Lokatoren oder Verknüpfungsrichtung. |
| 1.9 | Abschnitt 2: Vergabestellen für `TC` und `EV` in Regel 4 ergänzt; Abschnitt 5: Umsetzungsstand der Pfade (alle `RUL` nach Pfad 2, Anwendbarkeit der `RR` über `RR_APPLICABILITY`) und Begriff „Evidenzdatei“ klargestellt. Keine Änderung an ID-Format, `SRC`, Lokatoren, Pflichtfeldern oder Verknüpfungsrichtung. |
