from pydantic import BaseModel, Field

class ProductSchemas(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: int = Field(ge=1)
    quantities: int = Field(ge=1)

