import pandas as pd

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from api.tools.tools import format_float_number

templates = Jinja2Templates(directory="templates")


def fetch_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request, "message": "Hello, FastAPI!"})


def fetch_historic():
    data = pd.read_csv(f"data/historic.csv", sep=";")
    response = HTMLResponse(content=data.to_html(), status_code=200)
    return response


def fetch_last_operations(car_name: str):
    """This method is importing a CSV file, processing the data and then return a HTML response"""
    data = pd.read_csv(f"data/last_operations_{car_name}.csv", sep=";")

    integer_columns = data.select_dtypes(include=["int", "float"]).columns
    data[integer_columns] = data[integer_columns].astype(float)

    response = HTMLResponse(
        content=data.to_html(
            col_space=120,
            justify="center",
            na_rep="",
            float_format=format_float_number
        ),
        status_code=200
    )
    return response


def add_new_operation():
    return
