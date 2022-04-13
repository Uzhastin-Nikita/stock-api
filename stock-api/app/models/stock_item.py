from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from . import base

class Stock_Item(base.Base):
    __tablename__ = "stock_item"

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    quntity = Column(Integer)
    items = relationship("Items", back_populates="owner")
    stokcs = relationship("Stocks", back_populates="owner")
