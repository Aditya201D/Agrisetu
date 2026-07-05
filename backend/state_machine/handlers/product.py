from state_machine.states import State

PRODUCTS = {
    "1": "Urea",
    "2": "DAP",
    "3": "NPKs",
    "4": "SSP",
    "5": "MOP",
    "6": "FOM",
    "7": "All",
}

VALID_PRODUCTS = set(PRODUCTS.values())


def product_handler(session, message):

    if message in PRODUCTS:
        session.product_group = PRODUCTS[message]

    elif message in VALID_PRODUCTS:
        session.product_group = message

    else:
        return "Please choose a product from the menu."

    session.state = State.QUERY_DB
    return None