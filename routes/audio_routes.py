from fastapi import APIRouter, UploadFile, File
import whisper
import os

router = APIRouter()

model = whisper.load_model("base")


@router.post("/transcribe-audio")

async def transcribe_audio(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    result = model.transcribe(file_location)

    os.remove(file_location)

    return {
        "transcription": result["text"]
    }