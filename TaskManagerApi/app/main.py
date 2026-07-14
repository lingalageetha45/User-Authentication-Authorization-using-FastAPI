from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from .database import Base
from .database import SessionLocal
from .database import engine

from . import crud
from . import models
from . import schemas


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Simple CRUD API using FastAPI",
    version="1.0.0"
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    return crud.create_task(db, task)


@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_all_tasks(
    db: Session = Depends(get_db)
):

    return crud.get_tasks(db)


@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_task(db, task_id, task)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@app.delete(
    "/tasks/{task_id}"
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_task(db, task_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }