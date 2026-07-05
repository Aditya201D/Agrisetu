from fastapi import APIRouter
from pydantic import BaseModel

from auth.hashing import hash_password
from database.users import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)

from auth.hashing import (
    hash_password,
    verify_password,
)

from database.users import (
    create_user,
    get_user_by_email,
    get_user_by_username,
    get_user_by_username_or_email,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    identifier: str
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

@router.post("/login")
def login(request: LoginRequest):

    user = get_user_by_username_or_email(
        request.identifier
    )

    if user is None:
        return {
            "success": False,
            "message": "Invalid username/email or password.",
        }

    if not verify_password(
        request.password,
        user["password_hash"],
    ):
        return {
            "success": False,
            "message": "Invalid username/email or password.",
        }

    return {
        "success": True,
        "message": "Login successful.",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
        },
    }