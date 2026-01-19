from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
from app.routes.product import router as product_router

app = FastAPI(title="FastAPI", description="FastAPI", version="0.0.1")
app.include_router(product_router)


@app.get("/")
def read_root():
    return {"message": "FastAPI is Working"}

@app.get("/greeting/{name}")
def greet(name: str,age: int):
        return {
        "name": name,
        "age": age,
        "message": f"Hello {name}"
    }
@app.get("/square/{num}")
def squr(num:int):
    return num * num

@app.get("/info")
def status():
    return{
        "app":"Phase 1",
        "status":"learning"
    }





class User(BaseModel):
    username: str = Field(...,min_length=3,max_length=10)
    email: str = Field(...,example="john.doe@example.com")
    age: int = Field(...,gt=18,lt=100,example=30)
    is_active : Optional[bool] = True

class UserResponse(BaseModel):
    message:str
    user:User
   



@app.post("/users",response_model=UserResponse)
def create_user(user: User):
    new_user = User(**user.dict())
    return {
        "message":"User created successfully",
        "user":new_user
    }

