from demand_simulator import DemandSimulator

simulator = DemandSimulator(seed=42)

for price in range(300, 801, 50):
    demand = simulator.simulate_demand(price)
    print(f"Price: {price}, Demand: {demand}")
