from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import Token
from app.schemas.user import UserCreate, UserOut
from app.core.security import create_access_token, hash_password, verify_password
from app.db.session import get_db

router = APIRouter(prefix="/auth")

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserOut)
def register(data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.username == data.username) | (User.email == data.email)).first()
    if existing_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User already exist with same credentials")
    db_user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user