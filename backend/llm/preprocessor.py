from llm.extractor import extract_intent
from nlp.matcher import normalize_district, normalize_product


def preprocess(session, message):
    intent = extract_intent(message)

    if intent is None:
        return None

    if intent.search_mode:
        session.search_mode = intent.search_mode

    if intent.district_name:
        session.district_name = normalize_district(
            intent.district_name
        ).value

    if intent.product_group:
        product = normalize_product(intent.product_group)

        if hasattr(product, "value"):
            session.product_group = product.value
        else:
            session.product_group = product

    if intent.post_results_choice:
        session.post_results_choice = intent.post_results_choice

    return intent