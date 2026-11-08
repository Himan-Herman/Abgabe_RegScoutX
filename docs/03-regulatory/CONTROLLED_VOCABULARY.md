# Kontrolliertes Vokabular (Themencluster und Lebenszyklusphasen)

Version 1.0 · Status: aktiv

Diese Datei ist die führende Definition der zulässigen Werte für die Pflichtattribute `Themencluster` und `Lebenszyklusphase` regulatorischer Anforderungen (`RR`) gemäß [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 6. Andere Dokumente verwenden ausschließlich die hier festgelegten Werte.

Der Untersuchungsumfang folgt den in [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 4 genannten Themenclustern und der dort festgehaltenen Abgrenzung; die Quellenbasis ist in [SOURCES.md](SOURCES.md) geführt.

Die Werte sind **projektinterne Ordnungskategorien** für die Gap-Analyse. Sie sind keine Rechtsbegriffe und keine Gliederung eines Regelwerks. Aus der Zuordnung folgt keine regulatorische Aussage; die normative Grundlage einer Anforderung ergibt sich ausschließlich aus ihrem Quellen-Lokator.

---

## 1. Themencluster

Verbindlich sind genau diese acht Werte. Weitere Werte sind unzulässig.

### 1.1 Qualitäts- und Risikomanagement
*English: Quality and Risk Management*

**Definition:** Anforderungen an die organisatorischen und prozessualen Vorkehrungen, mit denen ein Hersteller die Konformität eines Produkts systematisch plant, steuert, nachweist und aufrechterhält, sowie an die systematische Identifikation, Bewertung, Beherrschung und Überwachung von Risiken über den Produktlebenszyklus.

**Abgrenzung:** Erfasst die Managementsysteme und ihre Prozesse, nicht die technischen Produkteigenschaften, die daraus folgen. Technische Ergebnisse einer Risikobeherrschung gehören in den Cluster, der ihren primären Gegenstand beschreibt (z. B. `Robustheit` oder `Gebrauchstauglichkeit`).

**Hinweis zur Granularität:** Qualitäts- und Risikomanagement bleiben auf oberster Ebene bewusst ein gemeinsamer Cluster. Das entspricht der Abstraktionsebene der Themencluster im Exposé. Eine feinere Trennung wird erst vorgenommen, wenn die Anforderungsextraktion sie nachweislich erfordert; eine solche Änderung wäre eine Scope-Entscheidung und zu begründen.

### 1.2 Data Governance
*English: Data Governance*

**Definition:** Anforderungen an Herkunft, Eignung, Qualität, Repräsentativität, Aufbereitung, Verwaltung und Dokumentation der Daten, die für Entwicklung, Training, Validierung, Prüfung und Betrieb eines KI-basierten Produkts verwendet werden.

**Abgrenzung:** Betrifft die Daten und ihre Steuerung, nicht das Verhalten des Systems im Betrieb (`Robustheit`) und nicht die Information von Nutzenden über das System (`Transparenz`). Datenschutzrechtliche Anforderungen sind nicht Gegenstand dieses Clusters (siehe Abschnitt 4).

### 1.3 Transparenz
*English: Transparency*

**Definition:** Anforderungen an die Bereitstellung von Informationen über Zweckbestimmung, Funktionsweise, Leistungsgrenzen, Voraussetzungen und Ergebnisse eines Systems, sodass Ausgaben durch die vorgesehenen Adressaten sachgerecht interpretiert werden können.

**Abgrenzung:** Betrifft die Information selbst und ihre Bereitstellung. Ob und wie ein Mensch auf dieser Grundlage eingreifen kann, gehört zu `Menschliche Aufsicht`; ob die Information ergonomisch erfassbar dargeboten wird, zu `Gebrauchstauglichkeit`. Interne Nachweisdokumentation gegenüber Behörden oder Benannten Stellen bildet keinen eigenen Cluster (siehe Abschnitt 4).

### 1.4 Menschliche Aufsicht
*English: Human Oversight*

**Definition:** Anforderungen an die Vorkehrungen, die natürlichen Personen die Beaufsichtigung eines Systems im Betrieb ermöglichen — insbesondere Überwachung, Interpretation, Eingriff, Übersteuerung und Abschaltung sowie die dafür erforderlichen Kompetenzen und Zuständigkeiten.

**Abgrenzung zu `Gebrauchstauglichkeit`:** `Menschliche Aufsicht` betrifft die **Kontrollfähigkeit** über das System — ob eine Person die Funktionsweise erkennen, einordnen und wirksam eingreifen kann. `Gebrauchstauglichkeit` betrifft die **Bedienbarkeit** der Benutzungsschnittstelle und die Vermeidung von Anwendungsfehlern. Eine Anforderung, die Eingriffs- oder Übersteuerungsmöglichkeiten verlangt, gehört zu `Menschliche Aufsicht`; eine Anforderung an die Gestaltung und Evaluierung der Benutzungsschnittstelle zu `Gebrauchstauglichkeit`.

### 1.5 Robustheit
*English: Robustness*

**Definition:** Anforderungen an Genauigkeit, Zuverlässigkeit, Konsistenz und Widerstandsfähigkeit des Systemverhaltens, einschließlich des Verhaltens bei Fehlern, Störungen, unerwarteten Eingaben und über die Betriebsdauer.

**Abgrenzung:** Der Cluster wird **nicht** eigenmächtig zu einem vollständigen Cybersecurity- oder allgemeinen Software-Sicherheitscluster erweitert. Sicherheitsbezogene Aspekte werden nur insoweit erfasst, wie sie im Untersuchungsumfang unmittelbar an Genauigkeit, Zuverlässigkeit und Widerstandsfähigkeit anknüpfen. Eine umfassendere Cybersecurity-Taxonomie wäre eine Scope-Erweiterung und ist derzeit nicht Gegenstand der Arbeit.

### 1.6 Post-Market-Monitoring
*English: Post-Market Monitoring*

**Definition:** Anforderungen an die systematische, planmäßige Sammlung, Analyse und Bewertung von Erkenntnissen über ein bereits in Verkehr gebrachtes Produkt.

**Abgrenzung:** Betrifft die planmäßige Beobachtung und Auswertung. Vigilanz im Sinne der ereignisbezogenen Melde- und Sicherheitskorrekturpflichten bildet keinen eigenen Hauptcluster (siehe Abschnitt 4). Änderungen, die aus Beobachtungsergebnissen folgen, gehören zu `Software-Lebenszyklus` bzw. zur Lebenszyklusphase `Änderung und Wartung`.

### 1.7 Software-Lebenszyklus
*English: Software Life Cycle*

**Definition:** Anforderungen an die Prozesse der Softwareentwicklung und -pflege, insbesondere Planung, Architektur und Entwurf, Implementierung, Integration, Verifikation, Konfigurations- und Problemlösungsmanagement sowie Änderungssteuerung.

**Abgrenzung — wichtig:** `Software-Lebenszyklus` ist ein **Themencluster** und darf **nicht** mit dem Attribut `Lebenszyklusphase` (Abschnitt 3) gleichgesetzt werden. Der Cluster beschreibt den inhaltlichen Gegenstand einer Anforderung; die Lebenszyklusphase beschreibt, wann sie gilt oder zu erfüllen ist. Eine Anforderung mit dem Cluster `Software-Lebenszyklus` kann jeder Phase zugeordnet sein, und Anforderungen anderer Cluster können ebenfalls Phasen tragen.

### 1.8 Gebrauchstauglichkeit
*English: Usability*

**Definition:** Anforderungen an die Analyse, Spezifikation, Gestaltung und Evaluierung der Benutzungsschnittstelle im Hinblick auf sichere Anwendung, insbesondere zur Vermeidung von Anwendungsfehlern im normalen Gebrauch.

**Abgrenzung:** Siehe 1.4. Zusätzlich abzugrenzen von `Transparenz`: Welche Information bereitgestellt werden muss, ist `Transparenz`; wie sie erfassbar und fehlerarm dargeboten wird, ist `Gebrauchstauglichkeit`.

---

## 2. Zuordnungsregel Themencluster

**Verbindlich: Jede atomare `RR` erhält genau einen Themencluster.**

- Maßgeblich ist der **primäre normative Gegenstand der atomaren Verpflichtung** — also das, was die Verpflichtung selbst verlangt, nicht das Kapitel, in dem sie steht.
- Enthält eine Fundstelle mehrere voneinander getrennt prüfbare Verpflichtungen mit unterschiedlichem Gegenstand, werden diese bei der Extraktion als **getrennte atomare `RR`** geführt und erhalten jeweils ihren eigenen Cluster.
- Bloße Querverweise, thematische Wechselwirkungen oder Rückkopplungen zwischen Clustern rechtfertigen **keine** Mehrfachklassifikation.
- Es gibt **kein** Primär-/Sekundärcluster-Modell und keine Mehrfachzuordnung.

Begründung: Eindeutige Zuordnung hält die Gap-Auswertung reproduzierbar und verhindert, dass dieselbe Lücke in mehreren Clustern doppelt gezählt wird.

---

## 3. Lebenszyklusphasen

Verbindlich sind genau diese sieben Werte. Weitere Werte sind unzulässig.

### 3.1 Planung und Konzeption
*English: Planning and Conception*

**Definition:** Festlegung von Zweckbestimmung, Anwendungskontext, Nutzergruppen, Anforderungen und Planungsgrundlagen vor der technischen Realisierung.

**Abgrenzung:** Endet mit der festgelegten Anforderungs- und Planungsgrundlage; die technische Umsetzung gehört zu 3.2.

### 3.2 Entwicklung und Realisierung
*English: Development and Realisation*

**Definition:** Entwurf, Implementierung, Integration und Herstellung des Produkts einschließlich der Erzeugung der zugehörigen Entwicklungsdokumentation.

**Abgrenzung:** Umfasst die Erstellung, nicht den planmäßigen Nachweis der Erfüllung (3.3).

### 3.3 Verifikation und Validierung
*English: Verification and Validation*

**Definition:** Planmäßiger Nachweis, dass festgelegte Anforderungen erfüllt sind und das Produkt seine Zweckbestimmung im vorgesehenen Anwendungskontext erfüllt.

**Abgrenzung:** Betrifft die Nachweisführung durch den Hersteller. Die verfahrensrechtliche Bewertung der Konformität gehört zu 3.4.

### 3.4 Konformitätsbewertung
*English: Conformity Assessment*

**Definition:** Durchführung des vorgesehenen Konformitätsbewertungsverfahrens einschließlich der Bereitstellung der dafür erforderlichen Nachweise und, soweit einschlägig, der Einbindung einer Benannten Stelle.

**Abgrenzung:** Als **Lebenszyklusphase** bezeichnet dieser Wert den zeitlichen Abschnitt, in dem eine Anforderung gilt oder zu erfüllen ist. Konformitätsbewertung ist dagegen **kein** Themencluster (siehe Abschnitt 4).

### 3.5 Inverkehrbringen, Inbetriebnahme und Betrieb
*English: Placing on the Market, Putting into Service and Operation*

**Definition:** Erstmaliges Inverkehrbringen des Produkts, Inbetriebnahme und anschließende bestimmungsgemäße Verwendung im Betrieb.

**Abgrenzung:** Betrifft den regulären Betrieb. Die planmäßige Beobachtung des Produkts nach Inverkehrbringen gehört zu 3.6.

### 3.6 Post-Market-Überwachung
*English: Post-Market Monitoring and Surveillance*

**Definition:** Planmäßige Beobachtung, Sammlung und Auswertung von Erkenntnissen über das in Verkehr gebrachte Produkt sowie die daraus abgeleitete Bewertung.

**Abgrenzung zum gleichnamigen Themencluster:** 3.6 beschreibt den **Zeitabschnitt**, `Post-Market-Monitoring` (1.6) den **Gegenstand** einer Anforderung. Beide sind unabhängig voneinander zuzuordnen.

### 3.7 Änderung und Wartung
*English: Modification and Maintenance*

**Definition:** Geplante oder anlassbezogene Änderung, Korrektur, Aktualisierung und Pflege des Produkts nach Inverkehrbringen einschließlich der Bewertung der Auswirkungen einer Änderung.

**Abgrenzung:** Betrifft Eingriffe in das Produkt. Die reine Beobachtung ohne Eingriff gehört zu 3.6.

**Keine achte Phase:** Außerbetriebnahme, Stilllegung und Entsorgung werden bewusst **nicht** als eigene Phase geführt, da sie im Untersuchungsumfang dieser Arbeit kein untersuchter Gap-Bereich sind (siehe Abschnitt 4).

---

## 4. Zuordnungsregel Lebenszyklusphasen

**Verbindlich: Jede `RR` erhält mindestens eine Lebenszyklusphase.**

- Mehrere Werte sind zulässig, wenn dieselbe atomare Verpflichtung tatsächlich in mehreren Phasen gilt oder in mehreren Phasen erfüllt werden muss.
- Es gibt **kein** Primär-/Sekundärmodell; mehrfach zugeordnete Phasen sind gleichrangig.
- Ein Sammelwert wie `lebenszyklusübergreifend` wird **nicht** eingeführt. Gilt eine Verpflichtung über mehrere Phasen, werden die zutreffenden Phasen einzeln angegeben.

Begründung: Einzelne Phasenangaben bleiben auswertbar; ein Sammelwert würde die Phasenzuordnung ihrer Aussagekraft berauben.

---

## 5. Scope-Abgrenzung der Themencluster

Die folgenden Bereiche bilden derzeit **keine eigenen Gap-Themencluster**. Das ist eine bewusste Begrenzung des Untersuchungsumfangs gemäß der Abgrenzung in [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 4 und keine Aussage über ihre regulatorische Bedeutung:

- technische Dokumentation als vollständiger eigener Compliance-Bereich,
- klinische bzw. leistungsbezogene Bewertung als eigener vollständiger Bereich,
- Qualifikation,
- Klassifizierung,
- regulatorische Einordnung,
- Konformitätsbewertung,
- Vigilanz als eigener Hauptcluster,
- Datenschutz und DSGVO,
- allgemeine Ethik- und Grundrechte-Taxonomie,
- vollständige Hersteller- und Wirtschaftsakteurspflichten,
- behördliche Marktüberwachung,
- Produktion und Herstellung als eigener Softwarecluster,
- Außerbetriebnahme und Entsorgung als eigener untersuchter Gap-Bereich.

**Wichtige Klarstellung:** Qualifikation und Klassifizierung sind damit **nicht** aus dem Gesamtsystem ausgeschlossen. Sie gehören zur vorgelagerten Applicability- und Entscheidungslogik und werden dort über Entscheidungsregeln (`RUL`) abgebildet — nicht über die Gap-Themencluster-Taxonomie. Konformitätsbewertung erscheint aus demselben Grund als Lebenszyklusphase (3.4), aber nicht als Themencluster.

---

## 6. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: acht Themencluster, sieben Lebenszyklusphasen, Zuordnungsregeln und Scope-Abgrenzung festgelegt. |
