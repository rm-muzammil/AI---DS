from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "FastAPI is Working"}

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
