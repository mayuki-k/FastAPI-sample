from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

#デフォルト引数にしてあげないと上手くいかないので注意
@app.get("/items/")
def items(name:str = '', count:int = 0):
    return {"name":name, "count":count}

@app.get("/valid/")
def valid(name:str = Query("default value", min_length=0, max_length=8, regex="[a-f]")):
    return {"name":name}

if __name__ == "__main__":
    uvicorn.run("app:app")