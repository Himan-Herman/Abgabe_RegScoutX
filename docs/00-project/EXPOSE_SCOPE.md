# Exposé (bereinigte Fassung) – verbindlicher wissenschaftlicher Rahmen

## Status und Zweck dieses Dokuments

Dieses Dokument gibt den Inhalt des bei den Prüfern eingereichten und akzeptierten Exposés zur Masterarbeit wieder. Es ist innerhalb dieses Repositories die verbindliche wissenschaftliche Referenz für Problemstellung, Zielstellung, Scope, erwartete Ergebnisse, Evaluationskonzept und Arbeitsplan.

Das Exposé definiert den wissenschaftlichen Mindestumfang, nicht die maximale technische Qualität. Technische Erweiterungen sind zulässig, solange keine Aussage dieses Dokuments verletzt wird. Widerspricht eine geplante Änderung dem Exposé, ist dies vor der Umsetzung ausdrücklich zu kennzeichnen und zu klären.

| Merkmal | Angabe |
| --- | --- |
| Dokumenttyp | Bereinigte Wiedergabe des genehmigten Exposés |
| Stand des Originals | Juli 2026 |
| Studiengang | Master Nachhaltige Gesundheitstechnologien |
| Geplanter Bearbeitungsbeginn | 1. August 2026 |
| Version dieses Dokuments | 1.0 |

### Provenienz und Bereinigung

- Das vollständige Original-Exposé (PDF) wird ausschließlich lokal unter `private/` vorgehalten und ist über `.gitignore` von der Versionierung ausgeschlossen.
- Diese Fassung ist inhaltlich unverändert; es wurden keine fachlichen Aussagen ergänzt, gestrichen oder umformuliert. Die Gliederung des Originals (Abschnitte 1–7) bleibt erhalten.
- Entfernt wurden ausschließlich personenbezogene Angaben: Name der verfassenden Person, Matrikelnummer sowie Namen von Erst- und Zweitprüfer.
- Rein formale Anpassungen: Auszeichnung als Markdown, Tabellendarstellung des Arbeitsplans.

---

## 1. Vorläufiger Titel

Entwicklung und Evaluation eines regelbasierten Assistenzsystems zur integrierten Anforderungs- und Gap-Analyse nach MDR und EU AI Act für KI-basierte Medizinproduktesoftware

## 2. Problemstellung

KI-basierte Medizinproduktesoftware kann gleichzeitig der Medizinprodukteverordnung (MDR, Verordnung (EU) 2017/745) und dem EU AI Act (Verordnung (EU) 2024/1689) unterliegen. Die gemeinsame Leitlinie AIB 2025-1 / MDCG 2025-6 (Juni 2025) erläutert erstmals das Zusammenspiel beider Regelwerke: KI-basierte Medizinproduktesoftware ab Klasse IIa kann aufgrund des erforderlichen Konformitätsbewertungsverfahrens unter Einbindung einer Benannten Stelle als Hochrisiko-KI-System gemäß Art. 6 Abs. 1 EU AI Act einzustufen sein. Damit treffen Anforderungen an Qualitäts- und Risikomanagement, technische Dokumentation, Datenqualität, Transparenz, menschliche Aufsicht und Robustheit aufeinander.

Insbesondere für kleine und mittlere Hersteller ohne eigene Regulatory-Abteilung ist häufig nicht unmittelbar erkennbar, welche konkrete technische, organisatorische oder dokumentarische Maßnahme aus einer regulatorischen Anforderung folgt. Es fehlt ein direkt nutzbares, phasenbezogenes Modell, das Anforderungen beider Regelwerke strukturiert zusammenführt und mit konkreten Maßnahmen und Nachweisen verknüpft. Etablierte Assistenzkonzepte aus anderen Domänen – etwa geführte, dialogbasierte Systeme im Steuerbereich – zeigen, dass komplexe regulatorische Anforderungen durch strukturierte Nutzerführung zugänglich gemacht werden können. Nach bisheriger Recherche ist keine öffentlich zugängliche Lösung bekannt, die Anforderungen aus MDR und EU AI Act in der hier vorgesehenen Form integriert, regelbasiert bewertet und in eine nachvollziehbare Gap-Analyse überführt.

## 3. Zielstellung

Ziel der Arbeit ist die Entwicklung und Evaluation eines regelbasierten Assistenzsystems, das anhand strukturierter Produkteingaben (Fragebogen) relevante Anforderungen aus MDR und EU AI Act für einen definierten Typ KI-basierter Medizinproduktesoftware identifiziert, den Erfüllungsstand abgleicht und eine nachvollziehbare Gap-Analyse mit Quellenverweisen erstellt.

Das Konzept des Systems wird aus dem Stand der Technik wissenschaftlich hergeleitet: Zunächst werden allgemeine Assistenz- und Interaktionskonzepte (u. a. dialog-, formular- und wizardbasierte Systeme, Entscheidungsunterstützungssysteme) sowie bestehende anwendungsspezifische Lösungen im Umfeld von MDR-Compliance und Regulatory Affairs untersucht und hinsichtlich ihrer Vor- und Nachteile verglichen. Aus diesem Vergleich werden die Anforderungen an das System und das gewählte Interaktions- und Architekturkonzept begründet abgeleitet.

### Bewertungskriterien der Zielerreichung

- **Korrektheit:** Anteil der im Testfall korrekt identifizierten Anforderungen, gemessen an einer zuvor manuell erstellten Referenzbewertung (Soll-Ergebnis) des Fallbeispiels.
- **Vollständigkeit:** Abdeckung der Gap-Analyse innerhalb des definierten Untersuchungsumfangs gegenüber der Referenzbewertung.
- **Reproduzierbarkeit:** Identische Eingaben führen zu identischen Ergebnissen; jede Ausgabe ist bis zur regulatorischen Quelle rückverfolgbar.
- **Nachvollziehbarkeit:** Strukturierte Bewertung der Ergebnisberichte anhand definierter Kriterien (Verständlichkeit, Konsistenz, Quellenbezug); soweit organisatorisch möglich ergänzt um ein fachliches Review.

## 4. Erwartetes Ergebnis

- Ein aus dem Stand der Technik abgeleiteter und begründeter Konzeptentwurf (Anforderungen an das System, Interaktions- und Architekturkonzept).
- Ein quellenbasierter, versionierter Anforderungskatalog für die ausgewählten Themencluster (u. a. Qualitäts- und Risikomanagement, Data Governance, Transparenz, menschliche Aufsicht, Robustheit, Post-Market-Monitoring) aus MDR, AI Act, einschlägigen MDCG-Leitlinien und ausgewählten Normen (ISO 13485, ISO 14971, IEC 62304, IEC 62366-1).
- Eine Traceability-Matrix, die jede Anforderung mit Quelle, Lebenszyklusphase, Maßnahme und Nachweisdokument verknüpft, sowie eine formalisierte, regelbasierte Entscheidungs- und Gap-Logik.
- Ein funktionsfähiger webbasierter Demonstrator (strukturierter Fragebogen, Regelverarbeitung, Gap-Darstellung, automatisch erzeugter Ergebnisbericht mit Quellenverweisen). Der Demonstrator ist bewusst regelbasiert und ohne generative KI ausgeführt, um Reproduzierbarkeit und Prüfbarkeit zu gewährleisten; eine spätere KI-gestützte Erweiterung (z. B. adaptive Befragung) wird im Ausblick skizziert.
- Eine dokumentierte Evaluation anhand von Testfällen und einer vollständigen Fallstudie.

**Abgrenzung:** Die Arbeit bildet weder MDR noch AI Act vollständig ab, sondern beschränkt sich auf definierte Themencluster und ein Fallbeispiel. Der Demonstrator ist ein Prüfmittel für die entwickelte Methodik, kein Produktivsystem; er ersetzt keine juristische Beratung, Zertifizierung oder behördliche Konformitätsbewertung.

## 5. Geplante Evaluation

- **Logikverifikation:** Überprüfung der Entscheidungsregeln anhand definierter Testfälle mit erwarteten Soll-Ergebnissen (u. a. Grenzfälle der Qualifikation und Klassifikation).
- **Fallstudie:** Vollständige Anwendung des Systems auf ein beschriebenes Szenario einer KI-basierten Medizinproduktesoftware (z. B. ein KI-gestützter Symptomchecker, voraussichtlich Klasse IIa nach Regel 11). Verglichen wird das Systemergebnis mit einer vorab manuell erstellten Referenzbewertung; Abweichungen werden analysiert und dokumentiert.
- **Kriteriengestützte Bewertung:** Bewertung von Nachvollziehbarkeit, Konsistenz, Quellenrückverfolgbarkeit und Verständlichkeit der Ergebnisberichte anhand definierter Kriterien; soweit organisatorisch möglich, ergänzt um ein strukturiertes fachliches Review. Die Auswertung erfolgt primär qualitativ-deskriptiv.

## 6. Grober Arbeitsplan

| Phase | Inhalt |
| --- | --- |
| 1 | Stand der Technik (allgemein und anwendungsspezifisch), Quellenanalyse, Scope-Festlegung, Anforderungsextraktion |
| 2 | Konzeptableitung, Traceability-Matrix, Entscheidungs- und Gap-Logik |
| 3 | Prototypische Umsetzung des webbasierten Demonstrators |
| 4 | Evaluation (Testfälle, Fallstudie, kriteriengestützte Bewertung) und schriftliche Ausarbeitung |

Geplanter Bearbeitungsbeginn: 1. August 2026.

## 7. Vorläufige Kernquellen

- Verordnung (EU) 2017/745 über Medizinprodukte (MDR); Verordnung (EU) 2024/1689 über künstliche Intelligenz (EU AI Act).
- AIB 2025-1 / MDCG 2025-6: Interplay between the MDR/IVDR and the AI Act, Juni 2025; MDCG 2019-11 Rev. 1, Juni 2025.
- ISO 13485:2016; ISO 14971:2019; IEC 62304:2006 + A1:2015; IEC 62366-1:2015 + A1:2020.
- Ergänzend: Fachliteratur zu Assistenz- und Entscheidungsunterstützungssystemen sowie aktuelle Veröffentlichungen zur digitalen Unterstützung regulatorischer Prozesse bei Medizinprodukten.

---

## Verwendung im Projekt

Bei jeder Aufgabe gilt die Kette:

**Exposé → wissenschaftliche Anforderung → technische Umsetzung → Test → Evidenz → Dokumentation → Traceability.**

Verweise auf dieses Dokument erfolgen abschnittsgenau, z. B. `EXPOSE_SCOPE.md#4-erwartetes-ergebnis`. Die dafür verwendeten Identifikatoren sind in [DOCUMENTATION_CONVENTIONS.md](DOCUMENTATION_CONVENTIONS.md) festgelegt.
