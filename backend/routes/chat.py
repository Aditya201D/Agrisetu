from fastapi import APIRouter, Depends
from pydantic import BaseModel

from auth.dependencies import get_current_user
from llm.preprocessor import preprocess
from schemas.chat_response import ChatResponse
from services.session_store import get_session
from state_machine.dispatcher import process_message, INTERNAL_STATES
from state_machine.states import State
from services.session_store import (
    get_session,
    save_session,
)
from database.conversations import (
    create_conversation,
    touch_conversation,
)
from database.chat_history import save_message
from database.chat_history import get_history
from schemas.chat_history import ChatHistoryMessage

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    user_id: int = Depends(get_current_user),
):
    session = get_session(str(user_id))
    intent = None

    # Ensure the user always has an active conversation.
    if session.conversation_id is None:
        session.conversation_id = create_conversation(user_id)
        save_session(str(user_id), session)

    message = request.message.strip()
    message_lower = message.lower()

    # Only these states benefit from natural-language understanding.
    LLM_STATES = {
        State.ASK_SEARCH_MODE,
        State.POST_RESULTS,
    }

    # Inputs that don't require an LLM.
    SIMPLE_INPUTS = {
        State.ASK_SEARCH_MODE: {
            "1",
            "2",
            "district",
            "by district",
            "near me",
            "nearby",
        },
        State.POST_RESULTS: {
            "1",
            "2",
            "3",
            "4",
            "new search",
            "change product",
            "change area",
            "done",
        },
    }

    use_llm = (
        message
        and session.state in LLM_STATES
        and message_lower not in SIMPLE_INPUTS.get(session.state, set())
    )

    if use_llm:
        intent = preprocess(session, message)

        if intent is not None and not intent.in_domain:
            return ChatResponse(
                reply=(
                    "I'm designed to help users find fertilizer retailers.\n\n"
                    "Please choose one of the available options below."
                ),
                session=session,
                options=get_options(session.state),
            )
        
    if message:
        save_message(
            session.conversation_id,
            user_id,
            "user",
            message,
        )

    reply = process_message(
        session,
        message,
        intent,
    )

    while session.state in INTERNAL_STATES:
        reply = process_message(session, "")

    if reply.strip():
        save_message(
            session.conversation_id,
            user_id,
            "bot",
            reply,
        )

    save_session(
        str(user_id),
        session,
    )
    touch_conversation(session.conversation_id)

    return ChatResponse(
        reply=reply,
        session=session,
        options=get_options(session.state),
    )

@router.get(
    "/chat/history",
    response_model=list[ChatHistoryMessage],
)
def chat_history(
    user_id: int = Depends(get_current_user),
):

    history = get_history(user_id)

    return [
        ChatHistoryMessage(
            sender=row["sender"],
            message=row["message"],
        )
        for row in history
    ]

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