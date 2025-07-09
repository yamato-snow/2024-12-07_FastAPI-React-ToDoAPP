# crud/task.py
from sqlalchemy.orm import Session
from ..models import task as task_model
from ..schemas import task as task_schema

def create_task(db: Session, task: task_schema.TaskCreate):
    db_task = task_model.Task(**task.dict(by_alias=False))
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(task_model.Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(task_model.Task).filter(task_model.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task: task_schema.TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task:
        update_data = task.dict(exclude_unset=True, by_alias=False)
        for key, value in update_data.items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task