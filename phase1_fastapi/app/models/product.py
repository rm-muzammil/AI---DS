from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    name: str = Field(..., min_length=3)
    price: int = Field(..., gt=0)
    in_stock: bool = True

class ProductOut(BaseModel):
    name: str
    price: int

class ProductResponse(BaseModel):
    message: str
    product: ProductOut
class ProductListResponse(BaseModel):
    message: str
    products: list[ProductOut]

class ProductUpdate(BaseModel):
    name: Optional[str]
    price: Optional[int]
    in_stock: Optional[bool]