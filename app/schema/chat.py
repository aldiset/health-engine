from pydantic import BaseModel

class SchemaChats(BaseModel):
    role: str
    content: str


class SchemaChatResponse(SchemaChats):
    message_id: str
