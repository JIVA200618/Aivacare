from fastapi import FastAPI
from routes import patient_routes
from routes import consultation_routes
from routes import ai_routes
from routes import audio_routes
from routes import realtime_routes


app = FastAPI(title="AIvaCare Platform")

app.include_router(patient_routes.router)
app.include_router(consultation_routes.router)
app.include_router(ai_routes.router)
app.include_router(audio_routes.router)
app.include_router(realtime_routes.router)

@app.get("/")
def home():
    return {
        "message": "AIvaCare backend running",
        "status": "OK"
    }

app.include_router(realtime_routes.router)

