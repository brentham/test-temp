from typing import Optional
from sqlmodel import SQLModel, Field

class Users(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool = Field(default=True)