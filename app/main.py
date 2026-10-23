"""Aplicação HTTP da API_CARLOS."""
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field, HttpUrl

from app.config import settings
from app.extraction import extract_url
from app.security import require_api_key


class ExtractionRequest(BaseModel):
    url: HttpUrl = Field(description="URL HTTP(S) pública e acessível sem autenticação externa.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="API modular para extração controlada de dados públicos. Versão inicial síncrona.",
    lifespan=lifespan,
)


@app.get("/health/live", tags=["health"])
async def live():
    return {"status": "ok", "service": settings.app_name}


@app.get("/health/ready", tags=["health"])
async def ready():
    return {"status": "ready", "version": "0.1.0"}


@app.post("/v1/extractions", tags=["extractions"], dependencies=[Depends(require_api_key)])
async def create_extraction(request: ExtractionRequest):
    """Extrai uma URL pública e devolve conteúdo normalizado com proveniência."""
    return await extract_url(str(request.url))


@app.get("/", include_in_schema=False)
async def root():
    return {"service": settings.app_name, "docs": "/docs", "openapi": "/openapi.json"}
