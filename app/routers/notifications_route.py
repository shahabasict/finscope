from fastapi import APIRouter
from app.services.supabase import get_table_data

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.get("/{user_id}", response_model=dict)
async def get_notifications(user_id: str):
    data = await get_table_data("notifications", user_id)
    return {"notifications": data}
