from app.services import supabase


async def get_accounts(user_id: str):
    return await supabase.get_table_data("accounts", user_id)


async def create_account(account_data: dict):
    data = await supabase.insert_table_data("accounts", account_data)
    return data[0]  # first inserted record


async def update_account(account_id: str, account_data: dict):
    data = await supabase.update_table_data("accounts", account_id, account_data)
    return data[0]  # updated record


async def delete_account(account_id: str):
    return await supabase.delete_table_data("accounts", account_id)
