"""Controlos de URL e autenticação; política de acesso restritiva por defeito."""
import ipaddress
import socket
from urllib.parse import urlsplit

from fastapi import Header, HTTPException

from app.config import settings


def validate_public_url(url: str) -> str:
    """Valida esquema, host, allowlist opcional e endereços IP públicos."""
    try:
        parsed = urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("Apenas URLs HTTP(S) absolutas são aceites.")
        if parsed.username or parsed.password:
            raise ValueError("Credenciais embutidas no URL não são permitidas.")
        host = parsed.hostname.rstrip(".").lower()
        if host in {"localhost"} or host.endswith((".localhost", ".local", ".internal")):
            raise ValueError("Host local ou interno bloqueado.")
        if settings.allowed_host_set and host not in settings.allowed_host_set:
            raise ValueError("Host não incluído na allowlist configurada.")
        try:
            addresses = [ipaddress.ip_address(host)]
        except ValueError:
            addresses = [ipaddress.ip_address(item[4][0]) for item in socket.getaddrinfo(
                host, parsed.port or (443 if parsed.scheme == "https" else 80),
                type=socket.SOCK_STREAM
            )]
        if not addresses or any(not address.is_global for address in addresses):
            raise ValueError("O URL resolve para endereço não público.")
        return url
    except (ValueError, OSError, socket.gaierror) as exc:
        raise HTTPException(status_code=400, detail={"code": "URL_NOT_ALLOWED", "message": str(exc)}) from exc


async def require_api_key(authorization: str | None = Header(default=None)) -> None:
    """Quando API_KEYS estiver configurado, exige Bearer token."""
    if not settings.api_key_set:
        return
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail={"code": "AUTH_REQUIRED", "message": "Bearer token obrigatório."})
    token = authorization.removeprefix("Bearer ").strip()
    if token not in settings.api_key_set:
        raise HTTPException(status_code=403, detail={"code": "AUTH_INVALID", "message": "Credencial inválida."})
