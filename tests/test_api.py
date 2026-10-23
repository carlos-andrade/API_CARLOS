from fastapi.testclient import TestClient
from app.main import app


def test_liveness():
    response = TestClient(app).get("/health/live")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_readiness():
    response = TestClient(app).get("/health/ready")
    assert response.status_code == 200
    assert response.json()["version"] == "0.1.0"


def test_extraction_requires_url():
    response = TestClient(app).post("/v1/extractions", json={})
    assert response.status_code == 422
