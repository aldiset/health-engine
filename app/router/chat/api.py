from typing import List
from sqlalchemy import and_
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, status, HTTPException

from app.database.object import Object
from app.schema.chat import SchemaChats
from app.models.models import Rooms, Chats, HealthData, AIResult
from app.engine.engine import ChatGPT

router = APIRouter()
object_room = Object(Rooms)
object_chat = Object(Chats)


@router.post("/{user_id}/{room_id}")
async def chat(chats: List[SchemaChats], user_id: str, room_id: str):
    room = await object_room.get_by_id(id=room_id)
    if not room:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="room id not found")

    user_message = jsonable_encoder(chats[-1])
    user_message["room_id"]=room_id
    user_message["user_id"]=user_id
    
    chat_gpt = ChatGPT(chats=chats)
    response = await chat_gpt.run()
    
    system_message = jsonable_encoder(response)
    system_message["room_id"]=room_id
    system_message["user_id"]=user_id

    data_user_message = await object_chat.create(user_message)
    data_system_message = await object_chat.create(system_message)

    return JSONResponse(content=data_system_message, status_code=status.HTTP_200_OK)

@router.get("/{user_id}/{room_id}")
async def get_chat(user_id: str, room_id: str, limit: int = None, offset: int = None):
    filters = [
        and_(Chats.user_id.__eq__(user_id), Chats.room_id.__eq__(room_id))
    ]
    return await object_chat.get_all(*filters, limit=limit, offset=offset)
