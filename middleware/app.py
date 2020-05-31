# call_nextは非同期的な挙動をするので注意

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    print('processing...')
    return {"A": "Apple"}

@app.middleware("http")
async def before_and_after_request(request: Request, call_next):
    print('start')
    response = await call_next(request)
    print('end')
    return response


if __name__ == "__main__":
    uvicorn.run("app:app")