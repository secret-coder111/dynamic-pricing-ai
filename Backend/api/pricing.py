from fastapi import APIRouter
from Backend.services.pricing_service import get_static_price

router = APIRouter()

@router.get("/static")
def static_price():
    price = get_static_price()
    return {"price": price}
