import pandas as pd

from fastapi import Request

from api.tools.tools import format_float_number
from api import templates


def fetch_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request, "message": "Hello, FastAPI!"})


def fetch_historic(request: Request):
    data = pd.read_csv(f"data/historic.csv", sep=";")

    html_table = data.to_html(
        col_space=120,
        justify="center",
        classes="center-table",
        escape=False,
        na_rep="",
        float_format=format_float_number
    )

    response = templates.TemplateResponse(
        "historic.html", {"request": request, "table_content": html_table}
    )
    return response


def fetch_last_operations(request: Request, car_name: str):
    """This method is importing a CSV file, processing the data and then return a HTML response"""
    data = pd.read_csv(f"data/last_operations_{car_name}.csv", sep=";")

    integer_columns = data.select_dtypes(include=["int", "float"]).columns
    data[integer_columns] = data[integer_columns].astype(float)

    html_table = data.to_html(
        col_space=120,
        justify="center",
        classes="center-table",
        escape=False,
        na_rep="",
        float_format=format_float_number
    )

    response = templates.TemplateResponse(
        "last_operations.html", {"request": request, "table_content": html_table}
    )
    return response


def add_new_operation():
    return
