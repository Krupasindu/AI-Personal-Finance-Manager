from fastapi import Depends, FastAPI, HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.database import engine, Base
from app.auth.routes import router as auth_router


# Create the database tables
Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/test/")
async def test():
    return {"hello":"World"}

