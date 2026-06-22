from schemas.session import Session
from state_machine.states import State

def process_message(session:Session, message: str) -> str:
    message = message.strip()

    if session.state == State.ASK_SEARCH_MODE:

        if message.lower() == "district":
            session.state = State.ASK_DISTRICT
            session.intent = "district_search"

            return "Please enter your district:"
        
        return (
            "How would you like to search? \n\n"
            "1. District\n"
            "2. Product\n"
            "3. Near me"
        )
    
    elif session.state == State.ASK_DISTRICT:
        session.district = message
        session.state = State.SHOW_RETAILERS

        return(
            f"Searching reatailers in {message}...\n\n"
            "(Database integration to be implemented)"
        )

    return "Something went wrong. Try again."
