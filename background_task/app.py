from fastapi import FastAPI, BackgroundTasks
import uvicorn
import time
from datetime import datetime

app = FastAPI()

def heveay_task():
    print(f'開始 {datetime.now()}')
    time.sleep(10)
    print(f'終了 {datetime.now()}')

@app.get("/")
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(heveay_task)
    return {"A": "Apple"}

if __name__ == "__main__":
    uvicorn.run("app:app")