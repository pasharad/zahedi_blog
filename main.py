from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Column, String, Integer


app = FastAPI()
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DBBlog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String, nullable=True)
    like = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)


class Blog(BaseModel):
    title: str
    description: str
    like: Optional[int] = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True


def get_blog(db: Session, blog_id: int):
    return db.query(DBBlog).where(DBBlog.id == blog_id).first()


def get_blogs(db: Session):
    return db.query(DBBlog).all()


def create_blog(db: Session, blog: Blog):
    db_blog = DBBlog(**blog.model_dump())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)

    return db_blog


@app.post('/blogs/', response_model=Blog)
def create_places_view(place: Blog, db: Session = Depends(get_db)):
    db_place = create_blog(db, place)
    return db_place


@app.get('/blogs/', response_model=List[Blog])
def get_places_view(db: Session = Depends(get_db)):
    return get_blogs(db)


@app.get('/blog/{blog_id}')
def get_place_view(blog_id: int, db: Session = Depends(get_db)):
    return get_blog(db, blog_id)
