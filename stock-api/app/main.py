import db
import db.config

print(db.saleman, db.buyer)

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import schemas
import crud
from models import base


base.Base.metadata.create_all(bind=db.config.engine)

app = FastAPI()


# Dependency
def get_db():
    db = db.config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/stock/", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    db_stock = x.crud.get_user_by_email(db, id=stock.id)
    if db_stock:
        raise HTTPException(status_code=400, detail="Stock already registered")
    return crud.create_stock(db=db, stock=stock)


@app.get("/stocks/", response_model=list[schemas.Stock])
def read_stocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stocks = crud.get_stocks(db, skip=skip, limit=limit)
    return stocks


@app.get("/stocks/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock(db, user_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock


@app.post("/stock/{stock_id}/items/", response_model=schemas.Item)
def create_item_for_stock(
    stock_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, stock_id=id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
