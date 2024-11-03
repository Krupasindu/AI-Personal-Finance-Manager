import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    PROJECT_NAME="AI Personal Finance Manager",
    DATABASE_URL=os.getenv("DATABASE_URL")
    SECRET_KEY=os.getenv("SECRET_KEY")
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30




setting=Settings()
 
