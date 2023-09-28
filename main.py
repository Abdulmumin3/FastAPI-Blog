from fastapi import Depends, FastAPI, status, Response, HTTPException
import schemas, models, hashing
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import uuid
from typing import List
from sqlalchemy.sql import func


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get('/blog-posts', status_code=status.HTTP_200_OK, response_model=List[schemas.Post], tags=["Blogs"])
def home(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.post('/create-blog-posts', status_code=201, tags=["Blogs"])
def create_blog(request: schemas.Post, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, created_at=request.created_at, published=request.published, user_id="2afeb3c8-8d59-4883-8c82-8a04cf4c474d")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/{id}', status_code=200, response_model=schemas.GetPost, tags=["Blogs"],)
def get_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not available",
        )
    return blog



@app.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PostUpdate, tags=["Blogs"])
async def update_post_by_id(id, request: schemas.PostUpdate, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    # updated_blog = request.dict()
    # blog.update(updated_blog)
    # db.commit()
    blog.title = request.title
    blog.body = request.body
    blog.published = request.published
    blog.updated_at = func.now()
    
    db.commit()
    return blog

@app.delete('/blog/{id}', status_code=204, tags=["Blogs"])
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with `{id}` not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return f'Blog with id {id} is deleted successfully'

# Users

@app.post('/create-user', status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser], tags=["Users"])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=["Users"])
def get_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with `{id}` not found")
    
    return user

@app.delete('/user/{id}', status_code=204, tags=["Users"])
def delete_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with `{id}` not found")
    
    user.delete(synchronize_session=False)
    db.commit()
    return 'deleted'