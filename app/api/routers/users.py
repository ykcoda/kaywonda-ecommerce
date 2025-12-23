from fastapi import APIRouter


users = APIRouter(prefix="/users", tags=["Users"])


@users.get("/")
def register_user():
    return "Register User"


@users.post("/login")
def login():
    return "login"


@users.post("/logout")
def logout():
    return 