from fastapi import APIRouter, status, Response, Depends
from app.Users.shemes import SUserAuth
from app.Users.models import User
from app.Users.dao import UsersDAO
from app.Users.auth import auth_user
from app.Users.dependencies import get_current_user
from app.exception import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.Users.auth import get_password_hash, verify_password,create_access_token
router = APIRouter(
  prefix="/auth",
  tags=["Auth & Users"]
)

@router.post("/register")
async def register_user(user_data: SUserAuth):
  existing_user =  await UsersDAO.find_one_or_none(email = user_data.email)
  if existing_user:
    raise UserAlreadyExistsException
  hashed_password = get_password_hash(user_data.password)
  await UsersDAO.add(email=user_data.email,password=hashed_password)
  return "Регистрация прошла успешно"

@router.post("/login")
async def login_user(response : Response,user_data: SUserAuth):
  user =  await auth_user(user_data.email,user_data.password)
  if not user:
    raise IncorrectEmailOrPasswordException
  access_token = create_access_token({"sub": str(user.id)})
  response.set_cookie("booking_access_token", access_token, httponly=True)
  return access_token

@router.post("/logout")
async def logout_user(response :Response):
  response.delete_cookie("booking_access_token")

@router.get("/me")
async def read_user_me(current_user : SUserAuth= Depends(get_current_user)):
  return current_user