from sqlalchemy import and_
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.database.object import Object
from app.utils.random_color import random_color
from app.models.models import HealthData, CheckUpHistory
from app.schema.health import HealthCreateSchemaBulk, CheckUpCreateSchemaBulk

router = APIRouter()

content = {"message":"success", "data":[]}
object_health = Object(HealthData)
object_checkup = Object(CheckUpHistory)

@router.get("/{user_id}/detail")
async def detail(user_id: str):
    data = []
    filters_health = [and_(HealthData.user_id.__eq__(user_id))]
    filters_checkup = [and_(CheckUpHistory.user_id.__eq__(user_id))]

    disease = await object_health.get_all(*filters_health)
    check_up_history = await object_checkup.get_all(*filters_checkup)
    
    data.append({"disease":jsonable_encoder(disease)})
    data.append({"check_up_history": jsonable_encoder(check_up_history)})
    content["data"] = data

    return JSONResponse(content=content, status_code=status.HTTP_200_OK)

@router.get("/prediction")
async def prediction():
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)

@router.get("/prevention")
async def prevention():
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)

@router.post("/create/bulk")
async def create_health_bulk(datas: HealthCreateSchemaBulk):
    for data in datas.data:
        data = jsonable_encoder(data)
        data["color"] = random_color()
        await object_health.create(data)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)

@router.post("/checkup/create/bulk")
async def create_checkup_bulk(datas: CheckUpCreateSchemaBulk):
    for data in datas.data:
        data = jsonable_encoder(data)
        await object_checkup.create(data)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)