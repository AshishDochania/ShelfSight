from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ShelfStatus(BaseModel):
    shelf_id: int
    product_id: int
    stock_level: int

@router.get("/shelf_status", response_model=List[ShelfStatus])
async def get_shelf_status():
    # In a real implementation, this would fetch data from a database
    return [
        ShelfStatus(shelf_id=1, product_id=101, stock_level=5),
        ShelfStatus(shelf_id=2, product_id=102, stock_level=3),
        ShelfStatus(shelf_id=3, product_id=103, stock_level=0),
    ]

@router.get("/shelf_status/{shelf_id}", response_model=ShelfStatus)
async def get_shelf_status_by_id(shelf_id: int):
    # In a real implementation, this would fetch data from a database
    if shelf_id == 1:
        return ShelfStatus(shelf_id=1, product_id=101, stock_level=5)
    raise HTTPException(status_code=404, detail="Shelf not found")