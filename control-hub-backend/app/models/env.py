from pydantic import BaseModel
from typing import Literal


Color = Literal["blue", "green"]


class ArgoStatus(BaseModel):
    sync_status: str
    health_status: str


class DevStatusResponse(BaseModel):
    environment: str
    active_color: Color
    argo: ArgoStatus


class SwitchRequest(BaseModel):
    target_color: Color


class SwitchResponse(BaseModel):
    environment: str
    previous_color: Color
    new_color: Color
    changed: bool
    message: str


class ColorMetrics(BaseModel):
    pods: int
    cpu_percent: float
    memory_mb: float


class MetricsResponse(BaseModel):
    environment: str
    blue: ColorMetrics
    green: ColorMetrics
