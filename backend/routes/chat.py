from fastapi import APIRouter
from fastapi import Depends
from auth.dependencies import get_current_user
from pydantic import BaseModel

from state_machine.states import State
from schemas.chat_response import ChatResponse

import time

from services.session_store import get_session
from state_machine.dispatcher import process_message, INTERNAL_STATES

from llm.preprocessor import preprocess

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest, user_id: int = Depends(get_current_user)):

    total = time.perf_counter()

    session = get_session(str(user_id))
    intent = None

    if request.message.strip():

        intent = preprocess(session, request.message)

        if intent is not None and not intent.in_domain:
            return ChatResponse(
                reply=(
                    "I'm designed to help users find fertilizer retailers.\n\n"
                    "Please choose one of the available options below."
                ),
                session=session,
                options=get_options(session.state),
            )
        
    print("Intent:", intent)
    print("Session state:", session.state)
    print("Search mode:", session.search_mode)
    print("District:", session.district_name)
    print("Product:", session.product_group)

    reply = process_message(
        session, request.message, intent
    )

    print("State after dispatcher:", session.state)

    options = get_options(session.state)
    
    while session.state in INTERNAL_STATES:
        reply = process_message(session, "")    #empty string ensures that no input is required

    return ChatResponse(
        reply=reply,
        session=session,
        options=options,
    )

def get_options(state: State):
    if state == State.ASK_SEARCH_MODE:
        return [
            "By District",
            "Near Me",
        ]

    if state == State.ASK_PRODUCT:
        return [
            "Urea",
            "DAP",
            "NPKs",
            "SSP",
            "MOP",
            "FOM",
            "All",
        ]

    if state == State.POST_RESULTS:
        return [
            "New Search",
            "Change Product",
            "Change Area",
            "Done",
        ]

    return []