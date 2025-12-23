import numpy as np
import matplotlib.pyplot as plt

from models.rl.pricing_env import PricingEnv

def train_q_learning(
        episodes=3000,
        alpha=0.1,
        gamma=0.95,
        epsilon=1.0,
        epsilon_decay=0.995,

):
    env = PricingEnv()
    n_states = len(env.prices)
    n_actions = 3
    Q = np.zeros((n_states, n_actions))
    reward_history = []

    for episode in range(episodes):
        state = env.reset()
        total_reward = 0

        for _ in range(50):
            if np.random.rand()<epsilon:
                action = np.random.randint(n_actions)
            else:
                action = np.argmax(Q[state])
            next_state , reward , done = env.step(action)

            Q[state,action] += alpha*(
                reward + gamma*np.max(Q[next_state])-Q[state,action]

            )
            state = next_state
            total_reward += reward

        reward_history.append(total_reward)
        epsilon *= epsilon_decay

    return Q,reward_history


if __name__== "__main__":
    Q,rewards = train_q_learning()

    # plt.figure(figsize=(8,5))
    plt.plot(rewards)
    plt.xlabel("Episode")
    plt.ylabel("Total Profit")

    plt.title("RL Training: Profit Improvement Over Time")
    plt.grid(True)
    plt.show()
    
    optimal_state = np.argmax(np.max(Q,axis=1))
    print("Optimal Price Learned by RL:", PricingEnv().prices[optimal_state])