import numpy as np
from Backend.services.model_store import get_model


def get_static_price(cost=250):
    model = get_model()
    prices = np.arange(300, 801, 10)
    profits = []

    for price in prices:
        demand = max(model.predict([[price]])[0], 0)
        profit = (price - cost) * demand
        profits.append(profit)

    optimal_price = int(prices[int(np.argmax(profits))])
    return optimal_price
