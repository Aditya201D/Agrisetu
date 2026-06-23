from schemas.session import Session
from state_machine.states import State

from services.retailer_service import (search_retailers_by_district)

def process_message(session:Session, message: str) -> str:
    message = message.strip()

    if session.state == State.ASK_SEARCH_MODE:

        if message.lower() in ["district", 1]:
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
        retailers = search_retailers_by_district(message)
        session.state = State.ASK_SEARCH_MODE

        if not retailers:
            return(f"No retailers found in {message}.")
        
        response = f"Retailers in {message}:\n\n"

        for retailer in retailers:
            response += (
                f"• {retailer.name}\n"
                f"  {retailer.address}\n"
                f"  {retailer.phone}\n\n"
            )

        return response
        
    return "Something went wrong. Try again."
