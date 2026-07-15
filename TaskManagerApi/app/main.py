from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import Base, engine
from .dependencies import get_db, get_current_user
from .models import User
from . import crud, schemas
from .auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Task Manager with JWT Authentication",
    version="2.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API with JWT Authentication",
        "docs": "/docs"
    }


@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"]
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_task(db, task, current_user)


@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse],
    tags=["Tasks"]
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_tasks(db, current_user)


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
    tags=["Tasks"]
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = crud.get_task(db, task_id, current_user)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
    tags=["Tasks"]
)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = crud.update_task(db, task_id, task, current_user)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@app.delete(
    "/tasks/{task_id}",
    tags=["Tasks"]
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = crud.delete_task(db, task_id, current_user)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }