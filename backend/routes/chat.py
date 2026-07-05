from fastapi import APIRouter
from state_machine.states import State
from pydantic import BaseModel
from schemas.chat_response import ChatResponse

import time

from services.session_store import get_session
from state_machine.dispatcher import process_message, INTERNAL_STATES

from llm.preprocessor import preprocess

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
def chat(request: ChatRequest):

    total = time.perf_counter()

    session = get_session(request.user_id)
    intent = None

    simple_inputs = {
        "1",
        "2",
        "district",
        "by district",
        "near me",
        "nearby",
    }

    if (
        session.state == State.ASK_SEARCH_MODE
        and request.message.lower().strip() not in simple_inputs
    ):
        intent = preprocess(session, request.message)
    else:
        intent = None

    reply = process_message(
        session, request.message, intent
    )

    options = []
    if session.state == State.ASK_SEARCH_MODE:
        options = [
            "By District",
            "Near Me",
        ]

    elif session.state == State.ASK_PRODUCT:
        options = [
            "Urea",
            "DAP",
            "NPKs",
            "SSP",
            "MOP",
            "FOM",
            "All",
        ]

    elif session.state == State.POST_RESULTS:
        options = [
            "New Search",
            "Change Product",
            "Change Area",
            "Done",
        ]
    
    while session.state in INTERNAL_STATES:
        reply = process_message(session, "")
        
    print(f"[TOTAL] {time.perf_counter()-total:.2f}s")    #empty string ensures that no input is required

    return ChatResponse(
        reply=reply,
        session=session,
        options=options,
    )