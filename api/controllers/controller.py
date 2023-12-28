from fastapi import APIRouter

from api import PREFIX


api_router = APIRouter(prefix=PREFIX)


@api_router.get("/", response_model=str)
def home_page() -> str:
    return "Hello World"
