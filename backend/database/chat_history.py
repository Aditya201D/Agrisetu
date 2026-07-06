from sqlalchemy import text

from database.connection import engine


def save_message(
    conversation_id: int,
    user_id: int,
    sender: str,
    message: str,
):

    query = text("""
        INSERT INTO chat_history
        (
            conversation_id,
            user_id,
            sender,
            message
        )
        VALUES
        (
            :conversation_id,
            :user_id,
            :sender,
            :message
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "conversation_id": conversation_id,
                "user_id": user_id,
                "sender": sender,
                "message": message,
            },
        )


def get_history(conversation_id: int):

    query = text("""
        SELECT
            sender,
            message,
            created_at
        FROM chat_history
        WHERE conversation_id = :conversation_id
        ORDER BY id ASC
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {
                "conversation_id": conversation_id,
            },
        ).mappings().all()


def clear_history(conversation_id: int):

    query = text("""
        DELETE
        FROM chat_history
        WHERE conversation_id = :conversation_id
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "conversation_id": conversation_id,
            },
        )