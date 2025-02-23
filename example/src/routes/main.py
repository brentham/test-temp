from fastapi import APIRouter
from sqlmodel import SQLModel
from src.config.database import engine

from src.routes import auth
from src.routes.auth import route
from src.routes import todo
from src.routes.todo import route

api_router = APIRouter()

# ---------------Models-------------------
# SQLModel.metadata.create_all(engine)
todo.models.SQLModel.metadata.create_all(engine)
auth.models.SQLModel.metadata.create_all(engine)
# ----------------------------------------

# ---------------Routes-------------------
api_router.include_router(auth.route.router)
api_router.include_router(todo.route.router)
# ----------------------------------------