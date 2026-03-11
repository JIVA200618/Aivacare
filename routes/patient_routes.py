from fastapi import APIRouter
from database.mongodb import patients_collection

router = APIRouter()

@router.post("/patients")

def create_patient(data: dict):

    patients_collection.insert_one(data)

    return {
        "message": "Patient stored successfully"
    }


@router.get("/patients")

def get_patients():

    patients = list(patients_collection.find({}, {"_id":0}))

    return patients