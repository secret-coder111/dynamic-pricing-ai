from Backend.services.model_store import get_model


def predict_demand(price: float) -> float:
    model = get_model()
    demand = model.predict([[price]])[0]
    return float(max(demand, 0))
