from pydantic import BaseModel, Field


class ProductFormSelect(BaseModel):
    product_name: str = Field(..., max_length=100)


class ProductFormDelete(BaseModel):
    product_id: str = Field(..., max_length=100)


class ProductFormUpdate(BaseModel):
    product_id: str = Field(..., max_length=100)
    product_name: str = Field(..., max_length=100)
