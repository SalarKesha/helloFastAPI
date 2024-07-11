from datetime import datetime
from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    created_time: datetime | None = None
    modified_time: datetime | None = None


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True

