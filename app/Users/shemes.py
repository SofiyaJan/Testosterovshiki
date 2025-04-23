from pydantic import BaseModel, EmailStr
from typing import Optional

class SUserAuth(BaseModel):
  email: EmailStr
  password: str