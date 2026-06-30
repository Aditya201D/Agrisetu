from state_machine.states import State

def auth_handler(session, message):
    session.state = State.ASK_SEARCH_MODE
    return None