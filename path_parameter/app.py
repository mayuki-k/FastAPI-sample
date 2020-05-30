from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

@app.get("/path/{id}")
def path(id:int):
    return {"value":id}

if __name__ == "__main__":
    uvicorn.run("app:app")