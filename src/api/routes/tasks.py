from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Task(BaseModel):
    task_id: int
    description: str
    priority: str

@router.get("/tasks", response_model=List[Task])
async def get_tasks():
    # In a real implementation, this would fetch data from a database
    return [
        Task(task_id=1, description="Restock shelf 1", priority="high"),
        Task(task_id=2, description="Check inventory in aisle 3", priority="medium"),
        Task(task_id=3, description="Clean up spill in aisle 2", priority="low"),
    ]

@router.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int):
    # In a real implementation, this would fetch data from a database
    if task_id == 1:
        return Task(task_id=1, description="Restock shelf 1", priority="high")
    raise HTTPException(status_code=404, detail="Task not found")