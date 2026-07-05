import os
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 60))

print("SECRET:", SECRET_KEY)
print("ALGORITHM:", ALGORITHM)
print("EXPIRE:", EXPIRE_MINUTES)


def create_access_token(user_id: int):

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        print(payload)

        return int(payload["sub"])

    except Exception as e:
        print("JWT ERROR:", repr(e))
        return None