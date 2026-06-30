from state_machine.states import State

def district_handler(session, message):
    session.district_name = message
    session.state = State.ASK_PRODUCT

    return None