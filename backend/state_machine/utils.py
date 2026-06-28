from schemas.session import Session

def reset_session(session: Session) -> None:
    session.search_mode = None
    session.district_name = None
    session.latitude = None
    session.longitude = None
    session.radius_km = None
    session.product_group = None
    session.last_results = None