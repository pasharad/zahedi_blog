from fastapi import Depends, FastAPI
from typing import List
from sqlalchemy.orm import Session
import managers
from models import get_db
from schema import Blog, User, Comment


app = FastAPI()


@app.post('/blogs/', response_model=Blog)
async def create_blogs_view(blog: Blog, db: Session = Depends(get_db)):
    db_blog = managers.create_blog(db, blog)
    return db_blog


@app.get('/blogs/', response_model=List[Blog])
async def get_blogs_view(db: Session = Depends(get_db)):
    return managers.get_blogs(db)


@app.get('/blogs/{blog_id}')
async def get_blog_view(blog_id: int, db: Session = Depends(get_db)):
    return managers.get_blog(db, blog_id)


@app.get('/comments/{comment_id}')
async def get_comment_view(comment_id: int, db: Session = Depends(get_db)):
    return managers.get_comment(db, comment_id)


@app.get('/comments/', response_model=List[Comment])
async def get_comments_view(db: Session = Depends(get_db)):
    return managers.get_comments(db)


@app.post('/comments/', response_model=Comment)
async def create_comment_view(comment: Comment, db: Session = Depends(get_db)):
    db_comment = managers.create_comment(db, comment)
    return db_comment


@app.post('/users/', response_model=User)
async def create_user_view(user: User, db: Session = Depends(get_db)):
    db_user = managers.create_user(db, user)
    return db_user


@app.get('/users/', response_model=List[User])
async def get_users_view(db: Session = Depends(get_db)):
    return managers.get_users


@app.get('/users/{user_id}')
async def get_user_view(user_id: int, db: Session = Depends(get_db)):
    return managers.get_user(db, user_id)
