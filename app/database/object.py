import uuid
from app.database.crud import CRUD
from app.database.connect import session

class Object:
    def __init__(self, model) -> None:
        self.crud = CRUD(db=session(), model=model)
    
    async def get_by_id(self, id):
        return await self.crud.get(id=id)
    
    async def get_all(self, *filter, limit: int = None, offset: int = None):
        return await self.crud.get_all(*filter, limit=limit, offset=offset)
    
    async def create(self, data: dict):
        data["id"] = str(uuid.uuid4())
        return await self.crud.create(obj_in=data)
    
    async def update(self, id, obj_in):
        obj = await self.get_by_id(id=id)
        if not obj:
            return False
        return await self.crud.update(obj=obj, obj_in=obj_in)

    async def delete(self, id):
        obj = await self.get_by_id(id=id)
        if not obj:
            return False
        return await self.crud.delete(obj=obj)
    