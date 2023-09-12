from pydantic import BaseModel


class Completion(BaseModel):
    prompt: str