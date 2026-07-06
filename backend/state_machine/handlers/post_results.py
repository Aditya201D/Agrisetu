from state_machine.states import State
from state_machine.utils import reset_session
from state_machine.ui_text import POST_RESULTS_MENU, SEARCH_MODE_MENU

def post_results_handler(session, message):
    choice = message.lower().strip()

    if choice in ["1", "new search"]:
        reset_session(session)

        session.state = State.ASK_SEARCH_MODE

        return None
    
    if choice in ["2", "change product"]:
        session.product_group = None
        session.last_results = None

        session.state = State.ASK_PRODUCT

        return None
    
    if choice in ["3", "change area"]:
        session.district_name = None
        session.latitude = None
        session.longitude = None
        session.radius_km = None
        session.last_results = None

        session.state = State.ASK_SEARCH_MODE

        return None
    
    if choice in ["4", "done"]:
        reset_session(session)
        session.state = State.ASK_SEARCH_MODE
        return "Thank you for using AgriSetu!\n\n" + SEARCH_MODE_MENU
    
    else:
        return (
        "Invalid choice.\n\n"
        + POST_RESULTS_MENU
    )