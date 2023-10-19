from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from app.models.category_model import Category
    from app.models.review_model import Review
    from app.models.discount_model import Discount


class Product(BaseUUIDModel):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    stock_quantity: Mapped[int] = mapped_column(nullable=False)
    category_id: Mapped[UUID] = mapped_column(ForeignKey('category.id'))

    categories: Mapped['Category'] = relationship(back_populates='products', lazy='selectin')
    reviews: Mapped[list['Review']] = relationship(back_populates='product', lazy='selectin')
    discount: Mapped['Discount'] = relationship(back_populates='product')