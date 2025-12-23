import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from joblib import load,dump

def find_optimal_static_price(
        model_path: str = "models/demand/rf_demand_model.joblib",
        min_price: int  = 300,
        max_price: int =  800,
        step: int  = 10,
        cost: float = 250.0

):
    """
    Find the optimal static price using a trained demand prediction model.
    """

    #load trained model
    model = load(model_path)

    prices = np.arange(min_price,max_price+step,step)
    profits = []
    
    for price in prices:
        predicted_demand = model.predict(np.array([[price]]))[0]
        predicted_demand = max(predicted_demand,0)

        profit = (price  - cost)*predicted_demand
        profits.append(profit)

    #fid optimal price
    optimal_index = np.argmax(profits)
    optimal_price = prices[optimal_index]
    optimal_profit = profits[optimal_index]

    print(f"Optimal static price : ${optimal_price}")
    print(f"Expected profit : ${optimal_profit:.2f}")

    plt.figure(figsize=(8,5))
    plt.plot(prices , profits , marker='o')
    plt.xlabel("Price ($)")
    plt.ylabel("Predicted Profit ($)")
    plt.title("Ml based Static Pricing Optimization")
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    find_optimal_static_price()
    
