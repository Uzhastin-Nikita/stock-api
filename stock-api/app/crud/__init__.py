from sqlalchemy.orm import Session

from models import stock, item
import schemas

def get_stock(db: Session, stock_id: int):
    return db.query(stock.Stock).filter(stock.Stock.id == stock_id).first()


def get_stocks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(stock.Stock).offset(skip).limit(limit).all()


def create_stock(db: Session, stock: schemas.ItemCreate):
    db_stock = stock.Stock(id=stock.id)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, stock_id: int):
    db_item = item.Item(**item.dict(), owner_id=stock_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item