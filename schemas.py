from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime


class Post(BaseModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    title: str
    body: str
    created_at: datetime
    published: Optional[bool]
    updated_at: datetime
    
class PostBase(Post):
    class Config():
        orm_mode=True

class PostUpdate(BaseModel):
    title: str = Field(default="(Updated)")
    body: str
    published: Optional[bool]
    updated_at: datetime
    # created_at: datetime
    
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    name: str
    email: str
    posts: List[PostBase]
    
    class Config():
        orm_mode = True
        
class GetPost(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    updated_at: datetime
    created_at: datetime
    author: ShowUser
    
    class Config():
        orm_mode = True