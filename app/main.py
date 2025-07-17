from fastapi import FastAPI
from app.routers import user_route, notifications, accounts, categories, transactions, budgets, goals, dashboard

app = FastAPI(
    title="FinScope API",
    version="1.0.0",
    description="Personal finance managing app built with FastAPI and Supabase"
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "FinScope backend is running 🚀"}

# Include routers here
app.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])

# app.include_router(user_route.router, prefix="/users", tags=["Users"])
# app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
# Add these as you build them:
# app.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
# app.include_router(categories.router, prefix="/categories", tags=["Categories"])
# app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
# app.include_router(budgets.router, prefix="/budgets", tags=["Budgets"])
# app.include_router(goals.router, prefix="/goals", tags=["Goals"])
# app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
