import pandas as pd

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")


def fetch_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request, "message": "Hello, FastAPI!"})


def fetch_historic(request: Request):
    historic = pd.read_csv("data/historic.csv", sep=";")
    response = HTMLResponse(content=historic.to_html(), status_code=200)
    return response


def fetch_last_operations():
    return


def add_new_operation():
    return
