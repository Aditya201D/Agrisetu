from llm.extractor import extract_intent


def preprocess(session, message: str):
    intent = extract_intent(message)

    if intent is None:
        return message

    return intent