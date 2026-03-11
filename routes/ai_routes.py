from fastapi import APIRouter
from services.ai_engine import process_consultation
from database.mongodb import consultations_collection


router = APIRouter()

@router.post("/process-consultation")

def process(data: dict):

    text = data["conversation"]

    result = process_consultation(text)

    consultations_collection.insert_one({
    "conversation": text,
    "analysis": result
})

