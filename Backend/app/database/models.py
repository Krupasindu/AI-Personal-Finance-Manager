##Define the SQLAlchemy user model.

from sqlalchemy import Column, String, Integer,Text,DateTime
from sqlalchemy.sql import func
from app.database import Base

class users(Base):
    __tablename__="users"
    id= Column(Integer,primary_key=True,index=True)
    phone_number = Column(String(10), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    username = Column(String(70), unique=True, index=True)
    hashed_password = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())


