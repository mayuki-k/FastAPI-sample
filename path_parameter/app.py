from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

@app.get("/path/{id}")
def path(id:int):
    return {"value":id}

@app.get("/items/{id}")
def items(id:int = Path(..., gt=5, le=10)):
    return {"id":id}

@app.get("/items2/{id}")
def items2(id:int = Path(..., ge=5, lt=10)):
    return {"id":id}

if __name__ == "__main__":
    uvicorn.run("app:app")