from state_machine.states import State

PRODUCTS = {
            "1": "Urea",
            "2": "DAP",
            "3": "NPKs",
            "4": "SSP",
            "5": "MOP",
            "6": "FOM",
            "7": "All"
        }

def product_handler(session, message):
    session.product_group = (PRODUCTS.get(message,message))
    session.state = State.QUERY_DB

    return None