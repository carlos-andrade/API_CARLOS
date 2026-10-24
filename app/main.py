# API-CARLOS | app/main.py
# ID: API-CARLOS-SRC-APP-MAIN-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: MÓDULO PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.2.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Endurecimento do serviço HTTP
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

"""Aplicação HTTP da API_CARLOS."""
import asyncio
import json
import logging
import time
import uuid
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Request
from pydantic import BaseModel, Field, HttpUrl

from app.audit import initialize_audit_store, record_request
from app.config import settings
from app.extraction import extract_url
from app.security import require_api_key

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
logger = logging.getLogger("api_carlos.audit")
_extraction_slots = asyncio.Semaphore(settings.max_concurrent_extractions)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.validate_production()
    if settings.audit_db_path:
        initialize_audit_store(settings.audit_db_path)
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.2.0",
    description="API de extração controlada de dados públicos; a produção exige configuração segura.",
    lifespan=lifespan,
)


@app.middleware("http")
async def audit_requests(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))[:128]
    started = time.monotonic()
    response = None
    try:
        response = await call_next(request)
        return response
    finally:
        event = {
                    "event": "http_request",
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": response.status_code if response else 500,
                    "duration_ms": round((time.monotonic() - started) * 1000, 2),
                    "client_ip": request.client.host if request.client else None,
                }
        logger.info(json.dumps(event, separators=(",", ":")))
        if settings.audit_db_path:
            record_request(settings.audit_db_path, event)


class ExtractionRequest(BaseModel):
    url: HttpUrl = Field(description="URL HTTP(S) pública incluída na allowlist operacional.")


@app.get("/health/live", tags=["health"])
async def live():
    return {"status": "ok", "service": settings.app_name}


@app.get("/health/ready", tags=["health"])
async def ready():
    settings.validate_production()
    return {"status": "ready", "version": "0.2.0"}


@app.post("/v1/extractions", tags=["extractions"], dependencies=[Depends(require_api_key)])
async def create_extraction(request: ExtractionRequest):
    """Extrai uma URL pública com limite de concorrência."""
    async with _extraction_slots:
        return await extract_url(str(request.url))


@app.get("/", include_in_schema=False)
async def root():
    return {"service": settings.app_name, "docs": "/docs", "openapi": "/openapi.json"}
