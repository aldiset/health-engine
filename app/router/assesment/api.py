from fastapi import APIRouter

from app.schema.assesment import HealthAssessmentSchema

router = APIRouter(prefix="/assesment", tags=["Health Assessment"])

class HealthAssessment:

    @router.get("/last-health-status/{user_id}")
    async def get_last_health_status(user_id: int):
        return
    
    @router.post("/current-health-status")
    async def get_current_health_status(request: HealthAssessmentSchema):
        return
    