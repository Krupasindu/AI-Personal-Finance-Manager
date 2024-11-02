##Define schemas for user registration.
from pydantic import BaseModel,EmailStr, Field

class CreateUser(BaseModel):
    phone_number:str=Field(...,max_length=10)
    email:str=Field(...,max_length=100)
    username:str=Field(...,max_length=70)
    hashed_password:str= Field(...,min_length=6)

class UserOut(BaseModel):
    id:int
    phone_number:str
    email:EmailStr
    username:str

class Config:
    orm_mode=True

class Token (BaseModel):
    access_token:str
    token_type:str
