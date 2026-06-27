from schemas.session import Session
from state_machine.states import State\

INTERNAL_STATES = {
    State.QUERY_DB,
    State.SHOW_RETAILERS,
    State.NO_RESULTS
}

def process_message(session:Session, message: str) -> str:
    message = message.strip()

    if session.state == State.AUTH_CHECK:
        session.state = State.ASK_SEARCH_MODE

        return (
            "How would you like to search?\n\n"
            "1. By District\n"
            "2. Near Me"
        )

    if session.state == State.ASK_SEARCH_MODE:
        user_input = message.lower().strip()

        if user_input in ["district", "1"]:

            session.search_mode = "district"
            session.state = State.ASK_DISTRICT

            return "Please select or enter your district."

        elif user_input in ["near me", "2"]:

            session.search_mode = "near_me"
            session.state = State.ASK_LOCATION

            return (
                "Please share your location.\n\n"
                "Frontend GPS integration will be added later."
            )

        return (
            "How would you like to search?\n\n"
            "1. By District\n"
            "2. Near Me"
        )
    
    elif session.state == State.ASK_DISTRICT:
        session.district_name = message
        session.state = State.ASK_PRODUCT

        return (
            f"District selected: {message}\n\n"
            "Choose a product:\n"
            "1. Urea\n"
            "2. DAP\n"
            "3. NPKs\n"
            "4. SSP\n"
            "5. MOP\n"
            "6. FOM\n"
            "7. All"
        )
    
    elif session.state == State.ASK_PRODUCT:
        products = {
            "1": "Urea",
            "2": "DAP",
            "3": "NPKs",
            "4": "SSP",
            "5": "MOP",
            "6": "FOM",
            "7": "All"
        }
        session.product_group = (products.get(message,message))

        session.state = State.QUERY_DB

        return (
            f"Product selected: "
            f"{session.product_group}"
        )
    
    elif session.state == State.QUERY_DB:

        from services.retailer_service import search_retailers

        retailers = search_retailers(session.district_name or "", session.product_group or "")

        session.last_results = list(retailers)

        if not retailers:
            session.state = State.NO_RESULTS

            return (
                f"No retailers found for "
                f"{session.product_group} "
                f"in {session.district_name}."
            )
        
        session.state = State.SHOW_RETAILERS

        return ""
        
    elif session.state == State.SHOW_RETAILERS:
        
        response = (
            f"Retailers stocking "
            f"{session.product_group} "
            f"in {session.district_name}:\n\n"
        )

        for retailer in session.last_results or []:

            response += (
                f"• {retailer['name']}\n"
                f"  Qty: {retailer['quantity']}\n"
                f"  {retailer['address']}\n"
                f"  {retailer['phone']}\n\n"
            )

        session.state = State.POST_RESULTS

        response += (
            "--------------------------------\n"
            "What would you like to do next?\n\n"
            "1. New Search\n"
            "2. Change Product\n"
            "3. Change Area\n"
            "4. Done"
        )

        return response
    
    elif session.state == State.NO_RESULTS:
        session.state = State.POST_RESULTS
        return (
            "No inventory found.\n\n"
            "Try another product or area.\n\n"
            "--------------------------------\n"
            "What would you like to do next?\n\n"
            "1. New Search\n"
            "2. Change Product\n"
            "3. Change Area\n"
            "4. Done"
        )
           
    elif session.state == State.POST_RESULTS:

        choice = message.lower().strip()

        if choice in ["1", "new search"]:
            session.search_mode = None
            session.district_name = None
            session.latitude = None
            session.longitude = None
            session.radius_km = None
            session.product_group = None
            session.last_results = None

            session.state = State.ASK_SEARCH_MODE

            return (
                "How would you like to search?\n\n"
                "1. By District\n"
                "2. Near Me"
            )
        
        if choice in ["2", "change product"]:
            session.product_group = None
            session.last_results = None

            session.state = State.ASK_PRODUCT

            return (
                "Choose a product:\n"
                "1. Urea\n"
                "2. DAP\n"
                "3. NPKs\n"
                "4. SSP\n"
                "5. MOP\n"
                "6. FOM\n"
                "7. All"
            )
        
        if choice in ["3", "change area"]:
            session.district_name = None
            session.latitude = None
            session.longitude = None
            session.radius_km = None
            session.last_results = None

            session.state = State.ASK_SEARCH_MODE

            return (
                "How would you like to search?\n\n"
                "1. By District\n"
                "2. Near Me"
            )
        
        if choice in ["4", "done"]:
            session.state = State.END
            return "Thank you for using AgriSetu!" 

    return "Something went wrong. Try again."
