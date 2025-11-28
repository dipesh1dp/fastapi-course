# Validating schema using pydantic BaseModel
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime 
from typing import Optional, Annotated


class UserCreate(BaseModel): 
    email: EmailStr
    password: str 


class UserOut(BaseModel): 
    id: int 
    email: EmailStr 
    created_at: datetime
    # Enable attribute reading from ORM instances
    model_config = ConfigDict(from_attributes=True)
    # Previously 
    # class Config: 
    #     orm_mode = True 


class PostBase(BaseModel): 
    title: str 
    content: str 
    published: bool = True  


class PostCreate(PostBase): 
    pass 


class Post(BaseModel): 
    id: int
    title: str 
    content: str 
    published: bool 
    created_at: datetime
    owner_id: int
    owner: UserOut
    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel): 
    Post: Post 
    votes: int

class UserLogin(BaseModel): 
    email: EmailStr 
    password: str 
    

class Token(BaseModel): 
    access_token: str 
    token_type: str 


class TokenData(BaseModel): 
    id: Optional[int] = None


class Vote(BaseModel): 
    post_id: int 
    dir: Annotated[int, Field(le=1)]
    # dir: conint(le=1) (pyantic v1)
