from state_machine.states import State


def show_retailers_handler(session, message):

    count = len(session.last_results or [])

    if session.search_mode == "district":
        location = f"in {session.district_name}"
    else:
        location = "near your location"

    session.state = State.POST_RESULTS

    return (
        f"Found {count} retailers stocking "
        f"{session.product_group} "
        f"{location}.\n\n"
        "See the table below.\n\n"
        "--------------------------------\n"
        "What would you like to do next?\n\n"
        "1. New Search\n"
        "2. Change Product\n"
        "3. Change Area\n"
        "4. Done"
    )