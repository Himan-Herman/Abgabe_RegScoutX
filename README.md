# RegScoutX

Lokaler Demonstrator für eine regelbasierte Anforderungs- und Gap-Analyse für KI-basierte Medizinproduktesoftware. Die regulatorische Verarbeitung erfolgt deterministisch anhand versionierter Kataloge.

## Start

Voraussetzung: Python ab Version 3.12. Die gebaute Weboberfläche liegt unter `web/dist`; für ihren Betrieb ist Node.js nicht erforderlich.

Im Wurzelverzeichnis dieses Ordners:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m regscoutx.web_server --data ./daten
```

Windows-Hinweise (ungetestet): `py -3` zur Anlage der Umgebung und `.venv\Scripts\python.exe` anstelle von `.venv/bin/python` verwenden. Praktisch geprüft wurde der Betrieb unter macOS.

Danach im Browser `http://127.0.0.1:8787/` öffnen. Bewertungen werden lokal unter `daten/` gespeichert. Den Server mit Strg+C beenden. Für die Installation der Abhängigkeiten ist ein Paketquellenzugang erforderlich; die Anwendung selbst benötigt keine externen Dienste.

## Weboberfläche neu bauen

Optional, mit Node.js ab Version 22.13 und npm:

```sh
cd web
npm ci
npm run build
```

Danach den Python-Server wieder aus dem Wurzelverzeichnis starten. Der Quelltext der Weboberfläche liegt unter `web/src/`.

Der Build erzeugt unter `web/dist/.vite/license.md` die Lizenztexte der gebündelten Drittanbieterbibliotheken. Diese Datei liegt der fertigen Weboberfläche bei; sie betrifft die dort aufgeführten Bibliotheken.

## Inhalt und Nachweise

- `regscoutx/`: Anwendungskern, lokale Schnittstelle, Speicherung und Berichterzeugung.
- `web/`: Webquelltext, Konfiguration, Ressourcen und fertige Weboberfläche.
- `tools/`: die vom Anwendungskern benötigten Katalog- und Verweisprüfwerkzeuge sowie die Werkzeuge zur Referenzableitung.
- `docs/`: Laufzeitkataloge und benötigte Referenzdokumente sowie ausgewählte Methoden-, Testfall- und Evaluationsnachweise des Berichts.
- `DATEIEN.sha256`: SHA-256-Prüfsummen der enthaltenen Dateien, ausgenommen die Prüfsummenliste selbst.

Die Traceability-Matrix lässt sich aus den enthaltenen Katalogen ableiten:

```sh
.venv/bin/python tools/traceability.py --markdown
```

`tools/validate_test_catalog.py` ist als von `traceability.py` benötigtes Modul enthalten; sein eigenständiger Prüflauf setzt zusätzlich die hier nicht enthaltenen Testsuiten und Prüfprogramme voraus und meldet deshalb im Abgabepaket `FAIL`.

Die Referenz lässt sich mit den mitgelieferten Werkzeugen `derive_case_reference.py` und `frozen_evaluation_inputs.py` aus den eingefrorenen Daten erneut ableiten und mit der gespeicherten Referenz vergleichen:

```sh
.venv/bin/python tools/derive_case_reference.py --check
```

Mit `--check` wird die gespeicherte Referenz nicht verändert; Exitcode 0 bestätigt die Übereinstimmung.

Der aktuelle Demonstrator verwendet Regelkatalog 0.3, Anwendbarkeitszuordnung 0.5 und Maßnahmenkatalog 0.2. Die historischen Evaluationen R1/R2 beziehen sich auf die gesondert aufbewahrten Fassungen 0.2, 0.4 und 0.1. Ihre Ergebnisdateien und Originalprotokolle sind unverändert enthalten; sie beschreiben frühere Läufe. Die vollständigen automatisierten Testsuiten und Programme zur Durchführung der Evaluation sind nicht Bestandteil dieses Pakets. Einzelne Quell- und Methodendokumente verweisen außerdem auf weiterführende Entwicklungsunterlagen außerhalb dieses Pakets.

Dieser Ordner enthält keine Git-Historie. Commit-Kennungen in den Belegen bezeichnen Stände des ursprünglichen Entwicklungsrepositorys; daraus folgt keine lokale Überprüfbarkeit dieser Commits in diesem Ordner. Dokumentierte Hashwerte der mitgelieferten Artefakte bleiben überprüfbar. Die Masterarbeit wird separat übergeben.

Quellen-, Lizenz-, Versions- und historische Zeitangaben bleiben Bestandteil der zugehörigen Nachweise. Die Lizenzbedingungen der mitgelieferten Schriften stehen in den jeweiligen Schriftverzeichnissen. Lizenzierte Normvolltexte sind nicht enthalten.
