from sqlalchemy.orm import Session
from models import DBBlog
from schema import Blog


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
