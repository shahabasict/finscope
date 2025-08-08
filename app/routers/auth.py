from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user_schema import UserCreate, UserRead
from app.services import user_service

router = APIRouter(prefix="/auth", tags=["Auth"])

JWT_SECRET = "SECRET_KEY"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

@router.post("/signup", response_model=UserRead)
async def signup(user:UserCreate):
    existing_user = await user_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400,detail="Email Already registered")
    created_user = await user_service.create_user(user.model_dump())
    return UserRead(**created_user)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await user_service.get_user_by_email(form_data.username)
    if not user:
        raise HTTPException(status_code=400,detail="Invalid Credentials")
    
    if not user_service.pwd_context.verify(form_data.password,user['hashed_password']):
        raise HTTPException(status_code=400,detail="Incorrect email or password")
    
    expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub":user['id']}
    token = jwt.encode(to_encode,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return {"access_token":token, "token_type":"bearer"}