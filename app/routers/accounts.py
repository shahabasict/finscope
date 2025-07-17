from fastapi import APIRouter, HTTPException
from app.services import account_service

router = APIRouter()

@router.get("/")
async def list_accounts(user_id: str):
    try:
        return await account_service.get_accounts(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def add_account(account: dict):  # Optional: validate with schema
    try:
        return await account_service.create_account(account)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
