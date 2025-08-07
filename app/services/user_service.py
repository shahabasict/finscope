from app.services import supabase
from passlib.context import CryptContext

pwd_context = CryptContext(schemas=["bcrypt"],deprecated="auto")

async def create_user(user_data: dict):
    hashed_password = pwd_context.hash(user_data.pop("password"))
    user_data["hashed_password"] = hashed_password
    data = await supabase.insert_table_data("users",user_data)
    return data[0]


async def get_user_by_email(email: str):
    async with supabase.http_client() as client:
        response = await client.get(
            f"{supabase.SUPABASE_URL}/rest/v1/users",
            headers=supabase.headers,
            params={"email": f"eq.{email}"}
        )
        if response.is_error:
            raise Exception(f"Supabase error: {response.text}")
        users = response.json()
        return users[0] if users else None