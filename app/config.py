# API-CARLOS | app/config.py
# ID: API-CARLOS-SRC-APP-CONFIG-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: MÓDULO PYTHON | Fase: I3 — Núcleo técnico inicial | Estado: EM_REVISAO
# Versão: 0.1.0 | Data de atualização: 2026-10-23 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: artefacto do projeto API_CARLOS
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

"""Configuração tipada e limites operacionais do serviço."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "API_CARLOS"
    app_env: str = "development"
    log_level: str = "INFO"
    request_timeout_seconds: float = 15.0
    max_response_bytes: int = 5_000_000
    max_text_chars: int = 200_000
    allowed_hosts: str = ""
    api_keys: str = ""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def allowed_host_set(self) -> set[str]:
        return {host.strip().lower() for host in self.allowed_hosts.split(",") if host.strip()}

    @property
    def api_key_set(self) -> set[str]:
        return {key.strip() for key in self.api_keys.split(",") if key.strip()}


settings = Settings()
