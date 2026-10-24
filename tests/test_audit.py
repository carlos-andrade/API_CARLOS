# API-CARLOS | tests/test_audit.py
# ID: API-CARLOS-SRC-TESTS-TEST-AUDIT-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: TESTES PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.1.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Testes do trilho de auditoria persistente
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

import sqlite3

from app.audit import initialize_audit_store, record_request


def test_audit_event_is_persisted_and_query_string_is_not_in_event(tmp_path):
    database = tmp_path / "audit.sqlite3"
    initialize_audit_store(str(database))
    event = {
        "request_id": "test-id",
        "method": "POST",
        "path": "/v1/extractions",
        "status_code": 200,
        "duration_ms": 12.5,
        "client_ip": "127.0.0.1",
    }
    record_request(str(database), event)
    with sqlite3.connect(database) as connection:
        row = connection.execute(
            "SELECT request_id, method, path, status_code, duration_ms, client_ip FROM request_audit"
        ).fetchone()
    assert row == ("test-id", "POST", "/v1/extractions", 200, 12.5, "127.0.0.1")
