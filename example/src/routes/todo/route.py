# route.py for todo
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.exceptions.handler import *
from sqlmodel import select

from src.routes.todo.models import *
from src.routes.todo.schemas import *
from src.routes.todo.service import *

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={401: {"user": "Not authorized"}}
    )

# Create a new task
@router.post("/tasks/")
def create_task(task: TaskModel, db: Session = Depends(get_db)):
    create_task_model = Task(
        title=task.title,
        description=task.description,
        completed=True
    )
    db.add(create_task_model)
    db.commit()
    db.refresh(create_task_model)
    return create_task_model

# Get all tasks
@router.get("/tasks/", response_model=List[Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.exec(select(Task)).all()

# Get a task by ID
@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="TaskModel not found")
    return task

# Update a task
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: Task, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="TaskModel not found")

    task.title = task_update.title
    task.description = task_update.description
    task.completed = task_update.completed

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Delete a task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="TaskModel not found")

    db.delete(task)
    db.commit()
    return {"message": "TaskModel deleted successfully"}