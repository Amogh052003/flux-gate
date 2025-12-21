import base64
import yaml
import requests

from app.core.config import settings


class GitHubService:
    def __init__(self):
        self.base = settings.github_api_base.rstrip("/")
        self.repo = f"{settings.github_owner}/{settings.github_repo}"
        self.headers = {
            "Authorization": f"Bearer {settings.github_token}",
            "Accept": "application/vnd.github+json",
        }

    def _traffic_path(self, env: str) -> str:
        return f"environments/{env}/traffic.yaml"

    def _get_file(self, path: str):
        url = f"{self.base}/repos/{self.repo}/contents/{path}"
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        data = r.json()
        content = base64.b64decode(data["content"]).decode()
        return content, data["sha"]

    def _put_file(self, path: str, content: str, sha: str, message: str):
        url = f"{self.base}/repos/{self.repo}/contents/{path}"
        payload = {
            "message": message,
            "content": base64.b64encode(content.encode()).decode(),
            "sha": sha,
        }
        r = requests.put(url, headers=self.headers, json=payload)
        r.raise_for_status()

    def get_active_color(self, environment: str) -> str:
        raw, _ = self._get_file(self._traffic_path(environment))
        doc = yaml.safe_load(raw)
        return doc["spec"]["selector"]["color"]

    def update_active_color(self, environment: str, target_color: str):
        raw, sha = self._get_file(self._traffic_path(environment))
        doc = yaml.safe_load(raw)

        doc.setdefault("spec", {}).setdefault("selector", {})
        doc["spec"]["selector"]["color"] = target_color

        updated = yaml.safe_dump(doc, sort_keys=False)
        self._put_file(
            self._traffic_path(environment),
            updated,
            sha,
            f"chore({environment}): switch traffic to {target_color}",
        )
