from state_machine.states import State

def show_retailers_handler(session, message):

    count = len(session.last_results or [])

    session.state = State.POST_RESULTS

    location = (
        session.district_name
        if session.search_mode == "district"
        else "near your location"
    )

    return (
        f"Found {count} retailers stocking "
        f"{session.product_group} "
        f"{'in' if session.search_mode == 'district' else ''} "
        f"{location}.\n\n"
        "See the table below.\n\n"
        "--------------------------------\n"
        "What would you like to do next?\n\n"
        "1. New Search\n"
        "2. Change Product\n"
        "3. Change Area\n"
        "4. Done"
    )