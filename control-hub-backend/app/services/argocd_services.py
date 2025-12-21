import logging
import requests

from app.core.config import settings
from app.models.env import ArgoStatus

logger = logging.getLogger(__name__)


class ArgoCDService:
    def __init__(self):
        self.enabled = bool(settings.argocd_base_url and settings.argocd_token)
        if not self.enabled:
            return

        self.base = settings.argocd_base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bearer {settings.argocd_token}"}
        )

    def get_application_status(self, environment: str) -> ArgoStatus:
        if not self.enabled:
            return ArgoStatus(sync_status="Unknown", health_status="Unknown")

        try:
            app = settings.argocd_app_name_dev
            url = f"{self.base}/api/v1/applications/{app}"
            r = self.session.get(url, verify=False, timeout=5)
            r.raise_for_status()
            data = r.json()
            return ArgoStatus(
                sync_status=data["status"]["sync"]["status"],
                health_status=data["status"]["health"]["status"],
            )
        except Exception as exc:
            logger.warning("Argo CD fetch failed: %s", exc)
            return ArgoStatus(sync_status="Unknown", health_status="Unknown")
