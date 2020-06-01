from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Fruit(BaseModel):
    id:int
    name:str
    price:int

@app.get("/")
def index():
    return {"A": "Apple"}

@app.post("/items/")
def items(item:Fruit):
    return {"ID":item.id, "NAME":item.name, "PRICE":item.price}



if __name__ == "__main__":
    uvicorn.run("app:app")