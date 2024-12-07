from sqlalchemy.orm import Session
from schema import BookCreate
from models import Book
from dataclasses import asdict


class BookCrud:

    def create(self, body: BookCreate, db: Session) -> Book:
        details = asdict(body)
        book = Book()
        for key, value in details.items():
            setattr(book, key, value)
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def read(self, db: Session, id: int) -> Book | None:
        data = db.query(Book).filter(Book.id == id).first()
        return data if data else None

    def read_all(self, db: Session) -> list[Book]:
        all_data = db.query(Book).all()
        return all_data

    def update(self) -> None:
        raise NotImplementedError

    def delete(self, db: Session, id: int) -> Book | None:
        entry = db.query(Book).filter(Book.id == id).first()
        db.delete(entry)
        db.commit()
        return entry


book_crud = BookCrud()
