from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    Pending = "Pending"
    Completed = "Completed"


class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


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
    user_id: int

    class Config:
        from_attributes = True