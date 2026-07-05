from state_machine.states import State
from state_machine.ui_text import SEARCH_MODE_MENU

def search_mode_handler(session, message):
    user_input = message.lower().strip()

    if user_input in ["district", "1"]:

        session.search_mode = "district"
        session.state = State.ASK_DISTRICT

        return None

    elif user_input in ["near me", "2"]:

        session.search_mode = "near_me"
        session.state = State.ASK_LOCATION

        return (
        "How would you like to provide your location?\n\n"
        "• Click '📍 Use Current Location'\n"
        "• Or enter coordinates manually.\n\n"
        "Example:\n"
        "25.3400,82.8000"
    )

    return SEARCH_MODE_MENU