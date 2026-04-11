from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

class StudentUpdate(BaseModel):
    name: str
    age: int
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str

    class Config:
        from_attributes = True