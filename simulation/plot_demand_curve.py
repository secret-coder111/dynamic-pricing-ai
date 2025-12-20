import numpy as np
import matplotlib.pyplot as plt

from demand_simulator import DemandSimulator


def plot_expected_price_curves(
    min_price: int = 300,
    max_price: int = 800,
    step: int = 25,
    cost: float = 250.0,
    simulations_per_price: int = 30,
    seed: int = 42
):
    """
    Plot expected demand, revenue, and profit as a function of price
    by averaging multiple market simulations per price.
    """

    simulator = DemandSimulator(seed=seed)

    prices = np.arange(min_price, max_price + step, step)

    expected_demand = []
    expected_revenue = []
    expected_profit = []

    for price in prices:
        demands = []

        for _ in range(simulations_per_price):
            demand = simulator.simulate_demand(price)
            demands.append(demand)

        avg_demand = np.mean(demands)
        avg_revenue = price * avg_demand
        avg_profit = (price - cost) * avg_demand

        expected_demand.append(avg_demand)
        expected_revenue.append(avg_revenue)
        expected_profit.append(avg_profit)

    # -------- Plot with dual y-axis --------
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel("Price")
    ax1.set_ylabel("Expected Demand", color="blue")
    ax1.plot(prices, expected_demand, color="blue", marker="o", label="Expected Demand")
    ax1.tick_params(axis="y", labelcolor="blue")

    ax2 = ax1.twinx()
    ax2.set_ylabel("Expected Revenue / Profit", color="green")
    ax2.plot(prices, expected_revenue, color="orange", marker="s", label="Expected Revenue")
    ax2.plot(prices, expected_profit, color="green", marker="^", label="Expected Profit")
    ax2.tick_params(axis="y", labelcolor="green")

    fig.suptitle("Expected Price vs Demand, Revenue, and Profit")
    fig.legend(loc="upper right", bbox_to_anchor=(0.9, 0.9))
    fig.tight_layout()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    plot_expected_price_curves()
