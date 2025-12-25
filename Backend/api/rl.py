from fastapi import APIRouter
from Backend.services.rl_service import get_rl_price

router = APIRouter()

@router.get("/rl")
def rl_price():
    price = get_rl_price()
    return {"price": price}
