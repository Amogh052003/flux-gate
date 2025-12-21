from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.env import router as env_router
from app.api.metrics import router as metrics_router


def create_app() -> FastAPI:
    app = FastAPI(title="FluxGate Control Hub")

    # CORS (UI access)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # tighten later
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(env_router, prefix="/api")
    app.include_router(metrics_router, prefix="/api")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()
