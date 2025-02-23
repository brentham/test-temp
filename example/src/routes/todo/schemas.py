# schemas.py for todo
from sqlmodel import SQLModel
from typing import Optional
    
class TaskModel(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool