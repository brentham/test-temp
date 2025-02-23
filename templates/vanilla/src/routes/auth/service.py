from fastapi import Depends
from typing import Annotated, Optional
from passlib.context import CryptContext
from sqlmodel import Session
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from sqlmodel import select

from src.config.config import settings
from src.util.db_dependency import get_db
from src.routes.auth.models import Users
from src.exceptions.handler import *

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

db_dependency = Annotated[Session, Depends(get_db)]

def get_password_hash(password):
    return bcrypt_context.hash(password)
def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str, db: db_dependency):
    statement = select(Users).where(Users.username == username)
    user = db.exec(statement).first()
    
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_cuurent_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    
    except JWTError:
        raise get_user_exception()