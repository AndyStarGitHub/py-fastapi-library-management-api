from datetime import datetime, date

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: datetime


class BookCreate(BookBase):
    author_id: int
    title: str
    summary: str
    publication_date: date


class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True
