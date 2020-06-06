#uvicornでは一つのリクエストしか処理できないので多分上手く動作しない

from fastapi import FastAPI, Request, WebSocket
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"Message text was: {data}")

if __name__ == "__main__":
    uvicorn.run("app:app")