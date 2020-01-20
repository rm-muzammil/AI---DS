from fastapi import FastAPI
from app.routes.product import router as product_router
from app.routes.app import router as app_router
from app.routes.user import router as user_router

app = FastAPI(title="FastAPI", description="FastAPI", version="0.0.1")


app.include_router(app_router)
app.include_router(product_router)
app.include_router(user_router)