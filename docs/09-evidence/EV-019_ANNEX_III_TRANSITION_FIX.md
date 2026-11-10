# EV-019 — Gezielte technische Behebung der Anhang-III-Übergangslücke

Version 1.0 · Status: aktiv · Datum: 04.11.2026

Ausgang: `17011f3`, Verfasserauftrag zur isolierten Behebung von R01-4.6-F01. Neuer technischer Stand: RUL_CATALOG 0.3, RR_APPLICABILITY 0.5; RR_CATALOG 0.26, SR_CATALOG 0.6, DATA_MODEL 0.8 und RR_MEASURE 0.2 unverändert. Keine neue Fallstudienevaluation und keine Aktualisierung der Abgabedateien.

## 1. Gegenfall und Korrektur

Der vor der Änderung ausgeführte Gegenfall beschreibt die Anhang-III-Triage ohne Produktroute: Bewertungsdatum 01.09.2028, Inverkehrbringen 01.01.2026, keine signifikante Änderung und keine Behördennutzung. Der alte Stand ergab `AI_ACT_HIGH_RISK` und aktivierte den Block (45 anwendbar, 61 ohne dokumentierte Bedingtheit und 9 mit nicht modellierter lokaler Bedingung ungeklärt). Das ist der dokumentierte Fehler, keine neue Evaluationsmessung.

Seit RUL 0.3 führt die Anhang-III-Kandidatenprüfung über RUL-044 bis RUL-047: Anwendungsbeginn → Inverkehrbringen/Inbetriebnahme → signifikante Konzeptionsänderung seit 02.12.2027 → Behördennutzung und Frist 02.08.2030. Der Gegenfall bleibt nun im Übergang; alle 115 AI-Act-Anforderungen erhalten blockseitig `NOT_APPLICABLE / SCOPE_LEGACY_TRANSITION`. Eine andere wirksame Route kann sie weiterhin aktivieren.

RUL-039 bleibt ersetzt mit Rückverknüpfung auf RUL-044 erhalten; nur aktive Regeln sind ausführbar. Die Frageführung bindet Text und Stichtag an die erreichte Regel statt an den ersten Katalogeintrag desselben Eingabeschlüssels. Der separate Anhang-III-Änderungsschlüssel verhindert die Gleichsetzung unterschiedlicher Änderungszeiträume beider Routen.

## 2. Tatsächlich ausgeführte Prüfung

In den öffentlichen Protokollkopien wurden lokale Benutzerpfade aus Datenschutzgründen gekürzt. Die Prüfergebnisse sind unverändert.

`PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest tests.test_annex_iii_transition`: 14 Tests, Exitcode 0, OK. [Originalausgabe](annex-iii-transition-2026-11-04/targeted-tests.txt), [Laufmetadaten](annex-iii-transition-2026-11-04/targeted-tests.json).

TC-062 prüft den Gegenfall, beide Stichtage, alle drei Hochrisiko-Kandidatenpfade, neue/geänderte Systeme, Behördennutzung vor und ab der Frist, fehlende und unklare Angaben, beide parallelen Routen mit getrennten Änderungsmerkmalen, DE/EN-Fragetext und korrekten Stichtag, Hashschutz historischer Kataloge sowie schreibgeschütztes historisches Öffnen und explizite Neubewertung als neue Revision.

Der neue Frageführungstest scheiterte vor der gezielten Korrektur mit `RUL-035 != RUL-045`; damit ist die falsche Kontextzuordnung konkret nachgewiesen. Ein erster breiterer Zwischenlauf hatte zwei YAML-Testdatenfehler im neu ergänzten Änderungshinweis; sie wurden korrigiert. Zwischenfehler sind keine bestandenen Läufe.

Zusätzliche vollständige Regression auf Python 3.13.15 / macOS 27.0.1 (ARM64):

| Prüfung | tatsächlich ausgeführt | Ergebnis |
| --- | --- | --- |
| Anwendungssuite `unittest discover -s tests -t .` | 223 Tests, einschließlich der 14 neuen Tests und TC-061 | Exitcode 0, OK |
| Werkzeugsuite `unittest discover -s tools -p test_*.py` | 144 Tests | Exitcode 0, OK |
| alle neun `tools/validate_*.py` | einschließlich Regel-, Testfall- und Referenzvalidator | jeweils Exitcode 0 |
| `tools/traceability.py` | aktuelle Katalog- und Verweisintegrität | Exitcode 0, PASS |
| `tools/derive_case_reference.py --check` | reine Reproduktion gegen eingefrorene Eingaben; keine Dateischreibung | Exitcode 0, bytegleiche Referenz |

[Anwendungslauf](annex-iii-transition-2026-11-04/application-suite.txt), [Werkzeuglauf](annex-iii-transition-2026-11-04/tools-suite.txt), [Validator-/Integritätsläufe](annex-iii-transition-2026-11-04/validators.txt); jeweilige JSON-Dateien enthalten Befehle, Dauer, Exitcode bzw. Umgebung. Die 14 gezielten Tests sind in den 223 enthalten und werden nicht zusätzlich als Gesamtzahl gezählt. Kein neuer Browser-, Build-, Screenreader- oder Nutzerstudienlauf. Die Frageführung wurde auf Serviceebene geprüft; vorhandene API-/Serverregressionen sind Bestandteil der Anwendungssuite. Unter `.github/` besteht kein konfigurierter Workflow; damit kein zusätzlicher Repository-CI-Lauf belegt.

## 3. Schutz historischer Ergebnisse

Die neuen eingefrorenen Kopien RUL 0.2 und RR_APPLICABILITY 0.4 wurden gegen die vollständigen Git-Dateien aus `9928f1b` (R1) und `219134c` (R2) per SHA-256 abgeglichen und sind bytegleich. Der bestehende Maßnahmen-Freeze 0.1 bleibt unverändert. Referenz-Reproduktion und TC-061 verwenden alle drei Fassungen mit Hashprüfung; die eigentliche Referenz und R1/R2 werden nicht neu geschrieben. Das historisch falsche Anhang-III-Routing bleibt in dieser Lesefassung ausdrücklich reproduzierbar und wird nicht rückwirkend berichtigt.

## 4. Primärquellenzugang und Aussagegrenzen

Grundlage bleibt SRC-002, CELEX 02024R1689-20260727; insbesondere Art. 111 Abs. 2 und Art. 113 Buchst. c Ziff. i. Keine Quellenaktualisierung und keine neue Normprüfung. Gezielter amtlicher Zugang am 04.11.2026: EUR-Lex-indexierte EN-Passagen zum einschlägigen Anwendungsbeginn, zur signifikanten Änderung und Behördenfrist zugänglich ([konsolidierter Text](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27), [amtliche konsolidierte PDF-Fundstelle](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02024R1689-20260727)). Direkte DE-/EN-Volltext- und PDF-Aufrufe zeigten eine JavaScript-Schranke. Daher kein neu vollständig gelesener DE/EN-Rechtsakt behauptet; die bestehende dokumentierte Primärrechtsauslegung wird technisch vervollständigt.

Die Tests prüfen spezifikationsgemäßes Verhalten der gezielten Korrektur. Sie bestätigen keine unabhängige regulatorische Richtigkeit, Nutzungswirksamkeit oder neue Evaluation des Maßnahmenstands 0.2. Die bestehenden Quellenpaket-, Referenz-, Berichts- und Reproduktionsgrenzen bleiben erhalten. Word, PDF, Pages, Manuskripttexte und Abbildungen werden in diesem technischen Auftrag nicht aktualisiert.

[Byte-Schutzvergleich](annex-iii-transition-2026-11-04/schutzvergleich.json): 96 besonders geschützte versionierte Pfade einschließlich Manuskript, historischer Ergebnisse, bestehender Evidenzdateien und Ausgaben unverändert; fünf bereits vor dem Auftrag fehlende Ausgabedateien nicht wiederhergestellt oder mitgestagt.
