from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.exceptions.handler import *
from sqlmodel import select

from src.routes.auth.models import *
from src.routes.auth.schemas import *
from src.routes.auth.service import *

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
    )

# @router.post("/create/user")
# async def create_new_user(create_user: Users, db: Session = Depends(get_db)):
#     create_user_model = Users()
#     create_user_model.email = create_user.email
#     create_user_model.username = create_user.username
#     create_user_model.first_name = create_user.first_name
#     create_user_model.last_name = create_user.last_name
#     hash_password = get_password_hash(create_user.password)
#     create_user_model.hashed_password = hash_password
#     create_user_model.is_active = True

#     db.add(create_user_model)
#     db.commit()
    
@router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = Users(
        email=create_user.email,
        username=create_user.username,
        first_name=create_user.first_name,
        last_name=create_user.last_name,
        hashed_password=get_password_hash(create_user.password),
        is_active=True
    )
    
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)
    return create_user_model


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, expires_delta=token_expires)

    return {"token": token}

@router.get("/users")
async def get_all_users(db: Session = Depends(get_db)):
    """Retrieve all users from PostgreSQL"""
    # users = db.query(Users).all()
    users = db.exec(select(Users)).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return {"users": users}