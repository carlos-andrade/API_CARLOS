# API-CARLOS | tests/test_api.py
# ID: API-CARLOS-SRC-TESTS-TEST-API-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: TESTES PYTHON | Fase: I3 — Núcleo técnico inicial | Estado: EM_REVISAO
# Versão: 0.1.0 | Data de atualização: 2026-10-23 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: artefacto do projeto API_CARLOS
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

from fastapi.testclient import TestClient

from app.config import settings
from app.main import app


def test_liveness():
    response = TestClient(app).get("/health/live")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_readiness():
    response = TestClient(app).get("/health/ready")
    assert response.status_code == 200
    assert response.json()["version"] == "0.2.0"


def test_extraction_requires_url():
    response = TestClient(app).post("/v1/extractions", json={})
    assert response.status_code == 422



def test_extraction_requires_bearer_when_api_keys_are_configured(monkeypatch):
    monkeypatch.setattr(settings, "api_keys", "test-secret-token-that-is-long-enough-123456")
    client = TestClient(app)
    response = client.post("/v1/extractions", json={"url": "http://127.0.0.1/"})
    assert response.status_code == 401

    response = client.post(
        "/v1/extractions",
        headers={"Authorization": "Bearer test-secret-token-that-is-long-enough-123456"},
        json={"url": "http://127.0.0.1/"},
    )
    assert response.status_code == 400
    assert response.json()["detail"]["code"] == "URL_NOT_ALLOWED"
