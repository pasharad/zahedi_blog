from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Blog(BaseModel):
    title: str
    discription: str
    like: int
    comment: Optional[str] = None


@app.get('/hi')
async def root():
    return {'message': 'Hello World!'}
