from pydantic import BaseModel
from typing import Optional

class Session(BaseModel):
    state: str = "ASK_SEARCH_MODE"
    intent: Optional[str] = None
    district: Optional[str] = None
    product: Optional[str] = None
    location: Optional[str] = None
    retailer: Optional[str] = None