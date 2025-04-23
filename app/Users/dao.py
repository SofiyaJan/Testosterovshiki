from app.dao.base import BaseDAO
from app.Users.models import User, Motivation

class UsersDAO(BaseDAO):
  model = User

class UsersMotivationDAO(BaseDAO):
  model =  Motivation