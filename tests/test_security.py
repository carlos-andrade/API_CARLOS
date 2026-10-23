# API-CARLOS | tests/test_security.py
# ID: API-CARLOS-SRC-TESTS-TEST-SECURITY-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: TESTES PYTHON | Fase: I3 — Núcleo técnico inicial | Estado: EM_REVISAO
# Versão: 0.1.0 | Data de atualização: 2026-10-23 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: artefacto do projeto API_CARLOS
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

import pytest
from fastapi import HTTPException

from app.security import validate_public_url


def test_rejects_non_http_scheme():
    with pytest.raises(HTTPException) as exc:
        validate_public_url("file:///etc/passwd")
    assert exc.value.status_code == 400


def test_rejects_localhost():
    with pytest.raises(HTTPException) as exc:
        validate_public_url("http://localhost/admin")
    assert exc.value.status_code == 400


def test_rejects_embedded_credentials():
    with pytest.raises(HTTPException) as exc:
        validate_public_url("https://user:pass@example.com/data")
    assert exc.value.status_code == 400
