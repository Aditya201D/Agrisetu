from state_machine.states import State
from schemas.session import Session

def location_handler(session: Session, message):
    try:
        lat, lon = map(float, message.split(","))

        session.latitude = lat
        session.longitude = lon
        session.radius_km = 10

        session.state = State.ASK_PRODUCT

        return None
    
    except Exception:
        return "Unable to read your location. Please try again."