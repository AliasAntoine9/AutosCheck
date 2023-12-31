from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse


from api import settings
from api.services.service import fetch_homepage, fetch_historic, fetch_last_operations


api_router = APIRouter(prefix=settings.prefix)


@api_router.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return fetch_homepage(request)


@api_router.get("/historic", response_class=HTMLResponse)
def get_historic():
    return fetch_historic()


@api_router.get("/last_operations/{car_name}", response_class=HTMLResponse)
def get_last_operation(car_name: str):
    return fetch_last_operations(car_name)
