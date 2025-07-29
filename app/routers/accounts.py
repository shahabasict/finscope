from fastapi import APIRouter, HTTPException
from app.services import account_service
from app.schemas.account_schema import AccountCreate, AccountRead
from typing import List

router = APIRouter()


@router.get("/", response_model=List[AccountRead])
async def list_accounts(user_id: str):
    try:
        return await account_service.get_accounts(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=AccountRead)
async def add_account(account: AccountCreate):
    try:
        return await account_service.create_account(account.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{account_id}", response_model=AccountRead)
async def update_account(account_id: str, account: AccountCreate):
    try:
        return await account_service.update_account(account_id, account.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{account_id}", response_model=dict)
async def delete_account(account_id: str):
    try:
        await account_service.delete_account(account_id)
        return {"detail": "Account deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
