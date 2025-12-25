import numpy as np
from models.rl.train_rl_agent import train_q_learning
from models.rl.pricing_env import PricingEnv

# Train once at startup
Q, _ = train_q_learning(episodes=2000)
env = PricingEnv()

def get_rl_price():
    best_state = int(np.argmax(np.max(Q, axis=1)))
    return int(env.prices[best_state])
