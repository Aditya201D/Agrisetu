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
        stream=False,
        keep_alive="30m",
        options={
            "temperature": 0,
            "num_predict": 80,
        },
    )

    return response.message.content