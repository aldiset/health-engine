from fastapi import APIRouter
from app.schema.analysis import TrackerAndAnalyticSchema


router = APIRouter(prefix="/analysis", tags=["Tracker And Analytics"])

class TrackerAndAnalytics:

    @router.get("/{analysis_id}")
    async def get_last_health_status(analysis_id: int):
        return
    
    @router.post("/")
    async def get_current_health_status(request: TrackerAndAnalyticSchema):
        return
    