from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from api import settings


api_router = APIRouter(prefix=settings.prefix)


@api_router.get("/", response_model=str)
def home_page() -> str:
    return "Hello World"
