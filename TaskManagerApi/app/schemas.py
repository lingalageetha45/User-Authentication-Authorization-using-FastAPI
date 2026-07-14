from enum import Enum

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    Pending = "Pending"
    Completed = "Completed"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

    description: str | None = None

    status: TaskStatus = TaskStatus.Pending


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

    description: str | None = None

    status: TaskStatus


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus

    class Config:
        from_attributes = True