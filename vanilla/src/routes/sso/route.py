from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from msal import ConfidentialClientApplication
from jose import jwt
from config.config import settings
# from src.sso.schemas import OpenID
import datetime

router = APIRouter(
    prefix="/sso",
    tags=["sso"],
    responses={401: {"user": "Not authorized"}}
    )

AUTHORITY = f"https://login.microsoftonline.com/{settings.AUTHORITY}"
SCOPES = ["User.Read"]  # Microsoft Graph API permissions

msal_app = ConfidentialClientApplication(
    client_id=settings.CLIENT_ID,
    client_credential=settings.CLIENT_SECRET,
    authority=settings.AUTHORITY,
)

async def create_jwt_token(user_info: dict):
    # expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    expiration = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1)
    token = jwt.encode({"exp": expiration, "sub": user_info["oid"], "pld": user_info}, settings.SECRET_KEY, algorithm="HS256")
    return token

@router.get("/login")
async def login():
    auth_url = msal_app.get_authorization_request_url(
        scopes=SCOPES,
        redirect_uri=settings.REDIRECT_URI
    )
    return RedirectResponse(auth_url)

@router.get("/callback")
async def auth_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")

    # Exchange code for token
    result = msal_app.acquire_token_by_authorization_code(
        code,
        scopes=SCOPES,
        redirect_uri=settings.REDIRECT_URI
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail="Token acquisition failed")

    # Parse and create JWT for client session
    user_info = result.get("id_token_claims")
    jwt_token = await create_jwt_token(user_info)

    response = RedirectResponse(url="/")
    response.set_cookie(key="token", value=jwt_token)
    return response