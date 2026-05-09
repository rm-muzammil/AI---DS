from app.models.product import ProductUpdate
from fastapi import APIRouter,Depends,HTTPException,status

from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models.product import ProductDB
from app.models.product import Product, ProductResponse, ProductListResponse,ProductOut

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return {
        "message": "Product created",
        "product": db_product
    }
@router.get("/{product_id}", response_model=ProductResponse,status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {
        "message": "Product found",
        "product": product
    }
@router.put("/{product_id}", response_model=ProductResponse,status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    for field, value in product_data.dict(exclude_unset=True).items():
        if value is not None:
            setattr(product, field, value)
    db.add(product)
    db.commit()
    db.refresh(product)
    return {
        "message": "Product updated",
        "product": product
    }
@router.delete("/{product_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(product)
    db.commit()
 
@router.get("/", response_model=ProductListResponse)
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductDB).all()
    return {
        "message": "Products list",
        "products": products
    }