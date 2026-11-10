# Extraktions- und Coverage-Plan für den regulatorischen Anforderungskatalog

Version 1.53 · Status: aktiv

Dieser Plan definiert **ex ante** den endlichen Untersuchungs- und Extraktionskorpus für die regulatorische Anforderungsextraktion. Er wird vor Beginn der systematischen Extraktion eingefroren.

Zweck ist, eine selektive Auswahl einzelner „interessanter" Fundstellen zu verhindern: Nicht die während der Arbeit auffallenden Stellen bestimmen den Korpus, sondern der vorab festgelegte Korpus bestimmt, was geprüft wird.

Abgrenzungen:

- Der Plan ist **keine** vollständige MDR- oder EU-AI-Act-Compliance-Taxonomie und erhebt nicht den Anspruch, eines der beiden Regelwerke vollständig abzudecken.
- Der Plan enthält selbst **keine** regulatorischen Anforderungen (`RR`) und vergibt keine Identifikatoren.
- Innerhalb eines freigegebenen Quellenbereichs erfolgt später eine vollständige `0 / 1 / n`-Prüfung nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md).
- Der Plan konkretisiert den ausgewählten Anforderungskatalog aus [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 4 und bleibt an dessen Abgrenzung gebunden.

Führende Bezugsdokumente: [SOURCES.md](SOURCES.md) für die Quellen und ihre Fassungen, [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) für Themencluster und Lebenszyklusphasen, [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) für Identifikatoren und Lokator-Syntax, [RR_CATALOG.yaml](RR_CATALOG.yaml) als führende Vergabestelle der `RR`.

---

## 1. Methodische Grundsätze

### 1.1 Ex-ante-Abgrenzung

Die Core-Coverage wird vor der weiteren Extraktion festgelegt. Die Core-Auswahl beruht auf:

- dem genehmigten Exposé,
- dem definierten Untersuchungsgegenstand,
- den acht Themenclustern,
- der regulatorischen Relevanz,
- der Compliance- bzw. Gap-Fähigkeit,
- der Quellenrolle,
- dem Core-Adressatenscope.

Die Fallstudie darf die Core-Coverage **nicht** nachträglich erweitern. Sie darf ausschließlich Bereiche aktivieren, die hier vorab als `Ergänzungsbereich` bzw. conditional festgelegt sind.

### 1.2 Core-Adressaten

| Regelwerk | Core-Adressat |
| --- | --- |
| MDR (`SRC-001`) | Hersteller |
| EU AI Act (`SRC-002`) | Anbieter / Provider |

Deployer- bzw. Betreiberpflichten sind grundsätzlich **ergänzend und conditional**. Sie werden nur aktiviert, wenn die spätere System- bzw. Fallstudienabgrenzung diese Perspektive ausdrücklich umfasst.

Wichtig: Anforderungen, die Informationen oder Eigenschaften **für** Deployer bereitstellen, können gleichwohl providerseitige Core-Pflichten sein. Maßgeblich ist der Adressat der Pflicht, nicht der Begünstigte.

### 1.3 Coverage-Einheit

Die Coverage-Einheit dieses Plans ist der **Quellenbereich**.

Ein Quellenbereich ist ein vorab abgegrenzter Artikel, Absatz, Buchstabenbereich, Anhangsabschnitt, Guidance-Bereich oder autorisierter Normabschnitt, der später vollständig auf `0 / 1 / n RR` geprüft wird.

Ein Quellenbereich ist **keine** `RR`.

---

## 2. Inclusion Criteria

| Nr. | Kriterium | Begründung |
| --- | --- | --- |
| I-1 | Bezug zum genehmigten Untersuchungsgegenstand | Der Korpus bleibt an das Exposé gebunden und wächst nicht über den genehmigten Rahmen hinaus. |
| I-2 | Bezug zu mindestens einem der acht Themencluster | Ohne Clusterbezug entstünde eine Anforderung ohne auswertbaren Platz in der Gap-Analyse. |
| I-3 | Potenzieller Compliance-/Gap-Sollzustand | Nur Stellen, für die ein Erfüllungsstatus sinnvoll bestimmbar sein kann, tragen zur Gap-Analyse bei. |
| I-4 | Core-Adressatenbezug | Der Untersuchungsgegenstand ist die Hersteller- bzw. Anbieterperspektive; abweichende Adressaten sind gesondert zu aktivieren. |
| I-5 | Regulatorische Relevanz für die regelbasierte Gap-Analyse | Der Demonstrator soll entscheidungsrelevante Anforderungen abbilden, nicht beliebige Normtexte. |
| I-6 | Quellenrolle rechtfertigt systematische Prüfung | Rechtsakt, Guidance und Norm tragen unterschiedlich zum Gap-Katalog bei (Abschnitt 4). |
| I-7 | Verifizierbare Quellenbasis | Nur Fundstellen aus einer in `SOURCES.md` geführten Fassung sind reproduzierbar zitierbar. |
| I-8 | Ex-ante-Coverage statt Fallstudienselektion | Die Auswahl erfolgt vor der Extraktion, damit das Ergebnis nicht durch das Fallbeispiel vorgeprägt wird. |

Eine mögliche Dublette ist **kein** Inclusion Criterion und wird an dieser Stelle nicht geprüft.

---

## 3. Exclusion Criteria

| Nr. | Kriterium | Begründung | Alternative Behandlung |
| --- | --- | --- | --- |
| E-1 | Reine Definition ohne eigenen Compliance-Sollzustand | Eine Definition begründet keine eigenständig prüfbare Pflicht. | Kontext, `supplementary`-Lokator oder `RUL`-Kontext |
| E-2 | Reine Applicability-, Qualifikations- oder Klassifikationslogik | Solche Stellen bestimmen die Anwendbarkeit, nicht den Erfüllungsstand. | `SRC → RUL` nach `DOCUMENTATION_CONVENTIONS.md` Abschnitt 5 |
| E-3 | Reine Behörden- oder institutionelle Pflichten | Der Untersuchungsgegenstand ist die Herstellerperspektive. | Kontext, keine Gap-`RR` |
| E-4 | Sanktionen, behördliche Durchsetzung, Marktüberwachung | Kein Gegenstand der herstellerseitigen Gap-Analyse. | außerhalb Gap-Coverage |
| E-5 | Primärer Gegenstand außerhalb der acht Themencluster | Ohne Cluster ist keine reproduzierbare Auswertung möglich. | nur durch formelle Coverage-Änderung (Abschnitt 10) |
| E-6 | Vollständige klinische bzw. leistungsbezogene Bewertung | Im Exposé ausdrücklich nicht als eigener Bereich vorgesehen. | keine Vollauswertung |
| E-7 | Vollständige technische Dokumentation | Bildet nach `CONTROLLED_VOCABULARY.md` Abschnitt 5 keinen eigenen Gap-Cluster. | kein eigener Gap-Bereich |
| E-8 | Vollständiges Konformitätsbewertungsverfahren | Konformitätsbewertung ist Lebenszyklusphase, nicht Themencluster. | Lifecycle-/Applicability-Kontext |
| E-9 | Sonstige Wirtschaftsakteurspflichten als eigener Katalog | Außerhalb des Core-Adressatenscope. | außerhalb Core |
| E-10 | Deployer-/Betreiberpflicht außerhalb aktivierter Perspektive | Die Perspektive ist erst durch die Systemabgrenzung zu aktivieren. | ergänzend / conditional |
| E-11 | Produktion und Fertigung als eigenständiger Gegenstand | Bildet keinen eigenen Themencluster. | kein eigener Themencluster |
| E-12 | Nicht verifizierbarer lizenzierter Norminhalt | Ohne autorisierten Volltext ist keine belastbare Extraktion möglich. | Status `blockiert`, **nicht** dauerhaft `ausgeschlossen` |

Ausdrücklich: Eine vermeintliche Dublette ist **kein** vorgelagertes Exclusion Criterion. Über Dubletten wird erst nach der `0 / 1 / n`-Analyse entschieden (Abschnitt 5).

---

## 4. Quellenrollen

| Ebene | Quellen | Methodische Rolle | Standardbehandlung |
| --- | --- | --- | --- |
| A | `SRC-001`, `SRC-002`, `SRC-009`, `SRC-010` | Primäre, rechtsverbindliche Anforderungen | systematische Gap-Extraktion in den freigegebenen Quellenbereichen |
| B | `SRC-003`, `SRC-004` | Nicht rechtsverbindliche Interpretation, Interplay, Qualification/Classification | Ergänzungs- und Interpretationsquelle; kein zweiter Gap-Kernkatalog |
| C | `SRC-005` – `SRC-008` | Technische, QMS-, Lifecycle- und Usability-Normen | konkrete Normanforderungen erst aus autorisiertem Volltext |

Zur Ebene B im Einzelnen:

- `SRC-003` dient primär als Crosswalk-, Interpretations- und Deduplizierungsquelle.
- `SRC-004` dient primär als Qualification-, Classification- und `RUL`-Quelle.

Die normative Qualität der Ebenen wird zu keinem Zeitpunkt nivelliert. Guidance und Norm werden sprachlich nicht zu gesetzlichen Pflichten aufgewertet.

Die Tabelle nennt die derzeit zugeordneten Quellen. Weitere Quellen werden ausschließlich über Abschnitt 4.3 zugeordnet.

Zur Ebene A: `SRC-009` ist über die Change Control in Abschnitt 10.23 aufgenommen und wird mit der Nutzungsart `triggerbasiert` geführt; ihre Quellenbereiche stehen in Abschnitt 9.9. `SRC-010` ist über die Change Control in Abschnitt 10.34 aufgenommen und wird mit der Nutzungsart `unterstützend` ausschließlich als Primärrechtsanker der MDR/IVDR-Abgrenzungslogik geführt; die Standardbehandlung „systematische Gap-Extraktion“ der Ebene A gilt für `SRC-010` nicht (Abschnitt 9.10).

### 4.1 Definition der Quellenebenen

Die Ebenen A, B und C bleiben unverändert bestehen. Allgemein gilt:

| Ebene | Umfang |
| --- | --- |
| A | rechtsverbindliche regulatorische Quellen |
| B | nicht rechtsverbindliche regulatorische Guidance- und Interpretationsquellen |
| C | technische Normen und formale Standardisierungspublikationen, soweit sie für den wissenschaftlichen Scope relevant sind; insbesondere ISO- und IEC-Normen sowie gegebenenfalls Technische Spezifikationen (TS), Technische Berichte (TR) oder öffentlich verfügbare Spezifikationen (PAS) |

Die Zugehörigkeit zu einer Ebene — insbesondere zu Ebene C — bedeutet **nicht** automatisch, dass aus der Quelle regulatorische Anforderungen extrahiert werden. Ob und wie eine Quelle genutzt wird, bestimmt ausschließlich ihre Nutzungsart (Abschnitt 4.2). Allein der Dokumenttyp (Norm, TS, TR, PAS) begründet keine Requirement-Extraktion.

### 4.2 Nutzungsart

Die Nutzungsart ist ein von der Quellenebene unabhängiges Merkmal einer Quelle. Jede Ebene kann grundsätzlich mit jeder Nutzungsart kombiniert werden; eine Ebene-C-Quelle kann also systematisch, unterstützend oder triggerbasiert genutzt werden.

| Nutzungsart | Bedeutung |
| --- | --- |
| `systematisch` | Die Quelle kann Teil der systematischen Requirement- bzw. Gap-Analyse sein. Eine Requirement-Extraktion erfolgt nur bei ausreichender Source Fidelity und, bei lizenzpflichtigen Quellen, nur bei autorisiertem Volltext (Abschnitt 4.4). |
| `unterstützend` | Die Quelle dient Interpretation, Crosswalk, Terminologie, wissenschaftlicher Herleitung oder Evidenz. Sie erzeugt grundsätzlich keine eigenen `RR`. |
| `triggerbasiert` | Die Quelle wird erst bei dokumentierter Erfüllung eines Applicability-Triggers für einen konkreten Produkttyp bzw. Fall aktiviert. |

Abgrenzung:

- Die Nutzungsart gilt je Quelle. Die Coverage-Kategorien aus Abschnitt 6 gelten dagegen je Quelle und Themencluster, die Priorität `Ergänzend, conditional` in Abschnitt 9 je Quellenbereich. Beide bleiben unverändert.
- Die Nutzungsart wird für jede nach Abschnitt 4.3 neu aufgenommene Quelle in deren Change Control ausdrücklich festgelegt. Für `SRC-001` bis `SRC-008` gelten die bestehenden Rollenbeschreibungen dieses Abschnitts und der Abschnitte 8 und 9 unverändert fort; eine rückwirkende Zuordnung erfolgt nicht.
- Eine spätere Änderung der Nutzungsart einer Quelle ist eine scope-wirksame Änderung nach Abschnitt 10.2.

### 4.3 Aufnahme weiterer Quellen

`SRC-005` bis `SRC-008` sind der im Exposé ausdrücklich benannte initiale Normenbestand, aber keine abschließende Positivliste. Eine weitere Quelle darf innerhalb des unveränderten wissenschaftlichen Scopes aufgenommen werden, wenn kumulativ:

1. sie für KI-basierte Medizinproduktesoftware innerhalb mindestens eines bestehenden Themenclusters nach [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) relevant ist **oder** für eine freigegebene regelbasierte Applicability-, Qualification-, Classification- oder Boundary-Logik ([RUL_METHOD.md](RUL_METHOD.md)) als notwendiger Primärrechtsanker benötigt wird;
2. sie gegenüber dem vorhandenen Quellenkorpus einen eigenständigen, nachvollziehbaren Beitrag leistet;
3. ihre Aufnahme durch eine dokumentierte Coverage Change Control nach Abschnitt 10.2 freigegeben wurde, einschließlich Quellenebene und Nutzungsart;
4. Fassung, Status und Bezugsquelle anhand einer belastbaren Primärquelle verifiziert wurden.

Erst danach wird in [SOURCES.md](SOURCES.md) eine `SRC`-ID vergeben.

Eine Aufnahme allein als Primärrechtsanker nach Nr. 1 zweite Alternative begründet weder Theme-Coverage noch `RR` und autorisiert **nicht** automatisch eine systematische Gap- bzw. `RR`-Extraktion aus der Quelle; eine solche Extraktion setzt eine eigene Coverage Change Control nach Abschnitt 10.2 voraus. Quellenebenen und Nutzungsarten bleiben unverändert; eine neue Quellenkategorie wird nicht eingeführt.

**Scope-Regel:** RegScoutX verfolgt **keine** vollständige atomare Abbildung sämtlicher produktspezifischer Normen der Medizintechnik. Systematisch betrachtet werden horizontale Quellen, die für KI-basierte Medizinproduktesoftware innerhalb des definierten Untersuchungsumfangs relevant sind.

**Triggerprinzip:** Produktspezifische Quellen bzw. Normfamilien werden nur bei einem entsprechenden Applicability-Trigger aktiviert. Die Fallstudie darf dabei nach Abschnitt 1.1 nur Trigger auslösen, die vorab festgelegt wurden; sie erweitert die Core-Coverage nicht.

### 4.4 Volltext und Source Fidelity

- Es gilt die bestehende Logik: Zugänglichkeit `lizenzpflichtig` in [SOURCES.md](SOURCES.md), Bearbeitungsstatus `blockiert` in diesem Plan (Abschnitt 10.1). Ein zusätzlicher Status wird nicht eingeführt.
- Eine systematische Requirement-Extraktion aus einer lizenzpflichtigen Norm ist blockiert, solange kein autorisierter Volltext im Projekt vorliegt (Exclusion Criterion E-12).
- Normanforderungen werden **niemals** aus Erinnerung, Inhaltsverzeichnissen, Produktseiten oder Sekundärquellen rekonstruiert.
- Dasselbe Source-Fidelity-Prinzip gilt für unterstützende Quellen: Nicht belegte Norminhalte werden auch zu Interpretations-, Crosswalk- oder Evidenzzwecken nicht erfunden.

### 4.5 Fachliche Relevanz und MDR-Harmonisierungsstatus

- Fachliche Relevanz und MDR-Harmonisierungsstatus sind voneinander unabhängig.
- Eine Quelle darf fachlich relevant sein, ohne in der aktuellen MDR-Harmonisierungsliste geführt zu sein.
- Eine Harmonisierung darf nur behauptet werden, wenn die konkrete EN-Referenz einschließlich der relevanten Fassung und Amendments anhand der zum Prüfzeitpunkt maßgeblichen amtlichen Fundstelle nach Durchführungsbeschluss (EU) 2021/1182 nachvollziehbar geprüft wurde.
- Ein fehlender Treffer in der Harmonisierungsliste darf nicht als fehlende fachliche Relevanz interpretiert werden.
- Ein strukturiertes Harmonisierungsfeld wird derzeit **nicht** eingeführt. Es wird erst eingeführt, falls dies bei der späteren Registrierung konkreter Quellen methodisch erforderlich ist.

### 4.6 Noch nicht veröffentlichte Normungsprojekte

Unveröffentlichte Normungsprojekte (z. B. im Stadium AWI, CD oder DIS) erhalten **keine** `SRC`-ID und gehören nicht zum aktiven Quellenkorpus. Eine Research-Watchlist kann später gemeinsam mit einem dokumentierten Landscape-Audit eingerichtet werden; sie ist nicht Bestandteil dieses Plans.

---

## 5. Cross-Source-Deduplizierung

Die Deduplizierung findet **nach** der `0 / 1 / n`-Analyse und **vor** dem endgültigen Katalog-Freeze statt. Sie ist kein Filter, der vor der Extraktion angewendet wird.

### 5.1 Rechtsakt ↔ Rechtsakt

Zwei Fundstellen bezeichnen nur dann denselben atomaren Sollzustand, wenn insbesondere

- Adressat,
- Trigger,
- normativer Gegenstand und
- Compliance-Ergebnis

materiell übereinstimmen **und** derselbe Erfüllungsstatus beide Stellen sachgerecht abbildet.

Thematische oder sprachliche Ähnlichkeit genügt nicht.

### 5.2 Guidance → Rechtsakt

Die Paraphrase oder Interpretation einer gesetzlichen Pflicht erzeugt keine neue `RR`. Die gesetzliche Pflicht bleibt am Rechtsakt verankert; die Guidance kann als `supplementary`- bzw. Interpretationsquelle geführt werden.

### 5.3 Norm → Rechtsakt

Eine technische Konkretisierung erzeugt nicht automatisch eine zweite `RR`. Nur ein eigenständig prüfbarer normativer Sollzustand wird nach der regulären `RR`-Methode separat beurteilt.

### 5.4 Eigenständiger Guidance- oder Normgehalt

Eine eigene `RR` entsteht nur, wenn

- im eigenen Quellenkontext ein eigenständig prüfbarer Sollzustand vorliegt,
- dies regulatorisch sinnvoll ist und
- die `RR`-Methode vollständig erfüllt ist.

**Merksatz:** Eine neue `RR` entsteht nie allein deshalb, weil dieselbe Pflicht in einer zweiten Quelle anders formuliert oder ausführlicher erläutert wird.

---

## 6. Coverage-Kategorien

| Kategorie | Bedeutung |
| --- | --- |
| `Kernbereich` | Direkter, im festgelegten Scope systematisch zu prüfender Anforderungsbereich. |
| `Ergänzungsbereich` | Nur bei definiertem Trigger oder nach Abgleich mit bereits extrahierten Kernanforderungen zu vertiefender Inhalt. |
| `voraussichtlich nicht relevant` | Kein geplanter systematischer Beitrag zum betreffenden Cluster. Spätere Aufnahme nur durch Change Control. |
| `derzeit nicht belastbar beurteilbar` | Der Quellen- bzw. Volltextzugriff reicht für eine belastbare Einordnung noch nicht aus. |

---

## 7. `expected_theme_clusters`

Coverage-Ebene und `RR`-Ebene werden strikt getrennt.

Das Coverage-Feld `expected_theme_clusters` bezeichnet eine **nichtnormative Vorauswahl** möglicher späterer `RR`-Themen. Für einen Gap-Kandidaten enthält es `1..n` Werte, ausschließlich aus den acht kanonischen Werten in [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 1.

Mehrere Werte bedeuten **nicht**, dass eine `RR` mehrfach klassifiziert würde. Sie bedeuten ausschließlich: Aus einem Quellenbereich können nach der `0 / 1 / n`-Analyse mehrere atomare `RR` mit unterschiedlichem primärem Gegenstand entstehen.

Nach der Extraktion trägt jede `RR` weiterhin exakt **einen** `theme_cluster`.

**Formalpräzisierung:** In `expected_theme_clusters` wird kein neunter Wert eingeführt. Ist für einen `RUL`-, Interpretations- oder ausgeschlossenen Bereich keine Gap-Clusterprognose sinnvoll, steht dort `—`, und der Grund wird im Hinweisfeld erläutert. So entsteht keine zweite Taxonomie.

---

## 8. Source-to-Theme-Coverage-Matrix

Abkürzungen der Spalten: QRM = Qualitäts- und Risikomanagement, DG = Data Governance, TR = Transparenz, MA = Menschliche Aufsicht, RO = Robustheit, PMM = Post-Market-Monitoring, SLZ = Software-Lebenszyklus, GT = Gebrauchstauglichkeit.

| Quelle | QRM | DG | TR | MA | RO | PMM | SLZ | GT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SRC-001` | Kernbereich | voraussichtlich nicht relevant | Kernbereich | voraussichtlich nicht relevant | Kernbereich | Kernbereich | Kernbereich | Kernbereich |
| `SRC-002` | Kernbereich | Kernbereich | Kernbereich | Kernbereich | Kernbereich | Kernbereich | Ergänzungsbereich | voraussichtlich nicht relevant |
| `SRC-003` | Ergänzungsbereich | Ergänzungsbereich | Ergänzungsbereich | Ergänzungsbereich | Ergänzungsbereich | Ergänzungsbereich | voraussichtlich nicht relevant | voraussichtlich nicht relevant |
| `SRC-004` | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant |
| `SRC-005` | Kernbereich | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | derzeit nicht belastbar beurteilbar | derzeit nicht belastbar beurteilbar | derzeit nicht belastbar beurteilbar |
| `SRC-006` | Kernbereich | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | Ergänzungsbereich | derzeit nicht belastbar beurteilbar | Ergänzungsbereich |
| `SRC-007` | derzeit nicht belastbar beurteilbar | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | derzeit nicht belastbar beurteilbar | Kernbereich | derzeit nicht belastbar beurteilbar |
| `SRC-008` | Ergänzungsbereich | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | voraussichtlich nicht relevant | voraussichtlich nicht relevant | derzeit nicht belastbar beurteilbar | derzeit nicht belastbar beurteilbar | Kernbereich |
| `SRC-009` | Ergänzungsbereich | voraussichtlich nicht relevant | Ergänzungsbereich | voraussichtlich nicht relevant | Ergänzungsbereich | Ergänzungsbereich | voraussichtlich nicht relevant | Ergänzungsbereich |
| `SRC-010` | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant | voraussichtlich nicht relevant |

Erläuterungen:

- `SRC-002` × Software-Lebenszyklus ist `Ergänzungsbereich` wegen `SRC-002#Art.17/Abs.1/Buchst.b` bis `Buchst.d`. Die Quelle bildet keinen eigenständigen Software-Lifecycle-Regelungskomplex wie `SRC-007`.
- `SRC-004` ist in allen acht Clustern `voraussichtlich nicht relevant` **für den Gap-Katalog**. Die Quelle bleibt gleichwohl wichtig für die `RUL`-, Qualification- und Classification-Logik (Abschnitt 9.4).
- `SRC-009` (Abschnitt 10.23): Die Zeile folgt aus den ex-ante erwarteten Themenclustern der freigegebenen Quellenbereiche in Abschnitt 9.9. Cluster mit erwartetem Beitrag stehen wegen der Nutzungsart `triggerbasiert` auf `Ergänzungsbereich` (Abschnitt 6: nur bei definiertem Trigger zu vertiefen); Cluster ohne erwarteten Beitrag auf `voraussichtlich nicht relevant`.
- `SRC-010` (Abschnitt 10.34) ist in allen acht Clustern `voraussichtlich nicht relevant` **für den Gap-Katalog**. Die Quelle dient ausschließlich als Primärrechtsanker der MDR/IVDR-Abgrenzung in der `RUL`-Logik (Abschnitt 9.10).

---

## 9. Freigegebene Quellenbereiche

Alle Bearbeitungsstatus stehen initial auf `geplant`, sofern nicht ausdrücklich `blockiert` vermerkt ist.

### 9.1 Gap-Coverage `SRC-001` — MDR

| Quellenbereich | `expected_theme_clusters` | Priorität | Trigger | Rolle / Hinweis | Bearbeitungsstatus | Scope-Begründung |
| --- | --- | --- | --- | --- | --- | --- |
| `SRC-001#Art.10/Abs.2` | Qualitäts- und Risikomanagement | Kern | — | Risikomanagementsystem des Herstellers | abgeschlossen | Kernpflicht im Cluster QRM, unmittelbar Compliance-/Gap-fähig |
| `SRC-001#Art.10/Abs.9` — Einleitung sowie Buchst. c, d, e, l, m | Qualitäts- und Risikomanagement | Kern | — | **Nicht** pauschal als gesamter Artikel; präzise Teil-Lokatoren verwenden, soweit sinnvoll | abgeschlossen | Core-QMS-Prüfung auf die thematisch einschlägigen Teilbereiche |
| `SRC-001#Art.10/Abs.9/Buchst.g` | Qualitäts- und Risikomanagement, Software-Lebenszyklus | Ergänzend | — | Endgültige Zuordnung erst bei Extraktion | abgeschlossen | Produktrealisierung einschließlich Planung, Auslegung und Entwicklung; ein vollständiger Ausschluss würde mögliche softwarebezogene Lifecycle-Pflichten vor der Atomisierung verlieren |
| `SRC-001#Art.10/Abs.9/Buchst.i` | Post-Market-Monitoring | Ergänzend | — | Später gegen Art. 83 atomar deduplizieren | abgeschlossen | Möglicher eigenständiger Beitrag im Cluster PMM |
| `SRC-001#Anh.I/Nr.3` | Qualitäts- und Risikomanagement | Kern | — | Als eigener Quellenbereich geführt, um die Abarbeitung transparent zu halten | abgeschlossen | Grundlegende Sicherheits- und Leistungsanforderung mit QRM-Gegenstand |
| `SRC-001#Anh.I/Nr.4` | Qualitäts- und Risikomanagement | Kern | — | Als eigener Quellenbereich geführt, um die Abarbeitung transparent zu halten | abgeschlossen | Grundlegende Sicherheits- und Leistungsanforderung mit QRM-Gegenstand |
| `SRC-001#Anh.I/Nr.5` | Gebrauchstauglichkeit | Kern | — | — | abgeschlossen | Anwendungsbezogene Risiken; Kerncluster GT |
| `SRC-001#Anh.I/Nr.17.1` | Robustheit | Kern | — | — | abgeschlossen | Verhalten und Zuverlässigkeit softwarebezogener Produkte |
| `SRC-001#Anh.I/Nr.17.2` | Software-Lebenszyklus | Kern | — | — | abgeschlossen | Entwicklungs- und Lebenszyklusbezogene Anforderung |
| `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` | Gebrauchstauglichkeit | Ergänzend, conditional | vorgesehene Laienanwendung | — | abgeschlossen | Nur bei Laienanwendung im Scope; sonst kein systematischer Beitrag |
| `SRC-001#Anh.I/Nr.23.1` | Transparenz, Gebrauchstauglichkeit | Kern | — | **Nicht** ex ante ausschließlich Transparenz zuordnen | abgeschlossen | Der Bereich enthält potenziell unterschiedliche atomare Informations- sowie Darbietungs-/Verständlichkeitsanforderungen |
| `SRC-001#Anh.I/Nr.23.4` — nur Buchst. b, e, f, g, h, j, k, s, ab | Transparenz | Ergänzend | — | **Nicht** vollständig aufnehmen; Applicability der einzelnen Buchstaben später erhalten | abgeschlossen | Nur die bereits verifizierten thematisch relevanten Unterpunkte werden geprüft |
| `SRC-001#Art.83` | Post-Market-Monitoring | Kern | — | — | abgeschlossen | Kernpflicht der Überwachung nach Inverkehrbringen |
| `SRC-001#Art.84` | Post-Market-Monitoring | Kern | — | — | abgeschlossen | Kernpflicht der Überwachung nach Inverkehrbringen |
| `SRC-001#Anh.III/Abschn.1` | Post-Market-Monitoring | Kern | — | Querverweise auf klinische Nachbeobachtung eröffnen **keine** Vollauswertung von Anhang XIV | abgeschlossen | Konkretisierung der PMM-Kernpflichten |
| `SRC-001#Art.85` | Post-Market-Monitoring | Ergänzend, conditional | Klasse I | — | abgeschlossen | Klassenabhängige PMM-Pflicht |
| `SRC-001#Art.86` | Post-Market-Monitoring | Ergänzend, conditional | Klasse IIa, IIb oder III | — | abgeschlossen | Klassenabhängige PMM-Pflicht |

### 9.2 `SRC-001` — bewusst nicht im initialen Gap-Coverage

| Bereich | `expected_theme_clusters` | Begründung | Behandlung |
| --- | --- | --- | --- |
| `SRC-001#Art.10/Abs.9` Buchst. a, b, f, h, j, k | — | Primärer Gegenstand außerhalb des definierten Gap-Scope bzw. in separat geregelten Compliance-Bereichen | nicht initial systematisch extrahiert; keine Gap-Clusterprognose sinnvoll |
| `SRC-001#Anh.I/Nr.17.4` | — | Primär IT- und Cybersecurity-Anforderungen; der Cluster Robustheit wird nicht künstlich erweitert | außerhalb initialem Gap-Coverage |
| `SRC-001#Anh.I/Nr.18.8` | — | Primär Schutz vor unbefugtem Zugriff | außerhalb initialem Robustheits-Scope |
| Vollständige klinische Bewertung | — | Exclusion Criterion E-6 | keine Vollauswertung |
| Vollständige technische Dokumentation | — | Exclusion Criterion E-7 | kein eigener Gap-Bereich |
| Vollständige Konformitätsbewertungsanhänge | — | Exclusion Criterion E-8 | Lifecycle-/Applicability-Kontext |

`SRC-001#Art.10/Abs.9/Buchst.g` ist **nicht** Teil dieser Ausschlusstabelle, sondern in Abschnitt 9.1 als `Ergänzungsbereich` geführt.

### 9.3 `SRC-001` — `RUL`-/Entscheidungslogik

Diese Bereiche sind von der Gap-Coverage und der Stopping Rule des `RR`-Katalogs getrennt zu verfolgen. Es wird keine `RUL`-ID vergeben.

| Quellenbereich | Rolle | Hinweis |
| --- | --- | --- |
| `SRC-001#Art.2/Nr.1` | Applicability / Qualification | `RUL` statt Gap-`RR`, soweit keine eigenständige Compliance-Pflicht extrahierbar ist |
| `SRC-001#Art.51/Abs.1` | Classification | `RUL` statt Gap-`RR`, soweit keine eigenständige Compliance-Pflicht extrahierbar ist |
| `SRC-001#Anh.VIII/Kap.III/Abschn.6.3/Regel.11` | Software Classification | `RUL` statt Gap-`RR`, soweit keine eigenständige Compliance-Pflicht extrahierbar ist |

### 9.4 Gap-Coverage `SRC-002` — EU AI Act

| Quellenbereich | `expected_theme_clusters` | Priorität | Trigger | Rolle / Hinweis | Bearbeitungsstatus | Scope-Begründung |
| --- | --- | --- | --- | --- | --- | --- |
| `SRC-002#Art.9` | Qualitäts- und Risikomanagement | Kern | — | Erster systematischer Quellenbereich nach dem Freeze | abgeschlossen | Kernpflicht im Cluster QRM |
| `SRC-002#Art.10` | Data Governance | Kern | — | Bereits bestehende Pilot-`RR` aus Abs. 2 Buchst. f/g nicht erneut duplizieren; der gesamte festgelegte Art.-10-Bereich wird gleichwohl systematisch abgearbeitet | abgeschlossen | Kernpflicht im Cluster DG |
| `SRC-002#Art.4a/Abs.1` | Data Governance | Ergänzend, conditional | Ein Anbieter eines Hochrisiko-KI-Systems nutzt die in Art. 4a Abs. 1 vorgesehene ausnahmsweise Verarbeitung besonderer Kategorien personenbezogener Daten, weil diese Verarbeitung zur Erkennung und Korrektur von Verzerrungen im Zusammenhang mit Art. 10 Abs. 2 Buchst. f und g strikt erforderlich ist. | Der vollständige Absatz wird vor jeder Clusterentscheidung zunächst auf `0 / 1 / n` atomisiert. Erst anschließend wird je atomarer Aussage bestimmt, ob ein vorhandener Gap-Cluster einschlägig ist oder die Aussage außerhalb des Gap-Themen-Scope liegt. Privacy-, Security-, Zugriffs-, Lösch- und Dokumentationsaspekte dürfen **nicht** allein wegen ihrer Position in Art. 4a automatisch dem Cluster Data Governance zugeordnet werden. Der Wert `Data Governance` ist eine reine Ex-ante-Erwartung nach Abschnitt 7 und keine vorweggenommene Clusterentscheidung; einzelne atomare Pflichten können nach der Prüfung einem anderen bereits bestehenden Cluster zugeordnet oder nach einem bestehenden Exclusion Criterion außerhalb des Gap-Themen-Scope eingeordnet werden. Es wird kein neuer Cluster geschaffen; Datenschutz und DSGVO bleiben nach `CONTROLLED_VOCABULARY.md` Abschnitt 5 weiterhin kein eigener Gap-Cluster. | abgeschlossen | Die aktuelle Fassung von Art. 10 Abs. 1 und Abs. 6 verweist ausdrücklich auf Art. 4a Abs. 1. Der Absatz enthält providerseitige Bedingungen für die ausnahmsweise Verarbeitung besonderer Kategorien personenbezogener Daten zur Bias-Erkennung und -Korrektur nach Art. 10 Abs. 2 Buchst. f und g. Wegen seines konditionalen Charakters wird er als ergänzender conditional Quellenbereich aufgenommen. |
| `SRC-002#Art.13` | Transparenz | Kern | — | Bestehende `RR-001`/`RR-002` aus Abs. 1 als bereits extrahierte Teile berücksichtigen, nicht neu vergeben | abgeschlossen | Kernpflicht im Cluster TR |
| `SRC-002#Art.14` | Menschliche Aufsicht | Kern | — | — | abgeschlossen | Kernpflicht im Cluster MA |
| `SRC-002#Art.15/Abs.1` | Robustheit | Kern | — | Siehe Scope- und Atomizitätsregel unten | abgeschlossen | Kernpflicht im Cluster RO |
| `SRC-002#Art.15/Abs.3` | Transparenz | Kern | — | — | abgeschlossen | Informationsbezogener Gegenstand |
| `SRC-002#Art.15/Abs.4` | Robustheit | Kern | — | — | abgeschlossen | Verhaltensbezogener Gegenstand |
| `SRC-002#Art.17/Abs.1` — Chapeau sowie Buchst. a, e, j, k, l, m | Qualitäts- und Risikomanagement | Kern | — | **Nicht** pauschal als homogener QRM-Block behandeln | abgeschlossen | Core-QMS-Bereiche des Qualitätsmanagementsystems |
| `SRC-002#Art.17/Abs.1` — Buchst. b, c, d | Qualitäts- und Risikomanagement, Software-Lebenszyklus | Kern | — | Ebenfalls Teil der systematischen Art.-17-Prüfung; endgültige `RR`-Zuordnung erst nach Atomisierung | abgeschlossen | Entwicklungs- und prüfbezogene Bestandteile mit möglichem Lifecycle-Gegenstand |
| `SRC-002#Art.17/Abs.1/Buchst.f` | Data Governance | Ergänzend | — | Nach Art. 10 prüfen und atomar deduplizieren | abgeschlossen | Möglicher eigenständiger DG-Beitrag |
| `SRC-002#Art.17/Abs.1/Buchst.g` | Qualitäts- und Risikomanagement | Ergänzend | — | Integration mit Art. 9 prüfen | abgeschlossen | Möglicher eigenständiger QRM-Beitrag |
| `SRC-002#Art.17/Abs.1/Buchst.h` | Post-Market-Monitoring | Ergänzend | — | Integration mit Art. 72 prüfen | abgeschlossen | Möglicher eigenständiger PMM-Beitrag |
| `SRC-002#Art.17/Abs.2` | Qualitäts- und Risikomanagement | Kern | — | — | abgeschlossen | Kernpflicht im Cluster QRM |
| `SRC-002#Art.72` | Post-Market-Monitoring | Kern | — | — | abgeschlossen | Kernpflicht im Cluster PMM |
| `SRC-002#Art.26/Abs.2` | Menschliche Aufsicht | Ergänzend, conditional | Deployer-Perspektive aktiviert | — | ausgeschlossen | Betreiberpflicht; nur bei aktivierter Perspektive im Scope |
| `SRC-002#Art.26/Abs.4` | Data Governance | Ergänzend, conditional | Deployer-Perspektive aktiviert | — | ausgeschlossen | Betreiberpflicht; nur bei aktivierter Perspektive im Scope |
| `SRC-002#Art.26/Abs.5` | Post-Market-Monitoring | Ergänzend, conditional | Deployer-Perspektive aktiviert | Erst nach Atomisierung bestimmen, ob der jeweilige Betriebsüberwachungs-/Feedbackanteil diesem Cluster zugeordnet werden kann; Vorfall- und Vigilanzanteile nicht automatisch aufnehmen | ausgeschlossen | Betreiberpflicht; nur bei aktivierter Perspektive im Scope |

**Scope- und Atomizitätsregel zu `SRC-002#Art.15/Abs.1`:**

Der **vollständige** Absatz wird zunächst der `0 / 1 / n`-Prüfung unterzogen. Es wird **keine** Cybersecurity-Komponente vor der Atomisierung entfernt.

- Ergibt die spätere Atomisierung eine eigenständige Cybersecurity-Verpflichtung, kann diese mangels Zuordenbarkeit zu den acht Themenclustern als außerhalb des Gap-Themen-Scope dokumentiert werden und erzeugt keine Gap-`RR`.
- Ergibt die Atomizitätsprüfung **keinen** zulässigen Split, darf die Cybersecurity-Komponente nicht aus dem gemeinsamen Normsatz entfernt werden. Die logische `und`-Struktur bleibt zwingend erhalten.

### 9.5 `SRC-002` — Interplay und Ausschluss

| Bereich | `expected_theme_clusters` | Einordnung | Behandlung |
| --- | --- | --- | --- |
| `SRC-002#Art.8/Abs.2` | — | Interplay- und Integrationskontext | Ergänzend; keine automatische Gap-`RR`; keine Gap-Clusterprognose sinnvoll |
| `SRC-002#Art.12` | — | Primärer Gegenstand Logging und Rückverfolgbarkeit | aus initialem Gap-Coverage; kein freigegebener eigener Cluster |
| `SRC-002#Art.15/Abs.2` | — | Institutioneller bzw. Kommissionskontext | außerhalb Gap-Coverage |
| `SRC-002#Art.15/Abs.5` | — | Eigenständiger Cybersecurity-Regelungsgegenstand | nicht künstlich in Robustheit umklassifizieren |
| `SRC-002#Art.17/Abs.1/Buchst.i` | — | Vorfallmelde- und Vigilanzbereich | außerhalb initialem Themen-Scope |
| `SRC-002#Art.17/Abs.3` | — | Interplay- und QMS-Integrationskontext | Ergänzend; keine automatische eigene Gap-`RR` |
| `SRC-002#Art.17/Abs.4` | — | Sonderregel für Finanzinstitute | außerhalb Adressaten- und Systemscope |

Diese Einordnung ändert **nicht** die Regel zu `SRC-002#Art.15/Abs.1`: Dort wird der gemeinsame Absatz zuerst vollständig atomisiert.

### 9.6 `SRC-002` — `RUL`-/Entscheidungslogik

Getrennt von der Gap-Coverage zu verfolgen. Bis Version 1.45 wurde hier keine `RUL`-ID vergeben; seit Abschnitt 10.36 sind die Bereiche als `RUL-027` bis `RUL-043` umgesetzt ([DECISION_LOGIC_SRC_002_AI_ACT_APPLICABILITY.md](DECISION_LOGIC_SRC_002_AI_ACT_APPLICABILITY.md)). Keine Gap-`RR`.

| Quellenbereich | Rolle | Hinweis | Bearbeitungsstatus |
| --- | --- | --- | --- |
| `SRC-002#Art.6/Abs.1` | Applicability / High-Risk Classification | `RUL` statt Gap-`RR`, soweit ausschließlich Einordnungslogik; einschließlich Abs. 1a bis 1c | abgeschlossen |
| `SRC-002#Anh.I/Abschn.A/Nr.11` | Produktrechtsbezug / High-Risk Applicability | `RUL` statt Gap-`RR`, soweit ausschließlich Einordnungslogik | abgeschlossen |
| `SRC-002#Art.2` (Abs. 1, 3, 6, 8) und `SRC-002#Art.3/Nr.1` | Anwendungsbereich und KI-System-Definition | `RUL-027` bis `RUL-029`; Art. 2 Abs. 13 ohne Begrenzungsprofil im Quellenstand | abgeschlossen |
| `SRC-002#Art.6/Abs.2` mit `SRC-002#Anh.III/Nr.1/Buchst.a` bis `c` und `Nr.5/Buchst.a`, `c`, `d` | Hochrisiko-Routing nach Anhang III | `RUL-038`; übrige Anhang-III-Bereiche nur als fail-closed Prüfhinweis | abgeschlossen |
| `SRC-002#Art.6/Abs.3` und `Abs.4`, `SRC-002#Art.49/Abs.2` | Ausnahme vom Anhang-III-Weg und Folgen der Selbsteinstufung | `RUL-040` bis `RUL-042`; Art. 6 Abs. 4 und Art. 49 Abs. 2 nur als Routing-/Compliance-Hinweis, keine `RR` | abgeschlossen |
| `SRC-002#Art.111/Abs.2` und `SRC-002#Art.113/Buchst.c` | Übergang und Anwendungstermine | `RUL-034` bis `RUL-037`, `RUL-039` | abgeschlossen |

### 9.7 `SRC-003` und `SRC-004`

**`SRC-003`** wird nicht als zweiter Gap-Kernkatalog behandelt. Methodische Rolle:

- Interplay,
- Crosswalk,
- Interpretation,
- Deduplizierung,
- Prüfung auf möglichen eigenständigen zusätzlichen Guidance-Gehalt, und zwar erst gegen den stabilisierten Rechtsakt-Korpus.

Coverage: Ergänzungsquelle in den Clustern Qualitäts- und Risikomanagement, Data Governance, Transparenz, Menschliche Aufsicht, Robustheit und Post-Market-Monitoring. Es wird zum jetzigen Zeitpunkt keine Guidance-`RR` erzeugt; einzelne Frage- oder Abschnittsnummern werden hier nicht festgelegt.

Bearbeitungsstatus `SRC-003` (Abschnitt 10.1): `abgeschlossen` (Abschnitt 10.32); Prüfung eröffnet in Abschnitt 10.31. Bis Version 1.40 war für `SRC-003` kein ausdrücklicher Statuseintrag geführt; die Prüfung war nach Abschnitt 13 noch nicht begonnen.

**`SRC-004`** dient primär der Qualification, der Classification, der Interpretation zu Regel 11 und der Unterstützung bei `RUL`-Grenzfällen. Ein systematischer Gap-`RR`-Katalog wird daraus nicht abgeleitet; einzelne Abschnittsnummern werden hier nicht festgelegt.

Bearbeitungsstatus `SRC-004` (Abschnitt 10.1): `abgeschlossen` (Abschnitt 10.34); Prüfung eröffnet in Abschnitt 10.33. Bis Version 1.42 war für `SRC-004` kein ausdrücklicher Statuseintrag geführt; die Prüfung war nach Abschnitt 13 noch nicht begonnen.

### 9.8 `SRC-005` bis `SRC-008` — Normen

Es werden keine Normklauseln rekonstruiert. Festgehalten wird ausschließlich der gesicherte Grobgegenstand.

| Quelle | Gesicherter Grobgegenstand | Core-Cluster | Ergänzend plausibel | Detail-Coverage | Blocker |
| --- | --- | --- | --- | --- | --- |
| `SRC-005` | Qualitätsmanagementsystem | Qualitäts- und Risikomanagement | — | abgeschlossen (Abschnitt 10.37) | Evidence-Freeze offen: `OPEN_SOURCE_PACKAGE_CHECK` (angekündigte Berichtigung) |
| `SRC-006` | Risikomanagement über den Produktlebenszyklus | Qualitäts- und Risikomanagement | Post-Market-Monitoring, Gebrauchstauglichkeit | abgeschlossen (Abschnitt 10.37) | — |
| `SRC-007` | Software-Lebenszyklusprozesse für Entwicklung und Wartung | Software-Lebenszyklus | — | abgeschlossen (Abschnitt 10.37) | — |
| `SRC-008` | Usability Engineering und Use-Error-Risiken | Gebrauchstauglichkeit | Qualitäts- und Risikomanagement | abgeschlossen (Abschnitt 10.37) | — |

Klarstellung: Der fehlende Volltext blockiert **nicht** den Start der systematischen Extraktion aus `SRC-001` und `SRC-002`. Er blockiert jedoch den methodisch vollständigen Abschluss des im Exposé vorgesehenen Gesamtkorpus. Bevor Norm-`RR` extrahiert werden, ist dieser Plan per Change Control auf autorisierte Klauselbereiche zu präzisieren.

Seit Version 1.47 (Abschnitt 10.37) liegen autorisierte Volltexte als deutsche Arbeitsfassungen vor; alle vier Normen sind vollständig klauselweise systematisch adjudiziert und als `RR-378` bis `RR-959` integriert ([RR_EXTRACTION_STANDARDS_SRC_005_008.md](RR_EXTRACTION_STANDARDS_SRC_005_008.md)). Die Spalten Grobgegenstand, Core-Cluster und „Ergänzend plausibel“ bleiben als Ex-ante-Festlegung unverändert.

### 9.9 `SRC-009` — Durchführungsverordnung (EU) 2021/2226

Quellenebene A, Nutzungsart `triggerbasiert` (Abschnitt 4.2); freigegeben durch die Change Control in Abschnitt 10.23. Globaler Applicability-Trigger aller Zeilen: elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware. Die Zeilen sind — wie die übrigen conditional Quellenbereiche — ex ante zur systematischen `0 / 1 / n`-Prüfung freigegeben; der Trigger bestimmt die Anwendbarkeit im konkreten Fall. Innerhalb der Quelle sind weitere Zweige erst bei der Extraktion zu unterscheiden (Abschnitt 10.23).

| Quellenbereich | `expected_theme_clusters` | Priorität | Trigger | Rolle / Hinweis | Bearbeitungsstatus | Scope-Begründung |
| --- | --- | --- | --- | --- | --- | --- |
| `SRC-009#Art.3` | Transparenz, Gebrauchstauglichkeit | Ergänzend, conditional | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware | innere Zweige nach Abschnitt 10.23 erst bei der Extraktion unterscheiden | abgeschlossen | Voraussetzungen und Pfade der elektronischen Gebrauchsanweisung |
| `SRC-009#Art.4` | Qualitäts- und Risikomanagement, Gebrauchstauglichkeit, Robustheit; für Abs. 2 zusätzlich Post-Market-Monitoring | Ergänzend, conditional | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware | — | abgeschlossen | systematisch zu prüfender Durchführungsartikel |
| `SRC-009#Art.5` | Qualitäts- und Risikomanagement, Transparenz, Gebrauchstauglichkeit, Robustheit | Ergänzend, conditional | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware | — | abgeschlossen | systematisch zu prüfender Durchführungsartikel |
| `SRC-009#Art.6` | Transparenz, Gebrauchstauglichkeit | Ergänzend, conditional | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware | — | abgeschlossen | systematisch zu prüfender Durchführungsartikel |
| `SRC-009#Art.7` | Transparenz, Robustheit, Gebrauchstauglichkeit | Ergänzend, conditional | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware | Datenschutzabhängigkeit in Abs. 2 Buchst. d (Abschnitt 10.23) | abgeschlossen | systematisch zu prüfender Durchführungsartikel |
| `SRC-009#Art.9` | Transparenz | Ergänzend, conditional | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware | — | abgeschlossen | systematisch zu prüfender Durchführungsartikel |

Die `expected_theme_clusters` sind nach Abschnitt 7 eine reine Ex-ante-Erwartung und keine Theme-Zuordnung künftiger `RR`. Die Freigabe zur systematischen Prüfung bedeutet nicht, dass jeder Artikel `RR` erzeugt.

**`SRC-009` — Kontext und keine Gap-Extraktion**

| Bereich | `expected_theme_clusters` | Einordnung | Behandlung |
| --- | --- | --- | --- |
| `SRC-009#Art.1` | — | Supporting Context | Kontext; keine systematische Gap-Extraktion |
| `SRC-009#Art.2` | — | Supporting Context | Kontext; keine systematische Gap-Extraktion |
| `SRC-009#Art.10` | — | Supporting Context | Kontext, insbesondere historische Korrelation zur aufgehobenen Verordnung (EU) Nr. 207/2012 |
| `SRC-009`, Anhang | — | Supporting Context | Kontext, insbesondere historische Korrelation zur aufgehobenen Verordnung (EU) Nr. 207/2012 |
| `SRC-009#Art.8` | — | im verbindlichen konsolidierten Rechtsstand gestrichen | keine Gap-Extraktion |
| `SRC-009#Art.11` | — | Inkrafttreten bzw. unmittelbare Geltung; kein Hersteller-Gap-Sollzustand | keine Gap-Extraktion |

### 9.10 `SRC-010` — IVDR, Primärrechtsanker der MDR/IVDR-Abgrenzung

Quellenebene A, Nutzungsart `unterstützend` (Abschnitt 4.2); freigegeben durch die Change Control in Abschnitt 10.34. Keine systematische IVDR-Gap-Extraktion, keine IVDR-`RR` und keine IVDR-Gap-Coverage.

| Quellenbereich | `expected_theme_clusters` | Rolle / Hinweis | Bearbeitungsstatus | Scope-Begründung |
| --- | --- | --- | --- | --- |
| `SRC-010#Art.2/Nr.2` | — | Rechtsverbindlicher Primärrechtsanker der Definition des In-vitro-Diagnostikums für die Boundary-`RUL` `RUL-006` bis `RUL-008` | abgeschlossen | Die MDR/IVDR-Abgrenzung aus `SRC-004` (Figure 2) setzt die IVD-Definition voraus; ohne Primärrechtsanker bliebe die Abgrenzung eine reine Guidance-Rechtsfolge. |

Weitere IVDR-Artikel sind nicht aktiviert. Eine Aktivierung wäre eine scope-wirksame Änderung nach Abschnitt 10.2.

---

## 10. Bearbeitungsstatus und Change Control

### 10.1 Bearbeitungsstatus des Coverage-Plans

| Wert | Definition |
| --- | --- |
| `geplant` | freigegeben, Prüfung nicht begonnen |
| `in Prüfung` | `0 / 1 / n`-Prüfung läuft |
| `abgeschlossen` | gesamter definierter Quellenbereich geprüft und Ergebnis dokumentiert |
| `ausgeschlossen` | nach Scope- oder Exclusion-Regel begründet aus dem aktiven Korpus entfernt |
| `blockiert` | vorgesehen, aber objektive Voraussetzung fehlt |

Diese Statuswerte gehören ausschließlich zum Coverage-Workflow. Sie verändern **nicht** das Artefaktstatus-Vokabular aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) für `RR`, `SR` und die übrigen Artefakttypen.

### 10.2 Change Control

Nach Version 1.0 gilt verbindlich: Kein neuer Quellenbereich darf ad hoc während der Extraktion aufgenommen, entfernt oder in seiner Priorität verändert werden.

Jede scope-wirksame Änderung benötigt **vor** der Bearbeitung:

1. eine fachliche Begründung,
2. einen Eintrag in der Änderungshistorie dieses Dokuments,
3. eine Impact-Prüfung auf bereits bearbeitete Bereiche,
4. eine Freigabe vor Extraktion des geänderten oder neuen Bereichs.

Wird während der Extraktion eine mögliche neue Fundstelle entdeckt, ist zuerst zu prüfen, ob sie bereits innerhalb eines freigegebenen Quellenbereichs liegt. Falls nein, ist die Coverage Change Control durchzuführen.

Rein redaktionelle Änderungen ohne Scope-Wirkung ändern den Coverage-Scope nicht.

### 10.3 Change Control Version 1.1 — `SRC-002` Art. 4a Abs. 1

**A. Fachliche Begründung**

- Art. 10 Abs. 1 und Abs. 6 beziehen Art. 4a Abs. 1 im aktuellen `SRC-002`-Rechtsstand ausdrücklich ein.
- Die Fundstelle enthält providerseitigen konditionalen Anforderungsgehalt.
- Ein vollständiges Ignorieren würde die aktuelle Art.-10-Systematik unvollständig abbilden.

**B. Scope-Entscheidung**

- Aufnahme als `Ergänzend, conditional`.
- Noch keine Extraktion.
- Vollständige `0 / 1 / n`-Prüfung vor jeder atomaren Clusterentscheidung.

**C. Impact-Prüfung**

| Betroffen | Ergebnis |
| --- | --- |
| Bestehende `RR-003` bis `RR-006` | kein materieller Impact: keine Textänderung, keine erneute Atomisierung; Art. 4a wird nicht als neuer `supplementary`-Lokator dieser `RR` benötigt |
| 16 neue Art.-10-Kandidaten | kein materieller Impact durch die Art.-4a-Coverage: keine Art.-4a-`supplementary`-Lokatoren, keine Textänderung allein wegen Art. 4a, kein Aktivierungsblocker |

Eine spätere rein lokatorbezogene Präzisierung des bisherigen `supplementary`-Eintrags `SRC-002#Art.10/Abs.2` auf Satz-Lokatoren ist eine separate Art.-10-Frage und **nicht** Teil dieses Coverage Changes.

**D. Freigabe**

Der Quellenbereich `SRC-002#Art.4a/Abs.1` ist mit Version 1.1 für eine spätere, triggerabhängige systematische Prüfung freigegeben. Damit ist **keine** Aussage verbunden, dass der Trigger im Demonstrator bereits erfüllt ist.


### 10.4 Statusabschluss `SRC-002` Art. 10

- Die vollständige systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_ART10.md](RR_EXTRACTION_ART10.md) Version 1.0 dokumentiert.
- 16 neue Anforderungen sind als `RR-030` bis `RR-045` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.5 aufgenommen.
- Die bestehenden `RR-003` bis `RR-006` sind materiell bestätigt; ihre `supplementary`-Lokatoren wurden rein locatorbezogen präzisiert.
- Innerhalb des definierten Art.-10-Quellenbereichs bestehen 0 unresolved und 0 deferred Kandidaten.
- Der Katalogvalidator ist erfolgreich (Katalogversion 0.5, 45 `RR`); die bestehenden 43 Tests sind erfolgreich.
- `SRC-002#Art.4a/Abs.1` bleibt separat als `Ergänzend, conditional` mit dem Bearbeitungsstatus `geplant` geführt.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-002#Art.10` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Diese Feststellung betrifft ausschließlich diesen Quellenbereich.


### 10.5 Statusabschluss `SRC-002` Art. 9

- Die vollständige systematische Extraktion des Quellenbereichs ist in [RR_EXTRACTION_ART9.md](RR_EXTRACTION_ART9.md) Version 1.2 dokumentiert.
- Geprüft wurden 25 Art.-9-interne Kandidaten; final bestehen 24 eigenständige `RR`-Kandidaten.
- Kandidat T ergibt nach der Cross-Source-Deduplizierung gegen den vollständigen Art.-13-Bestand 0 eigene `RR`; sein materieller Informationsgehalt ist über die Art.-13-`RR` erfasst, die Trainingskomponente über `RR-026`.
- Kandidat V ist nach Adjudikation der Sprachfassungsdivergenz als `RR-063` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.7 katalogisiert.
- Innerhalb des Quellenbereichs bestehen 0 zurückgestellte und 0 ungelöste Fälle.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-002#Art.9` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Diese Feststellung betrifft ausschließlich den hier definierten Coverage-Scope dieses Quellenbereichs und ist keine Aussage über den Artikel außerhalb dieses Scope.

### 10.6 Statusabschluss `SRC-002` Art. 13

- Die vollständige `0 / 1 / n`-Prüfung des Quellenbereichs ist in [RR_EXTRACTION_ART13.md](RR_EXTRACTION_ART13.md) Version 1.0 dokumentiert.
- `RR-001` und `RR-002` aus dem Pilot zu Abs. 1 sind materiell bestätigt und unverändert geblieben.
- 17 neue Anforderungen sind als `RR-046` bis `RR-062` in [RR_CATALOG.yaml](RR_CATALOG.yaml) katalogisiert.
- Innerhalb des Quellenbereichs bestehen 0 zurückgestellte und 0 ungelöste Fälle.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-002#Art.13` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.

Der Abschluss dieses Quellenbereichs schließt spätere Cross-Article-Deduplizierungen mit noch zu extrahierenden Artikeln **nicht** aus. Insbesondere bleibt der in [RR_EXTRACTION_ART13.md](RR_EXTRACTION_ART13.md) Abschnitt 8 festgehaltene Abgleich zwischen `SRC-002#Art.15/Abs.3` und `RR-050` bei der systematischen Art.-15-Extraktion zulässig und erforderlich; er steht dem Abschluss von Art. 13 selbst nicht entgegen.


### 10.7 Statusabschluss `SRC-002` Art. 14

- Die vollständige systematische `0 / 1 / n`-Prüfung des Quellenbereichs ist in [RR_EXTRACTION_ART14.md](RR_EXTRACTION_ART14.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- 10 materielle Kandidaten `A14-A` bis `A14-J` sind als `RR-064` bis `RR-073` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.8 katalogisiert.
- 9 Anforderungen sind regulär aktivierbar; `RR-073` ist wegen `SRC-002#Art.14/Abs.5` in Verbindung mit `SRC-002#Anh.III/Nr.1/Buchst.a` conditional und gilt nur für die dort bezeichneten biometrischen Fernidentifizierungssysteme. Der Katalogstatus dieses Eintrags bleibt `aktiv`; die Konditionalität steht im normativen Anforderungstext.
- Innerhalb des Quellenbereichs bestehen 0 ungelöste und 0 zurückgestellte Fälle.
- Der multilinguale Divergenzfall zu `A14-J` ist nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 adjudiziert.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-002#Art.14` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.

Der Abschluss dieses Quellenbereichs schließt die spätere Cross-Article-Prüfung gegen `SRC-002#Art.26` **nicht** aus; dieser Abgleich bleibt bei der systematischen Art.-26-Extraktion möglich und steht dem Abschluss von Art. 14 nicht entgegen. Über Art. 26 ist damit nichts entschieden.


### 10.8 Statusabschluss `SRC-002` Art. 15 Abs. 1, Abs. 3 und Abs. 4

- Die vollständige systematische `0 / 1 / n`-Prüfung der freigegebenen Bereiche `SRC-002#Art.15/Abs.1`, `SRC-002#Art.15/Abs.3` und `SRC-002#Art.15/Abs.4` ist in [RR_EXTRACTION_ART15.md](RR_EXTRACTION_ART15.md) Version 1.0 dokumentiert; 0 operative aktive Fundstellen blieben ohne Entscheidung.
- Sieben Gap-`RR`-Kandidaten `A15-A` bis `A15-G` sind als `RR-074` bis `RR-080` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.9 katalogisiert; fünf davon sind regulär, zwei conditional (`RR-079` und `RR-080`).
- Innerhalb der Bereiche bestehen 0 ungelöste und 0 zurückgestellte Fälle.
- `SRC-002#Art.15/Abs.4/UAbs.2` ergibt 0 `RR`, weil die dort genannten technischen Lösungen optional sind.
- Die Cybersecurity-Komponente aus `SRC-002#Art.15/Abs.1` wurde als eigenständiger atomarer Sollzustand erkannt, aber aufgrund des bestehenden Gap-Themen-Scope nicht als `RR` katalogisiert. Diese Scope-Entscheidung bedeutet **nicht**, dass die Cybersecurity-Pflicht rechtlich irrelevant wäre.
- `SRC-002#Art.15/Abs.3` wurde gegen `RR-050` geprüft: erheblicher partieller Overlap, aber kein identischer Erfüllungsstatus und daher keine vollständige Cross-Source-Deduplizierung. `A15-C` ist als `RR-076` eigenständig katalogisiert; `RR-050` blieb materiell unverändert, und `SRC-002#Art.15/Abs.3` wurde nicht als `supplementary`-Lokator zu `RR-050` ergänzt.
- Der multilinguale Feedback-Loop-Fall aus `SRC-002#Art.15/Abs.4/UAbs.3` ist nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 adjudiziert (0 unresolved). `A15-E` und `A15-G` wurden vor der Katalogintegration source-faithful nachadjudiziert; die Lebenszyklus-Zuordnungen wurden gegen [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) geprüft.

Nach der Statusdefinition aus Abschnitt 10.1 sind die drei freigegebenen Bereiche damit vollständig geprüft und das Ergebnis dokumentiert; ihr Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. `SRC-002#Art.15/Abs.2` und `SRC-002#Art.15/Abs.5` sind keine aktiven Gap-Coverage-Zeilen; ihre Einordnung in Abschnitt 9.5 bleibt unverändert.

Spätere Deduplizierungs- und Traceability-Prüfungen gegen noch nicht vollständig extrahierte Bereiche, insbesondere `SRC-002#Art.17` und `SRC-002#Art.72`, bleiben zulässig und erforderlich, sofern dort materieller Overlap entsteht. Sie stehen dem Abschluss dieser Art.-15-Bereiche nicht entgegen. Über Art. 17 und Art. 72 ist damit nichts entschieden.


### 10.9 Statusabschluss `SRC-002` Art. 17 Abs. 1 und Abs. 2

- Die vollständige systematische `0 / 1 / n`-Prüfung der freigegebenen Art.-17-Bereiche ist in [RR_EXTRACTION_ART17.md](RR_EXTRACTION_ART17.md) Version 1.0 dokumentiert; 0 operative aktive Fundstellen blieben ohne Entscheidung.
- 24 Kandidaten `A17-A` bis `A17-X` sind als `RR-081` bis `RR-104` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.10 katalogisiert; 23 davon sind regulär, einer ist conditional (`RR-093` / `A17-M`).
- Innerhalb der Bereiche bestehen 0 ungelöste und 0 zurückgestellte Fälle; 0 Kandidaten wurden Cross-Source-dedupliziert.
- `RR-093` bleibt fachlich conditional: Die Anforderung greift, wenn die einschlägigen harmonisierten Normen nicht vollständig angewandt werden oder nicht alle relevanten Anforderungen aus Abschnitt 2 abdecken. Der Katalogstatus bleibt `aktiv`; die Konditionalität steht im Anforderungstext.
- `SRC-002#Art.17/Abs.1/Buchst.f` ↔ Art. 10: keine vollständige Deduplizierung; `RR-094` bildet einen eigenständigen QMS-Data-Management-Status.
- `SRC-002#Art.17/Abs.1/Buchst.g` ↔ Art. 9: keine vollständige Deduplizierung; `RR-095` bildet einen eigenständigen QMS-Integrationsstatus.
- `SRC-002#Art.17/Abs.1/Buchst.h`: `RR-096` bis `RR-098` sind katalogisiert. Der spätere systematische Abgleich gegen `SRC-002#Art.72` bleibt zwingend vorbehalten; über Art. 72 ist damit nichts entschieden.
- `SRC-002#Art.17/Abs.1/Buchst.i` bleibt außerhalb der aktiven Gap-Coverage und ergibt keine `RR`; `SRC-002#Art.17/Abs.3` bleibt Interplay- und Integrationskontext ohne eigene `RR`; `SRC-002#Art.17/Abs.4` liegt außerhalb des aktuellen System- und Adressatenscope und ergibt keine `RR`. Die Einordnung in Abschnitt 9.5 bleibt unverändert; es erfolgt keine Scope-Erweiterung.

Nach der Statusdefinition aus Abschnitt 10.1 sind die sechs freigegebenen Art.-17-Bereiche damit vollständig geprüft und das Ergebnis dokumentiert; ihr Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Der vorbehaltene Art.-72-Abgleich steht dem Abschluss nicht entgegen.


### 10.10 Statusabschluss `SRC-002` Art. 72

- Die vollständige systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_ART72.md](RR_EXTRACTION_ART72.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- 11 finale Kandidaten `A72-A` bis `A72-K` sind als `RR-105` bis `RR-115` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.11 katalogisiert; 8 davon sind regulär, 3 conditional: `RR-111` wegen „Soweit dies relevant ist" bzw. „Where relevant", `RR-114` und `RR-115` wegen der gewählten Integrationsroute. Alle drei behalten den Katalogstatus `aktiv`; eine neue Statusart wird nicht eingeführt.
- Innerhalb des Quellenbereichs bestehen 0 ungelöste und 0 zurückgestellte Fälle; 0 Kandidaten wurden Cross-Source-dedupliziert.
- Art. 17 ↔ Art. 72: `RR-096`, `RR-097` und `RR-098` bleiben beibehalten und unverändert; es erfolgt keine vollständige Deduplizierung, und es werden keine zusätzlichen Art.-72-`supplementary`-Lokatoren ergänzt. `SRC-002#Art.17/Abs.1/Buchst.h` bildet die QMS-Integration des PMS ab, Art. 72 die materiellen PMS-Pflichten; Sollzustand und Erfüllungsstatus sind jeweils nicht identisch.
- `SRC-002#Art.72/Abs.2/Satz.3` ergibt 0 `RR`: Es handelt sich um eine Scope-Ausnahme für sensible operative Daten von Betreibern, die Strafverfolgungsbehörden sind. Die Stelle ist damit nicht regulatorisch irrelevant; ihre Relevanz für die spätere `RUL`- bzw. Applicability-Logik bleibt erhalten.
- `SRC-002#Art.72/Abs.3/Satz.3` ergibt 0 Anbieter-`RR`: Es handelt sich um eine institutionelle Pflicht der Kommission, nach dem projektverbindlichen Rechtsstand bis zum 2. September 2027 Leitlinien einschließlich einer Vorlage für den Plan zur Beobachtung nach dem Inverkehrbringen anzunehmen.
- `SRC-002#Art.72/Abs.4/UAbs.1`: Die Integrationswahl selbst ist eine optionale Route und ergibt als Interplay 0 `RR`. `RR-114` erfasst die Verwendung der Vorlage und `RR-115` das gleichwertige Schutzniveau, jeweils nur bei tatsächlich gewählter Integrationsroute. Die Route ist nicht verpflichtend, und die Vorlage ist nicht allgemein verpflichtend. Weil die Verordnung (EU) 2017/745 in Anhang I Abschnitt A aufgeführt ist, kann die Route für den Medizinproduktepfad relevant sein; MDR-Pflichten werden hier nicht extrahiert, und ein MDR-Crosswalk bleibt einem gesonderten Schritt vorbehalten.
- `SRC-002#Art.72/Abs.4/UAbs.2` liegt außerhalb Scope und ergibt keine `RR`.
- Für `SRC-002#Art.72/Abs.2/Satz.1` wurde eine Sprachfassungsabweichung adjudiziert (zusätzlich geprüft: FR, ES, PT); sie ist resolved, unresolved bleiben 0. Eine Methodenänderung war nicht erforderlich.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-002#Art.72` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.11 Statusabschluss `SRC-002` Art. 4a Abs. 1

- Die vollständige systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_ART4A.md](RR_EXTRACTION_ART4A.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 0 neue Gap-`RR`, 11 atomare regulatorische Pflichten außerhalb des Gap-Themen-Scope, 0 ungelöste und 0 zurückgestellte Fälle, 0 Cross-Source-Deduplizierungen.
- Das Ergebnis von 0 Gap-`RR` ist **kein** Coverage-Defizit: Der Quellenbereich wurde vollständig atomisiert und erst anschließend gegen den eingefrorenen Gap-Themen-Scope klassifiziert.
- Die 11 Atome sind regulatorisch relevant, liegen aber wegen ihres primären Datenschutz-, Privacy-, Security-, Zugriffs-, Speicherbegrenzungs- oder Verarbeitungsdokumentationsgegenstands außerhalb des definierten Gap-Themenkorpus. Grundlage ist das bestehende Exclusion Criterion E-5 in Abschnitt 3 in Verbindung mit [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 5; eine neue Exclusion Rule wird nicht eingeführt.
- Die optionale Verarbeitungserlaubnis ergibt 0 `RR` und bleibt Applicability-Kontext. Die strikte Erforderlichkeit und die angemessenen Schutzvorkehrungen sind jeweils eigenständige Out-of-Scope-Atome. Buchst. a ist out-of-scope und ergibt keine Data-Governance-`RR`; Buchst. b bis f sind gemäß Evidenz out-of-scope. Die Meta-Regel, dass alle Bedingungen a bis f erfüllt sein müssen, ergibt keine zusätzliche aggregierende `RR`.
- Art. 10: `RR-003` bis `RR-006` bleiben unverändert; 0 Cross-Source-Deduplizierungen, keine Katalogänderung. Art. 10 regelt die materiellen Pflichten zur Untersuchung möglicher Verzerrungen und zu den Maßnahmen dagegen; Art. 4a Abs. 1 regelt die besondere Zulässigkeit der Verarbeitung besonderer Kategorien personenbezogener Daten für diesen Zweck.
- Art. 4a Abs. 2 wurde nicht bearbeitet, nicht atomisiert und nicht aktiviert; über seine spätere Behandlung wird hier nichts ausgesagt.

Der ex-ante-Wert `Data Governance` in der Spalte `expected_theme_clusters` bleibt als historische Coverage-Erwartung nach Abschnitt 7 bestehen und wird nicht rückwirkend geändert. Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-002#Art.4a/Abs.1` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.12 Change Control Version 1.15 — Actor-Scope `SRC-002` Art. 26

Die Statusänderung entfernt drei Quellenbereiche aus dem aktiven Korpus. Sie wird deshalb nach Abschnitt 10.2 mit fachlicher Begründung, Impact-Prüfung und Freigabe dokumentiert. Eine Scope-Erweiterung erfolgt nicht.

**A. Fachliche Begründung**

- `SRC-002#Art.26/Abs.2`, `SRC-002#Art.26/Abs.4` und `SRC-002#Art.26/Abs.5` waren ex ante ausschließlich als `Ergänzend, conditional` mit dem Trigger „Deployer-Perspektive aktiviert" freigegeben.
- Nach Abschnitt 1.2 bleibt der Anbieter bzw. Provider Core-Adressat von `SRC-002`; Deployer- bzw. Betreiberpflichten werden nur aktiviert, wenn die System- bzw. Fallstudienabgrenzung diese Perspektive ausdrücklich umfasst.
- Der Trigger ist im aktuellen genehmigten Untersuchungs- und Fallstudien-Scope nicht aktiviert. [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) adressiert Hersteller KI-basierter Medizinproduktesoftware und die Anforderungen an einen definierten Produkttyp. Keine bestehende Scope-Entscheidung aktiviert eine eigenständige Deployer-Gap-Perspektive. Aus einem möglichen späteren Nutzungsszenario wird keine Deployer-Perspektive abgeleitet; nach Abschnitt 1.1 darf die Fallstudie die Core-Coverage nicht nachträglich erweitern.
- Damit greift Exclusion Criterion E-10 (Deployer- bzw. Betreiberpflicht außerhalb aktivierter Perspektive).

**B. Scope-Entscheidung**

- Keine systematische Gap-`RR`-Extraktion aus Art. 26; die drei Bereiche wurden **nicht** nach `0 / 1 / n` atomisiert.
- Status der drei Bereiche: `ausgeschlossen` im Sinne von Abschnitt 10.1, **nicht** `abgeschlossen`.
- Art. 26 ist regulatorisch relevant, liegt aber außerhalb des aktuell aktivierten Actor-Scope der Gap-Analyse.

**C. Impact-Prüfung**

| Betroffen | Ergebnis |
| --- | --- |
| Providerseitige `RR` aus Art. 13 (Transparenz- und Informationspflichten), Art. 14 (Bereitstellung von Human-Oversight-Fähigkeiten) und Art. 72 (PMS) | vollständig unverändert; dass Art. 26 spiegelbildliche oder ergänzende Deployer-Pflichten enthält, ändert den Provider-Katalog nicht |
| Deduplizierung gegen Art. 26 | nicht erforderlich, weil Art. 26 nicht aktiviert wird |
| In [RR_EXTRACTION_ART14.md](RR_EXTRACTION_ART14.md) und Abschnitt 10.7 vorgemerkte spätere Art.-26-Abgleiche (A14-E ↔ Art. 26 Abs. 5, A14-J ↔ Art. 26 Abs. 2) | entfallen mangels Aktivierung; die Evidenzdatei bleibt unverändert, und der Vorbehalt lebt bei einer späteren Aktivierung wieder auf |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | keine Änderung |

**D. Freigabe**

Die Entscheidung gilt für den eingefrorenen Gap-Katalog-Scope. Sollte aus zwingendem wissenschaftlichem Grund später eine echte Deployer-Perspektive Bestandteil der Fallstudie werden, bedarf ihre Aktivierung einer formellen Coverage Change Control **vor** jeder Art.-26-Extraktion. Eine automatische Reaktivierung erfolgt nicht.

### 10.13 Statusabschluss `SRC-001` Art. 10 — freigegebene Bereiche

- Die vollständige systematische `0 / 1 / n`-Prüfung von `SRC-001#Art.10/Abs.2` sowie der freigegebenen Teile von `SRC-001#Art.10/Abs.9` ist in [RR_EXTRACTION_MDR_ART10.md](RR_EXTRACTION_MDR_ART10.md) Version 1.1 dokumentiert; 0 operative aktive Fundstellen blieben ohne Entscheidung.
- Ergebnis: 27 finale Gap-`RR`, davon 5 regulär und 22 mit konditionaler Anwendbarkeit; 0 ungelöste und 0 zurückgestellte Fälle, 0 Cross-Regulation-Deduplizierungen und 0 Out-of-Scope-Atome im final adjudizierten aktiven Bereich.
- Katalogintegration: `RR-116` bis `RR-142` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.12. Die konditionale Anwendbarkeit ist jeweils im Requirement Text erhalten; es wurde kein neues Schemafeld eingeführt.

**Vollständig geprüfte Bereiche**

| Bereich | Geprüft |
| --- | --- |
| `SRC-001#Art.10/Abs.2` | vollständig |
| `SRC-001#Art.10/Abs.9` — Einleitung (`UAbs.1/Satz.1` bis `UAbs.1/Satz.3`, `UAbs.2/Satz.1`, `UAbs.2/Satz.2`, `UAbs.3`) | vollständig |
| `SRC-001#Art.10/Abs.9/Buchst.c`, `Buchst.d`, `Buchst.e`, `Buchst.g`, `Buchst.i`, `Buchst.l`, `Buchst.m` | vollständig |

Damit ist **nicht** behauptet, dass `SRC-001#Art.10/Abs.9` in allen Buchstaben extrahiert wurde. Die bestehende Ausschlussentscheidung für Buchst. a, b, f, h, j und k (Abschnitt 9.2) bleibt unverändert; diese Bereiche wurden durch den aktuellen Durchlauf nicht systematisch extrahiert und werden nicht nachträglich aktiviert.

**Wesentliche Nachadjudikation vor der Katalogintegration**

- Wirksamkeit und Proportionalität der QMS-Compliance-Funktion bilden eine gemeinsame `RR` (`RR-128`).
- `SRC-001#Art.10/Abs.9/Buchst.g` bildet eine gemeinsame `RR` zur Produktrealisierung (`RR-134`); der Produktionsbestandteil wird nicht separat herausgelöst.
- Die Pflicht zur zeitgerechten Berücksichtigung relevanter Änderungen (`RR-121`) ist dem Themencluster `Qualitäts- und Risikomanagement` zugeordnet.
- Für das Risikomanagementsystem aus Art. 10 Abs. 2 ist `SRC-001#Anh.I/Nr.3` notwendiger normativer Supplementary-Kontext.
- Die Art.-10-Abs.-9-Lokatoren wurden auf die tatsächliche Unterabsatzstruktur präzisiert.

**MDR-interner Folgeabgleich**

| Quellenbereich | Behandlung | Atomarer Abgleich insbesondere mit |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.3` | wird später eigenständig systematisch extrahiert | `RR-116`, `RR-117`, `RR-118`, `RR-119`, `RR-133` |
| `SRC-001#Art.83` | wird später eigenständig systematisch extrahiert | `RR-135`, `RR-136`, `RR-137` |

Beide Folgeabgleiche sind **kein** ungelöster Fall, **kein** zurückgestellter Fall und **kein** Blocker für den Abschluss von Art. 10.

**Cross-Regulation**

Die systematischen Abgleiche gegen den bestehenden AI-Act-Bestand ergaben 0 Cross-Regulation-Deduplizierungen. `RR-001` bis `RR-115` bleiben unverändert. Die getrennte regulatorische Herkunft von MDR- und AI-Act-Anforderungen bleibt erhalten.

Nach der Statusdefinition aus Abschnitt 10.1 sind die vier freigegebenen Bereiche damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb jeweils auf `abgeschlossen` gesetzt.


### 10.14 Statusabschluss `SRC-001` Anhang I Nr. 3

- Die vollständige systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_MDR_ANNEXI_3.md](RR_EXTRACTION_MDR_ANNEXI_3.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 11 neue Gap-`RR`, davon 10 regulär und 1 mit konditionaler Anwendbarkeit; 4 MDR-intern deduplizierte Atome, 0 ungelöste und 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-143` bis `RR-153` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.13.

**Satz 1 — vollständige MDR-interne Deduplizierung**

Die vier Top-Level-Sollzustände aus `SRC-001#Anh.I/Nr.3/Satz.1` erzeugen **keine** neuen `RR`.

| Sollzustand | Bestehende `RR` |
| --- | --- |
| Einführung des Risikomanagementsystems | `RR-116` |
| Dokumentation des Risikomanagementsystems | `RR-117` |
| Umsetzung des Risikomanagementsystems | `RR-118` |
| Fortschreibung des Risikomanagementsystems | `RR-119` |

Im Rahmen der Katalogintegration wurden die Supplementary-Lokatoren von `RR-116` bis `RR-119` ausschließlich von `SRC-001#Anh.I/Nr.3` auf `SRC-001#Anh.I/Nr.3/Satz.1` präzisiert. Eine materielle Änderung dieser vier `RR` erfolgte nicht.

**Neue materielle Pflichten**

| `RR` | Gegenstand |
| --- | --- |
| `RR-143` | kontinuierlicher iterativer Risikomanagementprozess über den Produktlebenszyklus |
| `RR-144` | regelmäßige systematische Aktualisierung |
| `RR-145` | Festlegung des Risikomanagementplans |
| `RR-146` | Dokumentation des Risikomanagementplans |
| `RR-147` | Gefährdungsidentifikation |
| `RR-148` | Gefährdungsanalyse |
| `RR-149` | Risikoeinschätzung |
| `RR-150` | Risikobewertung |
| `RR-151` | Beseitigung oder Kontrolle bewerteter Risiken |
| `RR-152` | Bewertung von Fertigungs- und Post-Market-Informationen auf das Risikobild |
| `RR-153` | erforderlichenfalls Anpassung der Kontrollmaßnahmen |

**Abgrenzung zu `RR-133`**

`RR-133` (Einbindung des Risikomanagements in das QMS) bleibt eigenständig; es erfolgt **keine** Deduplizierung gegen `RR-143` bis `RR-153`. `RR-133` ist eine QMS-Integrationspflicht, `RR-143` bis `RR-153` sind materielle Risikomanagementpflichten mit unterschiedlichen Erfüllungsstatus.

**Nicht extrahierte Bereiche**

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.4` | **nicht** systematisch extrahiert; ausschließlich als notwendiger Supplementary-Kontext bei `RR-151` und `RR-153` verwendet. Der Bereich bleibt `geplant`; über sein Ergebnis wird hier nichts ausgesagt. |
| `SRC-001#Art.83` | **nicht** systematisch extrahiert; der spätere Cross-Article-Abgleich mit `RR-152` bleibt vorgemerkt. |

Beide sind **kein** ungelöster Fall, **kein** zurückgestellter Fall und **kein** Blocker für den Abschluss von Nr. 3.

**Cross-Regulation und Sprachfassungen**

Die Beziehungen zu den AI-Act-Risikomanagement-`RR` `RR-007` bis `RR-029` wurden geprüft: 0 Cross-Regulation-Deduplizierungen, bestehende AI-Act-`RR` unverändert. DE und EN wurden vollständig geprüft, FR und IT ergänzend; 0 materielle Divergenzen und 0 ungelöste Fälle. Die sprachlichen Varianten bei `implement` und `maintain` sowie die italienische Formulierung zur Aktualisierung wurden ohne Mehrheitsregel und ohne Sprachpriorität adjudiziert.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.3` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.15 Statusabschluss `SRC-001` Anhang I Nr. 4

- Die vollständige systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_MDR_ANNEXI_4.md](RR_EXTRACTION_MDR_ANNEXI_4.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 9 neue Gap-`RR`, davon 7 regulär und 2 mit konditionaler Anwendbarkeit; 0 MDR-interne Deduplizierungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-154` bis `RR-162` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.14.

**Abgedeckte Struktur**

| Fundstelle | Ergebnis | `RR` |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.4/Satz.1` | 1 `RR` | `RR-154` |
| `SRC-001#Anh.I/Nr.4/Satz.2` | 2 `RR` | `RR-155`, `RR-156` |
| `SRC-001#Anh.I/Nr.4/Satz.3` — Prioritätshierarchie | 1 `RR` | `RR-157` |
| `SRC-001#Anh.I/Nr.4/Buchst.a` | 1 `RR` | `RR-158` |
| `SRC-001#Anh.I/Nr.4/Buchst.b` | 1 conditional `RR` | `RR-159` |
| `SRC-001#Anh.I/Nr.4/Buchst.c` | 2 `RR` | `RR-160`, `RR-161` |
| `SRC-001#Anh.I/Nr.4/Satz.4` | 1 `RR` | `RR-162` |

**Wesentliche Adjudikation**

- Sicherheitsgrundsätze und allgemein anerkannter Stand der Technik bilden gemeinsam `RR-154`.
- Gefahrenspezifisches Restrisiko und Gesamtrestrisiko bleiben getrennte Sollzustände.
- Die gesetzliche Prioritätshierarchie ist ein eigenständiger Sollzustand.
- Buchst. a bleibt eine gemeinsame Risikoreduktionspflicht.
- Alarmvorrichtungen sind keine eigene `RR`.
- Sicherheitsinformation und Anwenderschulung bleiben getrennt.
- Die Restrisikoinformation nach Satz 4 bleibt eigenständig gegenüber der Sicherheitsinformation nach Buchst. c.

**Abgrenzung zu `RR-151` und `RR-153`**

Es erfolgte **keine** Deduplizierung. `RR-151` und `RR-153` bilden die übergeordneten Risikokontroll- bzw. Anpassungspflichten aus Anhang I Nr. 3 ab; `RR-154` bis `RR-162` enthalten die konkreten materiellen Sollzustände aus Nr. 4. Die Erfüllungsstatus sind unabhängig.

**Anhang I Nr. 2**

`SRC-001#Anh.I/Nr.2` wurde **nicht** systematisch extrahiert und **nicht** aktiviert. Der Bereich wurde ausschließlich als notwendiger normativer Supplementary-Kontext für `RR-158` verwendet; aus ihm entsteht keine eigene `RR`.

**Cross-Regulation**

Sachliche Beziehungen bestehen insbesondere `RR-155` ↔ `RR-022`, `RR-156` ↔ `RR-023`, `RR-158` ↔ `RR-024`, `RR-159` ↔ `RR-025` und `RR-161` ↔ `RR-026`. Cross-Regulation-Deduplizierungen: 0; die bestehenden AI-Act-`RR` bleiben unverändert.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.4` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.16 Statusabschluss `SRC-001` Anhang I Nr. 5

- Die vollständige systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_MDR_ANNEXI_5.md](RR_EXTRACTION_MDR_ANNEXI_5.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 2 neue Gap-`RR`, beide regulär und 0 conditional; 0 MDR-interne Deduplizierungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-163` und `RR-164` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.15.

**Abgedeckte Struktur**

| Fundstelle | Ergebnis | `RR` |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.5` — gemeinsamer Einleitungsrahmen | 0 eigene `RR` | notwendiger Kontext für Buchst. a und b |
| `SRC-001#Anh.I/Nr.5/Buchst.a` | 1 `RR` | `RR-163` |
| `SRC-001#Anh.I/Nr.5/Buchst.b` | 1 `RR` | `RR-164` |

Eine aggregierende zusätzliche `RR` für den Einleitungsrahmen wurde **nicht** gebildet.

**`RR-163`**

Die Verringerung anwendungsfehlerbedingter Risiken aus ergonomischen Merkmalen und aus der vorgesehenen Nutzungsumgebung bildet einen gemeinsamen Sollzustand; Themencluster `Gebrauchstauglichkeit`. `SRC-001#Anh.I/Nr.2` dient ausschließlich als notwendiger Supplementary-Kontext zur Bedeutung der weitestmöglichen Risikoverringerung und wurde **nicht** systematisch extrahiert. Gegenüber `RR-158` erfolgt **keine** Deduplizierung.

**`RR-164`**

Technische Kenntnisse, Erfahrung, Aus- und Weiterbildung, gegebenenfalls die Anwendungsumgebung sowie die gesundheitliche und körperliche Verfassung der vorgesehenen Anwender bilden ein gemeinsam zu berücksichtigendes Nutzerprofil; Themencluster `Gebrauchstauglichkeit`. Eine Mikroatomisierung der einzelnen Nutzerfaktoren erfolgt **nicht**; die Gesamt-`RR` ist **nicht** conditional.

**Multilingualer Divergenzfall zu Buchst. b**

Für die Position der Modalitätsklausel wurde eine materielle Sprachfassungsabweichung festgestellt. Geprüft wurden DE, EN, FR, ES und IT; der Fall ist `resolved`, 0 ungelöste Fälle. Adjudizierte Bedeutung: „gegebenenfalls" bzw. `where applicable` qualifiziert die Anwendungsumgebung. Die italienische Abweichung bleibt in der Evidenz dokumentiert. Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung priorisiert. Im Katalog entsteht keine Unsicherheit; `RR-164` trägt `uncertainty: null`.

**MDR-interner Abgleich**

`RR-158` betrifft die allgemeine sichere Auslegung zur Risikominimierung, `RR-163` die spezifische anwendungsfehler- und ergonomiebezogene Risikoreduktion. Die prüfbaren Sollzustände sind unterschiedlich. Für `RR-164` besteht keine bestehende statusidentische MDR-`RR`.

**Nicht extrahierte Bereiche**

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` | nicht systematisch extrahiert; späterer Abgleich mit `RR-163` und `RR-164` bleibt vorgemerkt, sofern die conditional Laienanwendung aktiviert wird |
| `SRC-001#Anh.I/Nr.23.1` | nicht systematisch extrahiert; späterer Abgleich insbesondere mit `RR-164` bleibt vorgemerkt |
| `SRC-008` — IEC 62366-1 | nicht extrahiert; es wurden keine Norminhalte in `RR-163` oder `RR-164` übernommen. Der Norm-Crosswalk bleibt ein eigener späterer Arbeitsschritt |

Keiner dieser Punkte ist ein zurückgestellter Fall oder ein Blocker für den Abschluss von Nr. 5.

**Cross-Regulation**

`RR-164` besitzt eine sachliche Beziehung zu `RR-063` (Berücksichtigung von Betreibermerkmalen und Nutzungskontext). Eine Cross-Regulation-Deduplizierung erfolgt **nicht**; `RR-063` bleibt unverändert. Cross-Regulation-Deduplizierungen insgesamt: 0.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.5` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.17 Statusabschluss `SRC-001` Anhang I Nr. 17.1

- Die vollständige systematische `0 / 1 / n`-Prüfung und die gezielte Nachadjudikation sind in [RR_EXTRACTION_MDR_ANNEXI_17_1.md](RR_EXTRACTION_MDR_ANNEXI_17_1.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 4 neue Gap-`RR`, alle regulär und 0 conditional; 0 MDR-interne Deduplizierungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-165` bis `RR-168` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.16.

**Abgedeckte Struktur**

| Fundstelle bzw. Aussage | Ergebnis | `RR` |
| --- | --- | --- |
| Produktkategorien (Applicability-Kontext) | 0 eigene `RR` | — |
| `SRC-001#Anh.I/Nr.17.1/Satz.1` — Wiederholbarkeit | 1 `RR` | `RR-165` |
| `SRC-001#Anh.I/Nr.17.1/Satz.1` — Zuverlässigkeit | 1 `RR` | `RR-166` |
| `SRC-001#Anh.I/Nr.17.1/Satz.1` — Leistung entsprechend der Zweckbestimmung | 1 `RR` | `RR-167` |
| `SRC-001#Anh.I/Nr.17.1/Satz.2` — Folgen eines Single-Fault-Zustands | 1 `RR` | `RR-168` |
| **Gesamt** | **4** | |

**Satz 1**

`RR-165` bis `RR-167` tragen jeweils das Themencluster `Robustheit` und sind regulär. Der gemeinsame Designrahmen aus Satz 1 erzeugt **keine** zusätzliche Meta-`RR`; die Produktkategorien sind Applicability-Kontext und erzeugen **keine** eigene `RR`. `RR-167` wird **nicht** auf eine vollständige klinische Leistungsbewertung ausgeweitet.

**Satz 2 — `RR-168`**

`RR-168` (Beherrschung von Folgen eines Single-Fault-Zustands) ist regulär, Themencluster `Robustheit`. Die wesentliche Struktur umfasst geeignete Vorkehrungen, den Single-Fault-Zustand, die resultierenden Risiken **oder** Leistungsbeeinträchtigungen sowie deren Ausschluss oder möglichst weitgehende Verringerung. Die Oder-Struktur bleibt innerhalb **einer** `RR` erhalten; es gibt **keine** getrennte `RR` für Risiken und **keine** getrennte `RR` für Leistungsbeeinträchtigungen.

**Conditional-Adjudikation**

Der Single-Fault-Zustand ist **keine** conditional Applicability-Bedingung, sondern eine spezifizierte Fehler- bzw. Betriebsbedingung einer bereits bei der Produktauslegung zu erfüllenden Robustheitsanforderung. `RR-168` ist deshalb regulär; conditional `RR` aus Nr. 17.1: 0.

**Verworfene Variante `M17_1-E`**

Im ersten Atomisierungsschritt wurde eine separate `RR` zur Leistungsbeeinträchtigung unter der temporären Kennung `M17_1-E` geprüft und vor permanenter Katalogisierung verworfen. Eine Aufteilung hätte die quellenmäßige Alternativstruktur „Risiken **oder** Leistungsbeeinträchtigungen" in zwei faktisch kumulative Gap-Status transformiert; nach [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 bleibt sie innerhalb `RR-168` erhalten. `M17_1-E` ist kein finaler Kandidat, erhält keine permanente Identifikation und keinen Katalogeintrag; ein `RR-169` existiert nicht.

**Anhang I Nr. 2**

`SRC-001#Anh.I/Nr.2` wurde **nicht** systematisch extrahiert und für `RR-168` **nicht** als Supplementary-Locator verwendet. Nr. 2 definiert die möglichst weitgehende Risikoreduktion, während `RR-168` eine gemeinsame Oder-Struktur aus Risiken oder Leistungsbeeinträchtigungen enthält. Nr. 2 bleibt deshalb dokumentierter Auslegungskontext des Risiko-Zweigs.

**MDR-interne Deduplizierung**

Gegenüber `RR-151`, `RR-153`, `RR-158` und `RR-159` erfolgt jeweils **keine** Deduplizierung. `RR-168` enthält einen spezifischen Single-Fault-Sollzustand für programmierbare Medizinprodukte bzw. Software, während die bestehenden Anforderungen aus Anhang I Nr. 3 und Nr. 4 allgemeinere Risikomanagement- bzw. Risikokontrollpflichten abbilden. Für `RR-165` bis `RR-167` besteht keine bestehende statusidentische MDR-`RR`. MDR-interne Deduplizierungen insgesamt: 0.

**Cross-Regulation**

Fachliche Traceability-Beziehungen: `RR-165` ↔ `RR-075`; `RR-166` ↔ `RR-075` sowie mittelbar `RR-077`; `RR-167` ↔ `RR-074` und `RR-075`; `RR-168` ↔ `RR-077` und `RR-078`. Cross-Regulation-Deduplizierungen: 0; die bestehenden AI-Act-`RR` bleiben unverändert.

**Sprachfassungen**

Eine materiell auffällige Sprachstelle wurde festgestellt: die deutsche Formulierung zum Erstauftreten eines Defekts gegenüber `single fault condition`. Ergänzend geprüft wurden FR, IT und ES; der Fall ist `resolved`, 0 ungelöste Fälle. Adjudizierte Bedeutung ist der Single-Fault-Zustand; der deutsche Requirement Text behält die authentische Formulierung. Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung priorisiert.

**Nicht extrahierte Bereiche**

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.2` | bleibt `geplant`; weder aktiviert noch extrahiert. Der spätere Abgleich mit `RR-165` bis `RR-168` ist vorgemerkt und ist kein zurückgestellter Fall für Nr. 17.1 |
| `SRC-001#Anh.I/Nr.17.4` | nicht extrahiert; der Cybersecurity-Scope wurde nicht erweitert |
| `SRC-007` — IEC 62304 | nicht extrahiert; keine Norminhalte importiert |

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.17.1` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.18 Statusabschluss `SRC-001` Anhang I Nr. 17.2

- Die vollständige systematische `0 / 1 / n`-Prüfung sowie die Lifecycle- und Multilingual-Nachadjudikation sind in [RR_EXTRACTION_MDR_ANNEXI_17_2.md](RR_EXTRACTION_MDR_ANNEXI_17_2.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 5 neue Gap-`RR`, alle regulär und 0 conditional; 0 MDR-interne Deduplizierungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-169` bis `RR-173` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.17.

**Finale Atomisierung**

| Aussage | Ergebnis | `RR` |
| --- | --- | --- |
| Applicability | 0 eigene `RR` | — |
| entwickelt und hergestellt | 0 eigene `RR` | gemeinsamer Handlungsrahmen |
| Stand der Technik | 1 `RR` | `RR-169` |
| Software-Lebenszyklus | 1 `RR` | `RR-170` |
| Risikomanagement einschließlich Informationssicherheit | 1 `RR` | `RR-171` |
| Verifizierung | 1 `RR` | `RR-172` |
| Validierung | 1 `RR` | `RR-173` |
| **Gesamt** | **5** | |

**`RR-169`**

Softwareentwicklung und -herstellung entsprechend dem Stand der Technik; Themencluster `Software-Lebenszyklus`, Lebenszyklusphasen `Entwicklung und Realisierung` sowie `Änderung und Wartung`. Gegenüber `RR-154` erfolgt **keine** Deduplizierung. Der Stand der Technik wurde mit **keiner** bestimmten Norm gleichgesetzt.

**`RR-170`**

Berücksichtigung der Grundsätze des Software-Lebenszyklus; Themencluster `Software-Lebenszyklus`, Lebenszyklusphasen `Entwicklung und Realisierung` sowie `Änderung und Wartung`. Der multilinguale Divergenzfall zwischen dem amtlichen deutschen Ausdruck und `development life cycle` wurde unter ergänzender Prüfung von FR, IT und ES adjudiziert; Status `resolved`, 0 ungelöste Fälle. Der deutsche Requirement Text behält den amtlichen Begriff; die adjudizierte engere Bedeutung im Entwicklungs- und Herstellungskontext bleibt in der Evidenz dokumentiert. Eine allgemeine Betriebs- oder Post-Market-Pflicht wird daraus **nicht** abgeleitet. Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung priorisiert.

**`RR-171`**

Berücksichtigung von Risikomanagementgrundsätzen einschließlich Informationssicherheit; Themencluster `Qualitäts- und Risikomanagement`, Lebenszyklusphasen `Entwicklung und Realisierung` sowie `Änderung und Wartung`. Die Informationssicherheit bleibt Bestandteil derselben `RR`. Es entsteht **keine** separate Security-`RR`, **kein** neuer Cybersecurity-Cluster; der Cluster `Robustheit` wurde nicht erweitert und Inhalte aus Nr. 17.4 wurden nicht importiert.

**`RR-172` und `RR-173`**

Verifizierungs- und Validierungsgrundsätze; beide mit Themencluster `Software-Lebenszyklus` und den Lebenszyklusphasen `Entwicklung und Realisierung` sowie `Änderung und Wartung`. Die Phase `Verifikation und Validierung` wird ausdrücklich **nicht** zugeordnet: Verifizierung bzw. Validierung ist jeweils der normative Gegenstand, während die Erfüllungsphase durch den gesetzlichen Rahmen der Entwicklung und Herstellung der Software bestimmt wird. Beide bleiben getrennte `RR`, weil sie unabhängig statusfähig und regulatorisch vollständig sind.

**Lifecycle-Gesamtaudit**

Alle `RR` von `RR-169` bis `RR-173` tragen ausschließlich `Entwicklung und Realisierung` sowie `Änderung und Wartung`. Insbesondere wurden `Planung und Konzeption`, `Verifikation und Validierung`, `Konformitätsbewertung`, `Inverkehrbringen, Inbetriebnahme und Betrieb` sowie `Post-Market-Überwachung` **nicht** zugeordnet. `Änderung und Wartung` bedeutet hier ausschließlich, dass der jeweilige Sollzustand erneut zu erfüllen ist, wenn eine Änderung, Korrektur oder Aktualisierung erneute Softwareentwicklung oder -herstellung auslöst; eine allgemeine Post-Market-Pflicht entsteht daraus nicht.

**MDR-interne Deduplizierung**

Gegenüber `RR-116` bis `RR-119`, `RR-133`, `RR-134`, `RR-143`, `RR-144`, `RR-154` sowie `RR-165` bis `RR-168` erfolgt jeweils **keine** vollständige Deduplizierung. Nr. 17.2 enthält spezifische materielle Anforderungen an die Softwareentwicklung und -herstellung, während die bestehenden QMS-, Risikomanagement- und Nr.-17.1-`RR` abweichende normative Gegenstände bzw. unabhängige Erfüllungsstatus besitzen. MDR-interne Deduplizierungen: 0.

**Cross-Regulation**

Fachliche Traceability-Beziehungen: `RR-169` zu den Entwicklungsanforderungen des AI Act; `RR-170` zu dessen Entwicklungs- und Lifecycle-Bezügen; `RR-171` zu den Risikomanagement-`RR` aus Art. 9; `RR-172` insbesondere zu `RR-087` und `RR-091`; `RR-173` insbesondere zu `RR-091`; ergänzend `RR-085`, `RR-086` und `RR-088`, soweit in der Evidenz dokumentiert. Cross-Regulation-Deduplizierungen: 0; die bestehenden AI-Act-`RR` bleiben unverändert.

**Verworfene Split-Varianten**

Geprüft und verworfen wurden: Entwicklung und Herstellung als zwei `RR`; Informationssicherheit als separate `RR`; Verifizierung und Validierung als gemeinsame `RR`; alle vier Prinzipienbereiche als eine aggregierte `RR`; ein synthetischer deutscher Begriff im finalen Requirement Text. Keine dieser Varianten erhält eine permanente Identifikation.

**Nicht extrahierte Bereiche**

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.4` | nicht systematisch extrahiert |
| `SRC-006` — ISO 14971 | nicht systematisch extrahiert |
| `SRC-007` — IEC 62304 | nicht systematisch extrahiert |

Externe Norminhalte wurden **nicht** importiert, und der Stand der Technik wurde **nicht** mit einer einzelnen Norm gleichgesetzt.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.17.2` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.


### 10.19 Change Control Version 1.29 — Governance der Quellenaufnahme und Nutzungsart

Die Änderung präzisiert ausschließlich die Governance für die spätere Aufnahme weiterer Quellen. Sie nimmt **keine** neue Quelle auf, vergibt keine `SRC`-ID, gibt keinen neuen Quellenbereich frei und extrahiert keine Anforderung.

**A. Anlass**

- Eine Recherche zur Normenlandschaft für KI-basierte Medizinproduktesoftware hat weitere horizontal relevante Normen und Standardisierungspublikationen identifiziert, die über `SRC-005` bis `SRC-008` hinausgehen.
- Die bisherige Aufnahmeregel in [SOURCES.md](SOURCES.md) Version 1.1 beschränkte das Register ausschließlich auf die Kernquellen aus [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 7. Abschnitt 4 dieses Plans kannte nur die Ebenen A, B und C mit fest zugeordneten Quellen, aber keine Unterscheidung nach Nutzungsart und keinen Ort für unveröffentlichte Normungsprojekte.
- Die Recherche selbst ist nicht Bestandteil dieses Change; sie wird später als dokumentierter Landscape-Audit abgelegt.

**B. Wissenschaftliche Begründung**

- [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) definiert den wissenschaftlichen Mindestumfang, nicht die maximale technische Qualität, und bezeichnet die Kernquellen in Abschnitt 7 ausdrücklich als vorläufig. Die dort benannten Normen sind der initiale Bestand, keine abschließende Positivliste.
- Ohne kontrollierte Aufnahmeregel entstünde entweder eine unvollständige Quellenbasis für den Untersuchungsgegenstand oder eine selektive, nicht reproduzierbare Ad-hoc-Erweiterung. Beides widerspräche Abschnitt 1.1 und den Bewertungskriterien Vollständigkeit und Nachvollziehbarkeit aus [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 3.
- Die Trennung von Quellenebene (normative Qualität) und Nutzungsart (methodische Verwendung) verhindert, dass ein Dokumenttyp wie TS, TR oder PAS automatisch als Requirement-Quelle behandelt wird.
- Die Begrenzung auf horizontale Quellen mit Triggerprinzip für produktspezifische Quellen hält den Korpus endlich und an den Untersuchungsgegenstand gebunden.
- Der wissenschaftliche Untersuchungsgegenstand, die acht Themencluster und die sieben Lebenszyklusphasen bleiben unverändert. Das Exposé-Thema wird nicht geändert.

**C. Scope-Entscheidung**

- Neue Abschnitte 4.1 bis 4.6: Ebenendefinition A/B/C (Ebenen unverändert erhalten), orthogonale Nutzungsart `systematisch` / `unterstützend` / `triggerbasiert`, Aufnahmevoraussetzungen, Scope-Regel für horizontale Quellen, Triggerprinzip, Volltext- und Source-Fidelity-Regel, Trennung von fachlicher Relevanz und MDR-Harmonisierungsstatus sowie Ausschluss unveröffentlichter Normungsprojekte.
- [SOURCES.md](SOURCES.md) Version 1.2 übernimmt die präzisierte Aufnahmeregel und verweist für Voraussetzungen, Ebenen und Nutzungsarten auf diesen Plan.
- Kein neuer Quellenbereich, keine neue Coverage-Zeile, keine Prioritätsänderung, keine Statusänderung.

**D. Impact-Prüfung**

| Betroffen | Ergebnis |
| --- | --- |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.17 (`RR-001` bis `RR-173`) | unverändert; keine rückwirkende Änderung bestehender `RR` |
| `SRC-001` bis `SRC-008` | inhaltlich unverändert; keine neue `SRC`-ID |
| Source-to-Theme-Matrix (Abschnitt 8) und Normenübersicht (Abschnitt 9.8) | unverändert, bis konkrete neue Quellen einzeln per Change Control freigegeben werden |
| Bearbeitungsstatus aller Quellenbereiche in Abschnitt 9 | unverändert; insbesondere bleibt `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` `in Prüfung` mit Priorität `Ergänzend, conditional`, erwartetem Themencluster `Gebrauchstauglichkeit` und Trigger „vorgesehene Laienanwendung“ |
| Extraktionsnachweise `RR_EXTRACTION_*.md` | unverändert |
| [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md), [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md), [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md), [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | unverändert; keine Änderung erforderlich |
| Stopping Rule (Abschnitt 11) | unverändert; neu aufgenommene Quellen werden erst mit ihrer eigenen Freigabe Teil der Stopping Rule |

**E. Freigabe**

Freigegeben ist ausschließlich die Governance-Präzisierung. Jede konkrete neue Quelle benötigt vor ihrer Registrierung eine eigene Change Control nach Abschnitt 10.2 mit Festlegung von Quellenebene, Nutzungsart und gegebenenfalls Trigger sowie die Primärquellenverifikation nach Abschnitt 4.3.


### 10.20 Statusabschluss `SRC-001` Anhang I Nr. 22.1 bis Nr. 22.3

- Die vollständige systematische `0 / 1 / n`-Prüfung des ergänzenden, conditional Quellenbereichs ist in [RR_EXTRACTION_MDR_ANNEXI_22_1_22_3.md](RR_EXTRACTION_MDR_ANNEXI_22_1_22_3.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 10 normative Kandidatenatome geprüft; 9 neue Gap-`RR`; 1 Out-of-Scope-Atom; 0 vollständige MDR-interne Deduplizierungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-174` bis `RR-182` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.18.

**Abgedeckte Struktur**

| Fundstelle | Ergebnis | `RR` |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.22.1` | 3 `RR` | `RR-174`, `RR-175`, `RR-176` |
| `SRC-001#Anh.I/Nr.22.2` | 4 `RR`, 1 Out-of-Scope-Atom | `RR-177`, `RR-178`, `RR-179`, `RR-180` |
| `SRC-001#Anh.I/Nr.22.3` | 2 `RR` | `RR-181`, `RR-182` |
| **Gesamt** | **9 `RR`** | |

**Conditionality**

- Alle 9 `RR` stehen unter dem äußeren Anwendbarkeitsvorbehalt dieses Quellenbereichs, dem unveränderten Coverage-Trigger „vorgesehene Laienanwendung" (Abschnitt 9.1).
- 3 `RR` sind zusätzlich inner conditional: `RR-180` (Interpretation von Ergebnissen einschlägig), `RR-181` („soweit angemessen") und `RR-182` („soweit angemessen" und „gegebenenfalls"). Die innere Bedingung steht jeweils im Requirement Text.
- Es wurde kein neues Katalogfeld eingeführt; die vollständige Trennung von äußerer Bedingung, innerer Bedingung und Modalität ist in der Evidenz dokumentiert.

**Theme und Lebenszyklus**

Alle 9 `RR` tragen das Themencluster `Gebrauchstauglichkeit`. Die Lebenszyklusphasen stammen ausschließlich aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 3 und sind in der Evidenz je Anforderung dokumentiert.

**Out-of-Scope-Atom**

Der Spiegelstrich in `SRC-001#Anh.I/Nr.22.2` zu unbeabsichtigtem Schneiden, Stechen bzw. Nadelstichverletzungen ergibt 0 `RR`. Er besitzt für den horizontalen Untersuchungsgegenstand KI-basierter Medizinproduktesoftware keinen systematischen Beitrag, weil es sich um einen physischen bzw. hardwarebezogenen Verletzungsmechanismus handelt. Dies ist **keine** Aussage, dass die Pflicht für jedes Produkt mit Software rechtlich irrelevant wäre; bei einem hardwarebezogenen Produkt, z. B. einem softwaregesteuerten Injektionssystem, kann sie anwendbar sein.

**Abgleich mit `RR-163` und `RR-164`**

Der in Abschnitt 10.16 vorgemerkte Abgleich ist abgeschlossen: `RR-174` sowie `RR-177` bis `RR-180` stehen in partiellem Overlap zu `RR-163` und `RR-164`, `RR-175`, `RR-176`, `RR-181` und `RR-182` sind davon unterschieden. Vollständige Deduplizierungen: 0. `RR-163` und `RR-164` bleiben unverändert.

**Sprachfassungen**

Die Sprachfassungsdivergenz „fehlerfrei" / `accurately` / `correctement` in Nr. 22.2 ist adjudiziert und in der Evidenz dokumentiert; `RR-178` verwendet in jeder Sprachfassung den authentischen Ausdruck. 0 ungelöste Fälle.

**Nicht extrahierte Bereiche**

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.23.1` | bleibt separat `geplant`; der in Abschnitt 10.16 vorgemerkte Abgleich mit `RR-164` bleibt bestehen |
| `SRC-008` — IEC 62366-1 | nicht extrahiert; keine Norminhalte vorweggenommen |
| Kandidaten des [Standards-Landscape-Audits](../01-research/MEDICAL_DEVICE_STANDARDS_LANDSCAPE_AUDIT.md) | nicht registriert und nicht verwendet |

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Priorität, erwartetes Themencluster und Trigger bleiben unverändert.


### 10.21 Aktivierung `SRC-001` Anhang I Nr. 23.1

- Die systematische `0 / 1 / n`-Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.23.1` wird gestartet; der Bearbeitungsstatus wird von `geplant` auf `in Prüfung` gesetzt.
- Priorität `Kern`, `expected_theme_clusters` `Transparenz, Gebrauchstauglichkeit`, Trigger `—` und der Hinweis „**Nicht** ex ante ausschließlich Transparenz zuordnen" bleiben unverändert. Die Cluster sind weiterhin eine reine Ex-ante-Erwartung nach Abschnitt 7 und keine Theme-Zuordnung künftiger `RR`.
- Der in Abschnitt 10.16 vorgemerkte und in Abschnitt 10.20 bestätigte spätere Abgleich insbesondere mit `RR-164` bleibt unverändert bestehen. Nach [RR_EXTRACTION_MDR_ANNEXI_5.md](RR_EXTRACTION_MDR_ANNEXI_5.md) Abschnitt 8 betrifft er die Anforderungen an die Informationsgestaltung unter Berücksichtigung von Nutzerkenntnissen, Erfahrung und Ausbildung. Eine Deduplizierungsentscheidung wird hier nicht getroffen; `RR-164` bleibt unverändert.
- Es erfolgt noch keine Extraktions-, Atomizitäts-, Theme-, Lifecycle-, Conditionality-, Deduplizierungs- oder Locator-Entscheidung und keine Aussage über die Anzahl künftiger `RR`. Es wird noch keine Evidenzdatei angelegt.
- Keine Änderung des Coverage-Scope und keine weitere Aktivierung: `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` bleibt `abgeschlossen`; `SRC-001#Anh.I/Nr.23.4`, `SRC-001#Art.83` ff. und die Normen-Coverage bleiben unverändert. Es wurden keine Norminhalte vorgezogen.


### 10.22 Statusabschluss `SRC-001` Anhang I Nr. 23.1

- Die vollständige systematische `0 / 1 / n`-Prüfung ist mit den vollständigen Research-Begründungen einschließlich der Nachadjudikation zu Triggerlogik, Empfängerkreis, negativer Ausnahme und externer Abhängigkeit in [RR_EXTRACTION_MDR_ANNEXI_23_1.md](RR_EXTRACTION_MDR_ANNEXI_23_1.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 27 potenzielle Einheiten geprüft; 22 neue Gap-`RR`, davon 13 regulär und 9 conditional; 5 0-`RR`-Entscheidungen; 0 Out-of-Scope-Atome; 0 vollständige MDR-interne Deduplizierungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Cross-Regulation-Deduplizierungen.
- Katalogintegration: `RR-183` bis `RR-204` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.19.

**Abgedeckte Struktur**

| Fundstelle | Ergebnis | `RR` |
| --- | --- | --- |
| Chapeau, Satz 1 | 4 `RR` | `RR-183` bis `RR-186` |
| Chapeau, Satz 2 | 2 conditional `RR`, 1 0-`RR` (Informationsorte als Permission) | `RR-187`, `RR-188` |
| Buchst. a | 7 `RR`, davon 1 conditional | `RR-189` bis `RR-195` |
| Buchst. b | 1 `RR`; Verpackungsfallback als alternative Modalität ohne eigene `RR` | `RR-196` |
| Buchst. c | 1 `RR`; maschinenlesbare Ergänzung als Permission ohne `RR` | `RR-197` |
| Buchst. d | 1 reguläre `RR` mit negativer Ausnahme; Klasse-I-/IIa-Ausnahme ohne eigene `RR` | `RR-198` |
| Buchst. e | 1 conditional `RR`; einzelne Ausfertigung als Permission ohne `RR` | `RR-199` |
| Buchst. f | 1 conditional `RR` | `RR-200` |
| Buchst. g | 1 conditional `RR` | `RR-201` |
| Buchst. h | 3 conditional `RR` | `RR-202` bis `RR-204` |
| **Gesamt** | **22 `RR`, 5 0-`RR`-Entscheidungen** | |

**Conditionality**

- Conditional sind `RR-187`, `RR-188`, `RR-195`, `RR-199`, `RR-200`, `RR-201`, `RR-202`, `RR-203` und `RR-204`; die jeweilige Bedingung steht im Requirement Text.
- `RR-185` und `RR-186` bleiben regulär; die bedingte Erweiterung des Empfängerkreises auf andere Personen ist im Requirement Text erhalten.
- `RR-198` bleibt regulär; die negative Ausnahme mit drei kumulativen Voraussetzungen (Klasse I oder IIa, sichere Anwendung ohne Gebrauchsanweisung, keine abweichende Vorschrift in Abschnitt 23) ist im Requirement Text erhalten. Klasse I oder IIa ist kein positiver Trigger.
- `RR-203` und `RR-204` sind komplementäre Triggerzweige: verwendetes Symbol bzw. verwendete Identifizierungsfarbe mit bzw. ohne einschlägige harmonisierte Norm oder Gemeinsame Spezifikation. Für dasselbe Symbol im selben Bereich werden sie nicht gleichzeitig aktiviert.
- Es wurde kein neues Katalogfeld eingeführt.

**Theme und Lebenszyklus**

13 `RR` tragen das Themencluster `Transparenz`, 9 `RR` das Themencluster `Gebrauchstauglichkeit`. Die Lebenszyklusphasen stammen ausschließlich aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 3.

**SOURCE_DEPENDENCY**

- `RR-200`: externe normative Abhängigkeit von Durchführungsverordnung (EU) 2021/2226 (konsolidiert 16.07.2025, einschließlich der Änderung durch (EU) 2025/1234). `SRC-001` bestimmt den MDR-Sollzustand; die externe Verordnung bestimmt die konkreten Durchführungsbedingungen. Die Abhängigkeit betrifft die vollständige Operationalisierung, nicht Existenz oder Atomizität der `RR`; kein Unresolved, Status `aktiv`.
- `RR-203` und `RR-204`: externe Evidenz zu einschlägigen harmonisierten Normen bzw. Gemeinsamen Spezifikationen ist für die vollständige Operationalisierung erforderlich; es wurde keine konkrete Norm ausgewählt.
- Durchführungsverordnung (EU) 2021/2226 ist **nicht** registriert: keine `SRC`-ID, kein Supplementary-Locator, keine daraus extrahierte `RR`. Ihre spätere Prüfung und Registrierung erfordert eine separate Coverage Change Control nach Abschnitt 10.2; empfohlen ist eine Einordnung als Ebene A mit Nutzungsart `triggerbasiert` (Trigger: elektronische bzw. Nicht-Papier-Gebrauchsanweisung im Anwendungsbereich von Nr. 23.1 Buchst. f). Diese Empfehlung wird hier nicht umgesetzt.
- Der Abschluss von Nr. 23.1 ist trotz dieser Abhängigkeiten zulässig, weil sie die Operationalisierung, nicht die Extraktion betreffen.

**Deduplizierung**

Der in Abschnitt 10.16 vorgemerkte und in den Abschnitten 10.20 und 10.21 bestätigte Abgleich mit `RR-164` ist abgeschlossen; zusätzlich wurden `RR-175` und `RR-176` geprüft. Partielle Überschneidungen bestehen zwischen `RR-189` bis `RR-193` und `RR-164`, zwischen `RR-189` bis `RR-195` und `RR-175`; `RR-189` bis `RR-195` sind von `RR-176` unterschieden. Zusätzlich dokumentiert: `RR-185` ↔ `RR-160` und `RR-201` ↔ `RR-162`, jeweils partieller Overlap. Vollständige Deduplizierungen: 0; alle bestehenden `RR` bleiben unverändert.

**Nicht extrahierte Bereiche**

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.23.2` bis `Nr.23.3` | nicht Teil der Coverage und nicht vorweggenommen; Nr. 23.2 nur interner Kontext zu `RR-196` |
| `SRC-001#Anh.I/Nr.23.4` — ausgewählte Buchstaben | nicht vorweggenommen; bleibt `geplant` |
| Durchführungsverordnung (EU) 2021/2226 | nicht registriert und nicht extrahiert |
| `SRC-005` bis `SRC-008`, harmonisierte Normen und Gemeinsame Spezifikationen, Kandidaten des [Standards-Landscape-Audits](../01-research/MEDICAL_DEVICE_STANDARDS_LANDSCAPE_AUDIT.md) | keine Norminhalte vorweggenommen |

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-001#Anh.I/Nr.23.1` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Priorität, erwartete Themencluster und Trigger bleiben unverändert.


### 10.23 Change Control Version 1.33 — Aufnahme `SRC-009` (Durchführungsverordnung (EU) 2021/2226)

**A. Anlass**

- `RR-200` (`SRC-001#Anh.I/Nr.23.1/Buchst.f`) besitzt eine aktive, in [RR_EXTRACTION_MDR_ANNEXI_23_1.md](RR_EXTRACTION_MDR_ANNEXI_23_1.md) Abschnitt 10 dokumentierte SOURCE_DEPENDENCY: `SRC-001` bestimmt den MDR-Sollzustand, die Durchführungsverordnung (EU) 2021/2226 die konkreten Durchführungsbedingungen für elektronische Gebrauchsanweisungen.
- Abschnitt 10.22 hat die spätere Prüfung und Registrierung dieser Quelle über eine separate Change Control vorgesehen.

**B. Wissenschaftliche Begründung und Aufnahmevoraussetzungen (Abschnitt 4.3)**

| Voraussetzung | Ergebnis |
| --- | --- |
| 1. Relevanz für KI-basierte Medizinproduktesoftware in mindestens einem bestehenden Themencluster | erfüllt; erwartete Cluster siehe Abschnitt 9.9 |
| 2. Eigenständiger Beitrag gegenüber dem Quellenkorpus | erfüllt; 2021/2226 ist unmittelbar geltendes EU-Recht und konkretisiert rechtsverbindlich den von MDR Anhang I Nr. 23.1 Buchst. f vorausgesetzten Durchführungsrahmen, den `SRC-001` selbst nicht enthält |
| 3. Dokumentierte Coverage Change Control mit Quellenebene und Nutzungsart | dieser Abschnitt |
| 4. Verifikation von Fassung, Status und Bezugsquelle anhand einer Primärquelle | in der abgeschlossenen Research-Entscheidung anhand von EUR-Lex; dokumentiert in [SOURCES.md](SOURCES.md) |

**C. Registrierung und Rechtsstand**

| Merkmal | Festlegung |
| --- | --- |
| `SRC`-ID | `SRC-009` ([SOURCES.md](SOURCES.md) Version 1.3) |
| Rechtsakt | Durchführungsverordnung (EU) 2021/2226 der Kommission vom 14. Dezember 2021 |
| Arbeitsfassung | konsolidierte Fassung 16.07.2025, CELEX `02021R2226-20250716`, einschließlich der Änderung durch Durchführungsverordnung (EU) 2025/1234; Basisrechtsakt CELEX `32021R2226` |
| Quellenebene | A — rechtsverbindliche Quelle |
| Nutzungsart | `triggerbasiert` (Abschnitt 4.2) |
| Globaler Applicability-Trigger | elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware |
| Verhältnis zu bestehenden Quellen | ersetzt keine Quelle; `SRC-001#Anh.I/Nr.23.1/Buchst.f` bleibt normative Hauptfundstelle von `RR-200` |

**D. Applicability-Trigger und innere Zweige**

Der globale Trigger aktiviert die Quellenprüfung. Die spätere `0 / 1 / n`- und Regellogik muss innerhalb der Quelle zusätzliche Zweige unterscheiden, insbesondere:

- elektronische Gebrauchsanweisung anstelle einer Papier-Gebrauchsanweisung;
- softwarespezifischer Pfad nach `SRC-009#Art.3/Abs.3`;
- professioneller Nutzerpfad nach `SRC-009#Art.3/Abs.1`;
- vorhersehbare Laiennutzung nach `SRC-009#Art.3/Abs.2`;
- elektronische Gebrauchsanweisung zusätzlich zu einer vollständigen Papier-Gebrauchsanweisung;
- softwareintegrierte bzw. sonstige elektronische Darstellung;
- Website;
- Papierexemplar auf Anforderung.

In diesem Schritt werden **keine** `RUL` und **keine** `RR` erzeugt.

**E. Coverage-Scope**

| Einordnung | Bereiche |
| --- | --- |
| systematische `0 / 1 / n`-Prüfung | `SRC-009#Art.3`, `SRC-009#Art.4`, `SRC-009#Art.5`, `SRC-009#Art.6`, `SRC-009#Art.7`, `SRC-009#Art.9` |
| Supporting Context | `SRC-009#Art.1`, `SRC-009#Art.2`, `SRC-009#Art.10`, Anhang |
| keine Gap-Extraktion | `SRC-009#Art.8` (im verbindlichen konsolidierten Rechtsstand gestrichen); `SRC-009#Art.11` (Inkrafttreten bzw. unmittelbare Geltung, kein Hersteller-Gap-Sollzustand) |

Die systematische Einordnung bedeutet ausschließlich, dass die Bereiche später methodisch `0 / 1 / n` geprüft werden; sie bedeutet nicht, dass jeder Artikel `RR` erzeugt. Die erwarteten Themencluster je Artikel stehen in Abschnitt 9.9; sie sind keine Theme-Zuordnung künftiger `RR`, und es wird kein neuer Cluster eingeführt.

**F. Bearbeitungsstatus**

Die sechs systematischen Quellenbereiche werden unmittelbar auf `in Prüfung` gesetzt, nicht auf `geplant`: `RR-200` enthält bereits eine aktive normative Abhängigkeit, und die systematische Prüfung dieser Quelle ist mit dieser Change Control ausdrücklich eröffnet. Wie bei den übrigen conditional Quellenbereichen (vgl. Abschnitt 10.20) erfolgt die Prüfung ex ante; die Nutzungsart `triggerbasiert` bestimmt die Anwendbarkeit der späteren Ergebnisse im konkreten Fall.

**G. Offene Abhängigkeiten ohne Registrierung**

| Abhängigkeit | Behandlung |
| --- | --- |
| Verordnung (EU) 2016/679 (DSGVO) | `SRC-009#Art.7/Abs.2/Buchst.d` enthält eine Datenschutzabhängigkeit. Datenschutz und DSGVO bilden nach [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 5 keinen Gap-Themencluster. Keine `SRC`-ID, keine systematische Aufnahme; ausschließlich Scope- bzw. Dependency-Hinweis. |
| mitgliedstaatliche Sprachfestlegung | Für eine konkrete länderspezifische Operationalisierung ist ein externer Jurisdiktionsparameter erforderlich. Keine `SRC`-ID. |
| Verordnung (EU) Nr. 207/2012 | aufgehoben; keine operative Quelle für den regulären Fall einer Medizinproduktesoftware im Rechtsstand 2026; ausschließlich historische Traceability bzw. Korrelation über `SRC-009#Art.10` und den Anhang. Keine `SRC`-ID. |

Es werden keine weiteren Quellen registriert.

**H. Impact-Prüfung**

| Betroffen | Ergebnis |
| --- | --- |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.19 (`RR-001` bis `RR-204`) | unverändert; keine neue `RR` |
| `RR-200` | unverändert; Primary bleibt `SRC-001#Anh.I/Nr.23.1/Buchst.f`; kein Supplementary-Locator ergänzt; die Beziehung ist als SOURCE_DEPENDENCY in der bestehenden Evidenz und in dieser Change Control dokumentiert |
| `SRC-001` bis `SRC-008` | inhaltlich unverändert |
| Extraktionsnachweise | unverändert |
| [MEDICAL_DEVICE_STANDARDS_LANDSCAPE_AUDIT.md](../01-research/MEDICAL_DEVICE_STANDARDS_LANDSCAPE_AUDIT.md) | unverändert; die dortigen Nummernvorschläge waren nicht reserviert, und der Audit vergibt keine `SRC`-IDs. Spätere tatsächliche `SRC`-IDs für Normenkandidaten verschieben sich entsprechend. |
| übrige Quellenbereiche, insbesondere `SRC-001#Anh.I/Nr.23.4` und `SRC-001#Art.83` ff. | unverändert; `SRC-001#Anh.I/Nr.23.4` bleibt `geplant` |
| Normen-Coverage | unverändert |

**I. Freigabe**

Freigegeben sind die Registrierung von `SRC-009` und die systematische Prüfung der in Abschnitt 9.9 genannten Quellenbereiche. In diesem Change-Control-Schritt erfolgt **keine** Extraktion.


### 10.24 Statusabschluss `SRC-009` Art. 3 bis 7 und Art. 9

- Die vollständige systematische `0 / 1 / n`-Prüfung mit den vollständigen Research-Begründungen einschließlich der Nachadjudikation zu `S9-5-A`, `S9-5-L`, `S9-6-A`/`S9-6-B`, `S9-5-V`/`S9-5-W` und zur Source-Level Conditionality ist in [RR_EXTRACTION_SRC_009_ART3_7_9.md](RR_EXTRACTION_SRC_009_ART3_7_9.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Rechtsstand: `SRC-009`, konsolidierte Fassung 16.07.2025 (CELEX `02021R2226-20250716`).
- Ergebnis: 67 geprüfte aktuelle potenzielle Einheiten; 61 neue Gap-`RR`, davon 0 regulär und 61 conditional; 6 0-`RR`-Entscheidungen; 0 ungelöste und 0 zurückgestellte Fälle; 0 vollständige Deduplizierungen.
- Katalogintegration: `RR-205` bis `RR-265` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.20.

**Abgedeckte Struktur**

| Quellenbereich | `RR` | 0-`RR` | IDs |
| --- | --- | --- | --- |
| `SRC-009#Art.3` | 1 | 2 (Abs. 1 und Abs. 3: Permission/Applicability) | `RR-205` |
| `SRC-009#Art.4` | 14 | 0 | `RR-206` bis `RR-219` |
| `SRC-009#Art.5` | 23 | 1 (Chapeau: Permission/gemeinsamer Rahmen) | `RR-220` bis `RR-242` |
| `SRC-009#Art.6` | 12 | 2 (Abs. 5: Symbole/Grafiken; Video-/Audiodateien) | `RR-243` bis `RR-254` |
| `SRC-009#Art.7` | 10 | 1 (Abs. 2 Buchst. d: DSGVO, Out-of-Scope) | `RR-255` bis `RR-264` |
| `SRC-009#Art.9` | 1 | 0 | `RR-265` |
| **Gesamt** | **61** | **6** | |

**Theme und Lebenszyklus**

| Themencluster | Anzahl |
| --- | --- |
| Qualitäts- und Risikomanagement | 17 |
| Transparenz | 31 |
| Gebrauchstauglichkeit | 7 |
| Robustheit | 6 |
| Data Governance, Menschliche Aufsicht, Post-Market-Monitoring, Software-Lebenszyklus | 0 |

| Lebenszyklusphase | Anzahl |
| --- | --- |
| Planung und Konzeption | 14 |
| Entwicklung und Realisierung | 44 |
| Verifikation und Validierung | 2 |
| Konformitätsbewertung | 0 |
| Inverkehrbringen, Inbetriebnahme und Betrieb | 41 |
| Post-Market-Überwachung | 1 |
| Änderung und Wartung | 52 |

**Applicability-Baum und Conditionality**

- Alle 61 `RR` sind conditional — nicht allein wegen der Nutzungsart `triggerbasiert`, sondern weil die konkreten Pflichten rechtlich nur in den jeweiligen eIFU-Anwendungszweigen gelten.
- Outer Conditional: Art. 4 bis 7 — eIFU anstelle der Papier-IFU im einschlägigen Art.-3-Pfad, für RegScoutX insbesondere MDR-Software nach Art. 3 Abs. 3; Art. 9 — eIFU zusätzlich zu einer vollständigen Papier-IFU; `RR-205` — professioneller Nutzerpfad und vernünftigerweise vorhersehbare Laiennutzung.
- Lokale Trigger (z. B. eingebautes Anzeigesystem, Anforderung der Papierfassung, sicherheitsrelevante Revision, Verfallsdatum, Speichermedium, UDI-Registrierungszeitpunkt) bleiben zusätzliche innere Bedingungen.
- Konsistent mit Abschnitt 10.20: Die äußere Block-Applicability erzeugt die Conditionality der materiellen `RR`, ohne selbst eine `RR` zu werden. Kein neues Katalogfeld.

**Source Dependencies**

| Abhängigkeit | Betroffen | Behandlung |
| --- | --- | --- |
| mitgliedstaatliche Sprachfestlegung | `RR-240` | jurisdiktionsabhängige Evidenz; keine nationale Quelle registriert |
| Verordnung (EU) 2016/679 (DSGVO) | Art. 7 Abs. 2 Buchst. d | echte Abhängigkeit, materieller Datenschutz-Gap außerhalb des Themen-Scope ([CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 5); 0 `RR`, keine `SRC`-ID |
| MDR-UDI (`SRC-001`) | `RR-248`, `RR-264` | innerhalb der bereits registrierten `SRC-001`; keine neue Quelle |
| interne `SRC-009`-Verweise | Art. 4 ↔ Art. 5, Art. 6 ↔ Art. 5 | keine neue Source Dependency |

**Rechtsstand und nicht extrahierte Bestandteile**

- `SRC-009#Art.8` ist im verbindlichen Rechtsstand vollständig gestrichen; keine Extraktion.
- Gestrichene Unterpunkte — Art. 5 Nr. 12, Art. 6 Abs. 4, Art. 7 Abs. 2 Buchst. f, Art. 9 Abs. 2 — wurden nicht aus älteren Fassungen importiert und nicht als 0-`RR` gezählt.
- Die Kontextbereiche Art. 1, Art. 2, Art. 10 und Anhang sowie Art. 11 bleiben entsprechend ihrer Einordnung in Abschnitt 9.9 ohne Gap-Extraktion.

**Deduplizierung**

Art. 4 bis 7 ↔ `RR-200`: partieller Overlap als normative Konkretisierung, keine Deduplizierung; `RR-265` ↔ `RR-200` unterschieden (Zusatzpfad). Weitere partielle Overlaps sind in der Evidenz Abschnitt 14 dokumentiert. Vollständige Deduplizierungen: 0. `RR-200` bleibt unverändert (Primary `SRC-001#Anh.I/Nr.23.1/Buchst.f`); alle übrigen bestehenden `RR` bleiben unverändert.

**Abgrenzung**

Es wurden keine weiteren Quellen importiert oder registriert und keine Norminhalte vorweggenommen. `SRC-001#Anh.I/Nr.23.4` bleibt `geplant`; `SRC-001#Art.83` ff. und die Normen-Coverage bleiben unverändert.

Nach der Statusdefinition aus Abschnitt 10.1 sind `SRC-009#Art.3`, `SRC-009#Art.4`, `SRC-009#Art.5`, `SRC-009#Art.6`, `SRC-009#Art.7` und `SRC-009#Art.9` damit vollständig geprüft und das Ergebnis dokumentiert; ihr Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Priorität, erwartete Themencluster und Trigger bleiben unverändert.


### 10.25 Aktivierung `SRC-001` Anhang I Nr. 23.4 — ausgewählte Buchstaben

- Die systematische `0 / 1 / n`-Prüfung des bereits in Abschnitt 9.1 freigegebenen, begrenzten Quellenbereichs `SRC-001#Anh.I/Nr.23.4` wird gestartet; der Bearbeitungsstatus wird von `geplant` auf `in Prüfung` gesetzt.
- Nr. 23.4 wird **nicht** vollständig extrahiert. Systematisch geprüft werden ausschließlich die bereits festgelegten neun Buchstaben: `SRC-001#Anh.I/Nr.23.4/Buchst.b`, `Buchst.e`, `Buchst.f`, `Buchst.g`, `Buchst.h`, `Buchst.j`, `Buchst.k`, `Buchst.s` und `Buchst.ab`. Die übrigen Buchstaben von Nr. 23.4 werden nicht aktiviert.
- Die Auswahl entspricht der bestehenden Festlegung in Abschnitt 9.1 („Nur die bereits verifizierten thematisch relevanten Unterpunkte werden geprüft") und dem horizontalen Untersuchungsgegenstand KI-basierter Medizinproduktesoftware (Abschnitt 4.3). Priorität `Ergänzend`, `expected_theme_clusters` `Transparenz`, Trigger `—` und der Hinweis, die Applicability der einzelnen Buchstaben zu erhalten, bleiben unverändert; die Cluster bleiben eine reine Ex-ante-Erwartung nach Abschnitt 7.
- Die endgültige `RR`-Relevanz der einzelnen Buchstaben wird erst durch die anschließende systematische `0 / 1 / n`-Prüfung entschieden. Die Aktivierung erzeugt noch keine `RR`; es erfolgt keine Extraktions-, Atomizitäts-, Theme-, Lifecycle-, Conditionality-, Deduplizierungs- oder Locator-Entscheidung, und es wird noch keine Evidenzdatei angelegt.
- Keine Änderung des Coverage-Scope und keine weitere Aktivierung: `SRC-001#Anh.I/Nr.23.2`, `SRC-001#Anh.I/Nr.23.3`, `SRC-001#Art.83` ff., weitere MDR-Bereiche und weitere Quellen bleiben unberührt. `SRC-001#Anh.I/Nr.23.1` sowie `SRC-009#Art.3` bis `Art.7` und `Art.9` bleiben `abgeschlossen`. Es wurden keine Norminhalte vorgezogen.


### 10.26 Statusabschluss `SRC-001` Anhang I Nr. 23.4 — ausgewählte Buchstaben

- Die systematische `0 / 1 / n`-Prüfung der Buchstaben b, e, f, g, h, j, k, s und ab ist in [RR_EXTRACTION_MDR_ANNEXI_23_4.md](RR_EXTRACTION_MDR_ANNEXI_23_4.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung. Nr. 23.4 wurde nicht vollständig extrahiert.
- Ergebnis: 35 potenzielle Einheiten; 30 neue Gap-`RR`, davon 9 regulär und 21 conditional; 5 0-`RR`-Entscheidungen (OUT_OF_SCOPE); 0 ungelöste Fälle; 0 vollständige Deduplizierungen.
- Katalogintegration: `RR-266` bis `RR-295` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.22.
- Theme: 30 × `Transparenz`. Lebenszyklus: alle 30 × Entwicklung und Realisierung, Inverkehrbringen, Inbetriebnahme und Betrieb sowie Änderung und Wartung.
- Scope: Die fünf 0-`RR`-Entscheidungen betreffen in Buchst. k vorbereitende Reinigung bzw. Desinfektion sowie Verbrauchskomponenten und in Buchst. s Arzneimittel, Gewebe, Zellen und biologische Stoffe, integrierten Arzneistoff bzw. biologisches Material sowie CMR-, endokrinschädliche und sensibilisierende Materialien — jeweils ohne horizontalen systematischen Beitrag für eigenständige Medizinproduktesoftware; keine Aussage über regulatorische Irrelevanz.
- Deduplizierung: dokumentierte partielle Überschneidungen bzw. Unterscheidungen u. a. zu `RR-160`, `RR-161`, `RR-162`, `RR-185`, `RR-186`, `RR-201` und `RR-233`. `SRC-009` regelt im eIFU-Fall Medium und Inhaltsparität, nicht die materiellen Nr.-23.4-Inhalte; `RR-200` und alle bestehenden `RR` bleiben unverändert.
- Keine neue externe Source Dependency; `SRC-001#Anh.I/Nr.17.4` wird nicht importiert.
- Die übrigen Buchstaben von Nr. 23.4 bleiben außerhalb dieser Aktivierung; `SRC-001#Anh.I/Nr.23.2`, `Nr.23.3`, `SRC-001#Art.83` ff., `SRC-009` und die Normen-Coverage bleiben unverändert.

Nach der Statusdefinition aus Abschnitt 10.1 ist der begrenzte Quellenbereich `SRC-001#Anh.I/Nr.23.4` (Buchst. b, e, f, g, h, j, k, s, ab) damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Priorität, erwartetes Themencluster und Trigger bleiben unverändert.


### 10.27 Aktivierung MDR-PMS-Block `SRC-001` Art. 83, Art. 84 und Anhang III Abschnitt 1

- Die bereits freigegebenen Kernbereiche `SRC-001#Art.83`, `SRC-001#Art.84` und `SRC-001#Anh.III/Abschn.1` werden als zusammenhängender PMS-Block zur systematischen `0 / 1 / n`-Prüfung eröffnet; ihr Bearbeitungsstatus wird von `geplant` auf `in Prüfung` gesetzt.
- Prioritäten, erwartete Themencluster, Trigger, Scope-Begründungen und Hinweise bleiben unverändert. Die in den Abschnitten 10.13 und 10.14 vorgemerkten Abgleiche mit `RR-135` bis `RR-137` und `RR-152` bleiben unverändert bestehen.
- Noch keine Extraktions- oder sonstige fachliche Entscheidung, keine `RR` und keine Evidenzdatei. `SRC-001#Art.85` und `SRC-001#Art.86` sowie alle übrigen Coverage-Bereiche bleiben unverändert.


### 10.28 Statusabschluss MDR-PMS-Block `SRC-001` Art. 83, Art. 84 und Anhang III Abschnitt 1

- Die systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_MDR_PMS_ART83_84_ANNEXIII_1.md](RR_EXTRACTION_MDR_PMS_ART83_84_ANNEXIII_1.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 61 potenzielle Einheiten; 57 neue Gap-`RR` (Art. 83: 34, Art. 84: 2, Anhang III Abschnitt 1: 21), davon 49 regulär und 8 conditional; 4 0-`RR`-Entscheidungen (Chapeaus von Art. 83 Abs. 3 und Anhang III Abschnitt 1 Buchst. a und b als nicht atomarer gemeinsamer Rahmen; Verweis in Art. 84 Satz 1 als Querverweis); 0 ungelöste Fälle.
- Katalogintegration: `RR-296` bis `RR-352` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.23.
- Theme: 57 × `Post-Market-Monitoring`. Lebenszyklus: Planung und Konzeption 27, Konformitätsbewertung 1, Post-Market-Überwachung 31, übrige Phasen 0. Die Anhang-III-Kandidaten betreffen den PMS-Plan, die Art.-83-Kandidaten den tatsächlichen PMS-Betrieb.
- Deduplizierung: Die in den Abschnitten 10.13 und 10.14 vorgemerkten Abgleiche sind durchgeführt — `M83-B`, `M83-D`, `M83-E` und `M83-H` gegenüber `RR-135` bis `RR-137` sowie `M83-P` und `M83-Q` gegenüber `RR-152` jeweils partieller Overlap. Vollständige Deduplizierungen: 0; alle bestehenden `RR` bleiben unverändert.
- Keine externe Source Dependency; MDR-interne Verweise (u. a. Art. 32, 86, 87, 88, Anhang II, Anhang XIV Teil B) bleiben Kontext und werden nicht vorgezogen.
- `SRC-001#Art.85` und `SRC-001#Art.86` bleiben `geplant`; alle übrigen Coverage-Bereiche bleiben unverändert.

Nach der Statusdefinition aus Abschnitt 10.1 sind `SRC-001#Art.83`, `SRC-001#Art.84` und `SRC-001#Anh.III/Abschn.1` damit vollständig geprüft und das Ergebnis dokumentiert; ihr Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Prioritäten, erwartete Themencluster und Trigger bleiben unverändert.


### 10.29 Aktivierung klassenspezifischer MDR-PMS-Berichtsblock `SRC-001` Art. 85 und Art. 86

- Die bereits freigegebenen conditional Bereiche `SRC-001#Art.85` (Klasse-I-Zweig) und `SRC-001#Art.86` (Klasse-IIa/IIb/III-Zweig) werden als zusammengehörender klassenspezifischer PMS-Berichtsblock zur systematischen `0 / 1 / n`-Prüfung eröffnet; ihr Bearbeitungsstatus wird von `geplant` auf `in Prüfung` gesetzt.
- Prioritäten (`Ergänzend, conditional`), erwartete Themencluster, Trigger (Klasse I bzw. Klasse IIa, IIb oder III) und Scope-Begründungen bleiben unverändert.
- Noch keine Extraktions- oder sonstige fachliche Entscheidung, keine `RR` und keine Evidenzdatei. Alle übrigen Coverage-Bereiche bleiben unverändert.


### 10.30 Statusabschluss klassenspezifischer MDR-PMS-Berichtsblock `SRC-001` Art. 85 und Art. 86

- Die systematische `0 / 1 / n`-Prüfung ist in [RR_EXTRACTION_MDR_PMS_ART85_86.md](RR_EXTRACTION_MDR_PMS_ART85_86.md) Version 1.0 dokumentiert; 0 operative Fundstellen blieben ohne Entscheidung.
- Ergebnis: 28 potenzielle Einheiten; 25 neue Gap-`RR` (Art. 85: 7, Art. 86: 18), alle conditional; 3 0-`RR`-Entscheidungen (Produkt-/Kategorie-/Gruppen-Granularität in Art. 86 Abs. 1 als Modalität; Prüfung durch die Benannte Stelle und Systemzugänglichkeit für Behörden in Art. 86 Abs. 2 Satz 2 und 3 ohne Hersteller-Sollzustand); 0 ungelöste Fälle; 0 vollständige Deduplizierungen.
- Katalogintegration: `RR-353` bis `RR-377` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.24.
- Theme: 25 × `Post-Market-Monitoring`. Lebenszyklus: 25 × `Post-Market-Überwachung`.
- Klassenspezifische Trigger: Art. 85 — Klasse I (PMS-Bericht); Art. 86 — Klasse IIa, IIb oder III (PSUR), mit mindestens jährlicher Aktualisierung für IIb und III, bedarfsbezogener und mindestens zweijährlicher Aktualisierung für IIa, elektronischer Übermittlung an die Benannte Stelle für Klasse III bzw. implantierbare Produkte (Abs. 2) und Bereitstellung für Benannte Stelle und Behörden für die übrigen Art.-86-Produkte (Abs. 3).
- Keine externe Source Dependency; bestehende `RR` einschließlich `RR-296` bis `RR-352` bleiben unverändert.
- `SRC-001#Art.83`, `SRC-001#Art.84` und `SRC-001#Anh.III/Abschn.1` bleiben `abgeschlossen`; alle übrigen Coverage-Bereiche bleiben unverändert.

Nach der Statusdefinition aus Abschnitt 10.1 sind `SRC-001#Art.85` und `SRC-001#Art.86` damit vollständig geprüft und das Ergebnis dokumentiert; ihr Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt. Prioritäten, erwartete Themencluster und Trigger bleiben unverändert.


### 10.31 Aktivierung `SRC-003` (AIB 2025-1 / MDCG 2025-6)

- Nach Abschluss aller freigegebenen Gap-Bereiche aus `SRC-001`, `SRC-002` und `SRC-009` liegt der stabilisierte Rechtsakt-Korpus vor, gegen den `SRC-003` nach Abschnitt 9.7 geprüft wird. Die Prüfung von `SRC-003` wird entsprechend der Reihenfolge in Abschnitt 13 eröffnet; der Bearbeitungsstatus wird auf `in Prüfung` gesetzt.
- Die Quellenrolle bleibt unverändert: Ebene B, nicht rechtsverbindliche Guidance; Interplay-, Crosswalk-, Interpretations- und Deduplizierungsquelle; kein zweiter Gap-Kernkatalog und keine Gleichstellung mit rechtsverbindlichen Anforderungen. Guidance erzeugt keine neuen `RR` allein aufgrund ihrer Paraphrase oder Interpretation gesetzlicher Pflichten (Abschnitte 5.2 und 5.4); ob eigenständiger zusätzlicher Guidance-Gehalt besteht, entscheidet erst die Prüfung.
- Noch keine Extraktions-, Crosswalk- oder sonstige fachliche Entscheidung, keine `RR` und keine Evidenzdatei. `SRC-004` sowie alle übrigen Coverage-Bereiche bleiben unverändert; `SRC-005` bis `SRC-008` bleiben `blockiert`.

### 10.32 Abschluss `SRC-003` (AIB 2025-1 / MDCG 2025-6)

- Crosswalk- und Interpretationsprüfung von `SRC-003` gegen den stabilisierten Rechtsakt-Korpus `RR-001` bis `RR-377` abgeschlossen. Evidenz: [CROSSWALK_SRC_003_MDR_AI_ACT.md](CROSSWALK_SRC_003_MDR_AI_ACT.md) Version 1.0 mit 25 Crosswalk-Einträgen (`EXPLANATORY`, `CROSSWALK`, `INTERPRETATIVE`, `PROCESS_ALIGNMENT`; alle zusätzlich `NO_NEW_REQUIREMENT`).
- 0 neue `RR`; keine bestehende `RR` geändert; [RR_CATALOG.yaml](RR_CATALOG.yaml) bleibt Version 0.24 mit 377 `RR`. Keine Guidance-Aussage wird als rechtsverbindliche Anforderung geführt.
- Gemeinsame Evidenz ≠ normative Deduplizierung: Process Alignment für QMS, Risikomanagement, technische Dokumentation, Konformitätsbewertung und PMS unterstützt gemeinsame Prozesse und Evidenzartefakte, begründet aber keine Zusammenführung von `RR`; 0 Deduplizierungen.
- Aktuelles Primärrecht hat Vorrang vor veralteten Guidance-Aussagen: Q2/Q4, Q27/Q28, Q31 und Q34 sind als `STALE/SUPERSEDED_GUIDANCE` gegenüber `SRC-002` im Stand 27.07.2026 dokumentiert und werden nicht als aktueller Rechtsstand operationalisiert.
- RUL-relevante Guidance-Stellen (insbesondere Q2/Q4, Q27/Q28, Q29/Q30, Q31, Q35) sind dokumentiert; eine spätere Entscheidungsregel ist jeweils am aktuellen Rechtsakt zu verankern.
- 0 blockierende Unresolveds. Quellenrolle Ebene B unverändert. [SOURCES.md](SOURCES.md) Version 1.4 ergänzt ausschließlich den Lokator `SRC-003#Einleitung`. Keine Methodik-, Vocabulary- oder Scope-Änderung; `SRC-004` sowie alle übrigen Coverage-Bereiche bleiben unverändert; `SRC-005` bis `SRC-008` bleiben `blockiert`.

Nach der Statusdefinition aus Abschnitt 10.1 ist `SRC-003` damit vollständig geprüft und das Ergebnis dokumentiert; der Bearbeitungsstatus wird deshalb auf `abgeschlossen` gesetzt.

### 10.33 Aktivierung `SRC-004` (MDCG 2019-11 Rev. 1)

- Nach Abschluss von `SRC-003` (Abschnitt 10.32) wird die Prüfung von `SRC-004` entsprechend der Reihenfolge in Abschnitt 13 eröffnet; der Bearbeitungsstatus wird auf `in Prüfung` gesetzt.
- Prüfgegenstand ist `SRC-004` als Ebene-B-Guidance für Software-Qualifikation, MDR/IVDR-Abgrenzung, MDSW-Klassifikation, MDR Anhang VIII Regel 11 und die spätere regelbasierte `RUL`- bzw. Entscheidungslogik. Die bestehende Rollen- und Scope-Beschreibung in den Abschnitten 4, 8 und 9.7 bleibt unverändert.
- `SRC-004` ist keine eigenständige Gap-`RR`-Quelle; aus der Guidance werden keine `RR` erzeugt (Abschnitte 5.2 und 5.4).
- Noch keine Recherche-, Extraktions-, Classification- oder sonstige fachliche Entscheidung, keine `RR`, keine `RUL` und keine Evidenzdatei. `SRC-003` bleibt `abgeschlossen`; alle übrigen Coverage-Bereiche bleiben unverändert; `SRC-005` bis `SRC-008` bleiben `blockiert`.

### 10.34 Abschluss `SRC-004` und Aufnahme `SRC-010`

**`SRC-004` — Abschluss**

- `SRC-004` (MDCG 2019-11 Rev. 1) wurde als Ebene-B-Guidance vollständig für die regelbasierte Entscheidungslogik ausgewertet. Evidenz: [DECISION_LOGIC_SRC_004_MDSW_QUALIFICATION_CLASSIFICATION.md](DECISION_LOGIC_SRC_004_MDSW_QUALIFICATION_CLASSIFICATION.md) Version 1.0.
- Analysiert: Software-Qualifikation (Figure 1), MDR/IVDR-Abgrenzung (Figure 2), Regel 11 sowie die für MDSW relevanten zusätzlichen MDR-Regeln 12, 13, 15 und 22 einschließlich Anhang VIII Abschnitte 3.3 und 3.5, Module und Change Reassessment.
- 26 `RUL` als `RUL-001` bis `RUL-026` in [RUL_CATALOG.yaml](RUL_CATALOG.yaml) Version 0.1 nach [RUL_METHOD.md](RUL_METHOD.md) Version 1.0 angelegt. Jede `RUL` trägt getrennt einen Primary Legal Anchor (`SRC-001` bzw. `SRC-010`) und einen Guidance Anchor (`SRC-004`).
- 0 neue `RR`; [RR_CATALOG.yaml](RR_CATALOG.yaml) bleibt Version 0.24 mit 377 `RR`; keine bestehende `RR` geändert.
- `SRC-004` bleibt Guidance-Schicht: Keine `RUL` stellt `SRC-004` als alleinige rechtsverbindliche Grundlage dar; Guidance-Auslegungen über den Wortlaut hinaus sind als `GUIDANCE_INTERPRETATION` gekennzeichnet.
- Bearbeitungsstatus `SRC-004`: `abgeschlossen` (Abschnitt 9.7).

**`SRC-010` — Aufnahme (Coverage Change Control nach Abschnitt 10.2)**

1. **Fachliche Begründung:** Die MDR/IVDR-Abgrenzung aus `SRC-004` Figure 2 benötigt für eine rechtsfeste Entscheidungsregel die Definition des In-vitro-Diagnostikums als Primärrechtsanker (SOURCE_DEPENDENCY der Research-Adjudikation zu `SRC-004`). Zu Abschnitt 4.3: Die Quelle ist für KI-basierte Medizinproduktesoftware relevant, weil die Abgrenzung darüber entscheidet, ob der MDR-basierte Gap-Katalog in den bestehenden Themenclustern überhaupt anwendbar ist (Nr. 1); sie ist die einzige rechtsverbindliche Grundlage dieser Definition im Korpus (Nr. 2); Ebene A und Nutzungsart `unterstützend` werden hier festgelegt (Nr. 3); Fassung, Status und Bezugsquelle wurden am 25.09.2026 anhand von EUR-Lex verifiziert (Nr. 4). Die Anwendung von Nr. 1 auf eine reine Abgrenzungsquelle ohne eigenen Gap-Beitrag ist eine Auslegung dieser Aufnahmevoraussetzung und wird hiermit ausdrücklich dokumentiert.
2. **Umfang:** ausschließlich `SRC-010#Art.2/Nr.2` (Abschnitt 9.10); keine weiteren IVDR-Artikel, keine IVDR-Gap-Extraktion, keine IVDR-`RR`.
3. **Impact-Prüfung:** Keine Auswirkung auf bereits bearbeitete Gap-Bereiche, auf `RR-001` bis `RR-377` oder auf `SRC-001` bis `SRC-009`. Betroffen sind ausschließlich die Boundary-`RUL` `RUL-006` bis `RUL-008`.
4. **Freigabe:** mit diesem Eintrag; Registrierung in [SOURCES.md](SOURCES.md) Version 1.5.

Methode ([RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md)) und Controlled Vocabulary bleiben unverändert. `SRC-003` bleibt `abgeschlossen`; alle übrigen Coverage-Bereiche bleiben unverändert; `SRC-005` bis `SRC-008` bleiben `blockiert`.

### 10.35 Governance-Präzisierung der Quellenaufnahme für Primärrechtsanker

- Abschnitt 4.3 Nr. 1 knüpfte die Aufnahme einer Quelle ausschließlich an die Relevanz innerhalb eines bestehenden Themenclusters. Für Quellen, die ausschließlich als rechtsverbindlicher Primärrechtsanker einer freigegebenen Applicability-, Qualification-, Classification- oder Boundary-Logik dienen, bestand damit keine ausdrückliche Grundlage; Abschnitt 10.34 hatte dies für `SRC-010` als Auslegung dokumentiert.
- Abschnitt 4.3 Nr. 1 wird um diese zweite Alternative ergänzt. Eine solche Aufnahme begründet weder Theme-Coverage noch `RR` und autorisiert nicht automatisch eine Gap- bzw. `RR`-Extraktion.
- Keine neue Quelle, keine neue Quellenkategorie, keine Änderung der Ebenen A/B/C oder der Nutzungsarten, keine neue Aktivierung. `SRC-010` bleibt unverändert Ebene A, Nutzungsart `unterstützend`, Scope ausschließlich `SRC-010#Art.2/Nr.2`, keine IVDR-Gap-Coverage (Abschnitt 9.10). [SOURCES.md](SOURCES.md), [RR_CATALOG.yaml](RR_CATALOG.yaml) und [RUL_CATALOG.yaml](RUL_CATALOG.yaml) bleiben unverändert.


### 10.36 AI-Act-Applicability und Hochrisiko-Routing (`SRC-002`)

- Scope-wirksame Erweiterung des `RUL`-Bereichs in Abschnitt 9.6 um `SRC-002#Art.2`, `SRC-002#Art.3/Nr.1`, `SRC-002#Art.6/Abs.1a` bis `Abs.4`, die einschlägigen Fundstellen des Anhangs III, `SRC-002#Art.49/Abs.2`, `SRC-002#Art.111/Abs.2` und `SRC-002#Art.113/Buchst.c`. Fachliche Begründung: Ohne diese Knoten ist die Anwendbarkeit von `RR-001` bis `RR-115` nicht bestimmbar ([RR_APPLICABILITY_MAPPING.md](RR_APPLICABILITY_MAPPING.md) Abschnitt 4). Grundlage sind die finalen Rechercheunterlagen A bis C.
- Umsetzung als `RUL-027` bis `RUL-043` in [RUL_CATALOG.yaml](RUL_CATALOG.yaml) Version 0.2 nach [RUL_METHOD.md](RUL_METHOD.md) Version 1.1; Evidenz [DECISION_LOGIC_SRC_002_AI_ACT_APPLICABILITY.md](DECISION_LOGIC_SRC_002_AI_ACT_APPLICABILITY.md) Version 1.0. Primary Legal Anchor ausschließlich `SRC-002`, konsolidierte Fassung 27.07.2026.
- Impact-Prüfung: keine neue `RR`, keine Änderung an `RR-001` bis `RR-377`, an `RUL-001` bis `RUL-026`, an Gap-Bereichen oder an [SOURCES.md](SOURCES.md). [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.2 bindet den Block `RR-001` bis `RR-115` an das kombinierte Art.-6-Routing; lokale AI-Act-Bedingungen bleiben fail-closed.
- Art. 6 Abs. 4 und Art. 49 Abs. 2 werden nur als Routing-/Compliance-Hinweis geführt, nicht als Gap-`RR`.
- Bearbeitungsstatus der Bereiche in Abschnitt 9.6: `abgeschlossen`. `SRC-005` bis `SRC-008` bleiben `blockiert`; alle übrigen Coverage-Bereiche bleiben unverändert.

### 10.37 Systematische Normen-Coverage `SRC-005` bis `SRC-008`

- Anlass: Autorisierte Volltexte liegen als deutsche Arbeitsfassungen vor (DIN EN ISO 13485:2016-08, DIN EN ISO 14971:2020-07, DIN EN 62304 (VDE 0750-101):2016-10, DIN EN 62366-1 (VDE 0750-241-1):2021-08); der Blocker E-12 aus Abschnitt 9.8 ist damit aufgehoben. Die Volltexte und das Research-Handoff sind nicht Bestandteil des Repositorys.
- Präzisierung nach Abschnitt 9.8: Normativ geprüft wurden jeweils alle Klauseln des Anforderungskörpers einschließlich der normativen Anhänge (`SRC-005` Abschnitte 1 bis 8; `SRC-006` Abschnitte 1 bis 10; `SRC-007` Abschnitte 1 bis 9; `SRC-008` Abschnitte 1 bis 5 und Anhang C); informative Anhänge, Definitionen und Scope-Klauseln erzeugen keine `RR`. Die Einzelentscheidungen (`INCLUDE_RR`, `CROSSWALK_ONLY`, `OUT_OF_SCOPE`, `DEFINITION_ONLY`, `INFORMATIVE`) stammen aus der externen Research-Adjudikation und wurden unverändert übernommen.
- Ergebnis: 594 eingefrorene Kandidaten (209 / 107 / 185 / 93); normübergreifende Deduplizierung 1 `EXISTING_RR_SUPPORT`, 15 → 6 `CROSS_NORM_MERGE`, 576 `NEW_UNIQUE_RR`, 2 `CROSSWALK_ONLY`, 0 unresolved → **582 neue `RR`** (`RR-378` bis `RR-959`) in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.25. Themes 265 QRM, 197 SLZ, 79 GT, 39 PMM, 2 TR; Data Governance, Menschliche Aufsicht und Robustheit 0. Die Source-to-Theme-Matrix (Abschnitt 8) bleibt als Ex-ante-Erwartung unverändert.
- Impact-Prüfung: `RR-001` bis `RR-377` unverändert; `RR-157`, `RR-145` und `RR-146` werden ausschließlich über Stützungsbeziehungen in [RR_STANDARDS_MAPPING_SRC_005_008.yaml](RR_STANDARDS_MAPPING_SRC_005_008.yaml) mit `SRC-006` verknüpft. [SOURCES.md](SOURCES.md) Version 1.6 ergänzt die Arbeitsfassungen ohne neue `SRC`-ID. [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.3 ordnet alle 959 `RR` zu. Keine Änderung an Methode, Vocabulary, `RUL` oder Gap-Bereichen aus `SRC-001` bis `SRC-004`, `SRC-009` und `SRC-010`.
- Bearbeitungsstatus `SRC-005` bis `SRC-008` in Abschnitt 9.8: `abgeschlossen` (systematisch adjudiziert). Offen bleibt ausschließlich der finale Evidence-Freeze von `SRC-005` wegen `OPEN_SOURCE_PACKAGE_CHECK`; er blockiert den `RR`-Freeze nicht.
- Stopping Rule Abschnitt 11 Nr. 4 ist damit für die `RR`-Coverage erfüllt; Nr. 5 (atomare Cross-Source-Deduplizierung) ist für den Normbestand gegen `RR-001` bis `RR-377` und normübergreifend durchgeführt. Der abschließende Cross-Source- und Coverage-Audit nach Abschnitt 13 Nr. 8 steht aus.

### 10.38 Abschließender Cross-Source- und Coverage-Audit `SRC-005` bis `SRC-008`

- Abschluss-Audit nach Abschnitt 13 Nr. 8 für `SRC-005` bis `SRC-008` durchgeführt: reine Konsistenzprüfung von Katalog, Kandidatenzuordnung, Themes, Quellenbeteiligung, Coverage, Applicability und Traceability; keine erneute fachliche Adjudikation. Ergebnis **PASS**; Nachweis in [RR_EXTRACTION_STANDARDS_SRC_005_008.md](RR_EXTRACTION_STANDARDS_SRC_005_008.md) Version 1.1 Abschnitt 12.
- Redaktionelle Präzisierung von 15 kontextabhängigen Norm-`RR` (Rückverweise durch explizite Antezedenten ersetzt) in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.26; gleiche IDs, keine Bedeutungsänderung.
- Audit-Befund korrigiert: Die adjudizierte Routing-Regel `SRC-007#Abschnitt 4.3/g` (bis zur Klassifizierung gelten Klasse-C-Anforderungen) ist seit [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.4 abgebildet. Counts, Blöcke und Zuordnungen unverändert.
- Einziger verbleibender Source-Package-Punkt: `SRC-005` `OPEN_SOURCE_PACKAGE_CHECK`; er blockiert den `RR`-Arbeitsfreeze nicht. Die fehlende originale IEC-CSV für `SRC-007` und `SRC-008` ist kein Requirement-Blocker; die DIN-EN-Arbeitsfassungen sind in [SOURCES.md](SOURCES.md) dokumentiert.
- Abschnitt 13 Nr. 8 ist für den Normbestand abgeschlossen. Keine Scope-, Methoden- oder Vocabulary-Änderung.

### 10.39 Stand der Technik (Exposé Arbeitsplan Phase 1)

- Der Stand der Technik zu Assistenz- und Interaktionskonzepten sowie zu anwendungsspezifischen Regulatory-/MedTech-Lösungen ist in [../01-research/STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) Version 1.0 dokumentiert (strukturierte State-of-the-Art-/Scoping-Recherche, Stand 27.09.2026). Die Exposé-Punkte allgemeine Assistenz- und Interaktionskonzepte, anwendungsspezifische Lösungen, Vor- und Nachteile, Forschungslücke, Ableitung von Systemanforderungen sowie Begründung von Interaktions- und Architekturkonzept sind dort dokumentiert und gemappt (Abschnitt 10). Status: `abgeschlossen`.
- Der Stand der Technik ist **kein** Bestandteil des regulatorischen Extraktionskorpus: keine `SRC`-ID für Fachliteratur oder Produktquellen, keine `RR`, keine `RUL`, keine Änderung an `RR-001` bis `RR-959`, an Quellenbereichen, Stopping Rule oder Source-to-Theme-Matrix.
- Offen bleiben die Detailgestaltung des Interaktionskonzepts (Konzeptphase) und vier nicht angelegte `PROPOSED_SR_GAP` ([../01-research/STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) Abschnitt 8.3).
- Nachtrag Version 1.50: Die vier aus der Recherche identifizierten `PROPOSED_SR_GAP` sind als SR-040 bis SR-043 formal geschlossen ([../02-requirements/SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml) Version 0.3; [../01-research/STATE_OF_THE_ART.md](../01-research/STATE_OF_THE_ART.md) Version 1.1 Abschnitt 8.4). Offen bleibt nur die Detailgestaltung des Interaktionskonzepts. Der Stand-der-Technik-Block bleibt `abgeschlossen`; keine Änderung am regulatorischen Korpus.

### 10.40 Maßnahmenkatalog `RR_MEASURE` (Block 5)

- [RR_MEASURE_CATALOG.yaml](RR_MEASURE_CATALOG.yaml) Version 0.1 ordnet allen 959 `RR` einen Mapping-Status zu (457 `MAPPED`, 502 `REVIEW_REQUIRED`); 15 generische Maßnahmen mit vorgesehenen Nachweisarten, regelbasiert aus explizitem Wortlaut. Methode und Grenzen: [../07-testing/TEST_STRATEGY.md](../07-testing/TEST_STRATEGY.md) Abschnitt 4.
- Impact-Prüfung: keine neue oder geänderte `RR`, keine Änderung an Quellen, Quellenbereichen, Stopping Rule oder Applicability. Der Katalog ist Katalogdatenbestand zu SR-043, keine regulatorische Extraktion.

### 10.41 Maßnahmenkatalog `RR_MEASURE` Version 0.2 (Post-Evaluation)

- [RR_MEASURE_CATALOG.yaml](RR_MEASURE_CATALOG.yaml) Version 0.2 ordnet nach fachlicher Adjudikation der 502 offenen `RR` allen 959 `RR` eine vorgesehene Maßnahme und Nachweisart mit Mapping-Basis zu (378 `SOURCE_EXPLICIT`, 581 `PROJECT_DERIVED`); Methode: [RR_MEASURE_METHOD.md](RR_MEASURE_METHOD.md).
- Impact-Prüfung: keine neue oder geänderte `RR`, keine Änderung an Quellen, Quellenbereichen, Stopping Rule, Applicability oder `RUL`; Evaluation R1/R2 bleibt an Version 0.1 gebunden. Keine regulatorische Extraktion.

---

## 11. Stopping Rule

Die Gesamtextraktion ist nur abgeschlossen, wenn kumulativ:

1. alle freigegebenen Gap-Kernbereiche `abgeschlossen` oder fachlich begründet `ausgeschlossen` sind;
2. alle durch Trigger aktivierten ergänzenden bzw. conditional Gap-Bereiche `abgeschlossen` oder begründet `ausgeschlossen` sind;
3. kein exposé-relevanter Gap-Kernbereich mehr den Status `geplant`, `in Prüfung` oder `blockiert` trägt;
4. die erforderliche Norm-Coverage `SRC-005` bis `SRC-008` nach autorisiertem Volltextzugriff präzisiert und abgearbeitet wurde;
5. die Cross-Source-Deduplizierung auf atomarer Ebene abgeschlossen ist;
6. ein Coverage-Audit keinen ungeprüften freigegebenen Gap-Kernbereich findet;
7. alle Ausschlüsse einen nachvollziehbaren Grund besitzen;
8. alle scope-wirksamen Änderungen seit Version 1.0 dokumentiert und hinsichtlich ihrer Auswirkungen geprüft sind;
9. die im Plan vorgesehenen Themenbeiträge abgearbeitet sind — es besteht **keine** Forderung nach einer vollständigen Matrix aus acht Themenclustern und sieben Lebenszyklusphasen;
10. wobei die absolute `RR`-Anzahl **kein** Stopping Criterion ist.

`RUL`-, Qualification- und Classification-Bereiche werden separat verfolgt. Sie dürfen die Stopping Rule des `RR`-Gap-Katalogs nicht semantisch verfälschen.

---

## 12. Quantitative `RR`-Zahl

Es wird **keine** Zielzahl — etwa 30, 50 oder 100 `RR` — als Inclusion-, Splitting- oder Stopping-Kriterium festgelegt.

Die Anzahl der `RR` ist ausschließlich Ergebnis aus

- dem eingefrorenen Quellenkorpus,
- der regulatorischen Struktur der Quellen und
- der Atomizitätsregel aus `RR_EXTRACTION_METHOD.md`.

Eine spätere Mengenschätzung darf ausschließlich Projektplanungszwecken dienen und begründet keine methodische Anforderung.

---

## 13. Reihenfolge der systematischen Extraktion

1. `SRC-002` — rechtsverbindliche Core-Bereiche
2. `SRC-001` — rechtsverbindliche Core-Bereiche
3. `SRC-003` — Crosswalk und Interpretation
4. `SRC-004` — `RUL`, Qualification, Classification
5. `SRC-005` und `SRC-006` — nach Volltextzugriff
6. `SRC-007` — nach Volltextzugriff
7. `SRC-008` — nach Volltextzugriff
8. abschließender Cross-Source- und Coverage-Audit — für `SRC-005` bis `SRC-008` abgeschlossen (Abschnitt 10.38)

Erster systematischer Quellenbereich nach dem Freeze dieses Plans war **`SRC-002#Art.9`** (abgeschlossen, Abschnitt 10.5).

---

## 14. Piloten und Methodenaudit

Die beiden bestehenden Piloten — [`SRC-002` Art. 13 Abs. 1](RR_EXTRACTION_PILOT_ART13_1.md) und [`SRC-002` Art. 10 Abs. 2 Buchst. f/g](RR_EXTRACTION_PILOT_ART10_2_F_G.md) — reichen aus, um von der Pilotierung zur systematischen Extraktion überzugehen.

Sie beweisen **keine** universelle Validität der Atomizitätsmethode.

Nach dem ersten vollständig abgearbeiteten Core-Quellenbereich erfolgt ein kontrollierter Methodenaudit. Nur ein reproduzierbarer methodischer Widerspruch rechtfertigt eine Änderung der Extraktionsmethode. Eine Methodenänderung ist auf bestehende Pilot- und `RR`-Ergebnisse rückwirkend impact-zu-prüfen.

---

## Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Ex-ante-Coverage, Inclusion/Exclusion Criteria, Quellenrollen, Core-Adressatenscope, Source-to-Theme-Matrix, Quellenbereiche, Deduplizierung, Bearbeitungsstatus, Change Control und Stopping Rule vor Beginn der systematischen Extraktion eingefroren. |
| 1.1 | Scope-wirksame Change-Control-Erweiterung um `SRC-002` Art. 4a Abs. 1 als ergänzenden conditional Quellenbereich aufgrund der ausdrücklichen Verweise aus Art. 10 Abs. 1 und Abs. 6; Impact auf bestehende Art.-10-`RR` und neue Art.-10-Kandidaten geprüft. Bearbeitungsstatus von `SRC-002` Art. 10 auf `in Prüfung` aktualisiert. |
| 1.2 | Bearbeitungsstatus von `SRC-002` Art. 10 nach dokumentierter systematischer Extraktion und Katalogintegration von `in Prüfung` auf `abgeschlossen` gesetzt; Abschlussnachweis in Abschnitt 10.4 ergänzt. Keine Änderung des Coverage-Scope. `SRC-002#Art.4a/Abs.1` bleibt separat `geplant`. |
| 1.3 | Bearbeitungsstatus von `SRC-002#Art.13` vor Beginn der vollständigen systematischen `0 / 1 / n`-Prüfung von `geplant` auf `in Prüfung` gesetzt. Die bestehenden `RR-001` und `RR-002` aus dem Pilot zu Art. 13 Abs. 1 bleiben unverändert und sind bei der systematischen Prüfung zu deduplizieren. Keine Änderung des Coverage-Scope. |
| 1.4 | Bearbeitungsstatus von `SRC-002` Art. 9 nach finaler Cross-Source-Deduplizierung des Kandidaten T und Katalogisierung des Kandidaten V als `RR-063` sowie von `SRC-002#Art.13` nach vollständiger systematischer Extraktion und Katalogintegration jeweils von `in Prüfung` auf `abgeschlossen` gesetzt; Abschlussnachweise in den Abschnitten 10.5 und 10.6 ergänzt. In beiden Quellenbereichen bestehen 0 zurückgestellte und 0 ungelöste Fälle. Keine Änderung des Coverage-Scope. |
| 1.5 | Systematische Prüfung von `SRC-002` Art. 14 (Menschliche Aufsicht) gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope. |
| 1.6 | `SRC-002` Art. 14 nach vollständiger systematischer Extraktion, multilingualer Adjudikation und Katalogintegration als `RR-064` bis `RR-073` abgeschlossen; 0 ungelöste und 0 zurückgestellte Fälle. `RR-073` bleibt conditional. Der spätere Art.-26-Abgleich bleibt vorbehalten. Abschlussnachweis in Abschnitt 10.7 ergänzt; keine Änderung des Coverage-Scope. |
| 1.7 | Systematische Prüfung der freigegebenen Quellenbereiche `SRC-002#Art.15/Abs.1`, `SRC-002#Art.15/Abs.3` und `SRC-002#Art.15/Abs.4` gestartet; Bearbeitungsstatus jeweils von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope. |
| 1.8 | Die freigegebenen Gap-Coverage-Bereiche `SRC-002#Art.15/Abs.1`, `SRC-002#Art.15/Abs.3` und `SRC-002#Art.15/Abs.4` nach vollständiger systematischer Extraktion und Katalogintegration als `RR-074` bis `RR-080` abgeschlossen; 0 ungelöste und 0 zurückgestellte Fälle. Die eigenständige Cybersecurity-Komponente aus Abs. 1 verbleibt aufgrund der bestehenden Gap-Themen-Abgrenzung außerhalb des RR-Katalogs; spätere Cross-Article-Prüfungen bleiben vorbehalten. Abschlussnachweis in Abschnitt 10.8 ergänzt; keine Änderung des Coverage-Scope. |
| 1.9 | Systematische Prüfung der freigegebenen Quellenbereiche von `SRC-002` Art. 17 Abs. 1 und Abs. 2 gestartet; die Kern- und die ergänzenden Teilbereiche wurden von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope. |
| 1.10 | Die freigegebenen Bereiche von `SRC-002` Art. 17 Abs. 1 und Abs. 2 nach vollständiger systematischer Extraktion und Katalogintegration als `RR-081` bis `RR-104` abgeschlossen; 23 reguläre und eine konditionale Anforderung, 0 ungelöste und 0 zurückgestellte Fälle. Art. 17 Abs. 1 Buchst. i bleibt außerhalb der aktiven Gap-Coverage, Abs. 3 bleibt Interplay ohne eigene `RR`, Abs. 4 außerhalb Scope. Der spätere Abgleich von `RR-096` bis `RR-098` gegen Art. 72 bleibt vorbehalten. Abschlussnachweis in Abschnitt 10.9 ergänzt; keine Änderung des Coverage-Scope. |
| 1.11 | Systematische Prüfung von `SRC-002#Art.72` (Post-Market-Monitoring) gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope. |
| 1.12 | `SRC-002` Art. 72 nach vollständiger systematischer Extraktion und Katalogintegration als `RR-105` bis `RR-115` abgeschlossen; 8 reguläre und 3 konditionale Anforderungen, 0 ungelöste und 0 zurückgestellte Fälle, 0 Cross-Source-Deduplizierungen. `RR-096` bis `RR-098` bleiben nach dem dokumentierten Art.-17/Art.-72-Abgleich unverändert. Art. 72 Abs. 2 Satz 3 ist eine Scope-Ausnahme ohne eigene `RR`, Abs. 3 Satz 3 eine institutionelle Kommissionspflicht ohne Anbieter-`RR`, Abs. 4 UAbs. 2 bleibt außerhalb Scope. Die Integrationswahl nach Abs. 4 UAbs. 1 bleibt optional. Abschlussnachweis in Abschnitt 10.10 ergänzt; keine Änderung des Coverage-Scope. |
| 1.13 | Systematische Prüfung des freigegebenen conditional Quellenbereichs `SRC-002#Art.4a/Abs.1` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope; Art. 4a Abs. 2 wurde nicht aktiviert. |
| 1.14 | `SRC-002#Art.4a/Abs.1` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen. 0 neue Gap-`RR` innerhalb des kontrollierten Themen-Scope, 11 atomare regulatorische Pflichten außerhalb des Gap-Themen-Scope, 0 ungelöste und 0 zurückgestellte Fälle, 0 Cross-Source-Deduplizierungen. Die Out-of-Scope-Einordnung beruht auf der bestehenden Datenschutz-/DSGVO-Scope-Abgrenzung und ist keine Aussage über regulatorische Irrelevanz. Art. 4a Abs. 2 wurde nicht bearbeitet; `RR-003` bis `RR-006` bleiben unverändert. Abschlussnachweis in Abschnitt 10.11 ergänzt. |
| 1.15 | Die conditional Deployer-Bereiche `SRC-002#Art.26/Abs.2`, `SRC-002#Art.26/Abs.4` und `SRC-002#Art.26/Abs.5` wurden nach Actor-Scope-Prüfung gemäß Abschnitt 1.2 und Exclusion Criterion E-10 nicht aktiviert und von `geplant` auf `ausgeschlossen` gesetzt. Die Deployer-Perspektive ist im aktuellen genehmigten Gap- und Fallstudien-Scope nicht aktiviert; Core-Adressat von `SRC-002` bleibt der Anbieter. Dies ist keine Aussage über regulatorische Irrelevanz von Art. 26. Eine spätere Aktivierung würde eine formelle Coverage Change Control erfordern. Change-Control-Nachweis mit Impact-Prüfung in Abschnitt 10.12. |
| 1.16 | Systematische Prüfung der vier freigegebenen MDR-Art.-10-Bereiche gestartet: `SRC-001#Art.10/Abs.2`, `SRC-001#Art.10/Abs.9` — Einleitung sowie Buchst. c, d, e, l, m, `SRC-001#Art.10/Abs.9/Buchst.g` und `SRC-001#Art.10/Abs.9/Buchst.i` jeweils von `geplant` auf `in Prüfung` gesetzt. Keine Scope-Änderung; alle übrigen Felder und Coverage-Bereiche unverändert. Noch keine Ergebnisbehauptung, keine `RR`-Zuweisung und keine Katalogänderung. |
| 1.17 | Die vier freigegebenen MDR-Art.-10-Coverage-Bereiche wurden nach vollständiger systematischer Prüfung von `in Prüfung` auf `abgeschlossen` gesetzt. Grundlage ist [RR_EXTRACTION_MDR_ART10.md](RR_EXTRACTION_MDR_ART10.md) Version 1.1; die 27 finalen Gap-`RR` sind als `RR-116` bis `RR-142` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.12 integriert. Ergebnis: 5 reguläre Anforderungen, 22 Anforderungen mit konditionaler Anwendbarkeit, 0 ungelöste Fälle, 0 zurückgestellte Fälle, 0 Cross-Regulation-Deduplizierungen und 0 Out-of-Scope-Atome im final adjudizierten aktiven Bereich. Die späteren eigenständigen Abgleiche mit `SRC-001#Anh.I/Nr.3` und `SRC-001#Art.83` bleiben vorgemerkt und blockieren den Abschluss nicht. Keine Scope-Erweiterung und keine Katalogänderung. |
| 1.18 | Systematische Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.3` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen. Der in Abschnitt 10.13 vorgemerkte spätere atomare Abgleich mit `RR-116` bis `RR-119` und `RR-133` bleibt bestehen; er erfolgt erst nach vollständiger Atomisierung des Quellenbereichs. Noch keine Extraktions-, Atomisierungs- oder Deduplizierungsentscheidung und keine Ergebnisbehauptung. |
| 1.19 | `SRC-001#Anh.I/Nr.3` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen. 11 neue Gap-`RR` wurden als `RR-143` bis `RR-153` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.13 integriert, davon 10 reguläre Anforderungen und eine Anforderung mit konditionaler Anwendbarkeit. Die vier Top-Level-Sollzustände aus Satz 1 wurden vollständig gegen `RR-116` bis `RR-119` dedupliziert. Ergebnis: 0 ungelöste Fälle, 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. `SRC-001#Anh.I/Nr.4` und `SRC-001#Art.83` wurden nicht systematisch extrahiert. Keine Scope-Erweiterung und keine Katalogänderung. |
| 1.20 | Systematische Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.4` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen. Die in Abschnitt 10.14 dokumentierten Beziehungen zu `RR-151` und `RR-153`, die `SRC-001#Anh.I/Nr.4` als Supplementary-Kontext führen, bleiben für den späteren atomaren Abgleich vorgemerkt; dieser erfolgt erst nach vollständiger `0 / 1 / n`-Atomisierung des Quellenbereichs. Noch keine Extraktions-, Atomizitäts- oder Deduplizierungsentscheidung und keine Ergebnisbehauptung. |
| 1.21 | `SRC-001#Anh.I/Nr.4` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen. 9 neue Gap-`RR` wurden als `RR-154` bis `RR-162` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.14 integriert, davon 7 reguläre Anforderungen und 2 Anforderungen mit konditionaler Anwendbarkeit. Ergebnis: 0 MDR-interne Deduplizierungen, 0 ungelöste Fälle, 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. `SRC-001#Anh.I/Nr.2` wurde ausschließlich als Supplementary-Kontext verwendet und nicht systematisch extrahiert. Keine Scope-Erweiterung und keine Katalogänderung. |
| 1.22 | Systematische Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.5` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen. Noch keine Extraktions-, Atomizitäts-, Theme-, Lifecycle- oder Deduplizierungsentscheidung und keine Ergebnisbehauptung. `SRC-008` bleibt unverändert; ein Norm-Crosswalk erfolgt nicht in diesem Schritt. |
| 1.23 | `SRC-001#Anh.I/Nr.5` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen. 2 neue Gap-`RR` wurden als `RR-163` und `RR-164` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.15 integriert; beide Anforderungen sind regulär. Ergebnis: 0 MDR-interne Deduplizierungen, 0 ungelöste Fälle, 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. Die multilinguale Abweichung zur Position der Modalitätsklausel in Buchst. b wurde vollständig adjudiziert und erzeugt keine verbleibende Unsicherheit. `SRC-001#Anh.I/Nr.2`, `SRC-001#Anh.I/Nr.22`, `SRC-001#Anh.I/Nr.23.1` und IEC 62366-1 wurden nicht systematisch extrahiert. Keine Scope-Erweiterung und keine Katalogänderung. |
| 1.24 | Systematische Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.17.1` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen; `SRC-001#Anh.I/Nr.17.2` bleibt separat `geplant`, weil beide Quellenbereiche eigenständig geprüft werden. Der Themencluster `Robustheit` wird nicht erweitert, und `SRC-001#Anh.I/Nr.17.4` bleibt außerhalb des initialen Gap-Coverage. `SRC-007` bleibt unverändert; ein Norm-Crosswalk erfolgt nicht in diesem Schritt. Noch keine Extraktions-, Atomizitäts-, Theme-, Lifecycle-, Deduplizierungs- oder Cross-Regulation-Entscheidung und keine Ergebnisbehauptung. |
| 1.25 | `SRC-001#Anh.I/Nr.17.1` nach vollständiger systematischer `0 / 1 / n`-Prüfung und gezielter Nachadjudikation abgeschlossen. 4 neue Gap-`RR` wurden als `RR-165` bis `RR-168` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.16 integriert; alle vier sind regulär, 0 conditional. Satz 1 ergibt drei getrennte Sollzustände für Wiederholbarkeit, Zuverlässigkeit und Leistung entsprechend der Zweckbestimmung; Satz 2 ergibt eine gemeinsame reguläre Single-Fault-Anforderung mit erhaltener Oder-Struktur. Die temporäre Split-Variante `M17_1-E` wurde vor permanenter Katalogisierung verworfen und erhält keine permanente Identifikation. Ergebnis: 0 MDR-interne Deduplizierungen, 0 ungelöste Fälle, 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. `SRC-001#Anh.I/Nr.17.2`, `SRC-001#Anh.I/Nr.17.4` und IEC 62304 wurden nicht systematisch extrahiert. Keine Scope-Erweiterung und keine Katalogänderung. |
| 1.26 | Systematische Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.17.2` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen; `SRC-001#Anh.I/Nr.17.1` bleibt abgeschlossen, und `RR-165` bis `RR-168` bleiben unverändert. Noch keine Extraktions-, Atomizitäts-, Theme-, Lifecycle-, Deduplizierungs- oder Cross-Regulation-Entscheidung; der ex-ante-Wert `Software-Lebenszyklus` bleibt Coverage-Erwartung nach Abschnitt 7 und ist keine finale Theme-Entscheidung für spätere Atome. Es wurden keine Inhalte aus `SRC-001#Anh.I/Nr.17.4`, IEC 62304 oder ISO 14971 vorgezogen, und der Themencluster `Robustheit` wurde nicht zu einem Cybersecurity-Cluster erweitert. Keine Ergebnisbehauptung. |
| 1.27 | `SRC-001#Anh.I/Nr.17.2` nach vollständiger systematischer `0 / 1 / n`-Prüfung sowie Lifecycle- und Multilingual-Nachadjudikation abgeschlossen. 5 neue Gap-`RR` wurden als `RR-169` bis `RR-173` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.17 integriert; alle fünf sind regulär. Atomisiert wurden Stand der Technik, Software-Lebenszyklus, Risikomanagement einschließlich Informationssicherheit, Verifizierung und Validierung. Die Informationssicherheit bleibt Bestandteil von `RR-171` und erzeugt keine separate Security-`RR`. Die Sprachfassungsdivergenz zum Software-Lebenszyklus wurde vollständig adjudiziert. Alle fünf `RR` tragen final die Lebenszyklusphasen `Entwicklung und Realisierung` sowie `Änderung und Wartung`. Ergebnis: 0 MDR-interne Deduplizierungen, 0 ungelöste Fälle, 0 zurückgestellte Fälle, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. `SRC-001#Anh.I/Nr.17.4`, IEC 62304 und ISO 14971 wurden nicht systematisch extrahiert. Keine Scope-Erweiterung und keine Katalogänderung. |
| 1.28 | Systematische Prüfung des bereits freigegebenen ergänzenden, conditional MDR-Bereichs `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` gestartet; Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Der bestehende Coverage-Trigger „vorgesehene Laienanwendung" bleibt unverändert; es erfolgt keine Änderung des Coverage-Scope und keine weitere Aktivierung. Noch keine Extraktions-, Atomizitäts-, Theme-, Lifecycle-, Deduplizierungs-, Applicability- oder Regelentscheidung; insbesondere ist offen, wie der äußere Anwendbarkeitsvorbehalt und die inneren Bedingungen einzelner Anforderungen später getrennt adjudiziert werden. `SRC-001#Anh.I/Nr.5` bleibt abgeschlossen und `RR-163` sowie `RR-164` bleiben unverändert; `SRC-001#Anh.I/Nr.23.1` bleibt separat `geplant`. Es wurden keine Norminhalte aus IEC 62366-1 vorgezogen. Keine Ergebnisbehauptung. |
| 1.29 | Governance-Change-Control zur Quellenaufnahme (Abschnitt 10.19): Abschnitte 4.1 bis 4.6 ergänzt. Die Quellenebenen A, B und C bleiben erhalten und wurden allgemein definiert. Eine davon unabhängige Nutzungsart `systematisch` / `unterstützend` / `triggerbasiert` wurde eingeführt; der Dokumenttyp allein begründet keine Requirement-Extraktion. Aufnahmevoraussetzungen für weitere Quellen, Scope-Regel für horizontale Quellen, Triggerprinzip für produktspezifische Quellen, Volltext- und Source-Fidelity-Regel ohne neuen Status, Trennung von fachlicher Relevanz und MDR-Harmonisierungsstatus ohne neues Schemafeld sowie Ausschluss unveröffentlichter Normungsprojekte vom Quellenkorpus festgelegt. Keine neue `SRC`-ID, kein neuer Quellenbereich, keine Status- oder Prioritätsänderung; `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` bleibt `in Prüfung`. Keine Änderung bestehender `RR`. |
| 1.30 | `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen (Abschnitt 10.20). 10 normative Kandidatenatome geprüft; 9 neue Gap-`RR` als `RR-174` bis `RR-182` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.18 integriert; 1 Out-of-Scope-Atom. Alle 9 `RR` stehen unter dem äußeren Trigger „vorgesehene Laienanwendung", `RR-180` bis `RR-182` sind zusätzlich inner conditional. Themencluster jeweils `Gebrauchstauglichkeit`. Abgleich mit `RR-163` und `RR-164` abgeschlossen: 0 vollständige Deduplizierungen, beide unverändert. 0 ungelöste und 0 zurückgestellte Fälle. `SRC-001#Anh.I/Nr.23.1` bleibt `geplant`; keine Norminhalte vorweggenommen. Priorität, Trigger und erwartetes Themencluster des Bereichs unverändert; keine Scope-Änderung. |
| 1.31 | Systematische Prüfung des bereits freigegebenen MDR-Kernbereichs `SRC-001#Anh.I/Nr.23.1` gestartet (Abschnitt 10.21); Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Priorität, erwartete Themencluster und Trigger unverändert; der vorgemerkte spätere Abgleich insbesondere mit `RR-164` bleibt bestehen. Noch keine Extraktions-, Atomizitäts-, Theme-, Lifecycle-, Conditionality-, Deduplizierungs- oder Locator-Entscheidung und keine Ergebnisbehauptung. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen. |
| 1.32 | `SRC-001#Anh.I/Nr.23.1` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen (Abschnitt 10.22). 27 potenzielle Einheiten geprüft; 22 neue Gap-`RR` als `RR-183` bis `RR-204` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.19 integriert, davon 13 regulär und 9 conditional; 5 0-`RR`-Entscheidungen. Themes: 13 × Transparenz, 9 × Gebrauchstauglichkeit. Abgleich mit `RR-164`, `RR-175` und `RR-176` abgeschlossen, zusätzliche Abgleiche mit `RR-160` und `RR-162` dokumentiert: 0 vollständige Deduplizierungen. SOURCE_DEPENDENCY bei `RR-200` (Durchführungsverordnung (EU) 2021/2226, nicht registriert) und für die Operationalisierung von `RR-203` und `RR-204`. 0 ungelöste und 0 zurückgestellte Fälle. `SRC-001#Anh.I/Nr.23.4` bleibt `geplant`; Nr. 23.2 bis 23.4 und Normen nicht vorweggenommen. Priorität, Trigger und erwartete Themencluster unverändert; keine Scope-Änderung. |
| 1.33 | Scope-wirksame Change Control (Abschnitt 10.23): `SRC-009` (Durchführungsverordnung (EU) 2021/2226, konsolidierte Fassung 16.07.2025) als Ebene-A-Quelle mit Nutzungsart `triggerbasiert` und globalem Trigger „elektronische Gebrauchsanweisung für MDR-Medizinproduktesoftware" aufgenommen; Anlass ist die SOURCE_DEPENDENCY von `RR-200`. Neuer Abschnitt 9.9: `SRC-009#Art.3` bis `Art.7` und `Art.9` zur systematischen Prüfung freigegeben und auf `in Prüfung` gesetzt; Art. 1, Art. 2, Art. 10 und Anhang Supporting Context; Art. 8 gestrichen, Art. 11 ohne Gap-Sollzustand. Ebene-A-Zeile in Abschnitt 4 und Source-to-Theme-Matrix in Abschnitt 8 um `SRC-009` ergänzt. DSGVO, mitgliedstaatliche Sprachfestlegung und Verordnung (EU) Nr. 207/2012 nur als Abhängigkeiten ohne Registrierung dokumentiert. Keine Extraktion, keine neue `RR`, `RR-200` und alle übrigen `RR` unverändert. |
| 1.34 | `SRC-009#Art.3` bis `Art.7` und `Art.9` nach vollständiger systematischer `0 / 1 / n`-Prüfung abgeschlossen (Abschnitt 10.24). 67 geprüfte aktuelle potenzielle Einheiten; 61 neue Gap-`RR` als `RR-205` bis `RR-265` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.20 integriert, davon 0 regulär und 61 conditional; 6 0-`RR`-Entscheidungen. Themes: 17 Qualitäts- und Risikomanagement, 31 Transparenz, 7 Gebrauchstauglichkeit, 6 Robustheit. Source Dependencies (Sprachfestlegung, DSGVO außerhalb Scope, MDR-UDI innerhalb `SRC-001`) dokumentiert. Art. 8 und gestrichene Unterpunkte nicht extrahiert. 0 ungelöste und 0 zurückgestellte Fälle; 0 vollständige Deduplizierungen; `RR-200` unverändert. Kein Import weiterer Quellen; Priorität, Trigger und erwartete Themencluster unverändert. |
| 1.35 | Systematische Prüfung des bereits freigegebenen, begrenzten Quellenbereichs `SRC-001#Anh.I/Nr.23.4` gestartet (Abschnitt 10.25); Bearbeitungsstatus von `geplant` auf `in Prüfung` gesetzt. Geprüft werden ausschließlich Buchst. b, e, f, g, h, j, k, s und ab; übrige Buchstaben nicht aktiviert. Priorität, erwartete Themencluster und Trigger unverändert. Noch keine Extraktions- oder sonstige fachliche Entscheidung, keine `RR` und keine Ergebnisbehauptung. Keine Änderung des Coverage-Scope und keine weiteren Aktivierungen. |
| 1.36 | Begrenzter Quellenbereich `SRC-001#Anh.I/Nr.23.4` (ausschließlich Buchst. b, e, f, g, h, j, k, s, ab) nach systematischer `0 / 1 / n`-Prüfung abgeschlossen (Abschnitt 10.26). 35 potenzielle Einheiten; 30 neue Gap-`RR` als `RR-266` bis `RR-295` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.22 integriert, davon 9 regulär und 21 conditional; 5 0-`RR`-Entscheidungen (OUT_OF_SCOPE). Theme 30 × Transparenz. 0 ungelöste Fälle, 0 vollständige Deduplizierungen; bestehende `RR` unverändert. Übrige Buchstaben von Nr. 23.4 nicht aktiviert; keine Scope-Änderung. |
| 1.37 | MDR-PMS-Block `SRC-001#Art.83`, `SRC-001#Art.84` und `SRC-001#Anh.III/Abschn.1` zur systematischen `0 / 1 / n`-Prüfung eröffnet (Abschnitt 10.27); Bearbeitungsstatus jeweils von `geplant` auf `in Prüfung` gesetzt. Prioritäten, Cluster, Trigger, Scope-Begründungen und vorgemerkte Abgleiche mit `RR-135` bis `RR-137` und `RR-152` unverändert. Keine Extraktion, keine `RR`, keine Scope-Änderung. |
| 1.38 | MDR-PMS-Block `SRC-001#Art.83`, `SRC-001#Art.84` und `SRC-001#Anh.III/Abschn.1` nach systematischer `0 / 1 / n`-Prüfung abgeschlossen (Abschnitt 10.28). 61 potenzielle Einheiten; 57 neue Gap-`RR` als `RR-296` bis `RR-352` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.23 integriert, davon 49 regulär und 8 conditional; 4 0-`RR`-Entscheidungen. Theme 57 × Post-Market-Monitoring. Abgleiche mit `RR-135` bis `RR-137` und `RR-152` durchgeführt; 0 vollständige Deduplizierungen; bestehende `RR` unverändert. `SRC-001#Art.85` und `SRC-001#Art.86` bleiben `geplant`; keine Scope-Änderung. |
| 1.39 | Klassenspezifischer MDR-PMS-Berichtsblock `SRC-001#Art.85` (Klasse I) und `SRC-001#Art.86` (Klasse IIa, IIb oder III) zur systematischen `0 / 1 / n`-Prüfung eröffnet (Abschnitt 10.29); Bearbeitungsstatus jeweils von `geplant` auf `in Prüfung` gesetzt. Prioritäten, Cluster, Trigger und Scope-Begründungen unverändert. Keine Extraktion, keine `RR`, keine Scope-Änderung. |
| 1.40 | Klassenspezifischer MDR-PMS-Berichtsblock `SRC-001#Art.85` und `SRC-001#Art.86` nach systematischer `0 / 1 / n`-Prüfung abgeschlossen (Abschnitt 10.30). 28 potenzielle Einheiten; 25 neue Gap-`RR` als `RR-353` bis `RR-377` in [RR_CATALOG.yaml](RR_CATALOG.yaml) Version 0.24 integriert, alle conditional; 3 0-`RR`-Entscheidungen. Theme 25 × Post-Market-Monitoring, Lifecycle 25 × Post-Market-Überwachung. 0 ungelöste Fälle, 0 vollständige Deduplizierungen; bestehende `RR` unverändert. Keine Scope-Änderung. |
| 1.41 | Prüfung von `SRC-003` (AIB 2025-1 / MDCG 2025-6) als Interplay-, Crosswalk- und Interpretationsquelle gegen den stabilisierten Rechtsakt-Korpus eröffnet (Abschnitt 10.31); Bearbeitungsstatus `in Prüfung` in Abschnitt 9.7 ergänzt. Quellenrolle Ebene B unverändert; keine Gleichstellung mit rechtsverbindlichen Anforderungen; keine `RR`, keine Extraktion, keine Scope-Änderung. |
| 1.42 | Crosswalk- und Interpretationsprüfung von `SRC-003` (AIB 2025-1 / MDCG 2025-6) abgeschlossen (Abschnitt 10.32); Bearbeitungsstatus in Abschnitt 9.7 auf `abgeschlossen` gesetzt. Evidenz [CROSSWALK_SRC_003_MDR_AI_ACT.md](CROSSWALK_SRC_003_MDR_AI_ACT.md) Version 1.0: 25 Crosswalk-Einträge, 0 neue `RR`, 0 geänderte `RR`, 0 Deduplizierungen, 0 blockierende Unresolveds. Gemeinsame Evidenz ≠ normative Deduplizierung; Q2/Q4, Q27/Q28, Q31 und Q34 als `STALE/SUPERSEDED_GUIDANCE` gegenüber `SRC-002` dokumentiert; aktuelles Primärrecht hat Vorrang. `SOURCES.md` 1.4 nur Lokator `SRC-003#Einleitung`. Quellenrolle Ebene B, Methode, Vocabulary und Scope unverändert. |
| 1.43 | Prüfung von `SRC-004` (MDCG 2019-11 Rev. 1) als Ebene-B-Guidance für Software-Qualifikation, MDR/IVDR-Abgrenzung, MDSW-Klassifikation, MDR Anhang VIII Regel 11 und spätere `RUL`-/Entscheidungslogik eröffnet (Abschnitt 10.33); Bearbeitungsstatus `in Prüfung` in Abschnitt 9.7 ergänzt. Keine eigenständige Gap-`RR`-Quelle; keine `RR`, keine `RUL`, keine Extraktion; Rollen-, Scope- und übrige Coverage-Bereiche unverändert. |
| 1.44 | `SRC-004` (MDCG 2019-11 Rev. 1) als Guidance-Schicht der regelbasierten Entscheidungslogik abgeschlossen (Abschnitt 10.34); Bearbeitungsstatus in Abschnitt 9.7 auf `abgeschlossen` gesetzt. Qualifikation, MDR/IVDR-Abgrenzung, Regel 11 und zusätzliche MDR-Regeln, Module und Change Reassessment analysiert; 26 `RUL` (`RUL-001` bis `RUL-026`) in `RUL_CATALOG.yaml` 0.1 nach `RUL_METHOD.md` 1.0 angelegt; 0 neue `RR`. Scope-wirksame Aufnahme von `SRC-010` (IVDR, konsolidierte Fassung 10.01.2025) als Ebene-A-Quelle mit Nutzungsart `unterstützend`, ausschließlich `SRC-010#Art.2/Nr.2` als Primärrechtsanker der Abgrenzungs-`RUL` (neuer Abschnitt 9.10; Quellenrollentabelle Abschnitt 4 und Source-to-Theme-Matrix Abschnitt 8 ergänzt). Keine IVDR-Gap-Coverage; übrige Coverage-Bereiche unverändert. |
| 1.45 | Governance-Präzisierung (Abschnitt 10.35): Abschnitt 4.3 Nr. 1 lässt die Aufnahme einer Quelle auch dann zu, wenn sie für eine freigegebene regelbasierte Applicability-, Qualification-, Classification- oder Boundary-Logik als notwendiger Primärrechtsanker benötigt wird; eine solche Aufnahme autorisiert keine Gap-/`RR`-Extraktion. Keine neue Quelle oder Quellenkategorie, keine Änderung der Ebenen, Nutzungsarten oder Coverage-Bereiche; `SRC-010` unverändert. |
| 1.46 | Change Control 10.36: `RUL`-Bereich `SRC-002` in Abschnitt 9.6 um Art. 2, Art. 3 Nr. 1, Art. 6 Abs. 1a bis 4, Anhang III, Art. 49 Abs. 2, Art. 111 Abs. 2 und Art. 113 Buchst. c erweitert und als `RUL-027` bis `RUL-043` umgesetzt (Status `abgeschlossen`); Hinweis „keine `RUL`-ID“ entsprechend fortgeschrieben. Keine neue `RR`, keine Gap-Coverage-Änderung, keine Source-Änderung. |
| 1.47 | Change Control 10.37: Normen `SRC-005` bis `SRC-008` nach Vorliegen autorisierter Arbeitsfassungen systematisch adjudiziert und integriert; Bearbeitungsstatus in Abschnitt 9.8 auf `abgeschlossen` gesetzt. 594 Kandidaten → 582 neue `RR` (`RR-378` bis `RR-959`), Evidenz [RR_EXTRACTION_STANDARDS_SRC_005_008.md](RR_EXTRACTION_STANDARDS_SRC_005_008.md) Version 1.0. `SRC-005`: `OPEN_SOURCE_PACKAGE_CHECK` für den finalen Evidence-Freeze offen. Ex-ante-Matrix, Methode und Vocabulary unverändert. |
| 1.48 | Change Control 10.38: abschließender Cross-Source- und Coverage-Audit für `SRC-005` bis `SRC-008` PASS; Abschnitt 13 Nr. 8 für den Normbestand abgeschlossen. 15 Norm-`RR` redaktionell präzisiert (`RR_CATALOG.yaml` 0.26); Regel `SRC-007#Abschnitt 4.3/g` in `RR_APPLICABILITY.yaml` 0.4 abgebildet. Einziger offener Source-Package-Punkt bleibt `SRC-005` `OPEN_SOURCE_PACKAGE_CHECK`. |
| 1.49 | Abschnitt 10.39: Stand der Technik (Exposé Arbeitsplan Phase 1) in `docs/01-research/STATE_OF_THE_ART.md` dokumentiert und als `abgeschlossen` vermerkt; keine Änderung am regulatorischen Korpus. |
| 1.50 | Abschnitt 10.39 ergänzt: vier `PROPOSED_SR_GAP` als SR-040 bis SR-043 geschlossen; keine Änderung am regulatorischen Korpus. |
| 1.51 | Abschnitt 10.40: Maßnahmenkatalog `RR_MEASURE` (Mapping-Status aller 959 `RR`) dokumentiert; keine Änderung am regulatorischen Korpus. |
| 1.52 | Ausschließlich redaktionell: Abschnitt 13 nennt `SRC-002#Art.9` als abgeschlossenen ersten Bereich statt als noch nicht bearbeiteten. Keine Änderung an Korpus, Status, Methode, Stopping Rule oder Quellen. |
| 1.53 | Abschnitt 10.41: Maßnahmenkatalog `RR_MEASURE` 0.2 (959 zugeordnet, Mapping-Basis) dokumentiert; keine Änderung am regulatorischen Korpus. |
