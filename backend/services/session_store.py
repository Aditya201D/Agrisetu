from schemas.session import Session
from state_machine.states import State

from database.user_sessions import (
    get_session as db_get_session,
    create_session,
    update_session,
)


def get_session(user_id: str) -> Session:
    row = db_get_session(int(user_id))

    if row is None:
        create_session(int(user_id))
        return Session()

    return Session(
        state=State(row["state"]),
        search_mode=row["search_mode"],
        district_name=row["district_name"],
        latitude=row["latitude"],
        longitude=row["longitude"],
        radius_km=row["radius_km"],
        product_group=row["product_group"],
        post_results_choice=row["post_results_choice"],
        last_results=None,
    )


def save_session(user_id: str, session: Session):
    update_session(int(user_id), session)