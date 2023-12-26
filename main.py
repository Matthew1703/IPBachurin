import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect
import database
from routers import router

# Создание таблиц в БД
database.Base.metadata.create_all(bind=database.engine)

templates = Jinja2Templates(directory="templates/")

listwebsocket = []
listwebsocket2 = []
listwebsocket3 = []
listwebsocket4 = []
listwebsocket5 = []

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    http_protocol = request.headers.get("x-forwarded-proto", "http")
    ws_protocol = "wss" if http_protocol == "https" else "ws"
    server_urn = request.url.netloc
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "http_protocol": http_protocol,
                                       "ws_protocol": ws_protocol,
                                       "server_urn": server_urn})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    listwebsocket.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            [await websocket.send_text(f"Message text was: {data}") for websocket in listwebsocket]
    except WebSocketDisconnect:
        listwebsocket.remove(websocket)

@app.websocket("/ws2")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    listwebsocket2.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            [await websocket.send_text(f"Добавлен объект в базу: {data}") for websocket in listwebsocket2]
    except WebSocketDisconnect:
        listwebsocket2.remove(websocket)

@app.websocket("/ws3")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    listwebsocket3.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            [await websocket.send_text(f"{data}") for websocket in listwebsocket3]
    except WebSocketDisconnect:
        listwebsocket3.remove(websocket)

@app.websocket("/ws4")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    listwebsocket4.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            [await websocket.send_text(f"Объект изменен:{data}") for websocket in listwebsocket4]
    except WebSocketDisconnect:
        listwebsocket4.remove(websocket)

@app.websocket("/ws5")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    listwebsocket5.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            [await websocket.send_text(f"Удален объект") for websocket in listwebsocket5]
    except WebSocketDisconnect:
        listwebsocket5.remove(websocket)

app.include_router(
    router=router
)

app.mount("/templates/", StaticFiles(directory="templates"), name="templates")
if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)


