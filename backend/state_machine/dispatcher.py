from state_machine.states import State
from nlp.matcher import normalize_message
from state_machine.ui_text import MENU_MAP

from state_machine.handlers.auth import auth_handler
from state_machine.handlers.search_mode import search_mode_handler
from state_machine.handlers.district import district_handler
from state_machine.handlers.location import location_handler
from state_machine.handlers.product import product_handler
from state_machine.handlers.query_db import query_db_handler
from state_machine.handlers.show_retailers import show_retailers_handler
from state_machine.handlers.post_results import post_results_handler
from state_machine.handlers.no_results import no_results_handler

HANDLERS = {
    State.AUTH_CHECK: auth_handler,
    State.ASK_SEARCH_MODE: search_mode_handler,
    State.ASK_DISTRICT: district_handler,
    State.ASK_LOCATION: location_handler,
    State.ASK_PRODUCT: product_handler,
    State.QUERY_DB: query_db_handler,
    State.SHOW_RETAILERS: show_retailers_handler,
    State.POST_RESULTS: post_results_handler,
    State.NO_RESULTS: no_results_handler,
}

INTERNAL_STATES = {
    State.AUTH_CHECK,
    State.QUERY_DB,
    State.SHOW_RETAILERS,
    State.NO_RESULTS,
}


def process_message(session, message, intent=None):

    while True:

        print("LOOP START:", session.state)

        if session.state == State.ASK_SEARCH_MODE and intent is not None:

            print("Processing intent")

            if session.search_mode == "district":

                if session.district_name:

                    if session.product_group:
                        print("-> QUERY_DB")
                        session.state = State.QUERY_DB
                    else:
                        print("-> ASK_PRODUCT")
                        session.state = State.ASK_PRODUCT

                else:
                    print("-> ASK_DISTRICT")
                    session.state = State.ASK_DISTRICT

                continue

            elif session.search_mode == "near_me":
                print("-> ASK_LOCATION")
                session.state = State.ASK_LOCATION
                continue

        message = normalize_message(session.state, message)

        print("Calling handler:", session.state)

        current_state = session.state

        handler = HANDLERS[current_state]
        reply = handler(session, message)

        if reply is not None:
            return reply

        if current_state in INTERNAL_STATES:
            message = ""
            continue

        print("RETURN MENU:", session.state)

        return MENU_MAP[session.state]