# Extraktionspilot: SRC-002 Art. 13 Abs. 1

Version 1.0 · Status: aktiv

## 1. Zweck

Dies ist der erste reale Pilot der in [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) festgelegten Extraktionsmethode.

| Merkmal | Angabe |
| --- | --- |
| Untersuchte Fundstelle | `SRC-002#Art.13/Abs.1` |
| Verwendeter Rechtsstand | `SRC-002`, konsolidierter Stand 27.07.2026 (siehe [SOURCES.md](SOURCES.md)) |
| Ergebnis | 2 atomare `RR` |

Ziel war die praktische Prüfung der Methode an einer realen Fundstelle: RR-Relevanz, Atomizität, Quellenbezug sowie Themencluster- und Lebenszykluszuordnung.

Der Pilot ist bewusst auf Art. 13 Abs. 1 begrenzt. Er enthält **keine** allgemeine Analyse des gesamten Art. 13; die folgenden Absätze dieses Artikels wurden nicht untersucht.

## 2. Quellenprüfung

**Primär geprüft:**

- `SRC-002#Art.13/Abs.1/Satz.1`
- `SRC-002#Art.13/Abs.1/Satz.2`

**Zwingend ergänzend:**

- `SRC-002#Art.16/Buchst.a`

**Begründung des ergänzenden Lokators:** Art. 13 Abs. 1 formuliert die Anforderungen an das Hochrisiko-KI-System, ohne das verpflichtete Subjekt ausdrücklich zu benennen. Art. 16 Buchst. a begründet für die Katalogdarstellung den Anbieter als verpflichtetes Subjekt zur Sicherstellung der Anforderungen aus Abschnitt 2, dem Art. 13 angehört.

Weitere Fundstellen waren zur vollständigen und reproduzierbaren Bestimmung der beiden Anforderungen nicht erforderlich; entsprechend dem Minimalitätsprinzip aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 8 wurden keine weiteren aufgenommen.

## 3. Atomizitätsentscheidung

**Erster Analysevorschlag: 3 RR-Kandidaten**

1. Interpretation der Ausgaben
2. angemessene Verwendung der Ausgaben
3. geeignete Art und angemessenes Maß der Transparenz

**Finale Entscheidung: 2 atomare `RR`**

*Interpretation und angemessene Verwendung aus Satz 1 werden nicht getrennt.* Beide konkretisieren gemeinsam die Wirkung derselben geforderten Transparenzeigenschaft. Auch wenn ihre praktische Erfüllung unterschiedlich beurteilt werden könnte, bilden sie innerhalb dieser Quellenstelle keine hinreichend regulatorisch eigenständigen Compliance-Pflichten. Eine Trennung würde deshalb die gemeinsame Hauptpflicht duplizieren und die Zweck- bzw. Qualitätsbestandteile künstlich zu Mikro-`RR` verselbständigen. Damit ist die zweite Bedingung des Split-Tests aus [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) Abschnitt 4 nicht erfüllt.

*Satz 2 bleibt dagegen eigenständig.* Er enthält mit der geeigneten Art und dem angemessenen Maß der Transparenz einen gesonderten normativen Sollzustand im Hinblick auf die Pflichten nach Abschnitt 3. Sein Erfüllungsstatus kann sich von dem des Satzes 1 unterscheiden, und er bildet für sich eine vollständige Compliance-Aussage.

Zuordnung:

- Satz 1 → `RR-001`
- Satz 2 → `RR-002`

## 4. Resultat

| ID | Titel | Themencluster | Lebenszyklusphase | Unsicherheit | Status |
| --- | --- | --- | --- | --- | --- |
| `RR-001` | Transparenz zur Interpretation und angemessenen Verwendung von Systemausgaben | `Transparenz` | `Entwicklung und Realisierung` | keine dokumentierte Unsicherheit | `aktiv` |
| `RR-002` | Angemessene Art und angemessenes Maß der Transparenz | `Transparenz` | `Entwicklung und Realisierung` | keine dokumentierte Unsicherheit | `aktiv` |

Katalogversion nach Aufnahme: `0.2`.

Die vollständigen Einträge einschließlich Anforderungstext und Quellen-Lokatoren stehen in [RR_CATALOG.yaml](RR_CATALOG.yaml); sie werden hier nicht dupliziert. Die verwendeten Werte für Themencluster und Lebenszyklusphase stammen aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md).

## 5. Methodische Bewertung

- Die 0/1/n-Logik war auf die reale Fundstelle anwendbar.
- Die Regel „unabhängiger Erfüllungsstatus + regulatorische Eigenständigkeit" verhinderte hier eine Überfragmentierung.
- Satzgrenzen allein waren nicht das Atomizitätskriterium: Dass das Ergebnis den beiden Sätzen entspricht, folgt aus dem Split-Test, nicht aus der Satzstruktur.
- Der ergänzende Quellen-Lokator konnte den im Primärsatz nicht ausdrücklich genannten verpflichteten Adressaten nachvollziehbar ergänzen.
- Der Pilot bestätigt die grundsätzliche praktische Anwendbarkeit der Methode für diese Fundstelle.

**Einschränkung:** Aus einem einzigen Pilotfall darf **keine** allgemeine Validierung der Extraktionsmethode abgeleitet werden. Der Pilot belegt die Anwendbarkeit an dieser Fundstelle, nicht die Eignung der Methode über den gesamten Untersuchungsumfang.

## 6. Verworfene Alternative

Verworfen wurde das 3-`RR`-Modell mit separaten Anforderungen für `Interpretation` und `Verwendung`.

Grund: fehlende hinreichende regulatorische Eigenständigkeit der beiden Zweckbestandteile innerhalb von Satz 1 und die damit verbundene Gefahr künstlicher Mikro-`RR`.

## 7. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [RR_CATALOG.yaml](RR_CATALOG.yaml) | Führende Vergabestelle; enthält die vollständigen Einträge |
| [RR_EXTRACTION_METHOD.md](RR_EXTRACTION_METHOD.md) | Angewandte Extraktions- und Atomizitätsmethode |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | Kontrollierte Werte für Themencluster und Lebenszyklusphase |
| [SOURCES.md](SOURCES.md) | Quellenregister und Fassungsstand von `SRC-002` |

## 8. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Dokumentation des Extraktionspilots zu `SRC-002#Art.13/Abs.1` einschließlich Atomizitätsentscheidung 3 → 2 Kandidaten. |
