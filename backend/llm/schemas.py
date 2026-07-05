from typing import Literal
from pydantic import BaseModel

class Intent(BaseModel):
    search_mode: Literal["district", "near_me"] | None = None

    district_name: str | None = None

    product_group: Literal[
        "Urea",
        "DAP",
        "NPKs",
        "SSP",
        "MOP",
        "FOM",
        "All",
    ] | None = None

    post_results_choice: Literal[
        "1",
        "2",
        "3",
        "4",
    ] | None = None

    confidence: float = 0.0

    in_domain: bool = True