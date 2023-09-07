import uuid
import enum
from datetime import datetime 
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON

from app.database.connect import Base



class Role(enum.Enum):
    user = 'user'
    system = 'system'
    function = 'function'


class Rooms(Base):
    __tablename__= 'rooms'
    id= Column(String, primary_key=True, default=str(uuid.uuid4()))
    created_at= Column(DateTime, default=datetime.now())


class Chats(Base):
    __tablename__= 'chats'
    id= Column(String, primary_key=True, default=str(uuid.uuid4()))
    user_id= Column(String)
    room_id=Column(String, ForeignKey("rooms.id"))
    message_id= Column(String)
    role = Column(String)
    content= Column(String)
    created_at= Column(DateTime, default=datetime.now())


class HealthData(Base):
    __tablename__= 'health_data'
    id= Column(String, primary_key=True, default=str(uuid.uuid4()))
    user_id= Column(String)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)


class AIResult(Base):
    __tablename__= 'ai_result'
    id= Column(String, primary_key=True, default=str(uuid.uuid4()))
    user_id= Column(String)
    health_data = Column(String, ForeignKey("health_data.id"))
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)