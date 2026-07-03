from state_machine.states import State

SEARCH_MODE_MENU = (
    "How would you like to search?\n\n"
    "1. By District\n"
    "2. Near Me"
)

DISTRICT_PROMPT = (
    "Please select or enter your district."
)

LOCATION_PROMPT = (
    "Please share your location."
)

PRODUCT_MENU = (
    "Choose a product:\n"
    "1. Urea\n"
    "2. DAP\n"
    "3. NPKs\n"
    "4. SSP\n"
    "5. MOP\n"
    "6. FOM\n"
    "7. All"
)

POST_RESULTS_MENU = (
    "--------------------------------\n"
    "What would you like to do next?\n\n"
    "1. New Search\n"
    "2. Change Product\n"
    "3. Change Area\n"
    "4. Done"
)

NO_RESULTS_MESSAGE = (
    "No inventory found.\n"
    "Try another product or area.\n\n"
    + POST_RESULTS_MENU
)

SERVER_ERROR_MESSAGE = (
    "Something went wrong.\nPlease try again."
)

SESSION_EXPIRED_MESSAGE = (
    "Your session has expired.\nPlease log in again."
)

MENU_MAP = {
    State.ASK_SEARCH_MODE: SEARCH_MODE_MENU,
    State.ASK_DISTRICT: DISTRICT_PROMPT,
    State.ASK_LOCATION: LOCATION_PROMPT,
    State.ASK_PRODUCT: PRODUCT_MENU,
    State.POST_RESULTS: POST_RESULTS_MENU,
    State.NO_RESULTS: NO_RESULTS_MESSAGE,
}