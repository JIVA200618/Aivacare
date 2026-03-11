from pydantic import BaseModel

class ConsultationRequest(BaseModel):
    conversation: str