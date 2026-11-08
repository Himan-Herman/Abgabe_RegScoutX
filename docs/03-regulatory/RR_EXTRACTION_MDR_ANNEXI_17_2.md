# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 17.2

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.17.2` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Kernbereich |
| Expected Theme | Software-Lebenszyklus |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.26 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M17_2-A` bis `M17_2-E` sind ausschließlich temporäre Evidenzkennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Neue MDR-Gap-`RR`-Kandidaten | **5** — `M17_2-A` bis `M17_2-E` |
| davon regulär | 5 |
| davon conditional | 0 |
| MDR-intern deduplizierte Atome | 0 |
| Unresolved | 0 |
| Deferred | 0 |
| Out-of-Scope-Atome | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 5 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Quellenstruktur

`SRC-001#Anh.I/Nr.17.2` besteht aus genau einem grammatischen Satz. Primary-Locator für alle finalen Kandidaten ist deshalb `SRC-001#Anh.I/Nr.17.2`. Ein künstliches `/Satz.1` wird **nicht** gebildet, weil es keine zusätzliche sachliche Präzision erzeugt.

| Strukturelement | Inhalt |
| --- | --- |
| Applicability | Produkt enthält Software **oder** Software ist selbst ein Produkt |
| Gemeinsamer Handlungsrahmen | entwickelt und hergestellt / `developed and manufactured` |
| Qualitätsmaßstab | Stand der Technik / `state of the art` |
| Zu berücksichtigende Grundsätze | Software-Lebenszyklus / `development life cycle` · Risikomanagement einschließlich Informationssicherheit · Verifizierung · Validierung |

---

## 4. Vollständige `0 / 1 / n`-Prüfung

| Aussage | Ergebnis | Kandidat |
| --- | --- | --- |
| Applicability (Produktkategorien) | 0 eigene `RR` | — |
| entwickelt und hergestellt | 0 eigene `RR` | gemeinsamer Handlungsrahmen |
| Stand der Technik | 1 `RR` | `M17_2-A` |
| Software-Lebenszyklus | 1 `RR` | `M17_2-B` |
| Risikomanagement einschließlich Informationssicherheit | 1 `RR` | `M17_2-C` |
| Verifizierung | 1 `RR` | `M17_2-D` |
| Validierung | 1 `RR` | `M17_2-E` |
| **Gesamt** | **5** | |

### 4.1 Applicability

Die Alternativen — Produkt enthält Software, Software ist selbst ein Produkt — sind ausschließlich sachlicher Anwendungsbereich. Sie erzeugen **0** eigene `RR` und sind **nicht** conditional. Die Applicability bleibt in `M17_2-A` vollständig erhalten; in `M17_2-B` bis `M17_2-E` bleibt der gemeinsame Softwareentwicklungs- und Herstellungskontext quellentreu erhalten.

### 4.2 Entwickelt und hergestellt

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | grundsätzlich erfüllbar |
| Split-Bedingung 2 | nicht erfüllt |

„entwickelt und hergestellt" bildet ohne die nachfolgenden Qualifikationen keine zwei eigenständigen vollständigen Compliance-Sollzustände. Es entsteht **keine** `RR` nur für die Entwicklung und **keine** `RR` nur für die Herstellung. Externe Bedeutungen des Begriffs `manufactured` werden **nicht** importiert.

---

## 5. Kandidaten

### M17_2-A — Softwareentwicklung und -herstellung entsprechend dem Stand der Technik

- **Title EN:** Software Development and Manufacture in Accordance with the State of the Art
- **DE:** Der Hersteller muss sicherstellen, dass bei Produkten, zu deren Bestandteilen Software gehört, oder bei Software, die selbst ein Produkt ist, die Software entsprechend dem Stand der Technik entwickelt und hergestellt wird.
- **EN:** The manufacturer shall ensure that, for devices that incorporate software or for software that are devices in themselves, the software is developed and manufactured in accordance with the state of the art.
- **Primary:** `SRC-001#Anh.I/Nr.17.2`
- **Supplementary:** keine
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Der Stand-der-Technik-Maßstab besitzt einen von den vier Prinzipienanforderungen unterscheidbaren vollständigen Compliance-Status.

**MDR-interner Abgleich:** keine Deduplizierung gegen `RR-154` und keine gegen `RR-134`.

**Abgrenzung:** Der Stand der Technik wird **nicht** mit IEC 62304, ISO 14971 oder einer sonstigen einzelnen Norm gleichgesetzt.

### M17_2-B — Berücksichtigung der Grundsätze des Software-Lebenszyklus

- **Title EN:** Consideration of Development Life-Cycle Principles
- **DE:** Der Hersteller muss sicherstellen, dass bei der Entwicklung und Herstellung der Software die Grundsätze des Software-Lebenszyklus berücksichtigt werden.
- **EN:** The manufacturer shall ensure that, in the development and manufacture of the software, the principles of the development life cycle are taken into account.
- **Primary:** `SRC-001#Anh.I/Nr.17.2`
- **Supplementary:** keine
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Source Fidelity:** Im Requirement Text wird der amtliche deutsche Ausdruck „Software-Lebenszyklus" verwendet. Ein synthetischer Begriff wird **nicht** eingeführt; die enger adjudizierte Bedeutung wird ausschließlich in Abschnitt 6 erläutert.

### M17_2-C — Berücksichtigung von Risikomanagementgrundsätzen einschließlich Informationssicherheit bei Softwareentwicklung und -herstellung

- **Title EN:** Consideration of Risk-Management Principles Including Information Security in Software Development and Manufacture
- **DE:** Der Hersteller muss sicherstellen, dass bei der Entwicklung und Herstellung der Software die Grundsätze des Risikomanagements einschließlich der Informationssicherheit berücksichtigt werden.
- **EN:** The manufacturer shall ensure that, in the development and manufacture of the software, the principles of risk management, including information security, are taken into account.
- **Primary:** `SRC-001#Anh.I/Nr.17.2`
- **Supplementary:** keine
- **Theme:** Qualitäts- und Risikomanagement
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Das Risikomanagement bildet einen gegenüber Software-Lebenszyklus, Verifizierung und Validierung eigenständigen Sollzustand. Die Informationssicherheit bleibt zwingender Bestandteil **desselben** Atoms.

### M17_2-D — Berücksichtigung der Grundsätze der Verifizierung

- **Title EN:** Consideration of Verification Principles
- **DE:** Der Hersteller muss sicherstellen, dass bei der Entwicklung und Herstellung der Software die Grundsätze der Verifizierung berücksichtigt werden.
- **EN:** The manufacturer shall ensure that, in the development and manufacture of the software, the principles of verification are taken into account.
- **Primary:** `SRC-001#Anh.I/Nr.17.2`
- **Supplementary:** keine
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Lifecycle-Begründung:** Die Phase `Verifikation und Validierung` wird bewusst **nicht** zugeordnet. Der atomare Gegenstand sind die Verifizierungsgrundsätze; die tatsächliche Erfüllungsphase ist nach der Quellenstruktur die Entwicklung und Herstellung der Software. Der bloße Begriff „Verifizierung" erzeugt **keine** gleichnamige Lebenszyklusphase. Bei einer späteren Softwareänderung mit erneuter Entwicklung bzw. Herstellung gilt dieselbe Pflicht erneut.

### M17_2-E — Berücksichtigung der Grundsätze der Validierung

- **Title EN:** Consideration of Validation Principles
- **DE:** Der Hersteller muss sicherstellen, dass bei der Entwicklung und Herstellung der Software die Grundsätze der Validierung berücksichtigt werden.
- **EN:** The manufacturer shall ensure that, in the development and manufacture of the software, the principles of validation are taken into account.
- **Primary:** `SRC-001#Anh.I/Nr.17.2`
- **Supplementary:** keine
- **Theme:** Software-Lebenszyklus
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Lifecycle-Begründung:** analog zu `M17_2-D`; die Phase `Verifikation und Validierung` wird **nicht** zugeordnet.

**Verifizierung gegenüber Validierung:** Beide bleiben getrennt. Split-Bedingung 1 und Split-Bedingung 2 sind erfüllt: Sie können unabhängig unterschiedliche Compliance-Status besitzen und bilden mit dem gemeinsamen Entwicklungs- und Herstellungsrahmen jeweils vollständige regulatorische Prinzipienanforderungen. Die gleiche Theme-Zuordnung ist **kein** Zusammenführungsgrund.

---

## 6. Multilinguale Adjudikation zu M17_2-B

| Fassung | Ausdruck |
| --- | --- |
| DE | Software-Lebenszyklus |
| EN | `development life cycle` |
| FR | `cycle de développement` |
| IT | `ciclo di vita dello sviluppo` |
| ES | `ciclo de vida del desarrollo` |

| Merkmal | Ergebnis |
| --- | --- |
| Materielle Divergenz | JA |
| Status | RESOLVED |
| Unresolved | 0 |

**Final adjudizierte Bedeutung:** Nr. 17.2 begründet insoweit einen Bezug auf den Softwareentwicklungs- bzw. Development-Life-Cycle innerhalb des ausdrücklichen Entwicklungs- und Herstellungskontexts. Aus dem deutschen Ausdruck allein wird **keine** eigenständige allgemeine Pflicht über den Betrieb, die Post-Market-Überwachung oder den vollständigen Produktlebenszyklus abgeleitet.

Die Divergenz wird **nicht** durch eine Änderung des amtlichen deutschen Begriffs im Requirement Text verdeckt. Es wurde **keine** Mehrheitsregel angewendet und **keine** Sprachfassung priorisiert.

---

## 7. Informationssicherheit

| Fassung | Ausdruck |
| --- | --- |
| DE | Risikomanagement einschließlich der Informationssicherheit |
| EN | `risk management, including information security` |

**Finale Behandlung:** Bestandteil von `M17_2-C`; **keine** eigene `RR`. Die Konjunktion „einschließlich" konkretisiert den Umfang des Risikomanagementgegenstands.

Die Informationssicherheit wird **nicht** gelöscht, **nicht** out-of-scope gesetzt, **nicht** als eigene `RR` abgespalten und **nicht** in einen neuen Cluster verschoben.

| Merkmal | Ergebnis |
| --- | --- |
| Theme `M17_2-C` | Qualitäts- und Risikomanagement |
| Neuer Cybersecurity-Cluster | NEIN |
| Cluster `Robustheit` erweitert | NEIN |
| Inhalte aus `SRC-001#Anh.I/Nr.17.4` importiert | NEIN |

---

## 8. Lifecycle-Audit

| Kandidat | Lebenszyklusphasen |
| --- | --- |
| `M17_2-A` | Entwicklung und Realisierung · Änderung und Wartung |
| `M17_2-B` | Entwicklung und Realisierung · Änderung und Wartung |
| `M17_2-C` | Entwicklung und Realisierung · Änderung und Wartung |
| `M17_2-D` | Entwicklung und Realisierung · Änderung und Wartung |
| `M17_2-E` | Entwicklung und Realisierung · Änderung und Wartung |

Aus Nr. 17.2 werden ausdrücklich **nicht** abgeleitet: allgemeiner Betrieb, allgemeine Post-Market-Überwachung und Konformitätsbewertung. `Änderung und Wartung` bedeutet hier ausschließlich, dass der jeweilige Sollzustand erneut gilt, wenn eine Änderung, Korrektur oder Aktualisierung erneute Softwareentwicklung bzw. -herstellung auslöst.

---

## 9. MDR-interne Deduplizierung

| Bestehende `RR` | Ergebnis |
| --- | --- |
| `RR-116` bis `RR-119` | keine Deduplizierung |
| `RR-133` | keine Deduplizierung |
| `RR-134` | keine Deduplizierung |
| `RR-143` | keine Deduplizierung |
| `RR-144` | keine Deduplizierung |
| `RR-154` | keine Deduplizierung |
| `RR-165` bis `RR-168` | keine Deduplizierung |

**Begründung:** Nr. 17.2 normiert spezifische materielle Anforderungen an die Softwareentwicklung und -herstellung. Die bestehenden QMS- und Risikomanagement-`RR` sowie die Produktzustände aus Nr. 17.1 besitzen keine identischen Erfüllungsstatus.

**MDR-intern vollständig dedupliziert: 0.**

---

## 10. Cross-Article

| Quellenbereich | Behandlung |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.1` | nicht erneut extrahiert; `RR-165` bis `RR-168` stehen nur in fachlicher Beziehung |
| `SRC-001#Anh.I/Nr.17.4` | nicht extrahiert; für `M17_2-C` ist ein späterer Cross-Article-Abgleich vorgemerkt |

Beides ist **kein** zurückgestellter Fall.

---

## 11. Cross-Regulation

| Kandidat | Fachliche Beziehung im AI-Act-Bestand | Ergebnis |
| --- | --- | --- |
| `M17_2-A` | Entwicklungsanforderungen des AI Act | keine Deduplizierung |
| `M17_2-B` | — | keine Deduplizierung |
| `M17_2-C` | `RR` aus Art. 9 (Risikomanagement) | keine Deduplizierung |
| `M17_2-D` | insbesondere `RR-087` und `RR-091`, im Umfeld von `RR-085`, `RR-086` und `RR-088` | keine Deduplizierung |
| `M17_2-E` | insbesondere `RR-091` | keine Deduplizierung |

**Begründung:** unterschiedliche Rechtsregime, regulatorische Rollen, Bezugsobjekte, Pflichtumfänge und Compliance-Ergebnisse.

| Merkmal | Ergebnis |
| --- | --- |
| Cross-Regulation-Deduplizierungen | 0 |
| Bestehende AI-`RR` ändern | NEIN |

---

## 12. IEC 62304 und ISO 14971

`SRC-007` (IEC 62304) und `SRC-006` (ISO 14971) wurden **nicht** systematisch extrahiert; es wurden **keine** Klauselinhalte importiert. Insbesondere wurden keine zusätzlichen Pflichten zu Software-Sicherheitsklassen, zu vorbestehender Software, zu Software-Einheiten, zur Architektur, zu Integrationsprüfungen, zur Problemlösung oder zum Konfigurationsmanagement ergänzt.

Der Stand der Technik wird **nicht** mit einer bestimmten Norm gleichgesetzt.

---

## 13. Context und 0-`RR`-Aussagen

| Nr. | Aussage | Behandlung |
| --- | --- | --- |
| 1 | Produktkategorien | Applicability; 0 eigene `RR` |
| 2 | entwickelt und hergestellt | gemeinsamer Handlungsrahmen; 0 eigene `RR` |
| 3 | zu berücksichtigen / `taking into account` | gemeinsamer verbindlicher Handlungsmaßstab von `M17_2-B` bis `M17_2-E`; keine Meta-`RR` |
| 4 | einschließlich der Informationssicherheit | Bestandteil von `M17_2-C`; keine separate `RR` |

---

## 14. Verworfene Split-Varianten

| Variante | Ursprünglich geprüft | Final | Grund |
| --- | --- | --- | --- |
| A — Entwicklung und Herstellung getrennt | 2 `RR` | verworfen | Split-Bedingung 2 nicht erfüllt |
| B — Informationssicherheit getrennt | eigene Security-`RR` | verworfen | Konkretisierung durch „einschließlich" innerhalb `M17_2-C` |
| C — Verifizierung und Validierung gemeinsam | 1 gemeinsame `RR` | verworfen | beide Split-Bedingungen für getrennte `RR` erfüllt |
| D — alle vier Grundsätze gemeinsam | 1 aggregierte Prinzipien-`RR` | verworfen | unabhängige vollständige Compliance-Status |
| E — synthetischer deutscher Begriff in `M17_2-B` | „Softwareentwicklungslebenszyklus" im Requirement Text | verworfen | Source Fidelity; im Requirement Text steht der amtliche Ausdruck „Software-Lebenszyklus", die enger adjudizierte Bedeutung bleibt in Abschnitt 6 dokumentiert |

Keine dieser Varianten erhält eine permanente Identifikation.

---

## 15. Theme-Audit

| Kandidat | Themencluster |
| --- | --- |
| `M17_2-A` | Software-Lebenszyklus |
| `M17_2-B` | Software-Lebenszyklus |
| `M17_2-C` | Qualitäts- und Risikomanagement |
| `M17_2-D` | Software-Lebenszyklus |
| `M17_2-E` | Software-Lebenszyklus |

Je Kandidat genau ein Themencluster. Keine Mehrfachzuordnung und keine neue Taxonomie.

---

## 16. Scope-Audit

| Bereich | Ergebnis |
| --- | --- |
| `SRC-001#Anh.I/Nr.17.4` systematisch extrahiert | NEIN |
| IEC 62304 systematisch extrahiert | NEIN |
| ISO 14971 systematisch extrahiert | NEIN |
| Externe Norminhalte importiert | NEIN |
| Neuer Cybersecurity-Cluster | NEIN |
| Informationssicherheit verloren | NEIN |
| Out-of-Scope-Atome | 0 |

---

## 17. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. **Keine** Methodenänderung erforderlich.

Besonders bestätigt:

- Applicability ist keine Gap-`RR`;
- mehrere Verben allein erzeugen keinen Split;
- der Stand der Technik kann ein eigenständiger Sollzustand sein;
- unabhängig statusfähige Grundsätze können getrennt werden;
- „einschließlich" erzeugt nicht automatisch ein eigenes Atom;
- Theme und Lebenszyklusphase sind getrennte Dimensionen;
- ein Begriff wie Verifizierung oder Validierung erzeugt nicht automatisch die gleichnamige Lebenszyklusphase;
- eine bekannte Sprachdivergenz bleibt in der Evidenz erhalten;
- eine strukturierte normative Paraphrase verändert die normative Stärke nicht;
- externe Normen werden nicht in die gesetzliche `RR` importiert.

---

## 18. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.17.2`. 5 finale neue MDR-Gap-`RR`-Kandidaten `M17_2-A` bis `M17_2-E`, alle regulär. Atomisiert wurden Stand der Technik, Software-Lebenszyklus, Risikomanagement einschließlich Informationssicherheit, Verifizierung und Validierung. Die Informationssicherheit bleibt Bestandteil des Risikomanagementatoms und erzeugt keine separate `RR`. Die Divergenz zwischen „Software-Lebenszyklus" und `development life cycle` wurde multilingual adjudiziert; der deutsche Requirement Text behält aus Source-Fidelity-Gründen den amtlichen Ausdruck. Alle fünf Kandidaten tragen final die Lebenszyklusphasen Entwicklung und Realisierung sowie Änderung und Wartung. 0 MDR-interne Deduplizierungen, 0 unresolved, 0 deferred, 0 Out-of-Scope-Atome, 0 Cross-Regulation-Deduplizierungen und 0 operative Fundstellen ohne Entscheidung. |
