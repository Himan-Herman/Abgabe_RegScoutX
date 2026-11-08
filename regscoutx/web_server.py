"""APPLICATION_API: lokaler HTTP-Server und Composition Root der Web-Anwendung (ADR-0007).

Standardbibliothek (http.server), nur an localhost gebunden. Liefert die gebaute
Oberfläche (web/dist) und die JSON-API aus. Schutzmaßnahmen: Host-Prüfung gegen
DNS-Rebinding, Pflicht-Header für schreibende Anfragen (kein CSRF über einfache
Formulare), strikte Content-Security-Policy, keine CORS-Freigaben, begrenzte
Anfragegröße, pfadsichere Auslieferung statischer Dateien. Einzige Stelle, die
eine konkrete Persistenzimplementierung erzeugt.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

from regscoutx.assessment_application import AssessmentApplicationService
from regscoutx.catalog_repository import CatalogRepository
from regscoutx.json_assessment_repository import JsonFileAssessmentRepository
from regscoutx.web_api import JSON, ApiApplication, Response

MAX_BODY = 1_000_000
WRITE_HEADER = "X-RegScoutX-Request"
CSP = ("default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; "
       "font-src 'self'; connect-src 'self'; manifest-src 'self'; object-src 'none'; "
       "base-uri 'none'; form-action 'self'; frame-ancestors 'none'")
SECURITY_HEADERS = {"Content-Security-Policy": CSP, "X-Content-Type-Options": "nosniff",
                    "Referrer-Policy": "no-referrer", "X-Frame-Options": "DENY",
                    "Cross-Origin-Opener-Policy": "same-origin",
                    "Permissions-Policy": "camera=(), microphone=(), geolocation=()"}


def make_handler(api: ApiApplication, static_root: Path | None, allowed_hosts: set[str]):

    class Handler(BaseHTTPRequestHandler):
        server_version = "RegScoutX"
        sys_version = ""

        def log_message(self, format: str, *args: Any) -> None:  # keine Inhalte protokollieren
            return

        def _send(self, response: Response, cache: str = "no-store") -> None:
            self.send_response(response.status)
            self.send_header("Content-Type", response.content_type)
            self.send_header("Content-Length", str(len(response.body)))
            self.send_header("Cache-Control", cache)
            self.send_header("Connection", "close")
            for name, value in {**SECURITY_HEADERS, **response.headers}.items():
                self.send_header(name, value)
            try:
                self.end_headers()
                if self.command != "HEAD":
                    self.wfile.write(response.body)
            except (BrokenPipeError, ConnectionResetError):
                # Der Browser hat die Anfrage abgebrochen (z. B. Navigation); kein Fachzustand betroffen.
                self.close_connection = True

        def _error(self, status: int, code: str) -> None:
            self._send(Response(status, json.dumps({"error": {"code": code}}).encode(), JSON))

        def _dispatch(self) -> None:
            if self.headers.get("Host", "") not in allowed_hosts:
                return self._error(HTTPStatus.FORBIDDEN, "HOST_NOT_ALLOWED")
            url = urlsplit(self.path)
            if not url.path.startswith("/api/"):
                if self.command not in ("GET", "HEAD"):
                    return self._error(HTTPStatus.METHOD_NOT_ALLOWED, "METHOD_NOT_ALLOWED")
                return self._static(url.path)
            # Browser kennzeichnen seitenfremde Anfragen; auch lesende API-Aufrufe (z. B.
            # Berichtserzeugung mit Audit-Ereignis) werden nur von derselben Herkunft angenommen.
            if self.headers.get("Sec-Fetch-Site", "same-origin") not in ("same-origin", "none"):
                return self._error(HTTPStatus.FORBIDDEN, "CROSS_SITE_REQUEST")
            body = None
            if self.command in ("POST", "PUT", "PATCH", "DELETE"):
                if self.headers.get(WRITE_HEADER) != "1":
                    return self._error(HTTPStatus.FORBIDDEN, "MISSING_REQUEST_HEADER")
                try:
                    length = int(self.headers.get("Content-Length") or 0)
                except ValueError:
                    return self._error(HTTPStatus.BAD_REQUEST, "BAD_REQUEST")
                if length < 0:
                    return self._error(HTTPStatus.BAD_REQUEST, "BAD_REQUEST")
                if length > MAX_BODY:
                    return self._error(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, "BODY_TOO_LARGE")
                if length:
                    if not (self.headers.get("Content-Type") or "").startswith("application/json"):
                        return self._error(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, "JSON_REQUIRED")
                    try:
                        body = json.loads(self.rfile.read(length).decode("utf-8"))
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        return self._error(HTTPStatus.BAD_REQUEST, "INVALID_JSON")
            self._send(api.handle(self.command, url.path, dict(parse_qsl(url.query)), body))

        def _static(self, path: str) -> None:
            if static_root is None:
                return self._error(HTTPStatus.NOT_FOUND, "NOT_FOUND")
            candidate = (static_root / path.lstrip("/")).resolve()
            if static_root not in candidate.parents and candidate != static_root:
                return self._error(HTTPStatus.NOT_FOUND, "NOT_FOUND")
            if not candidate.is_file():
                candidate = static_root / "index.html"  # Einstieg der Einzelseitenanwendung
            content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
            if candidate.suffix == ".webmanifest":
                content_type = "application/manifest+json"
            cache = "no-cache" if candidate.name == "index.html" else "public, max-age=31536000, immutable" \
                if "/assets/" in candidate.as_posix() else "no-cache"
            self._send(Response(200, candidate.read_bytes(), content_type), cache)

        do_GET = do_HEAD = do_POST = do_PUT = do_PATCH = do_DELETE = _dispatch

    return Handler


class LocalServer(ThreadingHTTPServer):
    # Browser öffnen parallel mehrere Verbindungen (Skripte, Schriften, API); die Standard-
    # Warteschlange von 5 führt sonst zu abgewiesenen Verbindungen.
    request_queue_size = 64
    daemon_threads = True


def build_server(data_dir: Path, static_root: Path | None, host: str, port: int,
                 catalogs: CatalogRepository | None = None) -> LocalServer:
    if host not in ("127.0.0.1", "localhost", "::1"):
        raise ValueError("the demonstrator server only binds to localhost")
    catalogs = catalogs or CatalogRepository.load()
    service = AssessmentApplicationService(catalogs, JsonFileAssessmentRepository(data_dir))
    api = ApiApplication(catalogs, service)
    server = LocalServer((host, port), None)  # type: ignore[arg-type]
    actual_port = server.server_address[1]
    allowed = {f"127.0.0.1:{actual_port}", f"localhost:{actual_port}"}
    server.RequestHandlerClass = make_handler(api, static_root.resolve() if static_root else None,
                                              allowed)
    return server


def main() -> int:
    parser = argparse.ArgumentParser(description="RegScoutX local demonstrator server")
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--static", type=Path, default=Path("web/dist"))
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    static = args.static if args.static.is_dir() else None
    server = build_server(args.data, static, args.host, args.port)
    print(f"RegScoutX: http://{args.host}:{server.server_address[1]}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
