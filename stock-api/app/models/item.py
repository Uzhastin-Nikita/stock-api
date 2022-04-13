from sqlalchemy import  Column,  Integer, String
from . import base

class Item(base.Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)

