from sqlalchemy import text

from database.connection import engine


def get_session(user_id: int):

    query = text("""
        SELECT *
        FROM user_sessions
        WHERE user_id = :user_id
    """)

    with engine.connect() as conn:
        return conn.execute(
            query,
            {
                "user_id": user_id,
            },
        ).mappings().first()


def create_session(user_id: int):

    query = text("""
        INSERT INTO user_sessions
        (
            user_id,
            state,
            conversation_id
        )
        VALUES
        (
            :user_id,
            'ASK_SEARCH_MODE',
            NULL
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "user_id": user_id,
            },
        )


def update_session(user_id: int, session):

    query = text("""
        UPDATE user_sessions
        SET
            state = :state,
            search_mode = :search_mode,
            district_name = :district_name,
            latitude = :latitude,
            longitude = :longitude,
            radius_km = :radius_km,
            product_group = :product_group,
            post_results_choice = :post_results_choice,
            conversation_id = :conversation_id
        WHERE user_id = :user_id
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "user_id": user_id,
                "state": session.state.value,
                "search_mode": session.search_mode,
                "district_name": session.district_name,
                "latitude": session.latitude,
                "longitude": session.longitude,
                "radius_km": session.radius_km,
                "product_group": session.product_group,
                "post_results_choice": session.post_results_choice,
                "conversation_id": session.conversation_id,
            },
        )


def delete_session(user_id: int):

    query = text("""
        DELETE
        FROM user_sessions
        WHERE user_id = :user_id
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "user_id": user_id,
            },
        )