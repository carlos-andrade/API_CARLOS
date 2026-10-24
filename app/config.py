# API-CARLOS | app/config.py
# ID: API-CARLOS-SRC-APP-CONFIG-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: MÓDULO PYTHON | Fase: G2 — Endurecimento de segurança | Estado: EM_REVISAO
# Versão: 0.2.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Endurecimento da configuração da API
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

"""Configuração tipada e validação de pré-condições de produção."""
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
    egress_proxy_url: str = ""
    audit_db_path: str = ""
    rate_limit_requests: int = 60
    rate_limit_window_seconds: int = 60
    max_concurrent_extractions: int = 4
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def allowed_host_set(self) -> set[str]:
        return {host.strip().lower().rstrip(".") for host in self.allowed_hosts.split(",") if host.strip()}

    @property
    def api_key_set(self) -> set[str]:
        return {key.strip() for key in self.api_keys.split(",") if key.strip()}

    def validate_production(self) -> None:
        """Falha fechada: produção requer chaves, allowlist e limites válidos."""
        if self.app_env.lower() not in {"production", "prod"}:
            return
        missing = []
        if not self.api_key_set:
            missing.append("API_KEYS")
        if not self.allowed_host_set:
            missing.append("ALLOWED_HOSTS")
        if not self.egress_proxy_url.strip():
            missing.append("EGRESS_PROXY_URL (proxy de saída com política anti-SSRF)")
        if not self.audit_db_path.strip():
            missing.append("AUDIT_DB_PATH (auditoria persistente)")
        if self.rate_limit_requests < 1 or self.rate_limit_window_seconds < 1:
            missing.append("RATE_LIMIT_REQUESTS/RATE_LIMIT_WINDOW_SECONDS")
        if self.max_concurrent_extractions < 1:
            missing.append("MAX_CONCURRENT_EXTRACTIONS")
        if missing:
            raise RuntimeError("Configuração de produção inválida; configurar: " + ", ".join(missing))


settings = Settings()
