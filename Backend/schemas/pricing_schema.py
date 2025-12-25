from pydantic import BaseModel

class PriceInput(BaseModel):
    price: float
