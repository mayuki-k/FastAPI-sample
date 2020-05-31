# python-multipartというライブラリをインストールしていないと、POSTのbody送信でつまずくので注意

from fastapi import FastAPI, Form, Request
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"A": "Apple"}

@app.post("/items")
def items(*, id:int = Form(...), name:str = Form(...)):
    return {"id":id, "name":name}

@app.post("/items2")
async def items2(request:Request):
    data = await request.form()
    return {"id":data['id'], "name":data['name']}


if __name__ == "__main__":
    uvicorn.run("app:app")