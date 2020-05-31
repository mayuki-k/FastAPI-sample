from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

#デフォルト引数にしてあげないと上手くいかないので注意
@app.get("/items/")
def items(name:str = '', count:int = 0):
    return {"name":name, "count":count}

if __name__ == "__main__":
    uvicorn.run("app:app")