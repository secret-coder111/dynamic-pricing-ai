from fastapi import APIRouter
from Backend.schemas.pricing_schema import PriceInput
from Backend.services.demand_service import predict_demand

router = APIRouter()

@router.post("/predict")
def predict(price_input: PriceInput):
    demand = predict_demand(price_input.price)
    return {"demand": demand}
