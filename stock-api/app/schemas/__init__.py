from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class StockBase(BaseModel):
    id: int


class StockCreate(StockBase):
    pass


class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True