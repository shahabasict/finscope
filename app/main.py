from fastapi import FastAPI
from app.routers import notifications

app = FastAPI(
    title="FinScope API",
    version="1.0.0",
    description="Personal finance managing app built with FastAPI and Supabase"
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "FinScope backend is running 🚀"}

app.include_router(notifications.router)