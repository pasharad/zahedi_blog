from fastapi import Depends, FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from typing import List
from sqlalchemy.orm import Session
import managers
from pathlib import Path
from models import get_db
from schema import Blog, User, Comment, AboutUs
from fastapi.staticfiles import StaticFiles

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "template"))

app = FastAPI()
api_router = APIRouter()

app.mount("/assets", StaticFiles(directory=str(BASE_PATH / "template/assets")), name="assets")

@api_router.post('/blogs/create', response_model=Blog)
async def create_blogs_view(blog: Blog, db: Session = Depends(get_db)):
    db_blog = managers.create_blog(db, blog)
    return db_blog


@api_router.get('/blogs/', response_model=List[Blog], name="blogs")
async def get_blogs_view(request: Request, db: Session = Depends(get_db)) -> dict:
    blogs = managers.get_blogs(db)
    path = "blogs"
    return TEMPLATES.TemplateResponse(
        "blog.html", {"request":request, "blogs":blogs, "path":path}
        )


@api_router.get('/blogs/{blog_id}')
async def get_blog_view(blog_id: int, db: Session = Depends(get_db)):
    return managers.get_blog(db, blog_id)


@api_router.get('/comments/{comment_id}')
async def get_comment_view(comment_id: int, db: Session = Depends(get_db)):
    return managers.get_comment(db, comment_id)


@api_router.get('/comments/', response_model=List[Comment])
async def get_comments_view(db: Session = Depends(get_db)):
    return managers.get_comments(db)


@api_router.post('/comments/', response_model=Comment)
async def create_comment_view(comment: Comment, db: Session = Depends(get_db)):
    db_comment = managers.create_comment(db, comment)
    return db_comment


@api_router.post('/users/', response_model=User)
async def create_user_view(user: User, db: Session = Depends(get_db)):
    db_user = managers.create_user(db, user)
    return db_user


@api_router.get('/users/', response_model=List[User])
async def get_users_view(db: Session = Depends(get_db)):
    return managers.get_users


@api_router.get('/users/{user_id}')
async def get_user_view(user_id: int, db: Session = Depends(get_db)):
    return managers.get_user(db, user_id)


@api_router.get('/about-us/', name="about-us")
async def get_about_us_view(request: Request, db: Session = Depends(get_db)) -> dict:
    about_us_elements = managers.get_about_us(db)
    path = "about-us"
    return TEMPLATES.TemplateResponse(
        "about_us.html", 
        {"request":request,
          "about_us":about_us_elements,
          "path":path
          }
        )
@api_router.post("/about-us/", name="about-us-craete")
async def create_about_us(about: AboutUs, db: Session = Depends(get_db)):
    db_about_us = managers.create_about_us(db, about)
    return db_about_us

app.include_router(api_router)