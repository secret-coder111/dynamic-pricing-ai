import random


class Customer:
    """
    Represents a single customer with a price sensitivity profile.
    """

    SEGMENTS = {
        "price_sensitive": (300, 450),
        "normal": (400, 600),
        "premium": (550, 800)
    }

    def __init__(self, segment: str, seed: int | None = None):
        """
        Initialize a customer with a given segment.

        Args:
            segment (str): Customer segment type
            seed (int, optional): Random seed for reproducibility
        """
        if segment not in self.SEGMENTS:
            raise ValueError(f"Unknown customer segment: {segment}")

        if seed is not None:
            random.seed(seed)

        self.segment = segment
        self.min_price, self.max_price = self.SEGMENTS[segment]
        self.willingness_to_pay = random.uniform(self.min_price, self.max_price)

    def purchase_probability(self, price: float) -> float:
        """
        Returns probability of purchase at a given price.

        Instead of a hard yes/no decision, we model
        realistic probabilistic buying behavior.
        """
        if price >= self.willingness_to_pay:
            return 0.0

        sensitivity = (self.willingness_to_pay - price) / self.willingness_to_pay
        return min(1.0, sensitivity)

    def will_buy(self, price: float) -> bool:
        """
        Stochastic purchase decision based on probability.
        """
        return random.random() < self.purchase_probability(price)
