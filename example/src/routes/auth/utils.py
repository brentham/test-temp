from typing import Optional
from jose import JWTError, jwt
from config.config import Settings

auth_settings = Settings()

def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, auth_settings.SECRET_KEY, algorithms=[auth_settings.ALGORITHM])
        return payload
    except JWTError:
        return None