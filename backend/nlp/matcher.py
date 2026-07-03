from rapidfuzz import process, fuzz
from database.queries import get_all_districts
from state_machine.states import State

DISTRICTS = get_all_districts()

SEARCH_MODE_CHOICES = {
    "1": [
        "1",
        "district",
        "by district",
        "district search",
        "area",
        "1st",
        "first"
    ],
    "2": [
        "2",
        "near me",
        "nearby",
        "my location",
        "location",
        "closest",
        "around me",
        "second",
        "two",
        "2nd"
    ],
}

PRODUCT_CHOICES = {
    "Urea": ["urea", "ure", "ureaa", "urea fertilizer", "rea", "uurea"],
    "DAP": ["dap", "d a p", "d-a-p", "d.a.p", "dap fertilizer"],
    "NPKs": ["npk", "npks", "complex fertilizer", "n p k", "n-p-k", "n.p.k", "npk fertilizer"],
    "SSP": ["ssp", "single super phosphate", "s s p", "s-s-p", "s.s.p", "ssp fertilizer"],
    "MOP": ["mop", "muriate of potash", "m o p", "m-o-p", "m.o.p", "mop fertilizer"],
    "FOM": ["fom", "farmyard manure", "f o m", "f-o-m", "f.o.m", "fom fertilizer"],
    "All": ["all", "everything", "all products", "all fertilizers", "all fertilizer", "all types", "all types of fertilizers"],
}

POST_RESULT_CHOICES = {
    "1": [
        "1",
        "new search",
        "restart",
        "again",
        "search again",
    ],
    "2": [
        "2",
        "change product",
        "another product",
        "product",
    ],
    "3": [
        "3",
        "change area",
        "change district",
        "location",
        "new location",
    ],
    "4": [
        "4",
        "done",
        "exit",
        "quit",
        "bye",
        "thanks",
    ],
}

def fuzzy_match(
    text: str,
    choices: dict[str, list[str]],
    threshold: int = 85,
):
    text = text.lower().strip()

    aliases = {}

    for canonical, values in choices.items():
        for value in values:
            aliases[value] = canonical

    match = process.extractOne(
        text,
        aliases.keys(),
        scorer=fuzz.WRatio,
    )

    if match is None:
        return text

    matched_text, score, _ = match

    if score >= threshold:
        return aliases[matched_text]

    return text

def normalize_search_mode(message: str):
    return fuzzy_match(
        message,
        SEARCH_MODE_CHOICES,
    )

def normalize_product(message: str):
    return fuzzy_match(
        message,
        PRODUCT_CHOICES,
    )

def normalize_post_results(message: str):
    return fuzzy_match(
        message,
        POST_RESULT_CHOICES,
    )

def normalize_district(message: str):
    match = process.extractOne(
        message,
        DISTRICTS,
        scorer=fuzz.WRatio,
    )

    if match is None:
        return message

    district, score, _ = match

    return district if score >= 80 else message

def normalize_message(state: State, message: str):
    if not message.strip():
        return message

    if state == State.ASK_SEARCH_MODE:
        return normalize_search_mode(message)

    if state == State.ASK_PRODUCT:
        return normalize_product(message)

    if state == State.POST_RESULTS:
        return normalize_post_results(message)

    if state == State.ASK_DISTRICT:
        return normalize_district(message)
    
    normalized = ...
    original = message

    if normalized != message:
        print(f"[RapidFuzz] '{original}' -> '{normalized}'")
        return normalized

    return message