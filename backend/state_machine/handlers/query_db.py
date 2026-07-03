from state_machine.states import State
from services.retailer_service import search_retailers, search_retailers_nearby

def query_db_handler(session, message):
    if session.search_mode == "district":
        retailers = search_retailers(
            session.district_name,
            session.product_group,
        )

    else:
        retailers = []

        for radius in [10, 20, 30, 50]:
            retailers = search_retailers_nearby(
                session.latitude,
                session.longitude,
                radius,
                session.product_group,
            )

            if retailers:
                session.radius_km = radius
                break

    session.last_results = retailers

    if not retailers:
        session.state = State.NO_RESULTS

        return None
    
    session.state = State.SHOW_RETAILERS

    return None