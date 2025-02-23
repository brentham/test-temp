from sqlmodel import SQLModel
from typing import Optional
    
class CreateUser(SQLModel):
    email: Optional[str]
    username: str
    first_name: str
    last_name: str
    password: str