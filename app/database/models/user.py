from datetime import datetime
from uuid import uuid, uuid4
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid = Field(default=uuid4, primary_key=True)
    firstname: str
    lastname: str
    email: str = Field(unique=True)
    hashed_password: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
