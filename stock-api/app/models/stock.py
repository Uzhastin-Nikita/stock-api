
from sqlalchemy import Column,Integer 

from . import base

class Stock(base.Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)