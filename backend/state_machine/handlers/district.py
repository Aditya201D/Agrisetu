from state_machine.states import State
from nlp.matcher import normalize_district

def district_handler(session, message):

    if not session.district_name:
        match = normalize_district(message)
        if match.score < 80:
            return "I couldn't recognize that district. Please try again."
        
        session.district_name = match.value

    if session.product_group:
        session.state = State.QUERY_DB
    else:
        session.state = State.ASK_PRODUCT

    return None