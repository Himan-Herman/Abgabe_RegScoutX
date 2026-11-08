# Systematische RR-Extraktion — SRC-001 Anhang I Nr. 5

Version 1.0 · Status: aktiv

## 1. Gegenstand

| Merkmal | Angabe |
| --- | --- |
| Quelle | `SRC-001` |
| Quellenbereich | `SRC-001#Anh.I/Nr.5` |
| Rechtsstand | konsolidierter Stand 19.07.2026 gemäß [SOURCES.md](SOURCES.md) (CELEX `02017R0745-20260719`) |
| Coverage-Kategorie | Kernbereich |
| Expected Theme | Gebrauchstauglichkeit |
| Extraktionsmethode | [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 |
| Controlled Vocabulary | [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Version 1.0 |
| Coverage-Plan | [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Version 1.22 |
| Bearbeitungsstatus im Coverage-Plan | `in Prüfung` |

Diese Datei dokumentiert den final adjudizierten Stand der vollständigen systematischen `0 / 1 / n`-Prüfung des Quellenbereichs. Sie vergibt **keine** permanenten `RR`-Identifikatoren. `M5-A` und `M5-B` sind ausschließlich temporäre Evidenzkennungen. Die Vergabe permanenter Identifikatoren erfolgt später und ausschließlich in [RR_CATALOG.yaml](RR_CATALOG.yaml).

---

## 2. Finales Gesamtergebnis

| Stufe | Anzahl |
| --- | --- |
| Neue MDR-Gap-`RR`-Kandidaten | **2** — `M5-A`, `M5-B` |
| davon regulär | 2 |
| davon conditional | 0 |
| MDR-intern deduplizierte Atome | 0 |
| Unresolved | 0 |
| Deferred | 0 |
| Out-of-Scope-Atome | 0 |
| Cross-Regulation-Deduplizierungen | 0 |
| Operative Fundstellen ohne Entscheidung | 0 |

Es wurde **keine** quantitative Zielzahl verwendet. Die Zahl 2 ist ausschließlich Ergebnis der Quellenstruktur und der Atomizitätsmethode; das entspricht der Festlegung in [COVERAGE_PLAN.md](COVERAGE_PLAN.md) Abschnitt 12.

---

## 3. Quellenstruktur

`SRC-001#Anh.I/Nr.5` enthält:

- einen gemeinsamen normativen Rahmen zur Beseitigung bzw. Verringerung anwendungsfehlerbezogener Risiken,
- `SRC-001#Anh.I/Nr.5/Buchst.a`,
- `SRC-001#Anh.I/Nr.5/Buchst.b`.

Der gemeinsame Rahmen erzeugt **0** eigene `RR` und wird als notwendiger Supplementary-Kontext für `M5-A` und `M5-B` geführt. Für ihn wird **kein** eigenes Locator-Element eingeführt; er wird ausschließlich über `SRC-001#Anh.I/Nr.5` geführt. Das entspricht dem zulässigen Elementvokabular aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4.

---

## 4. Vollständige `0 / 1 / n`-Prüfung

| Locator | Ergebnis | Behandlung |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.5` | 0 eigene `RR` | gemeinsamer normativer Kontext; Supplementary für `M5-A` und `M5-B` |
| `SRC-001#Anh.I/Nr.5/Buchst.a` | 1 `RR` | `M5-A` |
| `SRC-001#Anh.I/Nr.5/Buchst.b` | 1 `RR` | `M5-B` |
| **Gesamt** | **2** | |

---

## 5. Kandidaten

### M5-A — Verringerung anwendungsfehlerbedingter Risiken aus ergonomischen Merkmalen und Nutzungsumgebung

- **Title EN:** Reduction of Use-Error Risks Related to Ergonomic Features and Intended Use Environment
- **DE:** Der Hersteller muss beim Ausschluss oder bei der Verringerung der durch Anwendungsfehler bedingten Risiken die Risiken aufgrund der ergonomischen Merkmale des Produkts und der Umgebung, in der das Produkt verwendet werden soll, so weit wie möglich verringern; die Risikoverringerung ist dabei so weit vorzunehmen, wie dies ohne negative Auswirkungen auf das Nutzen-Risiko-Verhältnis möglich ist.
- **EN:** The manufacturer shall, in eliminating or reducing risks related to use error, reduce as far as possible the risks related to the ergonomic features of the device and the environment in which the device is intended to be used; such risk reduction shall be pursued as far as possible without adversely affecting the benefit-risk ratio.
- **Primary:** `SRC-001#Anh.I/Nr.5/Buchst.a`
- **Supplementary:** `SRC-001#Anh.I/Nr.5` · `SRC-001#Anh.I/Nr.2`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Ergonomische Merkmale und vorgesehene Nutzungsumgebung bleiben gemeinsam.

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | erfüllt |
| Split-Bedingung 2 | nicht erfüllt |

Beide sind Risikoursachen innerhalb derselben anwendungsfehlerbezogenen Risikoreduktionspflicht. „so weit wie möglich" ist wesentliche normative Qualifikation. Die Klammerangabe zur auf die Sicherheit des Patienten ausgerichteten Produktauslegung ist funktionale Beschreibung derselben Pflicht und erzeugt **keine** eigene `RR`.

**Supplementary-Kontext:** `SRC-001#Anh.I/Nr.2` bestimmt die Bedeutung der weitestmöglichen Risikoverringerung und ist deshalb notwendiger normativer Kontext. Nr. 2 wurde **nicht** systematisch extrahiert.

### M5-B — Berücksichtigung von Nutzermerkmalen und Anwendungsumgebung bei anwendungsfehlerbezogenen Risiken

- **Title EN:** Consideration of Intended User Characteristics and Use Environment for Use-Error Risks
- **DE:** Der Hersteller muss beim Ausschluss oder bei der Verringerung der durch Anwendungsfehler bedingten Risiken die technischen Kenntnisse, die Erfahrung, die Aus- und Weiterbildung, gegebenenfalls die Anwendungsumgebung sowie die gesundheitliche und körperliche Verfassung der vorgesehenen Anwender berücksichtigen.
- **EN:** The manufacturer shall, in eliminating or reducing risks related to use error, give consideration to the technical knowledge, experience, education, training and use environment, where applicable, and the medical and physical conditions of intended users.
- **Primary:** `SRC-001#Anh.I/Nr.5/Buchst.b`
- **Supplementary:** `SRC-001#Anh.I/Nr.5`
- **Theme:** Gebrauchstauglichkeit
- **Lifecycle:** Planung und Konzeption · Entwicklung und Realisierung · Änderung und Wartung
- **Uncertainty:** null
- **Conditional:** NEIN
- **Trigger:** —

**Atomizität:** Die einzelnen Faktoren — technische Kenntnisse, Erfahrung, Aus- und Weiterbildung, Anwendungsumgebung, gesundheitliche Verfassung und körperliche Verfassung — bilden gemeinsam das zu berücksichtigende Profil bzw. den Nutzungskontext der vorgesehenen Anwender.

| Prüfung | Ergebnis |
| --- | --- |
| Split-Bedingung 1 | grundsätzlich erfüllt |
| Split-Bedingung 2 | nicht erfüllt |

Es erfolgt **keine** Mikroatomisierung nach einzelnen Nutzermerkmalen. Die Klammer zu Laien, Fachleuten, Menschen mit Behinderungen und sonstigen Anwendern ist funktionale Erläuterung der nutzerorientierten Produktauslegungspflicht und erzeugt **keine** separate `RR`.

---

## 6. Adjudikation der Modalitätsklausel „gegebenenfalls / where applicable"

| Merkmal | Ergebnis |
| --- | --- |
| Materielle Divergenz | JA |
| Status | RESOLVED |
| Unresolved | 0 |
| Geprüfte authentische Fassungen | DE · EN · FR · ES · IT |

**Befund:** Die deutsche und die englische Fassung sowie die französische und die spanische Fassung ordnen den jeweiligen Modalitätsausdruck syntaktisch der Anwendungsumgebung bzw. `use environment` zu. Die italienische Fassung positioniert `ove possibile` dagegen vor den medizinischen und körperlichen Bedingungen.

**Adjudikation nach dem Multilingual Source Divergence Protocol der Methode Version 1.2:** Es wurde **keine** Sprachfassung priorisiert und **keine** Mehrheitsregel verwendet. Die Auslegung stützt sich auf:

- die unmittelbare Syntax der jeweiligen Aufzählung;
- die Koordinationsstruktur, in der die Anwendungsumgebung als situativ abhängiger Faktor neben den personenbezogenen Merkmalen steht;
- den systematischen Kontext von Nr. 5, der auf anwendungsfehlerbezogene Risiken der vorgesehenen Anwender zielt;
- die Funktion der gesamten Berücksichtigungspflicht, die ein vollständiges Nutzerprofil verlangt.

**Final adjudizierte Bedeutung für die deutsche und englische Anforderung:** „gegebenenfalls" bzw. `where applicable` qualifiziert die Anwendungsumgebung bzw. `use environment`. Die gesundheitliche und körperliche Verfassung bleibt Bestandteil des gemeinsamen Nutzerprofils.

Die italienische Abweichung bleibt ausdrücklich dokumentiert und wird **nicht** als nie existent dargestellt.

| Auswirkung | Ergebnis |
| --- | --- |
| Atomisierung | NEIN |
| Theme | NEIN |
| Conditional-Status der Gesamt-`RR` | NEIN |

`M5-B` bleibt regulär.

---

## 7. MDR-interne Deduplizierung

| Gegenüberstellung | Ergebnis |
| --- | --- |
| `M5-A` ↔ `RR-158` | keine vollständige Deduplizierung |
| `M5-B` | keine bestehende statusidentische MDR-`RR` |

**Begründung:** `RR-158` enthält die allgemeine Pflicht zur weitestmöglichen Risikominimierung durch sichere Auslegung und Herstellung. `M5-A` enthält den spezifischen Sollzustand für anwendungsfehlerbezogene Risiken aufgrund ergonomischer Merkmale und vorgesehener Nutzungsumgebung. Die Erfüllungsstatus sind unabhängig.

**MDR-intern vollständig dedupliziert: 0.**

---

## 8. Spätere MDR-interne Abgleiche

| Quellenbereich | Behandlung | Vorgemerkter Abgleich |
| --- | --- | --- |
| `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` | wird später eigenständig systematisch geprüft, sobald die conditional Laienanwendung aktiviert ist | `M5-A` hinsichtlich Use-Error- und Umgebungsrisiken; `M5-B` hinsichtlich Fähigkeiten und Voraussetzungen der Laienanwender |
| `SRC-001#Anh.I/Nr.23.1` | wird später eigenständig systematisch extrahiert | `M5-B` hinsichtlich der Anforderungen an die Informationsgestaltung unter Berücksichtigung von Nutzerkenntnissen, Erfahrung und Ausbildung |

Beide Abgleiche sind **kein** zurückgestellter Fall und **kein** Blocker.

---

## 9. Cross-Regulation

`M5-B` besitzt eine starke sachliche Beziehung zu `RR-063` (Berücksichtigung von Betreibermerkmalen und Nutzungskontext, Primary `SRC-002#Art.9/Abs.5/UAbs.3`). Eine Cross-Regulation-Deduplizierung erfolgt **nicht**.

| Merkmal | `M5-B` | `RR-063` |
| --- | --- | --- |
| Adressat | Hersteller nach MDR | Anbieter nach AI Act |
| Bezugsobjekt | Medizinprodukt | Hochrisiko-KI-System |
| Personenbezug | vorgesehene Anwender | Betreiber und voraussichtlicher Nutzungskontext |
| Pflichtumfang | anwendungsfehlerbezogene Designpflicht einschließlich gesundheitlicher und körperlicher Verfassung | Risikomanagement nach AI Act |

Die regulatorischen Rollen, Bezugsobjekte, Pflichtumfänge und Rechtsregime sind unterschiedlich. Für `M5-A` besteht keine statusidentische AI-Act-`RR`.

| Merkmal | Ergebnis |
| --- | --- |
| Cross-Regulation-Deduplizierungen | 0 |
| Bestehende AI-`RR` ändern | NEIN |

---

## 10. Theme-Audit

| Kandidat | Themencluster |
| --- | --- |
| `M5-A` | Gebrauchstauglichkeit |
| `M5-B` | Gebrauchstauglichkeit |

**Begründung:** Primärer normativer Gegenstand beider Anforderungen ist die anwendungsfehlerbezogene, nutzer- und nutzungskontextorientierte Produktsicherheit und -gestaltung. Es erfolgt keine Mehrfachzuordnung.

---

## 11. Context und 0-`RR`-Aussagen

| Nr. | Fundstelle bzw. Gegenstand | Behandlung |
| --- | --- | --- |
| 1 | `SRC-001#Anh.I/Nr.5` — gemeinsamer Anwendungsfehlerrahmen | 0 eigene `RR`; Supplementary |
| 2 | `Buchst.a` — ergonomische Merkmale | kein separater Split |
| 3 | `Buchst.a` — vorgesehene Nutzungsumgebung | kein separater Split |
| 4 | auf die Sicherheit des Patienten ausgerichtete Produktauslegung | funktionale Erläuterung; 0 eigene `RR` |
| 5 | `SRC-001#Anh.I/Nr.2` | nur Supplementary von `M5-A`; keine systematische Extraktion |
| 6 | einzelne Nutzerfaktoren aus `Buchst.b` | keine Einzel-`RR` |
| 7 | „gegebenenfalls" bzw. `where applicable` | Modalität innerhalb `M5-B`; keine eigene `RR` |
| 8 | Nutzergruppen-Klammer | funktionale Erläuterung; keine separate Nutzergruppen-`RR` |

---

## 12. Scope-Audit

| Bereich | Ergebnis |
| --- | --- |
| `SRC-001#Anh.I/Nr.2` | nicht systematisch extrahiert |
| `SRC-001#Anh.I/Nr.22.1` bis `Nr.22.3` | nicht systematisch extrahiert |
| `SRC-001#Anh.I/Nr.23.1` | nicht systematisch extrahiert |
| IEC 62366-1 | keine Inhalte importiert |
| Andere MDR-Bereiche | nicht bearbeitet |
| Out-of-Scope-Atome | 0 |

---

## 13. Methodenaudit

[RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Version 1.2 war ausreichend. **Keine** Methodenänderung erforderlich.

Besonders bestätigt:

- ein gemeinsamer Einleitungsrahmen erzeugt keine aggregierende Doppel-`RR`;
- mehrere Risikoursachen unter einem gemeinsamen Sollzustand werden nicht künstlich getrennt;
- „so weit wie möglich" kann notwendigen normativen Supplementary-Kontext erfordern;
- erläuternde Klammern erzeugen keine eigene `RR`;
- Nutzermerkmalslisten werden nicht mechanisch mikroatomisiert;
- Modalitätsklauseln werden im Sollzustand erhalten;
- die spezifische Konkretisierung einer allgemeineren Risikokontrollpflicht ist nicht automatisch eine Deduplizierung;
- der multilinguale Divergenzfall wurde nach Version 1.2 adjudiziert.

---

## 14. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der vollständigen systematischen Extraktion von `SRC-001#Anh.I/Nr.5`. 2 finale neue MDR-Gap-`RR`-Kandidaten `M5-A` und `M5-B`, beide regulär. 0 MDR-interne Deduplizierungen, 0 unresolved, 0 deferred, 0 Out-of-Scope-Atome und 0 Cross-Regulation-Deduplizierungen. Die multilinguale Abweichung zur Position der Modalitätsklausel in Buchst. b wurde nach Methode Version 1.2 adjudiziert und bleibt dokumentiert. `SRC-001#Anh.I/Nr.2` wurde ausschließlich als notwendiger Supplementary-Kontext für `M5-A` verwendet und nicht systematisch extrahiert. |
