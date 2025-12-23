import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from joblib import dump


def evaluate_model(name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"{name} Results")
    print(f"MAE  : {mae:.3f}")
    print(f"RMSE : {rmse:.3f}\n")
    return mae, rmse


def train_demand_models(
    data_path: str = "models/demand/demand_data.csv",
    test_size: float = 0.2,
    random_state: int = 42
):
    # Load dataset
    data = pd.read_csv(data_path)

    X = data[["price"]]
    y = data["expected_demand"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # -----------------------------
    # 1. Linear Regression (baseline)
    # -----------------------------
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    y_pred_linear = linear_model.predict(X_test)

    evaluate_model("Linear Regression", y_test, y_pred_linear)

    # -----------------------------
    # 2. Polynomial Regression
    # -----------------------------
    poly_model = Pipeline([
        ("poly", PolynomialFeatures(degree=2)),
        ("lr", LinearRegression())
    ])

    poly_model.fit(X_train, y_train)
    y_pred_poly = poly_model.predict(X_test)

    evaluate_model("Polynomial Regression (degree=2)", y_test, y_pred_poly)

    # -----------------------------
    # 3. Random Forest Regression
    # -----------------------------
    rf_model = RandomForestRegressor(
        n_estimators=200,
        max_depth=5,
        random_state=random_state
    )

    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)

    evaluate_model("Random Forest Regression", y_test, y_pred_rf)

    # -----------------------------
    # Visualization
    # -----------------------------
    price_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    dump(rf_model, "models/demand/rf_demand_model.joblib")

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label="True Demand", color="black", alpha=0.6)

    plt.plot(price_range, linear_model.predict(price_range),
             label="Linear Regression", linestyle="--")

    plt.plot(price_range, poly_model.predict(price_range),
             label="Polynomial Regression")

    plt.plot(price_range, rf_model.predict(price_range),
             label="Random Forest Regression")

    plt.xlabel("Price")
    plt.ylabel("Expected Demand")
    plt.title("Demand Prediction Models Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    train_demand_models()
