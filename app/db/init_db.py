import json

from fastapi import UploadFile
from sqlalchemy import insert
from sqlalchemy.ext.asyncio.session import AsyncSession

from app import crud
from app.db.session import engine
from app.models import Base, Category, Product
from app.schemas import IGenderEnum
from app.schemas.category_schema import ICategoryCreate
from app.schemas.product_schema import IProductCreate
from app.schemas.profile_schema import IProfileCreate
from app.schemas.role_schema import IRoleCreate
from app.schemas.user_schema import IUserAccess

roles: list[IRoleCreate] = [
    IRoleCreate(name="admin"),
    IRoleCreate(name="manager"),
    IRoleCreate(name="user"),
]

users: list[dict[str, str | IUserAccess | IProfileCreate]] = [
    {
        "data": IUserAccess(
            username="Admin",
            password='root',
            email="admin@example.com",
            is_superuser=True,
        ),
        "role": "admin",
        'profile': None,
    },
    {
        "data": IUserAccess(
            username="Manager",
            password='root',
            email="manager@example.com",
            is_superuser=False,
        ),
        "role": "manager",
        'profile': None,
    },
    {
        "data": IUserAccess(
            username="User",
            password='root',
            email="user@example.com",
            is_superuser=False,
        ),
        "role": "user",
        'profile': IProfileCreate(
            first_name='Иван',
            last_name='Иванов',
            gender='male',
            address='ул. Ленина 13',
            phone_number='+79824097321',
        ),
    },
]


# categories: list[ICategoryCreate] = [
#     ICategoryCreate(name='Electronics'),
#     ICategoryCreate(name='Clothes'),
#     ICategoryCreate(name='Furniture'),
# ]
#
# products = [
#     {
#         'data': IProductCreate(
#             name='Canon EOS 650D',
#             description='Зеркальная камера',
#             price=31_472,
#             stock_quantity=20,
#         ),
#         'category': 'Electronics',
#         'image': './data/canon.jpg',
#     },
#     {
#         'data': IProductCreate(
#             name='Black Fox B10 Fox 32 ГБ голубой',
#             description='product main image ядер - 4x(1.4 ГГц),'
#                         ' 2 ГБ, 2 SIM, IPS, 1600x720, камера 13'
#                         ' Мп, NFC, 4G, GPS, FM, 4000 мА*ч',
#             price=5_599,
#             stock_quantity=50,
#         ),
#         'category': 'Electronics',
#         'image': './data/phone.jpg',
#     },
#     {
#         'data': IProductCreate(
#             name='Кровать Bella',
#             description='Современная мягкая компактная кровать '
#                         'Белла с большим количеством вариантов '
#                         'обивки дает вам возможность вписать ее '
#                         'в любой интерьер на который хватит вашей'
#                         ' фантазии.',
#             price=11_999,
#             stock_quantity=5,
#         ),
#         'category': 'Electronics',
#         'image': './data/bed.jpg',
#     },
#     {
#         'data': IProductCreate(
#             name='Ferz',
#             description='Шапка',
#             price=1254,
#             stock_quantity=34,
#         ),
#         'category': 'Electronics',
#         'image': './data/head.jpg',
#     },
# ]


async def init_db(async_session: AsyncSession):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    for role in roles:
        await crud.role.create(obj=role, db_session=async_session)

    for user in users:
        role = await crud.role.get_role_by_name(
            name=user["role"], db_session=async_session
        )
        user["data"].role_id = role.id
        new_user = await crud.user.create(obj=user["data"], db_session=async_session)
        if user['profile']:
            profile = user['profile']
            profile.user_id = new_user.id
            await crud.profile.create(obj=profile, db_session=async_session)

    # for category in categories:
    #     await crud.category.create(obj=category, db_session=async_session)

    # for product in products:
    #     category = await crud.category.fetch_one(name=product['category'], db_session=async_session)
    #     new_product_create = product['data']
    #     new_product_create.category_id = category.id
    #     new_product = await crud.product.create(obj=new_product_create, db_session=async_session)
    #     with open(product['image'], "rb") as file:
    #         upload_file = UploadFile(file=file, filename='canon.jpg')
    #         await crud.product.update_image(file=upload_file, product=new_product, db_session=async_session)

    def open_mock_json(model: str):
        with open(f"./data/{model}.json", encoding="utf-8") as file:
            return json.load(file)

    categories = open_mock_json("categories")

    for Model, values in [
        (Category, categories),
    ]:
        query = insert(Model).values(values)
        await async_session.execute(query)

    await async_session.commit()

    products = open_mock_json("products")

    for item in products:
        new_product_create = IProductCreate(**item['product'])
        new_product = await crud.product.create(obj=new_product_create, db_session=async_session)
        with open(item['image'], "rb") as file:
            upload_file = UploadFile(file=file, filename=file.name)
            await crud.product.update_image(file=upload_file, product=new_product, db_session=async_session)
