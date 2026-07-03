from rapidfuzz import process, fuzz
from database.queries import get_all_districts
from state_machine.states import State
from dataclasses import dataclass

DISTRICTS = get_all_districts()
@dataclass
class MatchResult:
    value: str
    score: float

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
        return MatchResult(value=aliases[matched_text], score=score)
    
    return MatchResult(value=text, score=score)

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

def normalize_district(message: str) -> MatchResult:
    match = process.extractOne(
        message,
        DISTRICTS,
        scorer=fuzz.WRatio,
    )

    if match is None:
        return MatchResult(
            value=message,
            score=0,
        )

    district, score, _ = match

    if score >= 80:
        return MatchResult(
            value=district,
            score=score,
        )

    return MatchResult(
        value=message,
        score=score,
    )

def normalize_message(state: State, message: str):
    if not message.strip():
        return message

    if state == State.ASK_SEARCH_MODE:
        result = normalize_search_mode(message)
    elif state == State.ASK_PRODUCT:
        result = normalize_product(message)
    elif state == State.POST_RESULTS:
        result = normalize_post_results(message)
    elif state == State.ASK_DISTRICT:
        result = normalize_district(message)
    else:
        return message

    if result.value != message:
        print(f"[RapidFuzz] '{message}' -> '{result.value}' ({result.score:.1f})")

    return result.value