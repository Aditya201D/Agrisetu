from state_machine.states import State
from state_machine.ui_text import SEARCH_MODE_MENU

def auth_handler(session, message):
    session.state = State.ASK_SEARCH_MODE
    return SEARCH_MODE_MENU