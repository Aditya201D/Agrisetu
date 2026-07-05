from sqlalchemy import text

from database.connection import engine


def get_user_by_username(username: str):

    query = text("""
        SELECT *
        FROM users
        WHERE username = :username
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {"username": username},
        ).mappings().first()


def get_user_by_email(email: str):

    query = text("""
        SELECT *
        FROM users
        WHERE email = :email
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {"email": email},
        ).mappings().first()


def create_user(
    username: str,
    email: str,
    password_hash: str,
):

    query = text("""
        INSERT INTO users
        (
            username,
            email,
            password_hash
        )
        VALUES
        (
            :username,
            :email,
            :password_hash
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "username": username,
                "email": email,
                "password_hash": password_hash,
            },
        )

def get_user_by_username_or_email(identifier: str):

    query = text("""
        SELECT *
        FROM users
        WHERE username = :identifier
           OR email = :identifier
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {"identifier": identifier},
        ).mappings().first()
    
def get_user_by_id(user_id: int):
    query = """
    SELECT
        id,
        username,
        email
    FROM users
    WHERE id = :id
    """

    with engine.connect() as conn:
        row = conn.execute(
            text(query),
            {"id": user_id},
        ).mappings().first()

    return row