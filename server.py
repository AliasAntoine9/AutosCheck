from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def home_page():
    return {"messages": "Hello World"}
