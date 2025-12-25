import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from joblib import dump
from Backend.services.model_store import load_model

def retrain_demand_model(csv_path: str):
    df = pd.read_csv(csv_path)

    if "price" not in df.columns or "demand" not in df.columns:
        raise ValueError("CSV must contain 'price' and 'demand' columns")

    X = df[["price"]]
    y = df["demand"]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)

    model_path = os.path.join("models", "demand", "rf_demand_model.joblib")
    dump(model, model_path)

    load_model()
