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
