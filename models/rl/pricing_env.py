import numpy as np
from simulation.demand_simulator import DemandSimulator


class PricingEnv:
    """
    Reinforcement Learning environment for dynamic pricing.
    """
    def __init__(
            self,
            price_min = 300,
            price_max = 800,
            price_step = 10,
            cost = 250,
            seed = 42
    ):
        self.prices = np.arange(price_min,price_max+price_step,price_step)
        self.cost = cost
        self.simulator = DemandSimulator(seed = seed)
        
        self.reset()

    def reset(self):
        self.price_index = len(self.prices)//2
        return self.price_index
    
    def step(self,action):
        """
        Actions:
        0 -> decrease price
        1 -> keep price
        2 -> increase price
        """

        if action ==0 :
            self.price_index = max(0,self.price_index-1)
        elif action ==2:
            self.price_index = min(len(self.prices)-1,self.price_index+1)

        price  = self.prices[self.price_index]
        demand = self.simulator.simulate_demand(price)
        reward = (price - self.cost)*demand

        done = False
        return self.price_index,reward,done
    
          
