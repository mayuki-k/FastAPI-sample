#TODO:cssやjsなどの紐付け

from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index():
    return {"A": "Apple"}

@app.get("/temp")
def temp(request:Request):
    title = "Templates Test"
    return templates.TemplateResponse("index.html", {"request": request, "title": title})

if __name__ == "__main__":
    uvicorn.run("app:app")