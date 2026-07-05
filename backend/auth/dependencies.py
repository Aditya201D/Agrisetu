from fastapi import Header, HTTPException

from auth.jwt_handler import verify_access_token


def get_current_user(
    authorization: str = Header(...)
):

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    token = authorization.split(" ", 1)[1]

    user_id = verify_access_token(token)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    return user_id