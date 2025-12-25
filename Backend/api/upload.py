from fastapi import APIRouter, UploadFile, File
import pandas as pd
import os
from Backend.services.retrain_service import retrain_demand_model

router = APIRouter()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-data")
async def upload_csv(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Retrain model using file PATH
    retrain_demand_model(file_path)
    df = pd.read_csv(file_path)
    df = df[["price", "demand"]]
    df = df.dropna()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["demand"] = pd.to_numeric(df["demand"], errors="coerce")
    df = df.dropna()

    # Read CSV ONLY ONCE
   

    return {
        "message": "Model retrained successfully",
        "prices": df["price"].astype(float).tolist(),
        "demands": df["demand"].astype(float).tolist()
    }
