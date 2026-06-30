from state_machine.states import State

def no_results_handler(session,message):
    session.state = State.POST_RESULTS
    return None