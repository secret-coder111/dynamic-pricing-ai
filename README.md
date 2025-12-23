# AI-Driven Dynamic Pricing System using Machine Learning and Reinforcement Learning

## 📌 Overview
This project implements a complete **dynamic pricing system** that learns how to optimally price a product under uncertain and stochastic customer demand.  
The system demonstrates why **demand prediction alone is not sufficient** and how **reinforcement learning (RL)** can outperform traditional static pricing strategies.

The project follows a real-world ML engineering pipeline:
- Market simulation
- Dataset generation
- Demand prediction using ML
- Profit-maximizing static pricing
- Reinforcement learning–based dynamic pricing

---

## 🎯 Problem Statement
In many real-world businesses such as e-commerce, ride-hailing, airlines, and hotels, pricing decisions are challenging because:

- Customer demand is uncertain and non-linear
- Customers have different willingness-to-pay
- Fixed pricing strategies often fail
- Pricing decisions affect long-term profit

**Objective:**  
Design a pricing system that **maximizes long-term profit**, not just short-term demand or prediction accuracy.


## 🧠 System Architecture
Customer Behavior Model
↓
Market Simulator
↓
Dataset Generation
↓
Machine Learning Demand Prediction
↓
Static Price Optimization (ML-based)
↓
Reinforcement Learning (Dynamic Pricing)


## 🏗️ Project Structure

dynamic-pricing-ai/
│
├── simulation/
│ ├── customer_model.py # Customer behavior & willingness to pay
│ ├── demand_simulator.py # Market demand simulation
│ ├── test_demand_curve.py # Sanity checks & visualization
│
├── models/
│ ├── demand/
│ │ ├── generate_dataset.py # Dataset generation from simulator
│ │ ├── train_demand_model.py# ML demand prediction models
│ │
│ ├── pricing/
│ │ └── static_pricing.py # ML-based static pricing optimization
│ │
│ ├── rl/
│ │ ├── pricing_env.py # RL environment
│ │ └── train_rl_agent.py # Q-learning agent
│
├── README.md
├── .gitignore



---

## 🧪 Methodology

### 1️⃣ Market Simulation
- Customers are divided into segments:
  - Price-sensitive
  - Normal
  - Premium
- Each customer has a probabilistic willingness-to-pay
- A **fixed customer population** is used to ensure the law of demand holds
- Demand decreases as price increases (validated)

---

### 2️⃣ Dataset Generation
- Prices are sampled across a realistic range
- Multiple simulations are run per price
- Expected demand is computed via averaging
- Results in a clean **price → expected demand** dataset

---

### 3️⃣ Demand Prediction Models
The following models are trained and compared:

| Model | Purpose |
|-----|--------|
| Linear Regression | Baseline |
| Polynomial Regression | Captures elasticity |
| Random Forest | Best non-linear performance |

**Observation:**  
Random Forest provides the best demand prediction, but accurate prediction alone does not guarantee optimal pricing.

---

### 4️⃣ Static Pricing Optimization (ML-Based)
- Uses the trained demand prediction model
- Computes profit using:
\[
profit = (price - cost) \times predicted\_demand
\]
- Selects a **single fixed price** that maximizes expected profit

This represents traditional ML-based pricing strategies used in many real systems.

---

### 5️⃣ Reinforcement Learning (Dynamic Pricing)
- Environment: simulated market
- State: current price index
- Actions:
  - Decrease price
  - Keep price
  - Increase price
- Reward: per-step profit
- Algorithm: **Q-learning**

The RL agent learns pricing decisions through interaction and adapts over time.

---

## 📊 Results & Insights

### ✔️ Key Findings
- Linear models fail due to non-linear demand elasticity
- Random Forest predicts demand accurately
- Static pricing is limited under uncertainty
- Reinforcement Learning achieves **higher long-term profit**
- RL training shows stable convergence despite stochastic demand

### ✔️ RL Training Behavior
- Early episodes: exploration and noisy rewards
- Middle phase: rapid learning and profit improvement
- Later phase: stable convergence with bounded variance

This behavior matches expected RL learning dynamics.

---

## ▶️ How to Run the Project

### 1️⃣ Generate Dataset
```bash
python -m models.demand.generate_dataset

2️⃣ Train Demand Prediction Models
python -m models.demand.train_demand_model

3️⃣ Static Pricing Optimization
python -m models.pricing.static_pricing

4️⃣ Train Reinforcement Learning Agent
python -m models.rl.train_rl_agent



