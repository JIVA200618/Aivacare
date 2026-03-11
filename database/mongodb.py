from pymongo import MongoClient

# connect to mongodb
client = MongoClient("mongodb://localhost:27017")

# database name
db = client["aivacare"]

# collections
patients_collection = db["patients"]
consultations_collection = db["consultations"]