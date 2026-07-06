from fastapi import APIRouter, Depends, HTTPException

from auth.dependencies import get_current_user

from database.chat_history import get_history
from database.conversations import (
    list_conversations,
    get_conversation,
)
from database.user_sessions import (
    get_session as db_get_session,
)

router = APIRouter(prefix="/history", tags=["History"])


@router.get("/conversations")
def conversations(
    user_id: int = Depends(get_current_user),
):
    return list_conversations(user_id)


@router.get("/current")
def current_history(
    user_id: int = Depends(get_current_user),
):
    session = db_get_session(user_id)

    if (
        session is None
        or session["conversation_id"] is None
    ):
        return []

    return get_history(session["conversation_id"])


@router.get("/{conversation_id}")
def conversation_history(
    conversation_id: int,
    user_id: int = Depends(get_current_user),
):
    conversation = get_conversation(conversation_id)

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found.",
        )

    if conversation["user_id"] != user_id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden.",
        )

    return get_history(conversation_id)