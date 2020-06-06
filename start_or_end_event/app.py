from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

@app.on_event("startup")
async def start_up():
    print('processing start!')

@app.on_event("shutdown")
async def shutdown():
    print('processing end!')

if __name__ == "__main__":
    uvicorn.run("app:app")