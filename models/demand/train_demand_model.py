import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_demand_model(
    data_path: str = "models/demand/demand_data.csv",
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Train a baseline demand prediction model.
    """

    # Load dataset
    data = pd.read_csv(data_path)

    X = data[["price"]]
    y = data["expected_demand"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Train linear regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("Baseline Linear Regression Results")
    print(f"MAE  : {mae:.3f}")
    print(f"RMSE : {rmse:.3f}")

    # Visualization
    plt.figure(figsize=(8, 5))
    plt.scatter(X_test, y_test, label="True Demand")
    plt.scatter(X_test, y_pred, label="Predicted Demand")
    plt.xlabel("Price")
    plt.ylabel("Expected Demand")
    plt.title("Linear Regression: True vs Predicted Demand")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    train_demand_model()
