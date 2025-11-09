from utils import Base
from uuid import uuid4
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column


class Products(Base):
    __tablename__ = "products"
    product_name: Mapped[Optional[str]] = mapped_column()
    id: Mapped[str] = mapped_column(
        primary_key=True, default_factory=lambda: str(uuid4())
    )


class ProductType(Base):
    __tablename__ = "product_types"
    product_type_name: Mapped[Optional[str]] = mapped_column()
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: uuid4)
