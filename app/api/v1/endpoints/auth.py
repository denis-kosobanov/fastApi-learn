from fastapi import APIRouter, HTTPException, status, Response, Depends

from app import crud
from app.core.config import get_settings
from app.core.security import create_access_token
from app.dependencies.user_deps import user_existing
from app.schemas.profile_schema import IProfileCreate
from app.schemas.role_schema import IRoleEnum
from app.schemas.user_schema import IUserCreate, IUserAccess, LoginData

router = APIRouter()


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
        user: IUserCreate = Depends(user_existing),
):
    user: IUserAccess = IUserAccess(**user.model_dump())
    role_user = await crud.role.fetch_one(name=IRoleEnum.user)
    user.role_id = role_user.id
    user.is_superuser = False
    new_user = await crud.user.create(obj=user)
    new_profile = IProfileCreate(user_id=new_user.id)
    await crud.profile.create(obj=new_profile)


@router.post('/login')
async def login_user(
        response: Response,
        login_data: LoginData
):
    email = login_data.email
    password = login_data.password
    auth_user = await crud.user.authenticate(obj=IUserCreate(email=email, password=password))
    if not auth_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token(auth_user.id)
    response.set_cookie(get_settings().name_access_token, access_token, httponly=True)
    return {"message": "Authentication successful", "access_token": access_token}


@router.post('/logout', status_code=status.HTTP_200_OK)
async def logout_user(response: Response):
    response.delete_cookie(get_settings().name_access_token)
