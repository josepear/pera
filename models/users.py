## Libraries
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    is_dog: bool = False
    password:str

class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

class UserCreate(UserBase):
    pass