# RegScoutX

Lokaler Demonstrator zur regelbasierten Anforderungs- und Gap-Analyse für KI-basierte Medizinproduktesoftware. Anhand eines Produktprofils ordnet RegScoutX das Produkt ein und bestimmt, welche Anforderungen anwendbar sind. Aus den eingegebenen Erfüllungsangaben und Nachweisreferenzen leitet es Gap-Ergebnisse ab und erstellt Berichte in HTML und PDF. Die Masterarbeit wird separat eingereicht.

## Start

Voraussetzung ist Python ab 3.12. Die Weboberfläche ist bereits gebaut. Für den Start genügt Python. Im Repository-Verzeichnis die folgenden Befehle ausführen und bei Bedarf `python3` durch den Aufruf der passenden Python-Version ersetzen:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m regscoutx.web_server --data ./daten
```

Im Browser [localhost:8787](http://127.0.0.1:8787/) öffnen. Ist Port 8787 belegt, beim Start etwa `--port 8788` ergänzen und die entsprechende Adresse öffnen. Bewertungen werden lokal in `daten/` gespeichert. Unter Windows entsprechend `py -3` und `.venv\Scripts\python.exe` verwenden (nicht getestet).

## Inhalt und Prüfung

- `regscoutx/` und `web/`: Anwendung und Weboberfläche. Optionaler Neubau: `npm ci` und `npm run build` in `web/` (Node.js ab 22.13).
- `docs/`: Laufzeitkataloge und Belege. R1 ist der erste Evaluationslauf, R2 der Lauf nach Korrekturen an Software und Prüfwerkzeug. Beide verwenden die [eingefrorenen Katalogstände](docs/08-evaluation/frozen/README.md). Historische Commit-Kennungen beziehen sich auf das Entwicklungsrepository.
- `DATEIEN.sha256`: Prüfsummen der mitgelieferten Dateien. Unter macOS mit `shasum -a 256 -c DATEIEN.sha256` prüfen. Die Lizenzen der gebündelten Bibliotheken stehen in `web/dist/.vite/license.md`.

```sh
.venv/bin/python tools/traceability.py --markdown
.venv/bin/python tools/derive_case_reference.py --check
```

Der erste Befehl erzeugt die Traceability-Matrix, der zweite vergleicht die erneut abgeleitete Fallreferenz mit der gespeicherten Fassung. Für eine vollständige Wiederholung von R1 und R2 wären weitere Testsuiten und Evaluationsprogramme erforderlich. `tools/validate_test_catalog.py` dient im Paket als Modul für `traceability.py`. Ein eigenständiger Prüflauf benötigt zusätzliche Testdateien.
