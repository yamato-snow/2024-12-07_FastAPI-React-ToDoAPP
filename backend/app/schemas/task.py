# schemas/task.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="タスクのタイトル")
    description: Optional[str] = Field(None, max_length=1000, description="タスクの詳細説明")
    completed: bool = Field(False, alias="is_completed", description="タスクの完了状態")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    completed: Optional[bool] = Field(None, alias="is_completed")

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

