from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import json

app = FastAPI()
app.mapp = [[0 for b in range(11)] for i in range(11)]

@app.websocket("/game")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            await websocket.send_text(json.dumps(
                {'map': app.mapp}
            ))
            data = await websocket.receive_json()
            if app.mapp[data["x"]][ data["y"]-1 ] == 1:
                app.mapp[data["x"]][ data["y"]-1 ] = 0
            elif app.mapp[data["x"]][ data["y"]+1 ] == 1:
                app.mapp[data["x"]][ data["y"]+1 ] = 0
            elif app.mapp[data["x"]+1][ data["y"]] == 1:
                app.mapp[data["x"]+1][ data["y"] ] = 0
            elif app.mapp[data["x"]-1][ data["y"]] == 1:
                app.mapp[data["x"]-1][ data["y"] ] = 0

            app.mapp[data["x"]][data["y"]] = 1

    except WebSocketDisconnect:
        pass