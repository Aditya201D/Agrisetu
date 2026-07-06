from pydantic import BaseModel


class ChatHistoryMessage(BaseModel):
    sender: str
    message: str