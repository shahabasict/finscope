from fastapi import APIRouter, Depends
from app.services.supabase import get_table_data

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.get("/{user_id}")
async def get_notifications(user_id: str):
    data = await get_table_data("notifications", user_id)
    return {"notifications": data}
