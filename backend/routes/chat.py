from fastapi import APIRouter
from pydantic import BaseModel

from services.session_store import get_session
from state_machine.handlers import process_message

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    session = get_session(request.user_id)
    reply = process_message(
        session, request.message
    )
    return {
        "reply": reply,
        "session": session.model_dump()
    }