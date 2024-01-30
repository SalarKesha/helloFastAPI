from database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String(40))
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    modified_time = Column(DateTime(timezone=True), onupdate=datetime.utcnow())

# class Post(Base):
#     __tablename__ = "post"
#     id = Column(Integer, autoincrement=True, primary_key=True)
