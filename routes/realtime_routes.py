from fastapi import APIRouter, WebSocket
from services.ai_engine import process_consultation

router = APIRouter()

@router.websocket("/realtime-ai")

async def realtime_ai(websocket: WebSocket):

    await websocket.accept()

    while True:

        data = await websocket.receive_text()

        result = process_consultation(data)

        await websocket.send_json(result)