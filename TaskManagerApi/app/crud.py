from sqlalchemy.orm import Session

from .models import Task, User
from .schemas import TaskCreate, TaskUpdate


def create_task(
    db: Session,
    task: TaskCreate,
    current_user: User
):

    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status.value,
        user_id=current_user.id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(
    db: Session,
    current_user: User
):

    return (
        db.query(Task)
        .filter(Task.user_id == current_user.id)
        .all()
    )


def get_task(
    db: Session,
    task_id: int,
    current_user: User
):

    return (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )


def update_task(
    db: Session,
    task_id: int,
    task: TaskUpdate,
    current_user: User
):

    db_task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )

    if db_task is None:
        return None

    db_task.title = task.title
    db_task.description = task.description
    db_task.status = task.status.value

    db.commit()
    db.refresh(db_task)

    return db_task



def delete_task(
    db: Session,
    task_id: int,
    current_user: User
):

    db_task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )

    if db_task is None:
        return None

    db.delete(db_task)
    db.commit()

    return db_task