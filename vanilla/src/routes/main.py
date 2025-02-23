from fastapi import APIRouter

from src.config.database import settings
from src.config.database import engine
from src.routes import auth

from src.routes.auth import route

api_router = APIRouter()

# ---------------Models-------------------
# auth.models.Base.metadata.create_all(bind=engine)
# auth.models.Base.metadata.create_all(bind=engine)
# ----------------------------------------

# ---------------Routes-------------------
api_router.include_router(auth.route.router)
# ----------------------------------------