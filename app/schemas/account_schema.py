from pydantic import BaseModel, Field
from typing import Optional


class AccountCreate(BaseModel):
    user_id: str
    name: str = Field(..., example="Salary Account")
    type: str = Field(..., example="Savings")
    balance: float = 0.0
    bank: Optional[str] = None


class AccountRead(AccountCreate):
    id: str
