from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=5, max_length=100)

class TaskSchema(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=0, max_length=500)
    user_id: int