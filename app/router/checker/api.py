from fastapi import APIRouter
from app.schema.checker import SymptomList


router = APIRouter(prefix="/checker", tags=["Symptom Checker"])

class SymptomChecker:

    @router.get("/symptom/{symptom_id}")
    async def get_last_health_status(symptom_id: int):
        return
    
    @router.post("/symptom")
    async def get_current_health_status(request: SymptomList):
        return
    