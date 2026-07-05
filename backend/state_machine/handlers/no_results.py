from state_machine.states import State


def no_results_handler(session, message):

    if session.search_mode == "district":
        location = f"in {session.district_name}"
    else:
        location = f"within {session.radius_km} km of your location"

    session.state = State.POST_RESULTS

    return (
        f"No retailers currently have "
        f"{session.product_group} "
        f"{location}.\n\n"
        "Try another product or search area.\n\n"
        "--------------------------------\n"
        "What would you like to do next?\n\n"
        "1. New Search\n"
        "2. Change Product\n"
        "3. Change Area\n"
        "4. Done"
    )