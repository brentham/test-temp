from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from src.config.config import settings
from src.routes.main import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Set-Cookie"],
    allow_credentials=True,
    
)

# ---------------Routes-------------------
app.include_router(api_router, prefix=settings.API_V1_STR)
# ----------------------------------------

# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")