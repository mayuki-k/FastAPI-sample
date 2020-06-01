from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

@app.get("/error/")
def error():
    raise HTTPException(status_code=500, detail="This is error")

if __name__ == "__main__":
    uvicorn.run("app:app")