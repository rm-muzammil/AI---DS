from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user  

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "FastAPI is Working"}

@router.get("/me")
def read_me(user_id = Depends(get_current_user)):
    return {"user_id": user_id}
@router.get("/greeting/{name}")
def greet(name: str,age: int):
        return {
        "name": name,
        "age": age,
        "message": f"Hello {name}"
    }
@router.get("/square/{num}")
def squr(num:int):
    return num * num
