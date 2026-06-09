from sqlalchemy import Column, Integer, String
from ..database.database import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

class UserCreate(BaseModel):
    name : str
    email : str