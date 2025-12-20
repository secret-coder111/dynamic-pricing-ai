import random
from customer_model import Customer

class DemandSimulator:
    def __init__(self, num_customers=100):
        self.num_customers = num_customers
    
    def generate_customers(self):
        """
        Generate a list of customers with different segments.
        """
        customers = []
        for i in range(self.num_customers):
            customer_type = random.choices(
                ["price_Sensitive", "normal" , "premimum"],
                weights=[0.5, 0.3 , 0.2]
                     )[0]
            customers.append(Customer(customer_type))
        return customers
    
    def simulate_demand(self,price):
        """
        Simulate how many customers buy at a given price.
        """
        customers = self.generate_customers()
        demand = 0

        for customer in customers:
            if customer.will_buy(price):
                demand += 1
        return demand

          
if __name__ == "__main__":
    simulator = DemandSimulator(num_customers=100)
    for price in [300, 400, 500, 600, 700]:
        demand = simulator.simulate_demand(price)
        print(f"Price: {price}, Demand: {demand}")
