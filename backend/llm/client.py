from ollama import chat

from llm.config import MODEL_NAME
from llm.prompts import SYSTEM_PROMPT
from llm.schemas import Intent


def ask_llm(message: str):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        format=Intent.model_json_schema(),
    )

    return response.message.content