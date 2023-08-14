from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    description: str
    like: Optional[int] = 0
    comment: Optional[str] = None

    class Config:
        orm_mode = True
