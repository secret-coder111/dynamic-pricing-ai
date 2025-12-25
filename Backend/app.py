from fastapi import FastAPI
from Backend.services.model_store import load_model
from Backend.api import demand, pricing, rl
from fastapi.middleware.cors import CORSMiddleware
from Backend.api import upload






app = FastAPI(title="Dynamic Pricing AI Backend")
@app.on_event("startup")
def startup_event():
    load_model()


# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(demand.router, prefix="/demand", tags=["Demand"])
app.include_router(pricing.router, prefix="/pricing", tags=["Pricing"])
app.include_router(rl.router, prefix="/pricing", tags=["Reinforcement Learning"])
app.include_router(upload.router, prefix="/data", tags=["Data Upload"])
# app.include_router(upload.router, prefix="/data", tags=["Upload"])

