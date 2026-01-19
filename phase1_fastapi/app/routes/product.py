from fastapi import APIRouter
from app.models.product import Product, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse)
def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product": product
    }
