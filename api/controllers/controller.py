import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api import settings


templates = Jinja2Templates(directory="templates")
api_router = APIRouter(prefix=settings.prefix)


@api_router.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request, "message": "Hello, FastAPI!"})
