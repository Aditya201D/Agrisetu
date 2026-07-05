import json
import time

from llm.client import ask_llm
from llm.schemas import Intent


def extract_intent(message: str) -> Intent | None:

    start = time.perf_counter()

    raw = ask_llm(message)
    raw = ask_llm(message).strip()

    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        raw = raw.rsplit("```", 1)[0].strip()

    llm_time = time.perf_counter() - start

    print("\n========== RAW LLM ==========")
    print(f"[LLM] {llm_time:.2f}s")
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