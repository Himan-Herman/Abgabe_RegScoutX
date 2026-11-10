# RegScoutX

Lokaler Demonstrator zur regelbasierten Anforderungs- und Gap-Analyse für KI-basierte Medizinproduktesoftware. Die Masterarbeit wird separat eingereicht.

## Start

Python ab 3.12. Die Weboberfläche ist bereits gebaut; Node.js ist für den Start nicht erforderlich. Im Repository-Verzeichnis ausführen:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m regscoutx.web_server --data ./daten
```

Im Browser [localhost:8787](http://127.0.0.1:8787/) öffnen. Bewertungen werden lokal in `daten/` gespeichert. Unter Windows entsprechend `py -3` und `.venv\Scripts\python.exe` verwenden (nicht getestet).

## Inhalt und Prüfung

- `regscoutx/` und `web/`: Anwendung und Weboberfläche. Optionaler Neubau: `npm ci` und `npm run build` in `web/` (Node.js ab 22.13).
- `docs/`: Laufzeitkataloge und Belege. Für R1 und R2 gelten die eingefrorenen Katalogstände in `docs/08-evaluation/frozen/`. Historische Commit-Kennungen beziehen sich auf das Entwicklungsrepository.
- `DATEIEN.sha256`: Prüfsummen der mitgelieferten Dateien. Die Lizenzen der gebündelten Bibliotheken stehen in `web/dist/.vite/license.md`.

```sh
.venv/bin/python tools/traceability.py --markdown
.venv/bin/python tools/derive_case_reference.py --check
```

Der erste Befehl erzeugt die Traceability-Matrix, der zweite vergleicht die erneut abgeleitete Referenz mit der gespeicherten Fassung. Vollständige Testsuiten und Evaluationsprogramme sind nicht enthalten. Der eigenständige Aufruf von `validate_test_catalog.py` meldet deshalb fehlende Testdateien.
