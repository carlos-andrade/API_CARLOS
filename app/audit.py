# API-CARLOS | app/audit.py
# ID: API-CARLOS-SRC-APP-AUDIT-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: MÓDULO PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.1.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Implementação de trilho de auditoria persistente
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

"""Auditoria SQLite persistente, sem tokens nem query strings."""
import sqlite3
from datetime import UTC, datetime, timedelta
from pathlib import Path
from threading import Lock

_lock = Lock()


def initialize_audit_store(path_value: str, retention_days: int = 90) -> None:
    path = Path(path_value)
    path.parent.mkdir(parents=True, exist_ok=True)
    with _lock, sqlite3.connect(path, timeout=5) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS request_audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                occurred_at TEXT NOT NULL,
                request_id TEXT NOT NULL,
                method TEXT NOT NULL,
                path TEXT NOT NULL,
                status_code INTEGER NOT NULL,
                duration_ms REAL NOT NULL,
                client_ip TEXT
            )"""
        )
        cutoff = (datetime.now(UTC) - timedelta(days=retention_days)).isoformat()
        connection.execute("DELETE FROM request_audit WHERE occurred_at < ?", (cutoff,))
        connection.commit()


def record_request(path_value: str, event: dict) -> None:
    if not path_value:
        return
    path = Path(path_value)
    with _lock, sqlite3.connect(path, timeout=5) as connection:
        connection.execute(
            """INSERT INTO request_audit
            (occurred_at, request_id, method, path, status_code, duration_ms, client_ip)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                datetime.now(UTC).isoformat(),
                event["request_id"],
                event["method"],
                event["path"],
                event["status_code"],
                event["duration_ms"],
                event["client_ip"],
            ),
        )
        connection.commit()
