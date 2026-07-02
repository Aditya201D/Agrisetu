from state_machine.states import State
from services.retailer_service import search_retailers

def query_db_handler(session, message):
    if session.search_mode == "district":
        retailers = search_retailers(
            session.district_name,
            session.product_group,
        )

    else:
        retailers = search_retailers_nearby(
            session.latitude,
            session.longitude,
            session.radius_km,
            session.product_group,
        )

    session.last_results = retailers

    if not retailers:
        session.state = State.NO_RESULTS

        return None
    
    session.state = State.SHOW_RETAILERS

    return None