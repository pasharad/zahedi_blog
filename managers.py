from sqlalchemy.orm import Session
from models import DBBlog, DBUser, DBComment, DBAboutUs
from schema import Blog, User, Comment, AboutUs


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


def create_about_us(db: Session, about_us: AboutUs):
    db_about_us = DBAboutUs(**about_us.model_dump())
    db.add(db_about_us)
    db.commit()
    db.refresh(db_about_us)

    return db_about_us


def select_about_us(db: Session):
    return db.query(DBAboutUs).all()


def get_about_us(db: Session):
    return db.query(DBAboutUs).where(DBAboutUs.status == True)

def create_user(db: Session, user: User):
    db_user = DBUser(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, user_id: int):
    return db.query(DBUser).where(DBUser.id == user_id).first()


def get_users(db: Session):
    return db.query(DBUser).all()


def create_comment(db: Session, comment: Comment):
    db_comment = DBComment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    return db_comment


def get_comment(db: Session, comment_id: int):
    return db.query(DBComment).where(DBComment.id == comment_id).first()


def get_comments(db: Session):
    return db.query(DBComment).all()
