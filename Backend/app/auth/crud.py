# Implement user creation and retrieval logic.

# app/auth/crud.py
from sqlalchemy.orm import Session
from app.database.models import User
from app.database.schemas import UserCreate
from app.utils.hashing import Hash

def create_user(db: Session, user: UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = User(
        phone_number=user.phone_number,
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
