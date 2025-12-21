import requests

from app.core.config import settings
from app.models.env import ColorMetrics


class PrometheusService:
    def __init__(self):
        if not settings.prometheus_base_url:
            raise RuntimeError("Prometheus not configured")
        self.base = settings.prometheus_base_url.rstrip("/")

    def query(self, promql: str) -> float:
        r = requests.get(
            f"{self.base}/api/v1/query",
            params={"query": promql},
            timeout=5,
        )
        r.raise_for_status()
        result = r.json()["data"]["result"]
        return float(result[0]["value"][1]) if result else 0.0

    def get_color_metrics(self, color: str, namespace: str) -> ColorMetrics:
        pods = self.query(
            f'count(kube_pod_labels{{label_color="{color}",namespace="{namespace}"}})'
        )
        cpu = self.query(
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",label_color="{color}"}}[1m]))'
        )
        mem = self.query(
            f'sum(container_memory_usage_bytes{{namespace="{namespace}",label_color="{color}"}})'
        ) / (1024 * 1024)

        return ColorMetrics(
            pods=int(pods),
            cpu_percent=round(cpu * 100, 2),
            memory_mb=round(mem, 2),
        )
