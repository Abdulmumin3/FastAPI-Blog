from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid
from sqlalchemy.sql import func
# from sqlalchemy.dialects.sqlite import UUID


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="author")
    

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    user_id = Column(String, ForeignKey('users.id'), default=str(uuid.uuid4()))
    author = relationship("User", back_populates="blogs")