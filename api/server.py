from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.controllers.controller import api_router
from . import settings


def create_api() -> FastAPI:
    """This method generates the API server"""

    app = FastAPI(
        title=settings.api_name,
        version=settings.version,
    )

    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.include_router(api_router)

    return app
