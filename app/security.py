# API-CARLOS | app/security.py
# ID: API-CARLOS-SRC-APP-SECURITY-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: MÓDULO PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.2.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Endurecimento da API após revisão de segurança
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

"""Validação de destinos, autenticação e controlo básico de abuso."""
import hmac
import ipaddress
import socket
import time
from collections import defaultdict, deque
from threading import Lock
from urllib.parse import urlsplit

from fastapi import Header, HTTPException, Request

from app.config import settings

_rate_events: dict[str, deque[float]] = defaultdict(deque)
_rate_lock = Lock()


def validate_public_url(url: str) -> str:
    """Valida esquema, credenciais, allowlist e todos os endereços resolvidos."""
    try:
        parsed = urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("Apenas URLs HTTP(S) absolutas são aceites.")
        if parsed.username or parsed.password:
            raise ValueError("Credenciais embutidas no URL não são permitidas.")
        if parsed.port is not None and not 1 <= parsed.port <= 65535:
            raise ValueError("Porta inválida.")
        host = parsed.hostname.rstrip(".").lower()
        if host == "localhost" or host.endswith((".localhost", ".local", ".internal", ".test")):
            raise ValueError("Host local ou interno bloqueado.")
        if settings.allowed_host_set and host not in settings.allowed_host_set:
            raise ValueError("Host não incluído na allowlist configurada.")
        try:
            addresses = [ipaddress.ip_address(host)]
        except ValueError:
            if settings.app_env.lower() in {"production", "prod"} and settings.egress_proxy_url:
                # Em produção, o proxy resolve o destino no momento da ligação e aplica ACL de egress.
                # A API não faz uma segunda resolução DNS suscetível a TOCTOU.
                return url
            answers = socket.getaddrinfo(
                host,
                parsed.port or (443 if parsed.scheme == "https" else 80),
                type=socket.SOCK_STREAM,
            )
            addresses = [ipaddress.ip_address(answer[4][0].split("%", 1)[0]) for answer in answers]
        if not addresses or any(not address.is_global for address in addresses):
            raise ValueError("O URL resolve para endereço não público.")
        return url
    except (ValueError, OSError, socket.gaierror) as exc:
        raise HTTPException(
            status_code=400,
            detail={"code": "URL_NOT_ALLOWED", "message": str(exc)},
        ) from exc


async def require_api_key(
    request: Request, authorization: str | None = Header(default=None)
) -> None:
    """Exige token em produção e compara credenciais em tempo constante."""
    keys = settings.api_key_set
    if settings.app_env.lower() in {"production", "prod"} and not keys:
        raise HTTPException(
            status_code=503,
            detail={"code": "AUTH_MISCONFIGURED", "message": "Autenticação não configurada."},
        )
    if keys:
        scheme, _, token = (authorization or "").partition(" ")
        if scheme.lower() != "bearer" or not token or not any(
            hmac.compare_digest(token, expected) for expected in keys
        ):
            raise HTTPException(
                status_code=401,
                headers={"WWW-Authenticate": "Bearer"},
                detail={"code": "AUTH_INVALID", "message": "Credencial inválida ou ausente."},
            )
    enforce_rate_limit(request)


def enforce_rate_limit(request: Request) -> None:
    """Rate limit local por cliente; em produção multi-instância exige gateway partilhado."""
    now = time.monotonic()
    window = settings.rate_limit_window_seconds
    key = request.client.host if request.client else "unknown"
    cutoff = now - window
    with _rate_lock:
        events = _rate_events[key]
        while events and events[0] <= cutoff:
            events.popleft()
        if len(events) >= settings.rate_limit_requests:
            raise HTTPException(
                status_code=429,
                headers={"Retry-After": str(max(1, int(window)))},
                detail={"code": "RATE_LIMITED", "message": "Limite de pedidos excedido."},
            )
        events.append(now)
