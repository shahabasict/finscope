from fastapi import FastAPI
from app.routers import accounts, notifications  # add other routers as created

app = FastAPI(
    title="FinScope API",
    version="1.0.0",
    description="Personal finance managing app built with FastAPI and Supabase"
)


@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "FinScope backend is running 🚀"}


app.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

# TODO: Add other routers here as you implement
