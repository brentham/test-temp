
# Bearer Token Authentication

# from fastapi import HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt
# from config.config import Settings
# from fastapi_sso.sso.base import OpenID

# settings = Settings()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# async def get_logged_user(token: str = Depends(oauth2_scheme)) -> OpenID:
#     """Get user's JWT stored in the Authorization header, parse it, and return the user's OpenID."""
#     try:
#         claims = jwt.decode(token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
#         return OpenID(**claims["pld"])
#     except Exception as error:
#         raise HTTPException(status_code=401, detail="Invalid authentication credentials") from error
    
    
# Cookie Authentication

from fastapi import HTTPException, Security
from fastapi.security import APIKeyCookie
from jose import jwt
from config.config import Settings
from fastapi_sso.sso.base import OpenID

settings = Settings()

api_key_cookie = APIKeyCookie(name="token")

async def get_logged_user(cookie: str = Security(api_key_cookie)) -> OpenID:
    """Get user's JWT stored in cookie 'token', parse it, and return the user's OpenID."""
    try:
        claims = jwt.decode(cookie, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        return OpenID(**claims["pld"])
    except Exception as error:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials") from error