from fastapi import APIRouter

from app.engine.engine import ChatGPT
from app.schema.test import Completion

router = APIRouter()

@router.post("/")
async def test_completion(data: Completion):
    return await ChatGPT(prompt=data.prompt, model="text-davinci-003").completion()