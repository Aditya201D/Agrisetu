from state_machine.states import State
from schemas.session import Session
from config.settings import SEARCH_RADIUS_KM

def location_handler(session: Session, message):
    try:
        lat, lon = map(float, message.split(","))

        session.latitude = lat
        session.longitude = lon
        session.radius_km = SEARCH_RADIUS_KM

        if session.product_group:
            session.state = State.QUERY_DB
        else:
            session.state = State.ASK_PRODUCT
        return None
    
    except Exception:
        return "Unable to read your location. Please try again."