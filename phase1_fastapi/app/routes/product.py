from fastapi import APIRouter
from app.models.product import Product, ProductResponse, ProductList
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
pro_list = [{ "name": "Product 1", "price": 100},{"name": "Product 2", "price": 200}]
@router.get("/",response_model=ProductList)
def get_products():
    return {"message": "Products", "products": pro_list}  