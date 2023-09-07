from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.database.object import Object
from app.models.models import Rooms

router = APIRouter()
object_room = Object(Rooms)


@router.post("/")
async def create():
    room = await object_room.create(data={})
    return JSONResponse(content=jsonable_encoder(room))