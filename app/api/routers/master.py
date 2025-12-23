from fastapi import APIRouter

from .users import users

master = APIRouter()
master.include_router(users)