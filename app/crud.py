from sqlalchemy.orm import Session
from schema import BookCreate, Book, BookUpdate
from models import Book


class BookCrud:

    async def create(self, body: BookCreate, db: Session) -> Book:
        Book()
        pass
        

    async def read(self) -> None:
        raise NotImplementedError

    async def update(self) -> None:
        raise NotImplementedError

    async def delete(self) -> None:
        raise NotImplementedError
