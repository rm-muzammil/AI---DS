from fastapi import APIRouter

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.db_models.product import ProductDB
from app.models.product import Product, ProductResponse, ProductListResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse)
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return {
        "message": "Product created",
        "product": db_product
    }

@router.get("/", response_model=ProductListResponse)
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductDB).all()
    return {
        "message": "Products list",
        "products": products
    }