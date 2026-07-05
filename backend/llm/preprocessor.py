from llm.extractor import extract_intent
from nlp.matcher import normalize_district, normalize_product


def preprocess(session, message):
    intent = extract_intent(message)

    if intent is None:
        return None
    
    if not intent.in_domain:
        return intent

    if intent.search_mode:
        session.search_mode = intent.search_mode

    if intent.district_name:
        district = normalize_district(intent.district_name)

        if district.score >= 80:
            session.district_name = district.value

    if intent.product_group:
        product = normalize_product(intent.product_group)

        if product.score >= 85:
            session.product_group = product.value

    if intent.post_results_choice:
        session.post_results_choice = intent.post_results_choice

    return intent