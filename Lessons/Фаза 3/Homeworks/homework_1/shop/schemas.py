from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    price: int = Field(ge=0)
    quantity: int = Field(ge=0)