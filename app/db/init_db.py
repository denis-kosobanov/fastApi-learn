from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app import crud
from app.schemas.role_schema import IRoleCreate
from app.schemas.user_schema import IUserCreate

roles: list[IRoleCreate] = [
    IRoleCreate(name="admin"),
    IRoleCreate(name="manager"),
    IRoleCreate(name="user"),
]

users: list[dict[str, str | IUserCreate]] = [
    {
        "data": IUserCreate(
            first_name="Admin",
            last_name="FastAPI",
            password_hash='root',
            email="admin@example.com",
            is_superuser=True,
        ),
        "role": "admin",
    },
    {
        "data": IUserCreate(
            first_name="Manager",
            last_name="FastAPI",
            password_hash='root',
            email="manager@example.com",
            is_superuser=False,
        ),
        "role": "manager",
    },
    {
        "data": IUserCreate(
            first_name="User",
            last_name="FastAPI",
            password_hash='root',
            email="user@example.com",
            is_superuser=False,
        ),
        "role": "user",
    },
]


async def init_db(async_session: async_sessionmaker[AsyncSession]):
    for role in roles:
        role_current = await crud.role.get_role_by_name(
            name=role.name, db_session=async_session
        )
        if not role_current:
            await crud.role.create(obj=role, db_session=async_session)

    for user in users:
        current_user = await crud.user.get_by_email(
            email=user["data"].email, db_session=async_session
        )
        role = await crud.role.get_role_by_name(
            name=user["role"], db_session=async_session
        )
        if not current_user:
            user["data"].role_id = role.id
            await crud.user.create(obj=user["data"], db_session=async_session)