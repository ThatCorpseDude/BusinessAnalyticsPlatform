from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

# ---- Mock Data Model ----
class KPI(BaseModel):
    team: str
    productivity: float
    error_rate: float

# ---- Sample Data ----
mock_data = [
    {"team": "Team A", "productivity": 78, "error_rate": 5},
    {"team": "Team B", "productivity": 65, "error_rate": 12},
    {"team": "Team C", "productivity": 85, "error_rate": 3},
]

# ---- Routes ----

@app.get("/kpis", response_model=List[KPI])
def get_kpis():
    return mock_data


@app.post("/generate-insights")
def generate_insights():
    # 🔹 Replace this later with OpenAI API
    insights = []

    for team in mock_data:
        if team["error_rate"] > 10:
            insights.append(
                f"{team['team']} has a high error rate ({team['error_rate']}%), consider retraining."
            )
        if team["productivity"] > 80:
            insights.append(
                f"{team['team']} shows strong productivity performance."
            )

    return {
        "summary": "Automated AI-generated insights based on KPI trends.",
        "insights": insights
    }
