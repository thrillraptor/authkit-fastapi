from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import oauth_scheme, verify_access_token
from app.models.user import User
from app.db.session import get_db

def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)) -> User:
    payload = verify_access_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user