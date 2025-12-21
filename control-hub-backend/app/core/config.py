import logging
from functools import lru_cache
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    # GitHub
    github_token: str
    github_owner: str
    github_repo: str
    github_api_base: AnyHttpUrl = "https://api.github.com"

    # Argo CD
    argocd_base_url: AnyHttpUrl | None = None
    argocd_token: str | None = None
    argocd_app_name_dev: str | None = None

    # Prometheus
    prometheus_base_url: AnyHttpUrl | None = None

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    logging.getLogger(__name__).info("Loading settings")
    return Settings()


settings = get_settings()
