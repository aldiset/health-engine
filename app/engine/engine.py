import openai
from typing import List
from fastapi.encoders import jsonable_encoder

from app.config.config import API_KEY_CHAT_GPT
from app.schema.chat import SchemaChats, SchemaChatResponse

class ChatGPT:
    def __init__(self, chats: List[SchemaChats], model: str = "gpt-3.5-turbo"):
        self.chats = chats
        self.model = model
        self.api_token = API_KEY_CHAT_GPT

    async def run(self):
        response = openai.ChatCompletion.create(
            model=self.model,  # Change the model to match your needs
            messages=jsonable_encoder(self.chats)
        )
        return SchemaChatResponse(
            message_id=response.get("id"),
            role=response.get("choices")[0].get("message").get("role"),
            content=response.get("choices")[0].get("message").get("content")
        )