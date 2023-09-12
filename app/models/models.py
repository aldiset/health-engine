import uuid
import enum
from datetime import datetime 
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON

from app.database.connect import Base
from app.utils.random_color import random_color


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
    title = Column(String, nullable=False)
    color = Column(String, default=random_color())
    value = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)


class AIResult(Base):
    __tablename__= 'ai_result'
    id= Column(String, primary_key=True, default=str(uuid.uuid4()))
    user_id= Column(String)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)


class PreventionData(Base):
    __tablename__= 'prevention'
    id= Column(String, primary_key=True, default=str(uuid.uuid4()))
    ai_result_id = Column(String)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)

class CheckUpHistory(Base):
    __tablename__ = 'checkup_history'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String)
    diagnosis = Column(String, nullable=False)
    doctor_name = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)