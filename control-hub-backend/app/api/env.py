from fastapi import APIRouter, HTTPException, status

from app.models.env import (
    DevStatusResponse,
    SwitchRequest,
    SwitchResponse,
)
from app.services.github_services import GitHubService
from app.services.argocd_services import ArgoCDService

router = APIRouter(prefix="/env/dev", tags=["env-dev"])


@router.get("/status", response_model=DevStatusResponse)
def get_dev_status():
    github = GitHubService()
    argocd = ArgoCDService()

    try:
        active_color = github.get_active_color("dev")
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Failed to read traffic config: {exc}",
        )

    argo_status = argocd.get_application_status("dev")

    return DevStatusResponse(
        environment="dev",
        active_color=active_color,
        argo=argo_status,
    )


@router.post("/switch", response_model=SwitchResponse)
def switch_dev_traffic(payload: SwitchRequest):
    github = GitHubService()

    current_color = github.get_active_color("dev")

    if payload.target_color == current_color:
        return SwitchResponse(
            environment="dev",
            previous_color=current_color,
            new_color=current_color,
            changed=False,
            message="Traffic already routed to requested color.",
        )

    github.update_active_color("dev", payload.target_color)

    return SwitchResponse(
        environment="dev",
        previous_color=current_color,
        new_color=payload.target_color,
        changed=True,
        message="Traffic switch committed to Git. Argo CD will reconcile.",
    )
