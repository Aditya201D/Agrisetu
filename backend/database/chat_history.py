from sqlalchemy import text

from database.connection import engine


def save_message(
    user_id: int,
    sender: str,
    message: str,
):

    query = text("""
        INSERT INTO chat_history
        (
            user_id,
            sender,
            message
        )
        VALUES
        (
            :user_id,
            :sender,
            :message
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "user_id": user_id,
                "sender": sender,
                "message": message,
            },
        )


def get_history(user_id: int):

    query = text("""
        SELECT
            sender,
            message,
            created_at
        FROM chat_history
        WHERE user_id = :user_id
        ORDER BY id ASC
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {
                "user_id": user_id,
            },
        ).mappings().all()


def clear_history(user_id: int):

    query = text("""
        DELETE
        FROM chat_history
        WHERE user_id = :user_id
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "user_id": user_id,
            },
        )