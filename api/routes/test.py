from utils import get_db
from models import Products
from schema import ProductFormSelect, ProductFormDelete, ProductFormUpdate
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

router = APIRouter()

# cookie notes
# secure must always be true in prod, false if dev
# httponly always true both prod and dev
# cookie expiry to env preferred
# samesite none is preferred
# fastapi middleware -> allow origins (url of FE, dynamically changes for prod and dev), allow credentials true

# for frontend, ensure to have env for API url for prod and dev


@router.get("/product")
async def get_product(session: AsyncSession = Depends(get_db)):
    query = select(Products)
    result = await session.execute(query)
    products = result.scalars().all()
    return {"products": products}


@router.post("/product")
async def add_product(
    product_form: ProductFormSelect, session: AsyncSession = Depends(get_db)
):
    query = Products(product_name=product_form.product_name)
    session.add(query)
    await session.commit()
    return {"message": product_form.model_dump()}


@router.put("/product")
async def update_product(
    product_form: ProductFormUpdate, session: AsyncSession = Depends(get_db)
):
    query = (
        update(Products)
        .where(
            (Products.product_name != product_form.product_name)
            & (Products.id == product_form.product_id)
        )
        .values(product_name=product_form.product_name)
    )
    await session.execute(query)
    await session.commit()
    return {"message": product_form.model_dump()}


@router.delete("/product")
async def delete_product(
    product_form: ProductFormDelete, session: AsyncSession = Depends(get_db)
):
    query = delete(Products).where(Products.id == product_form.product_id)
    await session.execute(query)
    await session.commit()
    return {"message": product_form.model_dump()}
