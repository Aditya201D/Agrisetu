from pydantic import BaseModel

class RetailerResult(BaseModel):
    retailer_id: int
    agency_name: str
    product_name: str
    quantity: float
    latitude: float
    longitude: float