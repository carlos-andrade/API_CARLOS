# API-CARLOS | app/extraction.py
# ID: API-CARLOS-SRC-APP-EXTRACTION-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: MÓDULO PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.2.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Endurecimento do cliente de extração HTTP
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

"""Extração HTTP com redirects bloqueados e limites de tempo e conteúdo."""
import asyncio
import csv
import io
import json
import xml.etree.ElementTree as ET
from datetime import UTC, datetime

import httpx
from bs4 import BeautifulSoup
from fastapi import HTTPException

from app.config import settings
from app.security import validate_public_url


async def extract_url(url: str) -> dict:
    safe_url = validate_public_url(url)
    timeout = httpx.Timeout(settings.request_timeout_seconds, connect=min(5.0, settings.request_timeout_seconds))
    try:
        async with asyncio.timeout(settings.request_timeout_seconds), httpx.AsyncClient(
                timeout=timeout,
                follow_redirects=False,
                trust_env=False,
                proxy=settings.egress_proxy_url or None,
                headers={"User-Agent": "API_CARLOS/0.2 (+public-data-extraction)"},
            ) as client:
                async with client.stream("GET", safe_url) as response:
                    if 300 <= response.status_code < 400:
                        raise HTTPException(
                            status_code=400,
                            detail={"code": "REDIRECT_BLOCKED", "message": "Redirecionamentos bloqueados; valide o destino separadamente."},
                        )
                    response.raise_for_status()
                    chunks, total = [], 0
                    async for chunk in response.aiter_bytes():
                        total += len(chunk)
                        if total > settings.max_response_bytes:
                            raise HTTPException(
                                status_code=413,
                                detail={"code": "RESPONSE_TOO_LARGE", "message": "A resposta excede o limite configurado."},
                            )
                        chunks.append(chunk)
                    body = b"".join(chunks)
                    content_type = response.headers.get("content-type", "").split(";")[0].lower()
                    status_code = response.status_code
    except HTTPException:
        raise
    except TimeoutError as exc:
        raise HTTPException(
            status_code=504,
            detail={"code": "SOURCE_TIMEOUT", "message": "A fonte excedeu o tempo limite."},
        ) from exc
    except httpx.TimeoutException as exc:
        raise HTTPException(
            status_code=504,
            detail={"code": "SOURCE_TIMEOUT", "message": "A fonte excedeu o tempo limite."},
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail={"code": "SOURCE_HTTP_ERROR", "message": "Falha ao consultar a fonte."},
        ) from exc

    text = body.decode("utf-8-sig", errors="replace")[:settings.max_text_chars]
    data, parser = text, "text"
    try:
        if content_type == "application/json" or content_type.endswith("+json"):
            data, parser = json.loads(text), "json"
        elif content_type in {"text/csv", "application/csv"}:
            data, parser = list(csv.DictReader(io.StringIO(text))), "csv"
        elif content_type in {"application/xml", "text/xml"} or content_type.endswith("+xml"):
            root = ET.fromstring(text)
            data, parser = {"root": root.tag, "xml": text}, "xml"
        elif content_type in {"text/html", "application/xhtml+xml"}:
            soup = BeautifulSoup(text, "html.parser")
            data, parser = {
                "title": soup.title.get_text(" ", strip=True) if soup.title else None,
                "text": soup.get_text(" ", strip=True)[:settings.max_text_chars],
                "links": [a.get("href") for a in soup.find_all("a", href=True)[:500]],
            }, "html"
    except (json.JSONDecodeError, csv.Error, ET.ParseError) as exc:
        raise HTTPException(
            status_code=422,
            detail={"code": "PARSE_ERROR", "message": "Conteúdo recebido não corresponde ao formato anunciado."},
        ) from exc

    return {
        "source_url": safe_url,
        "retrieved_at": datetime.now(UTC).isoformat(),
        "http_status": status_code,
        "content_type": content_type or "application/octet-stream",
        "parser": parser,
        "data": data,
        "truncated": len(body) > settings.max_text_chars,
    }
