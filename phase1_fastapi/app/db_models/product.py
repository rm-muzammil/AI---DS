from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class ProductDB(Base):
    __tablename__ = "products"

    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)
    in_stock = Column(Boolean, default=True)