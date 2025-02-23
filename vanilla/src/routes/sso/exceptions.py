from fastapi import HTTPException

class AuthenticationException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Could not validate credentials")