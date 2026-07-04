from llm.extractor import extract_intent

while True:

    text = input("> ")

    print(extract_intent(text))