from datetime import datetime
from sqlmodel import SQLModel


class UserBase(SQLModel):
    firstname: str
    lastname: str
    email: str


class UserRead(UserBase):
    created_at: datetime
    updated_at: datetime


class UserCreate(UserBase):
    password: str

class UserUpdate(SQLModel):
    firstname: str
    lastname: str