from fastapi import Depends, APIRouter
from app.models.user import User
from app.schemas.user import UserOut
from app.api.deps import get_current_user

router = APIRouter(prefix="/user")

@router.get("/me", response_model=UserOut)
def get_user(current_user: User = Depends(get_current_user)):
    return current_user