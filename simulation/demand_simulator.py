import random
from customer_model import Customer


class DemandSimulator:
    """
    Simulates market demand for a given price point.
    """

    def __init__(
        self,
        num_customers: int = 100,
        segment_distribution: dict | None = None,
        seed: int | None = None
    ):
        """
        Args:
            num_customers (int): Number of customers per simulation
            segment_distribution (dict): Probability distribution of segments
            seed (int): Random seed
        """
        self.num_customers = num_customers
        self.segment_distribution = segment_distribution or {
            "price_sensitive": 0.5,
            "normal": 0.3,
            "premium": 0.2
        }

        if seed is not None:
            random.seed(seed)

    def _sample_segment(self) -> str:
        return random.choices(
            population=list(self.segment_distribution.keys()),
            weights=list(self.segment_distribution.values())
        )[0]

    def simulate_demand(self, price: float) -> int:
        """
        Simulate total demand at a given price.
        """
        demand = 0

        for _ in range(self.num_customers):
            segment = self._sample_segment()
            customer = Customer(segment)

            if customer.will_buy(price):
                demand += 1

        return demand
