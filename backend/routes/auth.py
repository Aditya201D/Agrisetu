from fastapi import APIRouter
from pydantic import BaseModel

from auth.hashing import hash_password
from database.users import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register")
def register(request: RegisterRequest):

    if get_user_by_username(request.username):
        return {
            "success": False,
            "message": "Username already exists.",
        }

    if get_user_by_email(request.email):
        return {
            "success": False,
            "message": "Email already exists.",
        }

    password_hash = hash_password(
        request.password
    )

    create_user(
        request.username,
        request.email,
        password_hash,
    )

    return {
        "success": True,
        "message": "Registration successful.",
    }