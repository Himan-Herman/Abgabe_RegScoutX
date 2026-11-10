# Stand der Technik: Assistenz- und Interaktionskonzepte sowie Regulatory-/MedTech-Lösungen

Version 1.5 · Status: aktiv · Recherchestand: 27.08.2026

Dieses Dokument ist die führende Dokumentation des Stands der Technik nach [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 3 und Arbeitsplan-Phase 1. Es leitet daraus Design Implications ab und bildet sie auf die bestehenden Systemanforderungen ([SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml)) und die Architektur ([ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md)) ab.

Grundlage war eine vorliegende Rechercheausgabe vom 27.08.2026.

**Kennungen:** Literatur (`L01` bis `L18`), Produktquellen (`P01` bis `P13`) und Design Implications (`DI-001` bis `DI-012`) sind lokale Kennungen dieses Dokuments und keine projektweiten ID-Klassen. Fachliteratur erhält **keine** `SRC`-ID; `SRC` bezeichnet im Projekt ausschließlich die regulatorischen Quellen aus [SOURCES.md](../03-regulatory/SOURCES.md).

**Evidenzarten** (Kennzeichnung in Abschnitt 8): `E` empirische Evidenz · `T` theoretische Grundlage · `D` Designinferenz (begründete Übertragung auf RegScoutX) · `H` Hersteller-/Anbieterangabe · `S` eigene Synthese.

---

## 1. Methodik der Recherche

| Merkmal | Angabe |
| --- | --- |
| Recherchezeitpunkt | 27.08.2026 |
| Art | **strukturierte State-of-the-Art-/Scoping-Recherche**; kein vollständiger PRISMA-Systematic-Review (kein dokumentierter Scopus-/Web-of-Science-Deduplizierungs- und Screeningprozess) |
| Stränge | (1) wissenschaftliche Literatur zu HCI, adaptiven Fragebögen, Conversational Interfaces, Decision Support, regelbasierter Compliance und Traceability; (2) aktuelle offizielle Produkt- und Dokumentationsseiten relevanter Regulatory-/MedTech-Systeme |
| Suchräume | PubMed/PMC, Oxford Academic/JAMIA, ScienceDirect, Springer Nature, Wiley, SAGE, ACM-/IEEE-Metadaten, einschlägige Hochschulrepositorien, ISO; offizielle Hersteller- und Produktdokumentation |
| Suchbegriffe (Auswahl laut Research) | `adaptive questionnaire`, `dynamic questionnaire branching logic`, `web form usability error prevention`, `paging versus scrolling`, `wizard interface`, `conversational survey chatbot web form`, `decision support explainability`, `rule based compliance`, `production rule legal compliance`, `business process compliance checker`, `regulatory requirements engineering`, `requirements traceability medical device software`, `medical device regulatory information management`, `MDR compliance software`, `EU AI Act medical device compliance`, `SaMD regulatory compliance`, `MDR AI Act gap analysis`, `regulatory evidence mapping`, `regulatory source traceability` |
| Einschluss | nachvollziehbare wissenschaftliche Publikationsbasis und direkte Relevanz zu mindestens einem Untersuchungsaspekt; ältere Arbeiten nur, wenn sie ein grundlegendes Konzept begründen (Sweller, Taylor); Produktfunktionen nur, wenn auf aktueller offizieller Hersteller- oder Produktdokumentation explizit beschrieben |
| Ausschluss | SEO-Inhalte, generische Beratungsartikel, bloße Marktübersichten, nicht nachvollziehbare Drittanbieterbehauptungen; Marketingangaben zu Geschwindigkeit, Kostenersparnis oder Produktqualität werden nicht als nachgewiesene Wirkung übernommen |
| Grenzen | siehe Abschnitt 11 |

Bibliographische Angaben stützen sich vorrangig auf DOI bzw. Verlags-, PubMed-, ACM-/IEEE- oder institutionelle Quellen; ResearchGate wird nicht als bibliographische Quelle geführt.

---

## 2. Allgemeine Assistenz- und Interaktionskonzepte

### 2.1 Klassische Formulare

Formulare eignen sich, wenn Eingaben typisiert, vollständig und reproduzierbar erhoben werden müssen: Felder, Antworttypen und Validierungsregeln gelten für alle Nutzer identisch und sind protokollierbar. Bargas-Avila et al. zeigten experimentell (166 Teilnehmende), dass vorab kommunizierte Formatregeln Fehler und notwendige Eingabeversuche signifikant reduzieren; eine nur nachträgliche Fehlermeldung war ungünstiger [L01] (`E`). ISO 9241-110 nennt technologieunabhängige Interaktionsprinzipien, u. a. Aufgabenangemessenheit, Selbstbeschreibungsfähigkeit, Erwartungskonformität, Lernförderlichkeit, Steuerbarkeit und Robustheit gegen Benutzungsfehler [L18] (Norm). Ein vollständig statisches Formular zeigt jedoch auch fallirrelevante Fragen; die Cognitive-Load-Theorie liefert hierfür einen allgemeinen theoretischen Hintergrund, aber keinen direkten Nachweis für Regulatory-Software [L03] (`T`).

### 2.2 Mehrstufige Wizards

Ein Wizard ist ein sequenziell segmentiertes Formular mit logisch geordneten Schritten, häufig mit Fortschrittsanzeige, Zwischenspeicherung und feldbezogener Validierung. Ein genereller Vorteil des Aufteilens auf viele Seiten ist nicht belegt: Peytchev et al. verglichen Paging und Scrolling (über 10.000 Antwortende) und berichten Vor- und Nachteile beider Formen, abhängig u. a. von Fragebogenstruktur und Skip Patterns [L02] (`E`). Tragfähig ist daher nur die Begründung, dass eine fachlich strukturierte Segmentierung einen umfangreichen Prozess kontrollierbar machen kann, sofern Übersicht, Rücknavigation und getroffene Entscheidungen erhalten bleiben (`D`).

### 2.3 Adaptive und dynamische Fragebögen

Taylor beschreibt adaptive Fragebögen als hierarchisch organisierte Instrumente, die über *contingency branching* und automatisierte Fragenauswahl auf relevante Sachverhalte fokussieren [L04] (`T`). DQueST nutzt dynamische, aus strukturierten Kriterien und bisherigen Antworten abgeleitete Fragen, um Informationsüberlastung bei der Studiensuche zu verringern [L06] (`E`). Neururer, Hofer und Göbel entwickelten ein IT-gestütztes Werkzeug, das SOPs eines Biobanksystems gegen internationale Guidelines bewertet und Abweichungen identifiziert – ohne MDR- oder AI-Act-Bezug, aber als methodischer Analogiefall einer guideline-basierten Gap-Bewertung [L05] (`E`, Analogie). Vorteil für bedingte regulatorische Sachverhalte: irrelevante Teilbäume können ausgeblendet werden, ohne die Entscheidungslogik aufzugeben; „progressive disclosure“ ist hier als konkrete Umsetzung bedingungsabhängiger Darstellung zu verstehen, nicht als isoliert bewiesene Universalregel. Gegenpunkt: Ein falscher Branching-Trigger kann einen ganzen Anforderungszweig unsichtbar machen; Branching-Regeln müssen daher versioniert, testbar und nachvollziehbar sein (`D`).

### 2.4 Dialog- und conversational-basierte Systeme

Conversational Interfaces können schrittweise fragen, Rückfragen ermöglichen und in natürlicher Sprache erklären; die Evidenz ist uneinheitlich. Laranjo et al. schlossen in einem systematischen Review 17 von 1.513 Treffern ein; die Systeme nutzten überwiegend endliche Zustandsmodelle oder frame-basierte Dialogsteuerung, die Evidenzbasis war heterogen [L07] (`E`). Kim, Lee und Gweon beobachteten bei einem Chatbot-Fragebogen teilweise differenziertere Antworten und weniger Satisficing als beim Webformular, abhängig von Gesprächsgestaltung und Population [L08] (`E`). Zarouali et al. fanden longitudinal häufig günstigere Antwort- und Datenqualitätsmerkmale bei traditionellen Webbefragungen; der Chatbot wurde hinsichtlich Nutzen, Freude und Sicherheit ungünstiger bewertet [L09] (`E`). Eine Chatoberfläche als primäres regulatorisches Interaktionsmodell ist damit wissenschaftlich nicht begründbar; allenfalls eine erklärende oder navigierende Schicht, getrennt vom regulatorischen Entscheidungsstatus (`D`).

### 2.5 Regelbasierte Expertensysteme und Decision Rules

Maxwell und Antón modellierten rechtliche Anforderungen als Produktionsregeln und prüften damit bestehende Softwareanforderungen auf Rechtskonformität einschließlich Lücken [L10] (`E`, Fallstudie). Governatori modelliert Compliance über formal beschriebene Verpflichtungen und Ausführungsspuren [L11] (`T`); Regorous operationalisiert dies als Business-Process-Compliance-Checker [L12]. Explizite Regelmodelle sind damit für Compliance-Prüfungen geeignet; daraus folgt aber nicht automatisch Explainability: Nachvollziehbar wird ein Regelsystem erst, wenn Regelpfad, verwendete Fakten und Schlussfolgerung zugänglich sind (`D`). Ein deterministisches Regelsystem ist bei fester Regelbasis und identischen Eingaben prinzipiell reproduzierbar – im Unterschied zu probabilistischen oder generativen Komponenten (`T`). Rudin argumentiert für hochkritische Entscheidungen zugunsten inhärent interpretierbarer Modelle [L14]; die Arbeit bezieht sich primär auf Machine Learning und wird nur ergänzend als Designargument verwendet (`T`).

### 2.6 Decision Support Systems

Decision Support Systems sind eine funktionale Oberkategorie, keine UI- oder Algorithmusklasse. Ein systematischer Review zu human-centered AI in DSS (90 Arbeiten, 2015–2025) identifiziert Transparenz, Verlässlichkeit und menschliche Aufsicht als zentrale Gestaltungsprobleme [L17] (`E`, Review). Für RegScoutX ist die Bezeichnung **Assistenz- bzw. Decision-Support-System** präziser als ein System, das verbindliche regulatorische Entscheidungen trifft: Es erzeugt einen nachvollziehbaren Bewertungsvorschlag auf Basis einer formalisierten Regelbasis; die regulatorische Verantwortung verbleibt außerhalb des Demonstrators (`D`).

### 2.7 Traceability und Auditierbarkeit

Regan et al. zeigen für Medizinproduktesoftware die zentrale Rolle der Nachverfolgbarkeit über Entwicklungs- und Wartungsphasen in Standards und regulatorisch geprägten Prozessen sowie praktische Umsetzungsschwierigkeiten [L15] (`E`). Mucha, Kaufmann und Riehle zeigen in einem systematischen Review, dass Traceability bereits vor der Requirement-Spezifikation relevant ist, also bei der Verbindung von Anforderungen mit ihren Ursprüngen [L16] (`E`, Review). Hasan klassifiziert regulatorische Requirements Compliance als methodisch komplexes Requirements-Engineering-Problem [L13] (`E`, Review). Daraus ist eine durchgängige Kette `Nutzereingabe → Applicability-/Entscheidungsregel → Requirement → Gap-Status → regulatorische Quelle → vorgesehener Nachweis` besser begründbar als eine reine Ergebnisliste (`D`).

---

## 3. Vergleich der Interaktionskonzepte

Strukturbeschreibung ohne Bewertungsskala, Rangfolge oder Gesamturteil. Die letzte Zeile ist eine Synthese aus der Literatur (`S`), kein Ergebnis einer einzelnen Vergleichsstudie.

| Ansatz | Nutzerführung | bedingte Logik | Reproduzierbarkeit | Explainability | lange/komplexe Eingaben | Fehler / Cognitive Load | Auditierbarkeit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Klassisches Formular | explizite Gesamtstruktur | standardmäßig gering | hoch für feste Felder und Validierung | nur durch zusätzliche Hilfen | bei großen Formularen zunehmend belastend | Eingabefehler durch vorab erklärte Regeln reduzierbar [L01] | gut bei Versionierung und Logging |
| Wizard | sequenzielle, segmentierte Führung | optional | hoch bei festem Ablauf | Kontext muss aktiv angezeigt werden | gut segmentierbar; Übersicht kann verloren gehen | kein pauschaler Vorteil gegenüber Scrolling belegt [L02] | gut, wenn Schrittfolge protokolliert wird |
| Adaptiver Fragebogen | nur relevante Fragepfade | zentraler Bestandteil | hoch bei expliziten Branching-Regeln | gut, wenn Trigger sichtbar sind | geeignet für stark bedingte Eingaben | kann irrelevante Belastung reduzieren; Fehlverzweigung mit hoher Folgewirkung [L04] | hoch bei versionierten Regeln und Pfad-Logging |
| Conversational Interface | schrittweise, sprachlich flexibel | gut möglich | abhängig vom Dialogmodell; bei generativer Verarbeitung nicht inhärent deterministisch | sprachliche Erklärung möglich, aber nicht automatisch prüfbar | kann Interaktion erleichtern; Befunde gemischt | abhängig von Dialoggestaltung und Population [L08], [L09] | begrenzt, wenn Antwortgenerierung und Entscheidungslogik nicht getrennt sind |
| Regelbasiertes Expertensystem | UI-unabhängig | gut für verschachtelte Bedingungen | deterministisch bei fester Regelbasis | hoher Erklärungswert durch Rule Trace | Komplexität liegt in der Wissensbasis | Fehler verschieben sich in Regelmodellierung und -pflege | hoch bei Versionierung, Provenienz und Rule Trace [L10] |
| Decision Support System | systemabhängig | modellabhängig | abhängig vom Entscheidungsverfahren | zentrales Qualitätsmerkmal | hohe Komplexität integrierbar | abhängig von der Mensch-System-Aufgabenteilung | abhängig von Modell- und Datenprovenienz [L17] |
| Hybrid: Wizard + adaptive Fragen + Regeln (`S`) | strukturierte Oberfläche mit fallabhängiger Tiefe | explizit | hoch bei deterministischem Regelkern | Rule Trace und Quellbezug integrierbar | Komplexität schrittweise freigebbar | Eingabevalidierung und Verzweigung kombinierbar | technisch realisierbar |

Die Kombination mehrerer etablierter Konzepte ist damit begründbar, ohne zu behaupten, eine Studie habe genau den RegScoutX-Aufbau als vorteilhafter nachgewiesen.

---

## 4. Anwendungsspezifischer Lösungsstand (Regulatory/MedTech)

Alle Produktangaben sind **Hersteller-/Anbieterdokumentation** (`H`), Abruf 27.08.2026. Sie belegen ausschließlich, dass eine Funktion **öffentlich dokumentiert** ist – nicht, dass sie empirisch validiert, vollständig vorhanden oder technisch vorteilhaft ist. `nicht öffentlich nachgewiesen` (`n.ö.n.`) bedeutet nicht `nicht vorhanden`.

### 4.1 Regulatorische Informations-, QMS- und Traceability-Systeme

- **Rimsys** [P09]: Standards-, GSPR- und regulatorisches Requirements-Management, Verknüpfung mit Produkten, Registrierungen und Submissions, Change Monitoring und Impact Assessment über den Produktlebenszyklus. Eine integrierte EU-AI-Act-Funktion ist auf den untersuchten Seiten n.ö.n.
- **Greenlight Guru** [P10]: Medical-Device-QMS und Design Controls; mehrstufige Traceability, Risiko- und Design-Control-Verknüpfungen, Audit-Evidence, Software-/SaMD-Entwicklung. Eine produktintegrierte AI-Act-Applicability-/Gap-Logik ist n.ö.n.
- **Jama Connect** [P11]: Anforderungen, Risiken, Tests, V&V und Live Traceability für Medizinprodukte; nennt EU MDR und IEC 62304. Schwerpunkt Requirements-/Engineering-Management; MDR+AI-Act-Applicability-Logik n.ö.n.

### 4.2 Integrierte MedTech-/AI-Compliance-Lösungen

- **Leida AI** [P01]: dokumentiert MDR, IVDR und EU AI Act, Bestimmung anwendbarer Anforderungen, Gap-Erkennung, Requirement-Evidence-Verknüpfung, Quell-/Klauselbezug, Change Impact sowie einen Ablauf von Intended Purpose bis Post-Market; für AI-generierte Aussagen soll die Ursprungsklausel angezeigt werden. Die kontinuierliche Cross-Mapping-Funktion wird für MDR, IVDR und FDA beschrieben; eine gleich präzise MDR-/AI-Act-Cross-Mapping-Methodik und ein offengelegtes deterministisches Regelmodell sind n.ö.n.
- **Mia-Care P4SaMD** [P02], [P03]: Plattform für Software as a Medical Device; für die EU werden MDR und EU AI Act als regulatorische Grundlagen genannt; Zielmarkt, regulatorischer Rahmen und Software-Sicherheitsklasse bestimmen die geprüften Anforderungen; Requirements Traceability, Risiko- und Testverknüpfungen, Evidence-Erfassung, vollständiger Software-Lifecycle-Workflow; für bestehende Projekte ein sechsstufiger Guided Wizard mit anschließender Compliance-Gap-Analyse und priorisiertem Remediation Plan. Offen bleibt, wie die interne Applicability-Logik formalisiert ist, ob identische Eingaben nachweislich denselben Output erzeugen und ob jeder Gap atomar bis zur Originalquelle rückverfolgbar ist.
- **CertHub** [P05]: dokumentiert MDR-/IVDR-Gap-Analyse, Vollständigkeitsprüfung, Audit-Checks und TechDoc-Prüfungen und adressiert Softwareprodukte. **EU AI Act: `n.ö.n.`** (verbindliche Quellenkorrektur: ohne separate offizielle Quelle wird eine AI-Act-Unterstützung nicht als öffentlich belegt geführt). Eine offengelegte deterministische Rule Engine und eine Requirement-Level-Trace von Entscheidungsregel über Rechtsquelle zu Evidence sind n.ö.n.
- **Complear OS** [P06]: verbindet nach Anbieterbeschreibung Medical-Device-Compliance, AI Governance und weitere Digital-Health-Regime; MDR und EU AI Act ausdrücklich unterstützt; agentisches AI-Konzept mit Human-in-the-Loop, Produktphasen, Audit-View und aktualisierter technischer Dokumentation. Eine öffentlich spezifizierte deterministische Regelbasis mit Reproduzierbarkeitsaussage ist n.ö.n.
- **MoniDoseQMS** [P07], [P08]: EU-AI-Act-Modulsatz seit 2026; beschreibt die Verbindung von AI-Risiko, Data Governance und Post-Market-Monitoring mit Design Controls, ISO-14971-Risikodatei und klinischer Evidenz des Medizinprodukts in einem System (Integration auf QMS-/Evidence-Ebene). Eine atomisierte, deterministische Requirement-Applicability-/Gap-Engine mit Rule Trace ist n.ö.n.
- **DLG:MDR** [P04]: digitaler Decision-Support-Comparator ohne eQMS-Charakter; strukturierte Eingabe, gemeinsame MDR- und EU-AI-Act-Bewertung einschließlich Interaktion beider Rechtsrahmen, Borderline-Fälle, expert-reviewed Report mit Klassifikationsbegründung, regulatorischen Fundstellen, Evidence Gaps, Obligation Mapping und nächsten Schritten. Ein vollständig automatisierter deterministischer Requirement-Level-Regelkatalog mit Evidence-Mapping und formaler Lifecycle-Taxonomie ist n.ö.n.

### 4.3 AI-Act-Governance ohne MedTech-Fokus

- **Credo AI** [P12], [P13]: EU-AI-Act-Policy-Packs, Risikoklassifizierung, Konformitätsbewertungen, Evidence-Erhebung und auditierbare Reports; MDR- und Medical-Device-Software-Integration n.ö.n.

### 4.4 Ergebnis der Lösungsanalyse

Die Aussage „Es gibt keine Lösung für MDR und EU AI Act bei KI-Medizinprodukten“ ist für den untersuchten Stand September 2026 nicht haltbar. Mehrere öffentlich dokumentierte Lösungen adressieren beide Regime oder wesentliche Teile davon, insbesondere **Leida AI, Mia-Care P4SaMD, DLG:MDR, Complear OS und MoniDoseQMS**: DLG:MDR analysiert MDR und AI Act ausdrücklich gemeinsam, MoniDoseQMS beschreibt eine gemeinsame QMS-/Evidence-Integration, P4SaMD unterstützt beide Rahmenwerke für SaMD, Leida und Complear führen beide Regime in ihren Plattformen. CertHub wird in diese Aufzählung nicht einbezogen (EU AI Act n.ö.n.). Die belastbare Forschungslücke liegt daher eine Ebene tiefer (Abschnitt 6).

---

## 5. Vergleichsmatrix

**Legende:** `ja` = in der untersuchten offiziellen Dokumentation explizit beschrieben · `teilw.` = angrenzende oder unvollständige Funktion öffentlich beschrieben · `n.ö.n.` = nicht öffentlich nachgewiesen (kein Schluss auf technische Nichtexistenz). Wo der Research-Input eine Zwischen- oder Freitextangabe enthält, wird konservativ der nächstniedrigere Legendenwert geführt und die Originalangabe in Klammern ergänzt. Keine Scores, keine Rangfolge.

### 5.1 Interaktion und Entscheidungslogik

| Lösung | strukturierte Nutzerführung | dynamische/bedingte Fragen | deterministische Regelverarbeitung | Reproduzierbarkeit öffentlich belegt | Begründung/Explainability |
| --- | --- | --- | --- | --- | --- |
| Leida AI | ja | n.ö.n. | n.ö.n. | n.ö.n. | ja (Klausel-/Quellbezug) |
| Mia-Care P4SaMD | ja (Guided Workflows/Wizard) | teilw. (Anforderungsauswahl nach Rahmen/Sicherheitsklasse) | n.ö.n. | n.ö.n. | teilw. |
| CertHub | ja | n.ö.n. | n.ö.n. | n.ö.n. | teilw. (Prüf-/Bewertungsberichte) |
| Complear OS | ja | teilw. (stage-/framework-bezogene Workflows) | n.ö.n. (agentisches AI-System) | n.ö.n. | teilw. (Human-in-the-Loop, Audit Trail) |
| MoniDoseQMS | ja (modulare Workflows) | n.ö.n. | n.ö.n. | n.ö.n. | teilw. |
| DLG:MDR | ja (strukturierte Intake-Fragen) | n.ö.n. | n.ö.n. | n.ö.n. (Expert Review ist Bestandteil) | ja (Reasoning Chain, Quellenbasis) |
| Rimsys | ja | teilw. (Applicability-/Impact-Workflows) | teilw. (nur einzelne kontrollierte Logiken; keine Gap-Rule-Engine nachgewiesen) | n.ö.n. | teilw. (regulatorische Traceability) |
| Greenlight Guru | ja | n.ö.n. | n.ö.n. | n.ö.n. | teilw. (Traceability zwischen Artefakten) |
| Jama Connect | ja | n.ö.n. | n.ö.n. | n.ö.n. | teilw. (Live Traceability) |
| Credo AI | ja | teilw. (Governance-/Assessment-Workflows) | n.ö.n. | n.ö.n. | teilw. (Policies, Evidence, Audit) |

### 5.2 Regulatorischer und evidenzbezogener Funktionsumfang

| Lösung | MDR | EU AI Act | integrierte MDR+AI-Act-Betrachtung | MDSW/SaMD | Requirement-Level-Gap-Analyse | Source Traceability | Lifecycle-/Phasenbezug | Evidence Mapping | Reporting |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leida AI | ja | ja | teilw. (gemeinsame Plattform; AI-Act-Cross-Mapping methodisch nicht offengelegt) | ja | teilw. (Research: ja/weitgehend) | ja | ja | ja | ja |
| Mia-Care P4SaMD | ja | ja | teilw. (beide im EU-Assessment; Interaktionslogik nicht offengelegt) | ja | teilw. (Research: teilw. bis weitgehend) | teilw. | ja (vollständiger SDLC) | ja | ja |
| CertHub | ja | **n.ö.n.** (Quellenkorrektur) | **n.ö.n.** (Quellenkorrektur) | ja | teilw. | n.ö.n. (auf Einzelentscheidungsniveau) | teilw. | teilw. | ja |
| Complear OS | ja | ja | teilw. (gemeinsamer Workflow; Cross-Regulation-Logik nicht öffentlich) | ja | n.ö.n. | n.ö.n. (auf Requirement-Ebene) | ja | teilw. (Research: ja/teilw.) | teilw. |
| MoniDoseQMS | ja | ja | ja (auf QMS-/Evidence-Ebene) | ja (AI-enabled medical devices) | n.ö.n. | n.ö.n. (auf Requirement-Ebene) | teilw. (Research: ja/teilw.) | teilw. (Research: ja/teilw.) | n.ö.n. |
| DLG:MDR | ja | ja | ja (ausdrücklich analysiert) | ja (AI-enabled health products) | teilw. (Obligation Mapping, Evidence Gaps) | ja (für wesentliche Schlussfolgerungen) | teilw. (Entwicklungsstand statt formaler Lifecycle-Taxonomie) | teilw. | ja (strukturierter PDF-Report) |
| Rimsys | ja | n.ö.n. | n.ö.n. | teilw. (allgemeine MedTech-Unterstützung) | n.ö.n. (als Gap Engine) | ja (für Standards/GSPR/Produkte) | ja | teilw. (Research: ja/teilw.) | teilw. |
| Greenlight Guru | ja | n.ö.n. | n.ö.n. | ja | n.ö.n. (für regulatorische Requirement-Gaps) | teilw. (Artefakttraceability; vollständige Rechtsquellen-Trace n.ö.n.) | ja | ja | ja |
| Jama Connect | ja | n.ö.n. | n.ö.n. | ja | n.ö.n. (für regulatorische Applicability-Gaps) | teilw. (Engineering-Traceability; Rechtsquellen-Trace n.ö.n.) | ja | ja | ja |
| Credo AI | n.ö.n. | ja | n.ö.n. | n.ö.n. | teilw. (im AI-Governance-Kontext) | teilw. | teilw. | ja | ja |

Quellen je Zeile: Abschnitt 4 und Abschnitt 12.2.

---

## 6. Forschungslücke

### 6.1 Wissenschaftliche Literatur

Die Literatur behandelt die relevanten Teilprobleme weitgehend getrennt: regelbasierte Rechts-/Compliance-Prüfung [L10]–[L12], regulatorisches Requirements Engineering [L13], adaptive und dialogbasierte Interaktion [L04], [L06]–[L09], Decision Support und Explainability [L14], [L17] sowie Traceability in der Medizinproduktesoftware-Entwicklung [L15], [L16].

> **Im untersuchten wissenschaftlichen Literaturbestand wurde keine peer-reviewt dokumentierte und evaluierte Lösung identifiziert, die für KI-basierte Medizinproduktesoftware eine integrierte, regelbasierte MDR-/EU-AI-Act-Anforderungs- und Gap-Analyse in der untersuchten Form zusammenführt.**

Die Aussage bezieht sich auf den durchgeführten Rechercheumfang und ist kein globaler Nichtexistenzbeweis.

### 6.2 Untersuchter Produktbestand

> **Im untersuchten öffentlich zugänglichen Produktbestand wurde kein belastbarer öffentlicher Nachweis für eine Lösung gefunden, die gleichzeitig transparent dokumentiert:**
>
> - MDR + EU AI Act
> - KI-basierte Medizinproduktesoftware
> - explizite regelbasierte Applicability
> - deterministisch reproduzierbare Auswertung
> - atomare Requirement-Level-Gap-Analyse
> - Input → Rule → Requirement → Source Trace
> - Lifecycle-/Phasenzuordnung
> - Requirement-to-Evidence-Mapping

Leida AI und P4SaMD dokumentieren mehrere dieser Merkmale öffentlich; DLG:MDR dokumentiert besonders deutlich eine gemeinsame MDR-/AI-Act-Analyse und Schlussfolgerungs-Traceability. In der geprüften öffentlichen Dokumentation bleiben insbesondere die formal nachvollziehbare deterministische Entscheidungslogik und die vollständige Rule-to-Requirement-to-Evidence-Traceability unklar. Da interne Regeln kommerzieller Systeme typischerweise nicht öffentlich sind, ist dies eine Aussage über öffentliche Nachweise, nicht über die Systeme selbst (`S`).

### 6.3 Einordnung gegenüber dem Exposé

Das Exposé formuliert in Abschnitt 2, nach bisheriger Recherche sei keine öffentlich zugängliche Lösung bekannt, die Anforderungen aus MDR und EU AI Act „in der hier vorgesehenen Form“ integriert, regelbasiert bewertet und in eine nachvollziehbare Gap-Analyse überführt. Die vorliegende Recherche widerspricht dem nicht, präzisiert aber den Bezug: Die Abgrenzung liegt nicht in der gemeinsamen Betrachtung beider Regime, sondern in der Kombination aus deterministischer Regelbasis, Requirement-Level-Gap-Analyse, explizitem Entscheidungs- und Quellenpfad, Lifecycle-Zuordnung und Evidence Mapping sowie deren dokumentierter Evaluation. Das Exposé bleibt unverändert; die Präzisierung ist für die schriftliche Ausarbeitung zu übernehmen.

---

## 7. Abgrenzung von RegScoutX

RegScoutX ist **kein** Ersatz für QMS-, RIM-, ALM- oder Zertifizierungsplattformen und keine regulatorische Beratung ([EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 4, Abgrenzung). Wissenschaftlicher Fokus ist ein methodisches Artefakt:

> ein transparent formalisiertes und reproduzierbares Regelmodell, das strukturierte Produkteingaben auf konkrete MDR-/AI-Act-Anforderungen abbildet, daraus Requirement-Level-Gaps erzeugt und den Entscheidungsweg einschließlich Quelle, Lifecycle-Kontext und vorgesehenem Nachweis nachvollziehbar macht – mit durchgängiger Traceability im definierten Untersuchungsumfang.

Die Produktvergleiche dienen der Einordnung dieses Artefakts, nicht einer Positionierung im Markt.

---

## 8. Design Implications und Abgleich mit Systemanforderungen und Architektur

### 8.1 Design Implications

| ID | Design Implication | Evidenz (Art) | adressiertes Defizit |
| --- | --- | --- | --- |
| DI-001 | Hybrid aus strukturiertem Wizard und adaptiver Frageführung | [L04] (`T`), [L06] (`E`), [L02] (`E`: Paging nicht generell vorteilhaft); Kombination `S`/`D` | lange und stark bedingte regulatorische Eingaben |
| DI-002 | Deterministische Entscheidungslogik getrennt von der UI | [L10] (`E`), [L11], [L12] (`T`), [L14] (`T`, ergänzend) | fehlende Reproduzierbarkeit, Black-Box-Entscheidungen |
| DI-003 | Für jede Entscheidung ein maschinenlesbarer Rule Trace | [L10] (`E`), [L15], [L16] (`E`); `D` | Explainability nicht nur als frei formulierte Erklärung |
| DI-004 | Auslöser bedingter Fragen sichtbar und prüfbar machen | [L04] (`T`); `D` | unsichtbare Fehlverzweigung |
| DI-005 | Rücknavigation ohne Verlust konsistenter Folgeentscheidungen | [L18] (Norm: Steuerbarkeit, Erwartungskonformität); `D` | Korrektur früher Eingaben in langen Fragebäumen |
| DI-006 | Eingabebedingungen vor der Eingabe erklären und validieren | [L01] (`E`) | fehlerhafte Datenbasis der Regelverarbeitung |
| DI-007 | Explizite Source Traceability bis zur regulatorischen Quelle | [L15], [L16] (`E`); Tools [P01], [P04] (`H`) | Ergebnisse ohne prüfbare normative Herkunft |
| DI-008 | Requirement-to-Evidence-Verknüpfung als eigenes Datenobjekt | [L15] (`E`); [P01], [P10], [P11] (`H`) | Gap-Ergebnis ohne Aussage, womit Erfüllung belegt werden kann |
| DI-009 | Versionierte Knowledge-/Rule-Schicht getrennt von der Präsentation | [P09] (`H`: Change Monitoring mit Impact Analysis); `D` | Wartbarkeit, Auditierbarkeit, Folgen regulatorischer Änderungen |
| DI-010 | Lifecycle-/Phasenkontext im Ergebnis erhalten | [L15] (`E`) | flache Requirement-Liste ohne Umsetzungszeitpunkt |
| DI-011 | Unsicherheit bzw. unzureichende Eingaben explizit anzeigen statt Entscheidung erzwingen | [L17] (`E`, Review); [P04] (`H`) | falsche regulatorische Präzision |
| DI-012 | Conversational Assistance allenfalls als ergänzende Erklärungsschicht | [L07]–[L09] (`E`, gemischte Befunde) | Verlust von Struktur, Reproduzierbarkeit und Auditierbarkeit bei freier Dialoglogik |

### 8.2 Abgleich (Ausgangsstand SR-001 bis SR-039)

Status: `COVERED` = vollständig durch bestehende `SR` und Architektur abgedeckt · `PARTIAL` = Teilaspekt fehlt (präzise benannt) · `GAP` = weder in `SR` noch in Architektur enthalten. Bestehende `SR` wurden nicht umformuliert.

| ID | bestehende `SR` | Architektur-/Interaktionsbezug | Status | fehlender Teil / Anmerkung |
| --- | --- | --- | --- | --- |
| DI-001 | SR-001, SR-003, SR-039 | [RUL_METHOD.md](../03-regulatory/RUL_METHOD.md): Folgeregel je Zweig (`next`) bestimmt die nächste Frage aus der vorigen Antwort (adaptive Frageführung); ARCHITECTURE Abschnitt 3 (`PRESENTATION`: Fragebogen) und Abschnitt 5 Schritte 2–3 | PARTIAL | Adaptive, regelgesteuerte Frageführung ist abgedeckt. Die Segmentierung in Wizard-Schritte mit Übersicht und Fortschritt ist nicht festgelegt; sie gehört zum offenen Oberflächen- und Interaktionskonzept (ARCHITECTURE Abschnitt 7). Kein SR-Vorschlag, weil die Literatur keine bestimmte Segmentierungsform als notwendig belegt [L02]. |
| DI-002 | SR-002, SR-029, SR-030, SR-038, SR-039 | ARCHITECTURE Leitprinzipien 1–2, Abschnitt 4 (keine Engine hängt von `PRESENTATION` ab), Abschnitt 8 | COVERED | — |
| DI-003 | SR-006, SR-019, SR-020 | `RuleExecution`, `DecisionResult`, `ApplicableRequirement` (`evaluated_predicates`, `relevant_inputs`, `determined_by`) in [DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml); ARCHITECTURE Abschnitt 8 | COVERED | — |
| DI-004 | SR-006, SR-010, SR-019, SR-039 | versionierte, getestete Branching-Regeln ([RUL_DECISION_TESTS_SRC_004.yaml](../07-testing/RUL_DECISION_TESTS_SRC_004.yaml)); `reason_code` im Datenmodell | PARTIAL | Prüfbarkeit ist abgedeckt; sichtbar ist nach SR-010 nur die Begründung von `NOT_APPLICABLE`. Nicht gefordert ist, für `APPLICABLE` und `APPLICABILITY_UNRESOLVED` Begründungscode, ausgewertete Prädikate und herangezogene Applicability-Eingaben auszuweisen (siehe `PROPOSED_SR_GAP` 3). Die Anzeige des Auslösers einer Folgefrage während der Eingabe gehört zum offenen Interaktionskonzept. |
| DI-005 | SR-002 (technische Grundlage: zustandslose, deterministische Auswertung des vollständigen Eingabestands) | ARCHITECTURE Abschnitt 5 beschreibt nur den linearen Ablauf | GAP | Weder `SR` noch Architektur regeln die Änderung einer bereits erfassten Eingabe: Neuberechnung, Kennzeichnung nicht mehr erreichbarer Eingaben und betroffener Bewertungen (siehe `PROPOSED_SR_GAP` 1). |
| DI-006 | SR-001, SR-003, SR-034 | `ProductProfile`-Invarianten; kontrollierte Werte mit DE/EN-Bezeichnungen aus den Katalogen; Abweisung unzulässiger Eingaben (`InvalidInputError`) | PARTIAL | Validierung vor der Verarbeitung ist abgedeckt. Die vorherige Anzeige zulässiger Werte und Formate (insbesondere für Datumseingaben) ist nicht ausdrücklich gefordert; sie gehört zum offenen Interaktionskonzept. Kein SR-Vorschlag, da Eingaben überwiegend als kontrollierte Auswahl erfolgen. |
| DI-007 | SR-011, SR-019, SR-020, SR-022 | [TRACEABILITY_MODEL.md](../05-traceability/TRACEABILITY_MODEL.md); ARCHITECTURE Leitprinzip 5 | COVERED | — |
| DI-008 | SR-015, SR-017, SR-018 | `EvidenceReference`, `GapAssessment.evidence_ids`; `EVIDENCE_SERVICE` | PARTIAL | Die Verknüpfung Requirement → nutzerseitig referenzierter Nachweis ist als eigenes Datenobjekt abgedeckt. Nicht modelliert ist die katalogseitige Angabe der vorgesehenen Maßnahme bzw. des vorgesehenen Nachweisdokuments je `RR`, die das Exposé (Abschnitt 4, Traceability-Matrix) nennt (siehe `PROPOSED_SR_GAP` 4). |
| DI-009 | SR-021, SR-022, SR-030, SR-031, SR-037 | ARCHITECTURE Leitprinzip 1, `CATALOG_REPOSITORY`; Versionsbindung der Kataloge mit Impact-Review in den Validatoren | COVERED | — |
| DI-010 | SR-011, SR-023 (ohne Lebenszyklusbezug) | `lifecycle_phases` je `RR` im Katalog; Vokabular [CONTROLLED_VOCABULARY.md](../03-regulatory/CONTROLLED_VOCABULARY.md) | PARTIAL | Die Daten sind vorhanden, aber keine `SR` verlangt, die Lebenszyklusphasen je `RR` in Anzeige und Bericht auszuweisen (siehe `PROPOSED_SR_GAP` 2). |
| DI-011 | SR-003, SR-004, SR-009, SR-013, SR-023 | Status `INCOMPLETE`, `REVIEW_REQUIRED`, `APPLICABILITY_UNRESOLVED`, `NOT_ASSESSED`; fail-closed in ARCHITECTURE Abschnitt 8 | COVERED | — |
| DI-012 | SR-029, SR-038 | ARCHITECTURE Leitprinzip 2; Exposé Abschnitt 4 (keine generative KI im Demonstrator) | COVERED | Eine Dialogschicht ist nicht vorgesehen; eine spätere Erweiterung dürfte nur außerhalb der Entscheidungsmodule liegen. |

**Ergebnis im Ausgangsstand:** 6 `COVERED` (DI-002, DI-003, DI-007, DI-009, DI-011, DI-012), 5 `PARTIAL` (DI-001, DI-004, DI-006, DI-008, DI-010), 1 `GAP` (DI-005). Stand nach Aufnahme von SR-040 bis SR-043: Abschnitt 8.4.

**Deutsch/Englisch:** SR-026 bis SR-028 sind projektbezogene Systemanforderungen ([SYSTEM_REQUIREMENTS.md](../02-requirements/SYSTEM_REQUIREMENTS.md) Abschnitt 3) und kein Ergebnis dieser Recherche.

### 8.3 Vorgeschlagene SR-Ergänzungen (`PROPOSED_SR_GAP`)

Die vier Kandidaten wurden in Version 1.0 vorbereitet und sind seit [SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml) Version 0.3 als SR-040 bis SR-043 aufgenommen (Abschnitt 8.4); die dort geltenden Formulierungen sind maßgeblich. Die Entwürfe bleiben zur Nachvollziehbarkeit erhalten.

| Nr. | DI | Entwurf (DE) | Gruppe / Module | Herkunft |
| --- | --- | --- | --- | --- |
| 1 | DI-005 | Das System muss nach Änderung einer bereits erfassten Eingabe Entscheidungsergebnisse und Anwendbarkeit vollständig aus dem aktuellen Eingabestand neu bestimmen und nicht mehr erreichbare Eingaben sowie betroffene Bewertungen kennzeichnen, ohne sie still zu verwerfen. | `QUALIFICATION_CLASSIFICATION`; `ASSESSMENT_SERVICE`, `GAP_ENGINE`, `AUDIT_LOG` | Exposé Abschnitt 3 (Reproduzierbarkeit); DI-005 |
| 2 | DI-010 | Das System muss für jede angezeigte und berichtete `RR` ihre Lebenszyklusphasen aus dem `RR`-Katalog ausweisen. | `REPORTING`; `REQUIREMENT_SERVICE`, `REPORTING`, `PRESENTATION` | Exposé Abschnitte 2 und 4 (phasenbezogenes Modell, Traceability-Matrix mit Lebenszyklusphase); DI-010 |
| 3 | DI-004 | Das System muss für jede `RR` im Ergebnis den Begründungscode der Anwendbarkeit, die ausgewerteten Prädikate und die herangezogenen Applicability-Eingaben ausweisen. | `TRACEABILITY`; `APPLICABILITY_ENGINE`, `REPORTING` | Exposé Abschnitt 3 (Nachvollziehbarkeit); DI-004 |
| 4 | DI-008 | Das System muss je anwendbarer `RR` die im Katalog hinterlegte vorgesehene Maßnahme und Nachweisart anzeigen. | `EVIDENCE`; `REQUIREMENT_SERVICE`, `REPORTING` | Exposé Abschnitt 4 (Traceability-Matrix mit Maßnahme und Nachweisdokument); DI-008. **Abhängigkeit:** setzt eine separat zu adjudizierende Katalogerweiterung voraus; zum Zeitpunkt des Entwurfs existierten keine solchen Katalogdaten (seit Block 5: [RR_MEASURE_CATALOG.yaml](../03-regulatory/RR_MEASURE_CATALOG.yaml)). |

### 8.4 Schließung der `PROPOSED_SR_GAP` (SR-040 bis SR-043)

| `PROPOSED_SR_GAP` | neue `SR` | Design Implication | Datenmodell / Traceability |
| --- | --- | --- | --- |
| 1 | SR-040 konsistente Neuberechnung nach Eingabeänderung | DI-005 | bestehende Strukturen (`RuleExecution`, `ApplicableRequirement`, `AuditEvent`); zustandslose Auswertung nach SR-002 |
| 2 | SR-041 Lebenszykluskontext je Anforderung | DI-010 | `lifecycle_phases` der `RR`, Vokabular aus [CONTROLLED_VOCABULARY.md](../03-regulatory/CONTROLLED_VOCABULARY.md); keine neue Taxonomie |
| 3 | SR-042 nachvollziehbare Herleitung jeder Anwendbarkeitsentscheidung | DI-004 | bestehende Trace-Struktur von `ApplicableRequirement`; keine eigene Erklärungskomponente |
| 4 | SR-043 vorgesehene Maßnahme und Nachweisart je Anforderung | DI-008 | [DATA_MODEL.yaml](../04-architecture/DATA_MODEL.yaml) Version 0.4: Katalogart `RR_MEASURE`, `EvidenceReference.measure_key`; Maßnahmenkatalog zu diesem Zeitpunkt noch nicht befüllt (seit Block 5 `RR_MEASURE_CATALOG.yaml` 0.1: 457 `MAPPED`, 502 `REVIEW_REQUIRED`; seit 0.2 alle 959 `RR` zugeordnet, [RR_MEASURE_METHOD.md](../03-regulatory/RR_MEASURE_METHOD.md)) |

Jede neue `SR` verweist in `derived_from` auf den Exposé-Abschnitt und auf `STATE_OF_THE_ART.md#DI-NNN`; der SR-Validator prüft die Existenz der Design Implication.

| ID | Status vorher | Status nachher | Begründung |
| --- | --- | --- | --- |
| DI-001 | PARTIAL | PARTIAL | unverändert: Wizard-Segmentierung mit Übersicht und Fortschritt gehört zum offenen Interaktionskonzept; kein SR-Gap (Abschnitt 8.2) |
| DI-002 | COVERED | COVERED | — |
| DI-003 | COVERED | COVERED | — |
| DI-004 | PARTIAL | PARTIAL | Herleitung jeder Anwendbarkeitsentscheidung jetzt durch SR-042 abgedeckt; offen bleibt nur die Anzeige des Auslösers einer bedingten Folgefrage während der Eingabe (Interaktionskonzept) |
| DI-005 | GAP | COVERED | SR-040 |
| DI-006 | PARTIAL | PARTIAL | unverändert: vorherige Anzeige zulässiger Werte und Formate gehört zum offenen Interaktionskonzept; kein SR-Gap |
| DI-007 | COVERED | COVERED | — |
| DI-008 | PARTIAL | COVERED | SR-043 legt die System- und Datenfähigkeit fest; die inhaltliche Befüllung des Maßnahmenkatalogs ist ein nachgelagerter Arbeitsschritt, keine Anforderungslücke |
| DI-009 | COVERED | COVERED | — |
| DI-010 | PARTIAL | COVERED | SR-041 |
| DI-011 | COVERED | COVERED | — |
| DI-012 | COVERED | COVERED | — |

**Ergebnis nach SR-040 bis SR-043:** 9 `COVERED`, 3 `PARTIAL` (DI-001, DI-004, DI-006), 0 `GAP`. Die drei verbleibenden Teilaspekte betrafen ausschließlich die Detailgestaltung des damals noch nicht entschiedenen Interaktionskonzepts und sind keine Lücken des Systemanforderungsbestands; sie sind mit D4 geschlossen (Abschnitt 8.5).

### 8.5 Umsetzung im Interaktionskonzept (Demonstrator D4)

Die drei verbleibenden Teilaspekte sind im [Interaktionskonzept](../04-architecture/WEB_APPLICATION.md) umgesetzt. Die Umsetzung liegt im Kern (`regscoutx/questionnaire.py`, abgeleitet aus RUL-Katalog und Applicability-Zuordnung), die Oberfläche stellt nur dar. Keine `SR` wurde geändert; der Status beruht auf Implementierung und Test, nicht auf einer neuen Anforderung.

| DI | vorher | nachher | Umsetzung | Prüfung |
| --- | --- | --- | --- | --- |
| DI-001 | PARTIAL | COVERED | Hybrid aus segmentiertem Wizard (acht Abschnitte nach Regelkategorie bzw. ausgewertetem Anwendbarkeitsbereich, Übersicht mit Zustand, Zahl beantworteter und offener Fragen und Ergebnis je Abschnitt, Rücknavigation) und adaptiver Frageführung (Fragen nur auf dem aktuellen Regelpfad bzw. wenn eine Anforderung die Eingabe auswertet) | TC-055 (`QuestionnaireTest`, Browser-Ablauf Schritte 1–4) |
| DI-004 | PARTIAL | COVERED | Jede Frage nennt vor der Eingabe ihren Auslöser: Einstiegsfrage, Folgefrage mit auslösender Regel, Frage und Antwort, oder Anwendbarkeitsangabe mit betroffenen Bereichen und Anzahl der Anforderungen; die Herleitung jeder Anforderung zeigt der Decision Trace | TC-055, TC-056 |
| DI-006 | PARTIAL | COVERED | Zulässige Werte werden vor der Eingabe mit Folge je Wert aus dem Katalog angezeigt (Ergebnis, Prüfpunkt oder Folgeregel); Datumsfragen nennen die maßgeblichen Stichtage und das Format und werden erst auf Bestätigung übernommen; unzulässige Werte weist der Kern ab | TC-055, TC-057 |

**Ergebnis nach D4:** 12 `COVERED`, 0 `PARTIAL`, 0 `GAP`. Grenze: Die Wirksamkeit der Gestaltung für Nutzerinnen und Nutzer ist damit nicht empirisch belegt; eine Nutzerstudie ist nicht Gegenstand dieses Meilensteins.

---

## 9. Wissenschaftliche Herleitung bestehender Architektur- und Interaktionsentscheidungen

Die folgenden Entscheidungen bestehen bereits ([ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md), [ADR-0002](../decisions/0002-logical-architecture-and-traceability.md), [SR_CATALOG.yaml](../02-requirements/SR_CATALOG.yaml)); der Stand der Technik begründet sie nachträglich. Es wird keine neue Architektur eingeführt.

| Bestehende Entscheidung | Fundstelle im Projekt | Begründung aus dem Stand der Technik |
| --- | --- | --- |
| deterministischer Regelkern ohne generative KI | Leitprinzip 2; SR-002, SR-029 | Eignung expliziter Regelmodelle für Compliance [L10]–[L12]; Reproduzierbarkeit bei fester Regelbasis; inhärente Interpretierbarkeit [L14]; generative Dialogverarbeitung nicht inhärent deterministisch (Abschnitt 3) |
| Trennung von Regelkern und Oberfläche | Abschnitt 4; SR-038, SR-039 | Auditierbarkeit ist begrenzt, wenn Antwortgenerierung und Entscheidungslogik nicht getrennt sind (Abschnitt 3); Conversational Interfaces allenfalls als Erklärungsschicht [L07]–[L09] |
| adaptive, regelgesteuerte Frageführung | Abschnitt 5 Schritte 2–3; `RUL`-Folgeregeln; SR-001 | contingency branching [L04], dynamische Fragenauswahl [L06]; Branching-Regeln versioniert und getestet (SR-039) wegen hoher Folgewirkung von Fehlverzweigungen |
| Explainability über Rule Trace | SR-006, SR-019, SR-020; `RuleExecution`, `ApplicableRequirement` | Regelsysteme sind nur mit zugänglichem Regelpfad nachvollziehbar (Abschnitt 2.5); Traceability-Forschung [L15], [L16] |
| fail-closed / ungeklärt statt erzwungener Entscheidung | SR-003, SR-004, SR-009; `APPLICABILITY_UNRESOLVED` | Transparenz und menschliche Aufsicht als DSS-Gestaltungsprobleme [L17]; Vermeidung falscher regulatorischer Präzision (DI-011) |
| versionierte Wissens- und Regelbasis | Leitprinzip 1; SR-021, SR-030, SR-037 | regulatorische Änderungen erfordern Impact-Bewertung (DI-009); Auditierbarkeit bei Versionierung (Abschnitt 3) |
| Traceability bis zur Quelle | Leitprinzip 5; [TRACEABILITY_MODEL.md](../05-traceability/TRACEABILITY_MODEL.md) | [L15], [L16]; Kette Eingabe → Regel → Requirement → Quelle (Abschnitt 2.7) |
| Lebenszyklusbezug der Anforderungen | `lifecycle_phases` im `RR`-Katalog | Traceability über Entwicklungs- und Wartungsphasen [L15]; Ausweisung nach SR-041 |
| Evidence Mapping | SR-015, SR-017, SR-018; `EvidenceReference` | Verknüpfung von Anforderungen mit Nachweisen [L15]; vorgesehene Maßnahme und Nachweisart nach SR-043 (`RR_MEASURE`) |

**Interaktionskonzept:** Dieses Dokument liefert die wissenschaftliche Grundlage des Interaktionskonzepts (Abschnitte 2, 3 und 8): regelgesteuerte adaptive Frageführung als bestehender Kern, eine fachlich strukturierte Segmentierung mit Übersicht und Rücknavigation als begründbare, aber nicht zwingend belegte Ergänzung, sichtbare Auslöser bedingter Fragen, vorab erklärte Eingabebedingungen und keine Dialogoberfläche als primäres Interaktionsmodell. Zum Zeitpunkt der Recherche war die konkrete Gestaltung offen; sie ist mit Demonstrator D4 entschieden und umgesetzt ([ADR-0007](../decisions/0007-web-application.md), [WEB_APPLICATION.md](../04-architecture/WEB_APPLICATION.md), Abschnitt 8.5).

---

## 10. Exposé-Traceability

| Exposé-Auftrag | Fundstelle | Abschnitt dieses Dokuments | Status |
| --- | --- | --- | --- |
| allgemeine Assistenz- und Interaktionskonzepte (dialog-, formular-, wizardbasiert, Entscheidungsunterstützung) | Abschnitt 3 | 2, 3 | dokumentiert |
| anwendungsspezifische Lösungen im Umfeld MDR-Compliance und Regulatory Affairs | Abschnitte 3 und 7 („aktuelle Veröffentlichungen zur digitalen Unterstützung regulatorischer Prozesse“) | 4, 5 | dokumentiert |
| Vergleich hinsichtlich Vor- und Nachteilen | Abschnitt 3 | 2, 3, 5 | dokumentiert |
| Forschungslücke (Problemstellung) | Abschnitt 2 | 6 | dokumentiert, präzisiert (6.3) |
| Ableitung der Anforderungen an das System | Abschnitte 3 und 4 | 8 | gemappt auf SR-001 bis SR-043; vier Lücken als SR-040 bis SR-043 geschlossen |
| Begründung des Interaktionskonzepts | Abschnitte 3 und 4 | 3, 8, 9 | wissenschaftliche Grundlage dokumentiert; Detailgestaltung mit D4 umgesetzt (8.5) |
| Begründung des Architekturkonzepts | Abschnitte 3 und 4 | 9 | bestehende Entscheidungen hergeleitet |
| Fachliteratur zu Assistenz- und Entscheidungsunterstützungssystemen | Abschnitt 7 | 12.1 | 18 Quellen |
| Arbeitsplan Phase 1 „Stand der Technik (allgemein und anwendungsspezifisch)“ | Abschnitt 6 | 1–7 | abgeschlossen |

---

## 11. Evidenzgrenzen

1. Strukturierte Recherche, kein PRISMA-Systematic-Review; keine bibliometrische Vollständigkeit.
2. Produktaussagen stammen aus Anbieterdokumentation: belegt ist die öffentliche Beschreibung einer Funktion, nicht deren Funktionsfähigkeit, Vollständigkeit oder Qualität. Produktinformationen sind zeitabhängige Herstellerangaben (Stand 27.08.2026); Webseiten wurden nicht archiviert und nicht ins Repository übernommen.
3. `n.ö.n.` ist strikt von `nicht vorhanden` zu unterscheiden; Deterministik und Reproduzierbarkeit kommerzieller Systeme sind aus öffentlicher Dokumentation nicht beurteilbar.
4. Ein Teil der HCI-Evidenz stammt aus Befragungs-, Clinical-Trial- oder Health-IT-Kontexten; die Übertragung auf RegScoutX ist Designinferenz (`D`), kein direkter Nachweis für MDR-/AI-Act-Gap-Analyse.
5. Das im Exposé genannte Beispiel geführter, dialogbasierter Systeme im Steuerbereich wurde in dieser Recherche nicht gesondert untersucht.
6. Die Rechercheausgabe vom 27.08.2026 empfiehlt, die zitierten Produktseiten mit Abrufdatum und gegebenenfalls Screenshots außerhalb des Repositorys zu sichern.
7. In der Rechercheausgabe fehlen eigene URLs für P4SaMD Overview (P03), Complear AI Governance Solutions (P06) und Credo AI Regulatory Alignment (P13) sowie der Seitentitel für P08. Abschnitt 12.2 kennzeichnet diese Lücken.

---

## 12. Quellen

### 12.1 Wissenschaftliche Quellen und Norm

| Kennung | Quelle | Typ | Nachweis | Verwendung |
| --- | --- | --- | --- | --- |
| L01 | Bargas-Avila, J. A.; Orsini, S.; Piosczyk, H.; Urwyler, D.; Opwis, K. (2011): Enhancing online forms: Use format specifications for fields with format restrictions to help respondents. *Interacting with Computers*, 23(1), 33–39. | Journalartikel (peer-reviewt) | DOI 10.1016/j.intcom.2010.08.001 | Fehlerprävention in Formularen |
| L02 | Peytchev, A.; Couper, M. P.; McCabe, S. E.; Crawford, S. D. (2006): Web Survey Design: Paging versus Scrolling. *Public Opinion Quarterly*, 70(4), 596–607. | Journalartikel (peer-reviewt) | DOI 10.1093/poq/nfl028 | Wizard-/Paging-Abgrenzung |
| L03 | Sweller, J. (1988): Cognitive Load During Problem Solving: Effects on Learning. *Cognitive Science*, 12(2), 257–285. | Journalartikel, Grundlagenarbeit | DOI 10.1207/s15516709cog1202_4 | Cognitive Load |
| L04 | Taylor, B. H. (1987): Adaptive Questionnaire Applications. *Proceedings of the Human Factors Society Annual Meeting*, 31(3), 382–385. | Konferenzbeitrag | DOI 10.1177/154193128703100325 | adaptive Fragebögen, Branching |
| L05 | Neururer, S. B.; Hofer, P.; Göbel, G. (2016): An IT-Supported Evaluation Tool for Biobanks Based on International Guidelines to Improve the Biosample Quality. *Studies in Health Technology and Informatics*, 223, 46–53. | Proceedings-Beitrag (peer-reviewt) | DOI 10.3233/978-1-61499-645-3-46 | guideline-basierte Gap-Bewertung (Analogie) |
| L06 | Liu, C.; Yuan, C.; Butler, A. M.; Carvajal, R. D.; Li, Z. R.; Ta, C. N.; Weng, C. (2019): DQueST: dynamic questionnaire for search of clinical trials. *JAMIA*, 26(11), 1333–1343. | Journalartikel (peer-reviewt) | DOI 10.1093/jamia/ocz121 | dynamische Fragenauswahl |
| L07 | Laranjo, L.; Dunn, A. G.; Tong, H. L.; Kocaballi, A. B.; Chen, J.; Bashir, R.; Surian, D.; Gallego, B.; Magrabi, F.; Lau, A. Y. S.; Coiera, E. (2018): Conversational agents in healthcare: a systematic review. *JAMIA*, 25(9), 1248–1258. | systematischer Review | DOI 10.1093/jamia/ocy072 | Conversational Agents |
| L08 | Kim, S.; Lee, J.; Gweon, G. (2019): Comparing Data from Chatbot and Web Surveys: Effects of Platform and Conversational Style on Survey Response Quality. *Proceedings of CHI 2019*, Paper 86. | Konferenzbeitrag (peer-reviewt) | DOI 10.1145/3290605.3300316 | Chatbot vs. Webformular |
| L09 | Zarouali, B.; Araujo, T.; Ohme, J.; de Vreese, C. (2024): Comparing Chatbots and Online Surveys for (Longitudinal) Data Collection: An Investigation of Response Characteristics, Data Quality, and User Evaluation. *Communication Methods and Measures*, 18(1), 72–91. | Journalartikel (peer-reviewt) | DOI 10.1080/19312458.2022.2156489 | Gegenbefund zu Chatbot-Vorteilen |
| L10 | Maxwell, J. C.; Antón, A. I. (2009): Checking Existing Requirements for Compliance with Law Using a Production Rule Model. *Second International Workshop on Requirements Engineering and Law*, 1–6. | Workshop-Beitrag (peer-reviewt) | DOI 10.1109/RELAW.2009.3 | Produktionsregeln, Legal Compliance |
| L11 | Governatori, G. (2013): Business Process Compliance: An Abstract Normative Framework. *it – Information Technology*, 55(6), 231–238. | Journalartikel (peer-reviewt) | DOI 10.1515/itit.2013.2003 | formale normative Compliance |
| L12 | Governatori, G.; Shek, S. (2013): Regorous: A business process compliance checker. *Proceedings of ICAIL 2013*, 245–246. | Konferenzbeitrag (peer-reviewt) | DOI 10.1145/2514601.2514638 | regelbasierter Compliance Checker |
| L13 | Hasan, M. M. (2016): Regulatory Requirements Compliance in Requirements Engineering: A Systematic Classification and Analysis. *International Journal of Systems and Service-Oriented Engineering*, 6(4), 22–35. | systematischer Literaturreview | DOI 10.4018/IJSSOE.2016100102 | regulatorisches Requirements Engineering |
| L14 | Rudin, C. (2019): Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1, 206–215. | Perspective | DOI 10.1038/s42256-019-0048-x | inhärente Interpretierbarkeit (ergänzend) |
| L15 | Regan, G.; Mc Caffery, F.; Mc Daid, K.; Flood, D. (2013): Medical device standards' requirements for traceability during the software development lifecycle and implementation of a traceability assessment model. *Computer Standards & Interfaces*, 36(1), 3–9. | Journalartikel (peer-reviewt) | DOI 10.1016/j.csi.2013.07.012 | Traceability in der MDSW-Entwicklung |
| L16 | Mucha, J.; Kaufmann, A.; Riehle, D. (2024): A systematic literature review of pre-requirements specification traceability. *Requirements Engineering*, 29, 119–141. | systematischer Review | DOI 10.1007/s00766-023-00412-z | Quellen-/Pre-Requirement-Traceability |
| L17 | Fanfani, M.; Ipsaro Palesi, L. A.; Nesi, P. (2026): Human-Centered AI for Decision Support Systems: A Systematic Review of Application Domains, Architecture Designs, Current Trends and Future Directions. *Big Data and Cognitive Computing*, 10(6), 186. | systematischer Review | DOI 10.3390/bdcc10060186 | DSS: Transparenz, Verlässlichkeit, menschliche Aufsicht |
| L18 | ISO (2020): ISO 9241-110:2020, Ergonomics of human-system interaction — Part 110: Interaction principles. Edition 2. | Internationale Norm (Grundlage, nicht im Projektquellenregister) | https://www.iso.org/standard/75258.html (laut Research 2025 als aktuell bestätigt) | Interaktionsprinzipien |

Anzahl nach Typ: 7 Journalartikel (L01, L02, L03, L06, L09, L11, L15), 4 systematische Reviews (L07, L13, L16, L17), 5 Konferenz-, Proceedings- bzw. Workshop-Beiträge (L04, L05, L08, L10, L12), 1 Perspective (L14), 1 Internationale Norm (L18) – insgesamt 18. ISO 9241-110 ist eine HCI-Grundlage und wird bewusst nicht als regulatorische `SRC` registriert.

### 12.2 Produkt- und Webquellen (Hersteller-/Anbieterdokumentation)

Alle Angaben: Hersteller-/Anbieterdokumentation, Abruf 27.08.2026, zeitabhängig; keine unabhängigen Wirksamkeitsstudien. Keine Webseitenkopien im Repository.

| Kennung | Anbieter | Seitentitel | URL | Verwendungszweck |
| --- | --- | --- | --- | --- |
| P01 | Leida AI | Automated compliance for medical devices | https://leida.ai/ | MDR/AI Act, Requirements, Source Traceability, Evidence, Lifecycle |
| P02 | Mia-Care | P4SaMD Regulatory Coverage | https://docs.mia-care.io/docs/p4samd/regulatory-coverage/ | SaMD, MDR, AI Act, Lifecycle, Traceability |
| P03 | Mia-Care | Brownfield Import Overview (Handbook Products) | https://docs.mia-care.io/docs/p4samd/handbook/products/ (wie im Research zitiert) | sechsstufiger Guided Wizard, Gap-Analyse; zusätzlich P4SaMD Overview (URL im Research-Input nicht angegeben) |
| P04 | DLG:MDR (MDRAIR Ready) | Regulatory Decision Support for Health AI under EU MDR and the EU AI Act | https://www.mdraiready.eu/ | MDR+AI-Act-Interaktion, Reasoning, Source Trace, Evidence Gaps |
| P05 | CertHub | KI-Konformitätsprüfung & Gap-Analyse | https://www.certhub.de/de/ai-conformity-checker | MDR-Gap-Analyse, Audit-/TechDoc-Prüfung (EU AI Act n.ö.n.) |
| P06 | Complear | Complear OS Platform; AI Governance Solutions | https://complear.com/health/platform/ (AI Governance Solutions: URL im Research-Input nicht angegeben) | agentische Compliance, MDR, AI Act, Human-in-the-Loop |
| P07 | MoniDoseQMS | Built for the EU AI Act / EU AI Act Module Suite (Veröffentlichung April/Mai 2026) | https://monidoseqms.com/news/built-for-the-eu-ai-act | Integration AI Act mit Device-QMS/Evidence |
| P08 | MoniDoseQMS | Startseite (Seitentitel im Research-Input nicht angegeben) | https://monidoseqms.com/ | Matrixangaben zur Interaktion |
| P09 | Rimsys | Medical Device Standards and GSPR Managed in One Platform | https://www.rimsys.io/solutions/standards-essential-principles | RIM, Standards/GSPR, Change Impact, Lifecycle Trace |
| P10 | Greenlight Guru | Medical Device Design Control Software | https://www.greenlight.guru/design-control-software | Design Controls, Risk, Traceability, Evidence |
| P11 | Jama Software | Medical Device Requirements Management Software | https://www.jamasoftware.com/solutions/medtech/ | Requirements/Risk/V&V Traceability, EU MDR, IEC 62304 |
| P12 | Credo AI | Vendor Compliance | https://www.credo.ai/solutions/vendor-compliance | AI Act, Evidence, Assessments, Reporting |
| P13 | Credo AI | Regulatory Alignment | URL im Research-Input nicht angegeben | AI Act, Evidence, Assessments, Reporting |

---

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: strukturierte State-of-the-Art-/Scoping-Recherche (Stand 27.08.2026) zu Assistenz- und Interaktionskonzepten und Regulatory-/MedTech-Lösungen; Vergleich ohne Bewertungsskala, Vergleichsmatrix mit Legende `ja`/`teilw.`/`n.ö.n.`, CertHub-Quellenkorrektur (EU AI Act `n.ö.n.`), Forschungslücke bezogen auf den untersuchten Bestand, Abgrenzung, 12 Design Implications mit Abgleich gegen SR-001 bis SR-039 und Architektur (6 COVERED, 5 PARTIAL, 1 GAP), 4 `PROPOSED_SR_GAP` (nicht angelegt), Herleitung bestehender Architekturentscheidungen, Exposé-Traceability, 18 wissenschaftliche Quellen und 13 Produktquellen. |
| 1.1 | Abschnitt 8.4: vier `PROPOSED_SR_GAP` durch SR-040 bis SR-043 geschlossen (SR_CATALOG 0.3, DATA_MODEL 0.4); Status nachher 9 COVERED, 3 PARTIAL (nur Interaktionskonzept), 0 GAP; Abschnitte 9 und 10 fortgeschrieben. |
| 1.2 | Abschnitt 8.5: DI-001, DI-004 und DI-006 durch das umgesetzte Interaktionskonzept des Demonstrators D4 geschlossen ([WEB_APPLICATION.md](../04-architecture/WEB_APPLICATION.md), TC-055 bis TC-057); Status 12 COVERED, 0 PARTIAL, 0 GAP. Keine Änderung an Recherche, Quellen oder SR. |
| 1.3 | Redaktionell an den umgesetzten Stand angeglichen: Hinweise zum offenen Interaktionskonzept (Abschnitte 8.4, 9, 10) und zum noch nicht befüllten Maßnahmenkatalog (8.3, 8.4) als damaliger Stand gekennzeichnet; Abschnitt 7 präzisiert („durchgängige Traceability im definierten Untersuchungsumfang“). Keine Änderung an Recherche, Quellen, Design Implications oder Abgleichsergebnissen. |
| 1.4 | Abschnitt 8.4: Stand des Maßnahmenkatalogs (`RR_MEASURE` 0.2) nachgetragen. Keine Änderung an Recherche, Quellen oder Design Implications. |
| 1.5 | Datumsberichtigung auf ausdrückliche Bestätigung des Verfassers: Recherche, zugrunde liegende Research-Antwort und Anbieterabrufe erfolgten am 27.08.2026. Die bisherigen Septemberangaben sind entsprechend korrigiert. Keine erneute Recherche oder Änderung an Quellen, fachlichen Befunden und Design Implications; Git-Ablagezeiten bleiben unverändert. |
