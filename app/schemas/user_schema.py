from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    full_name: str | None = None

class UserRead(BaseModel):
    id: str
    email: EmailStr
    full_name: str | None = None
