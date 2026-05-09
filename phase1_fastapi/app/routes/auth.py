from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models.user import UserDB
from app.models.auth import LoginRequest, TokenResponse
from app.utils.security import verify_password
from app.utils.jwt import create_access_token
from app.dependencies.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router =APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/login",response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.get("/me")
def read_me(user_id = Depends(get_current_user)):
    return {"user_id": user_id}
