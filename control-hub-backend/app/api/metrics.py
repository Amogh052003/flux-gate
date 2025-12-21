from fastapi import APIRouter

from app.models.env import MetricsResponse, ColorMetrics
from app.services.prometheus_services import PrometheusService

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/dev", response_model=MetricsResponse)
def dev_metrics():
    prom = PrometheusService()

    try:
        blue = prom.get_color_metrics("blue", "fluxgate-dev")
        green = prom.get_color_metrics("green", "fluxgate-dev")
    except Exception:
        # Non-blocking
        blue = ColorMetrics(pods=0, cpu_percent=0, memory_mb=0)
        green = ColorMetrics(pods=0, cpu_percent=0, memory_mb=0)

    return MetricsResponse(
        environment="dev",
        blue=blue,
        green=green,
    )
