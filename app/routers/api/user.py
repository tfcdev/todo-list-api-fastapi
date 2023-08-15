from fastapi import APIRouter, Depends
from ...schemas.user import UserSchema
from ...services.user import UserService

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/", response_model=list[UserSchema])
def list_all(userService: UserService = Depends()) -> list[UserSchema]:
    return userService.list_all()


@router.post("/", response_model=UserSchema)
def create(user: UserSchema, userService: UserService = Depends()):
    return userService.create(user)
