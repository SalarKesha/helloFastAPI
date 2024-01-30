from database import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.sql import func
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String(40))
    created_time = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, onupdate=func.now())

# class Post(Base):
#     __tablename__ = "post"
#     id = Column(Integer, autoincrement=True, primary_key=True)
