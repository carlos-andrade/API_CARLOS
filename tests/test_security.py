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
