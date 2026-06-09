from sqlalchemy import Column, Integer, String
from ..config.database import Base
from pydantic import BaseModel

class student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)

class CreateStudent(BaseModel):
    name : str
    age : int
    course : str