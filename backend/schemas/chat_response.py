from pydantic import BaseModel
from typing import Optional

from schemas.session import Session

class ChatResponse(BaseModel):
    reply: str
    session: Session
    buttons: list[str] = []
    table: Optional[list] = None