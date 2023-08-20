import datetime
from sqlalchemy import UniqueConstraint, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime


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


class EntityBase:
    id = Column(Integer, primary_key=True, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)


class DBBlog(Base, EntityBase):
    __tablename__ = 'blogs'

    title = Column(String(50))
    description = Column(String, nullable=True)


class DBUser(Base, EntityBase):
    __tablename__ = 'users'

    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True)


class DBLikes(Base, EntityBase):
    __tablename__ = 'likes'
    __table_args__ = (
        UniqueConstraint('blog_id', 'user_id', name='unique_user_blog'),
    )

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    blog_id = Column(Integer, ForeignKey("blogs.id"), nullable=False)


class DBComment(Base, EntityBase):
    __tablename__ = 'comments'

    description = Column(String)
    parent_id = Column(Integer, ForeignKey("comments.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    blog_id = Column(Integer, ForeignKey("blogs.id"), nullable=False)


Base.metadata.create_all(bind=engine)
