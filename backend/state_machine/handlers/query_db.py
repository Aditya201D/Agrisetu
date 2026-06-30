from state_machine.states import State
from services.retailer_service import search_retailers

def query_db_handler(session, message):
    retailers = search_retailers(session.district_name or "", session.product_group or "")

    session.last_results = retailers

    if not retailers:
        session.state = State.NO_RESULTS

        return None
    
    session.state = State.SHOW_RETAILERS

    return None