from typing import List
from pydantic import BaseModel, validator



class HealthCreateSchema(BaseModel):
    user_id: str
    title: str
    color: str = None
    value: int


class CheckUpCreateSchema(BaseModel):
    user_id: str
    diagnosis: str = ""
    doctor_name: str


class HealthCreateSchemaBulk(BaseModel):
    data: List[HealthCreateSchema]


class CheckUpCreateSchemaBulk(BaseModel):
    data: List[CheckUpCreateSchema]


