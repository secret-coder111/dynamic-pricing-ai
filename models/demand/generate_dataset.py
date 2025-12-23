import csv
import numpy as np

from simulation.demand_simulator import DemandSimulator


def generate_demand_dataset(
    min_price: int = 300,
    max_price: int = 800,
    step: int = 20,
    simulations_per_price: int = 50,
    seed: int = 42,
    output_path: str = "models/demand/demand_data.csv"
):
    """
    Generate a dataset of price vs expected demand
    by averaging multiple demand simulations per price.
    """

    simulator = DemandSimulator(seed=seed)

    prices = np.arange(min_price, max_price + step, step)

    dataset = []

    for price in prices:
        demands = []

        for _ in range(simulations_per_price):
            demand = simulator.simulate_demand(price)
            demands.append(demand)

        expected_demand = np.mean(demands)

        dataset.append([price, expected_demand])

        print(f"Price: {price}, Expected Demand: {expected_demand:.2f}")

    # Save to CSV
    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["price", "expected_demand"])
        writer.writerows(dataset)

    print(f"\nDataset saved to {output_path}")


if __name__ == "__main__":
    generate_demand_dataset()
