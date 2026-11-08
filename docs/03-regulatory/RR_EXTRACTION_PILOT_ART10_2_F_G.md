# Extraktionspilot: SRC-002 Art. 10 Abs. 2 Buchst. f und g

Version 1.0 · Status: aktiv

## 1. Zweck

Dies ist der zweite reale Pilot der in [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) festgelegten Extraktionsmethode.

| Merkmal | Angabe |
| --- | --- |
| Untersuchte Fundstellen | `SRC-002#Art.10/Abs.2/Buchst.f`, `SRC-002#Art.10/Abs.2/Buchst.g` |
| Verwendeter Rechtsstand | `SRC-002`, konsolidierter Stand 27.07.2026 (siehe [SOURCES.md](SOURCES.md)) |
| Ergebnis | 4 atomare `RR` |

Ziel war die praktische Prüfung der Atomizitätsregel bei einer Aufzählungsstruktur und bei mehreren kumulativen Handlungsbestandteilen innerhalb eines Aufzählungspunktes.

Der Pilot ist auf die beiden genannten Buchstaben begrenzt. Er enthält **keine** systematische Extraktion von Art. 10; die übrigen Buchstaben und Absätze wurden nicht untersucht.

## 2. Quellenprüfung

**Geprüfte Hauptfundstellen:**

- `SRC-002#Art.10/Abs.2/Buchst.f`
- `SRC-002#Art.10/Abs.2/Buchst.g`

**Zwingend ergänzende Fundstellen:**

| Lokator | Funktion |
| --- | --- |
| `SRC-002#Art.10/Abs.2` | Liefert den grammatischen und normativen Chapeau für die Daten-Governance- und Datenverwaltungsverfahren. Die Buchstaben sind für sich keine vollständigen Normsätze. |
| `SRC-002#Art.10/Abs.6` | Begrenzt bei der Entwicklung von Hochrisiko-KI-Systemen, in denen keine Techniken eingesetzt werden, bei denen KI-Modelle trainiert werden, die Anforderungen aus Abs. 2 auf Testdatensätze. |
| `SRC-002#Art.16/Buchst.a` | Liefert den Anbieter als verpflichteten Adressaten zur Sicherstellung der Anforderungen aus Abschnitt 2. |

Für `RR-004` bis `RR-006` ist zusätzlich `SRC-002#Art.10/Abs.2/Buchst.f` als `supplementary` erforderlich, weil Buchst. g ausdrücklich auf die gemäß Buchst. f ermittelten möglichen Verzerrungen Bezug nimmt.

Weitere Fundstellen wurden nicht aufgenommen; das Minimalitätsprinzip aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8 wurde eingehalten.

## 3. Atomizitätsentscheidung Buchst. f

**Finale Entscheidung: Buchst. f → 1 atomare `RR` (`RR-003`)**

Buchst. f verlangt einen einheitlichen regulatorischen Sollzustand: eine Untersuchung möglicher Verzerrungen.

Die genannten möglichen Auswirkungen auf

- Gesundheit und Sicherheit,
- Grundrechte,
- unionsrechtlich verbotene Diskriminierung

werden **nicht** als einzelne `RR` aufgeteilt. Sie bestimmen gemeinsam den Gegenstandsbereich bzw. die Qualifikation der zu untersuchenden möglichen Verzerrungen und stellen keine eigenständigen regulatorischen Handlungen dar. Eine Aufteilung wäre künstliche Mikro-Atomisierung.

## 4. Atomizitätsentscheidung Buchst. g

**Finale Entscheidung: Buchst. g → 3 atomare `RR`**

- `RR-004`: Erkennung
- `RR-005`: Verhinderung
- `RR-006`: Abschwächung

Begründung nach exakt den beiden Split-Kriterien aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 4:

1. **Die Erfüllungsstatus können unabhängig unterschiedlich sein.** Es können beispielsweise geeignete Erkennungsmaßnahmen bestehen, während geeignete Verhinderungs- oder Abschwächungsmaßnahmen fehlen.
2. **Erkennung, Verhinderung und Abschwächung besitzen jeweils regulatorisch eigenständigen Compliance-Sinn.** Jede Funktion bezeichnet eine eigenständig geforderte Maßnahme gegenüber den nach Buchst. f ermittelten möglichen Verzerrungen; keine ist bloß Modalität oder Qualitätskriterium einer anderen.

**Ausdrücklich:** Mehrere Verben allein wären nicht ausreichend. Der Split folgt aus der Kombination von unabhängig möglichem Erfüllungsstatus **und** regulatorischer Eigenständigkeit.

## 5. Verhältnis von Buchst. f zu Buchst. g

Buchst. f und Buchst. g werden getrennt behandelt.

- Buchst. f: Untersuchung auf mögliche Verzerrungen.
- Buchst. g: geeignete Maßnahmen im Umgang mit den gemäß f ermittelten möglichen Verzerrungen.

Die Pflichten besitzen unterschiedliche normative Gegenstände und können unabhängig voneinander erfüllt oder verletzt sein. Der Querverweis aus g auf f führt nicht zu einer Zusammenführung, sondern wird über den `supplementary`-Lokator abgebildet.

## 6. Resultat

| ID | Titel |
| --- | --- |
| `RR-003` | Untersuchung möglicher Verzerrungen in Datensätzen |
| `RR-004` | Maßnahmen zur Erkennung möglicher Verzerrungen |
| `RR-005` | Maßnahmen zur Verhinderung möglicher Verzerrungen |
| `RR-006` | Maßnahmen zur Abschwächung möglicher Verzerrungen |

Für alle vier Einträge gilt:

| Attribut | Wert |
| --- | --- |
| Themencluster | `Data Governance` |
| Lebenszyklusphasen | `Entwicklung und Realisierung`, `Verifikation und Validierung` |
| Status | `aktiv` |
| Unsicherheit | keine dokumentierte Unsicherheit |
| Katalogversion | `0.3` |

Die vollständigen Einträge einschließlich Anforderungstext und Quellen-Lokatoren stehen in [RR_CATALOG.yaml](RR_CATALOG.yaml) und werden hier nicht dupliziert. Die verwendeten Attributwerte stammen aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md).

## 7. Lebenszykluszuordnung

Die Anforderungen beziehen sich auf Trainings-, Validierungs- und Testdatensätze. Sie werden deshalb nach dem kontrollierten Vokabular den Phasen `Entwicklung und Realisierung` und `Verifikation und Validierung` zugeordnet.

Maßgeblich ist dabei der tatsächliche regulatorische Gegenstand der Datenverwendung im Entwicklungs- und Prüfkontext. Die Zuordnung folgt **nicht** allein aus dem Vorkommen des Begriffs „Validierungsdatensatz"; ein Begriff im Normtext bestimmt die Lebenszyklusphase nicht automatisch.

Eine dritte Phase wurde nicht ergänzt.

## 8. Qualitätssicherungsbefund

Bei der Quellenprüfung wurde vor dem Commit ein Übertragungsfehler im ersten Entwurf von `RR-003` erkannt.

| | Erster Entwurf | Geprüfte Quelle |
| --- | --- | --- |
| Deutsch | `Gesundheit oder Sicherheit` | `Gesundheit und Sicherheit` |
| Englisch | `health or safety` | `health and safety` |

Der Fehler wurde vor Freigabe korrigiert.

**Methodische Bedeutung:** Die Prüfung der logischen Verknüpfungen `und` / `oder` ist erforderlich, weil ihre Veränderung den normativen Gehalt verändern kann. Der Befund bestätigt die Regel aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 3 Schritt 5, wonach die logische Struktur der Fundstelle bei der Paraphrase erhalten bleiben muss.

## 9. Methodische Bewertung

- Die 0/1/n-Methode war auch bei einer Aufzählungsstruktur anwendbar.
- Die Gliederung in Buchstaben führte nicht automatisch zu einer `RR` je Buchstabe.
- Mehrere Wirkungsbereiche in Buchst. f führten nicht automatisch zu mehreren `RR`.
- Mehrere kumulative Handlungen in Buchst. g wurden nur deshalb getrennt, weil beide Split-Kriterien erfüllt waren.
- `supplementary`-Lokatoren konnten Chapeau, Scope, Adressat und Querverweis abbilden, ohne die Hauptfundstelle zu verwässern.
- Der Pilot zeigt die praktische Anwendbarkeit der Methode für diese Fundstellen.

**Einschränkung:** Auch zwei erfolgreiche Pilotfälle validieren die Methode noch nicht für den gesamten Untersuchungsumfang.

## 10. Vergleich mit Pilot 1

[Pilot 1](RR_EXTRACTION_PILOT_ART13_1.md) zu Art. 13 Abs. 1 zeigte einen Fall, in dem separat beurteilbare Teilwirkungen wegen fehlender regulatorischer Eigenständigkeit **nicht** getrennt wurden.

Pilot 2 zeigt den Gegenfall: Erkennung, Verhinderung und Abschwächung werden getrennt, weil neben möglicher Statusunabhängigkeit auch regulatorische Eigenständigkeit besteht.

Daraus ergibt sich keine neue Atomizitätsregel. Die bereits definierte Zwei-Bedingungen-Regel genügte für beide Fälle.

## 11. Verworfene Alternativen

**A. Buchst. f nach den genannten Auswirkungen in mehrere `RR` aufteilen.** Verworfen wegen fehlender eigenständiger Handlungspflichten der einzelnen Wirkungsbereiche.

**B. Buchst. g als eine einzige `RR` behandeln.** Verworfen, weil damit drei regulatorisch eigenständige und unabhängig diagnostizierbare Compliance-Funktionen in einem Status gebündelt würden.

## 12. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | Führende Vergabestelle; enthält die vollständigen Einträge |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | Angewandte Extraktions- und Atomizitätsmethode |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | Kontrollierte Werte für Themencluster und Lebenszyklusphasen |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |
| [RR_EXTRACTION_PILOT_ART13_1.md](RR_EXTRACTION_PILOT_ART13_1.md) | Erster Extraktionspilot zum Vergleich |

## 13. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung des zweiten Extraktionspilots zu `SRC-002` Art. 10 Abs. 2 Buchst. f und g. |
