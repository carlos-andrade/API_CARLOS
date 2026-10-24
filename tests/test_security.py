# API-CARLOS | tests/test_security.py
# ID: API-CARLOS-SRC-TESTS-TEST-SECURITY-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: TESTES PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.2.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Testes de regressão para controlos de segurança
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

import socket

import pytest
from fastapi import HTTPException

from app.config import Settings
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


@pytest.mark.parametrize("address", ["127.0.0.1", "10.0.0.2", "169.254.169.254", "::1", "fc00::1"])
def test_rejects_non_public_ip_addresses(address):
    with pytest.raises(HTTPException) as exc:
        validate_public_url(f"http://[{address}]/" if ":" in address else f"http://{address}/")
    assert exc.value.status_code == 400


def test_rejects_hostname_with_any_non_public_dns_answer(monkeypatch):
    def fake_getaddrinfo(*args, **kwargs):
        return [
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 0)),
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("10.0.0.8", 0)),
        ]

    monkeypatch.setattr(socket, "getaddrinfo", fake_getaddrinfo)
    with pytest.raises(HTTPException) as exc:
        validate_public_url("https://example.com/data")
    assert exc.value.status_code == 400


def test_production_requires_auth_allowlist_and_proxy():
    settings = Settings(app_env="production", api_keys="", allowed_hosts="", egress_proxy_url="")
    with pytest.raises(RuntimeError, match="API_KEYS"):
        settings.validate_production()


def test_production_rejects_missing_proxy():
    settings = Settings(
        app_env="production",
        api_keys="a-long-random-key",
        allowed_hosts="example.com",
        egress_proxy_url="",
    )
    with pytest.raises(RuntimeError, match="EGRESS_PROXY_URL"):
        settings.validate_production()
