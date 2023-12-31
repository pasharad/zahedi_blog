from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    description: str

    class Config:
        from_attributes = True


class AboutUs(BaseModel):
    description: str
    our_vision: str
    our_mission: str
    why_choose_us:  str

    class Config:
        from_attributes = True


class User(BaseModel):
    first_name: str
    last_name: str
    username: str

    class Config:
        from_attributes = True


class Comment(BaseModel):
    description: str
    parent_id: Optional[int] = None
    user_id: int
    blog_id: int

    class Config:
        from_attributes = True
