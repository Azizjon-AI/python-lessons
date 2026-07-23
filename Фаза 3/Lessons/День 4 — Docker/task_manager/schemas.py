from pydantic import BaseModel, Field

class UserSchemas(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=10, max_length=100)

class TaskSchemas(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=10, max_length=100)
    user_id: int 

