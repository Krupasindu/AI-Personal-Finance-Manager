import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    PROJECT_NAME="AI Personal Finance Manager",
    DATABASE_URL=os.getenv("DATABASE_URL")
    SECRET_KEY=os.getenv("SECRET_KEY")
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30



Connection_string = (
'Driver={ODBC Driver 18 for SQL Server};'f'Server={os.getenv("SERVER")};1433;'f'DATABASE={os.getenv("DATABASE")};'f'UID={os.getenv("USERNAME")};'
    f'PWD={os.getenv("PASSWORD")};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'    
)
setting=Settings()
connection_string=Connection_string
