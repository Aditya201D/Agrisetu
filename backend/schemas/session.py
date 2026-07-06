from pydantic import BaseModel
from state_machine.states import State
from typing import Optional
from schemas.retailer import RetailerResult

class Session(BaseModel):
    state: State = State.ASK_SEARCH_MODE
    search_mode: str | None = None
    district_name: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    radius_km: int | None = None
    product_group: str | None = None
    last_results: list[RetailerResult] | None = None
    post_results_choice: str | None = None
    conversation_id: int | None = None