from pydantic import BaseModel, Field

class UserSchemas(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=15, max_length=100)

class TaskSchemas(BaseModel):
    title: str = Field(min_length=5, max_length=500)
    description: str = Field(min_length=0, max_length=1000)
    user_id: int
