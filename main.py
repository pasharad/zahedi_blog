from fastapi import Depends, FastAPI
from typing import List
from sqlalchemy.orm import Session
from managers import create_blog, get_blog, get_blogs
from models import get_db
from schema import Blog


app = FastAPI()


@app.post('/blogs/', response_model=Blog)
def create_blogs_view(place: Blog, db: Session = Depends(get_db)):
    db_place = create_blog(db, place)
    return db_place


@app.get('/blogs/', response_model=List[Blog])
def get_blogs_view(db: Session = Depends(get_db)):
    return get_blogs(db)


@app.get('/blog/{blog_id}')
def get_blog_view(blog_id: int, db: Session = Depends(get_db)):
    return get_blog(db, blog_id)
