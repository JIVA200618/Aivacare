from fastapi import APIRouter
from database.mongodb import consultations_collection

router = APIRouter()

@router.post("/consultations")

def add_consultation(data: dict):

    consultations_collection.insert_one(data)

    return {"message":"Consultation saved"}


@router.get("/consultations")

def get_consultations():

    consultations = list(consultations_collection.find({}, {"_id":0}))

    return consultations