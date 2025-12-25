from joblib import load
import os

# Absolute-safe model path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "demand", "rf_demand_model.joblib")

# Global model variable (in-memory)
demand_model = None


def load_model():
    """
    Load model from disk into memory.
    """
    global demand_model
    demand_model = load(MODEL_PATH)


def get_model():
    """
    Return current in-memory model.
    """
    return demand_model
