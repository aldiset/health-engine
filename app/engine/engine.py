import openai
from loguru import logger
from typing import List
from fastapi.encoders import jsonable_encoder

from app.config.config import API_KEY_CHAT_GPT
from app.utils.get_json import get_json_from_string
from app.schema.chat import SchemaChats, SchemaChatResponse


openai.api_key = API_KEY_CHAT_GPT
class ChatGPT:
    def __init__(self, chats: List[SchemaChats] = None, model: str = "gpt-3.5-turbo", prompt: str = None):
        self.chats = chats
        self.model = model
        self.prompt = prompt

    async def chat(self):
        response = openai.ChatCompletion.create(
            model=self.model,  # Change the model to match your needs
            messages=jsonable_encoder(self.chats)
        )
        return SchemaChatResponse(
            message_id=response.get("id"),
            role=response.get("choices")[0].get("message").get("role"),
            content=response.get("choices")[0].get("message").get("content")
        )

    async def completion(self, max_tokens: int = 1024):
        response = openai.Completion.create(
                                            model=self.model,
                                            prompt=self.prompt,
                                            temperature=0,
                                            max_tokens=max_tokens,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0
                                            )
        try:
            return response["choices"][0]["text"]
        except Exception as e:
            logger.warning(e)