from state_machine.states import State
from state_machine.ui_text import NO_RESULTS_MESSAGE

def no_results_handler(session,message):
    session.state = State.POST_RESULTS
    return (NO_RESULTS_MESSAGE)