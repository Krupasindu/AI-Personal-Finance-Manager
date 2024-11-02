# Create utilities for password hashing and JWT token management.

from datetime import datetime,datedelta
from jose import JWTError,jwt
from app.core.config import setting
from app.utils.hashing import Hash

def create_access_token(data:dict,expires_delta, timedelta=None):
    to_encode =data.copy()
    if expires_delta:
        expire=datetime.now(datetime.timezone.utc)+expires_delta
    else:
        expire=datetime.now(datetime.timezone.utc)+timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt= jwt.encode(to_encode,setting.SECRET_KEY,algorithm=setting.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        return jwt.decode(token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
    except JWTError:
        return None