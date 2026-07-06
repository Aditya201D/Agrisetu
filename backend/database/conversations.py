from sqlalchemy import text

from database.connection import engine


def create_conversation(
    user_id: int,
    title: str = "New Chat",
) -> int:
    """
    Creates a new conversation and returns its ID.
    """

    query = text("""
        INSERT INTO conversations
        (
            user_id,
            title
        )
        VALUES
        (
            :user_id,
            :title
        )
    """)

    with engine.begin() as conn:
        result = conn.execute(
            query,
            {
                "user_id": user_id,
                "title": title,
            },
        )

        return result.lastrowid


def list_conversations(user_id: int):
    """
    Returns all conversations for a user.
    """

    query = text("""
        SELECT
            id,
            title,
            created_at,
            updated_at
        FROM conversations
        WHERE user_id = :user_id
        ORDER BY updated_at DESC
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {
                "user_id": user_id,
            },
        ).mappings().all()


def get_conversation(conversation_id: int):

    query = text("""
        SELECT *
        FROM conversations
        WHERE id = :conversation_id
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {
                "conversation_id": conversation_id,
            },
        ).mappings().first()


def update_title(
    conversation_id: int,
    title: str,
):

    query = text("""
        UPDATE conversations
        SET
            title = :title
        WHERE id = :conversation_id
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "conversation_id": conversation_id,
                "title": title,
            },
        )


def touch_conversation(
    conversation_id: int,
):

    query = text("""
        UPDATE conversations
        SET updated_at = CURRENT_TIMESTAMP
        WHERE id = :conversation_id
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "conversation_id": conversation_id,
            },
        )