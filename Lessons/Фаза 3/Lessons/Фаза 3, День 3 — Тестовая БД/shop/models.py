from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    quantities = Column(Integer)

