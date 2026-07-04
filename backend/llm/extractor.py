import json

from llm.client import ask_llm
from llm.schemas import Intent


def extract_intent(message: str) -> Intent | None:

    raw = ask_llm(message)

    raw = ask_llm(message).strip()

    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        raw = raw.rsplit("```", 1)[0].strip()

    print("\n========== RAW LLM ==========")
    print(raw)
    print("=============================\n")

    try:
        data = json.loads(raw)

        if data is None:
            return None

        return Intent.model_validate(data)

    except Exception as e:
        print("LLM parse error:", e)
        return None