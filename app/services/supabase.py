import httpx
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
assert SUPABASE_URL and SUPABASE_API_KEY, "Supabase .env variables not loaded!"

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
        if response.is_error:
            raise Exception(f"Supabase error: {response.text}")
        return response.json()

async def insert_table_data(table: str, data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SUPABASE_URL}/rest/v1/{table}",
            headers=headers,
            json=[data]  # Supabase expects a list for bulk-insert, even if single.
        )
        if response.is_error:
            raise Exception(f"Supabase error: {response.text}")
        return response.json()

async def update_table_data(table: str, row_id: str, data: dict):
    # Replace row_id with appropriate identifier column if needed
    async with httpx.AsyncClient() as client:
        response = await client.patch(
            f"{SUPABASE_URL}/rest/v1/{table}?id=eq.{row_id}",  # Assuming 'id' pk
            headers=headers,
            json=data
        )
        if response.is_error:
            raise Exception(f"Supabase error: {response.text}")
        return response.json()

async def delete_table_data(table: str, row_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{SUPABASE_URL}/rest/v1/{table}?id=eq.{row_id}",
            headers=headers
        )
        if response.is_error:
            raise Exception(f"Supabase error: {response.text}")
        return response.json()
