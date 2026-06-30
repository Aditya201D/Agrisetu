from state_machine.states import State
from state_machine.ui_text import POST_RESULTS_MENU

def show_retailers_handler(session, message):
    response = (
        f"Retailers stocking "
        f"{session.product_group} "
        f"in {session.district_name}:\n\n"
    )

    for retailer in session.last_results or []:

        response += (
            f"• {retailer.agency_name}\n"
            f"  Product: {retailer.product_name}\n"
            f"  Qty: {retailer.quantity}\n"
        )

    session.state = State.POST_RESULTS

    response += POST_RESULTS_MENU

    return response