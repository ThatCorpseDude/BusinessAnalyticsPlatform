from fastapi import FastAPI
from backend.routes import router

# Create FastAPI app
app = FastAPI(
    title="AI Consulting Assistant API",
    description="Backend API for AI-powered consulting tools",
    version="1.0.0"
)

# Include routes
app.include_router(router)


# Optional: Root endpoint (for testing)
@app.get("/")
def read_root():
    return {"message": "AI Consulting Assistant API is running"}