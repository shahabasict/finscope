import httpx
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

async def get_table_data(table: str, user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/rest/v1/{table}",
            headers=headers,
            params={"user_id": f"eq.{user_id}"}
        )
        return response.json()
    
async def insert_table_data(table: str, data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SUPABASE_URL}/rest/v1/{table}",
            headers=headers,
            json=[data]  # Supabase requires a list of records
        )
        return response.json()
