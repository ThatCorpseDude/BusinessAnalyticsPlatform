from fastapi import APIRouter
from pydantic import BaseModel

from backend.ai_service import (
    analyze_requirements,
    recommend_architecture,
    migrate_code
)

router = APIRouter()


# Input schema (what the API expects)
class Input(BaseModel):
    text: str


# Route 1: Analyze Requirements
@router.post("/analyze")
def analyze(input: Input):
    result = analyze_requirements(input.text)
    return {"result": result}


# Route 2: Recommend Architecture
@router.post("/recommend")
def recommend(input: Input):
    result = recommend_architecture(input.text)
    return {"result": result}


# Route 3: Migrate Code
@router.post("/migrate")
def migrate(input: Input):
    result = migrate_code(input.text)
    return {"result": result}