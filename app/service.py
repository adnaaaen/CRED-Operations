from crud import book_crud
from dependency.database import get_session
from typing import Any
from schema import BookCreate
from models import Book


class BookServices:

    def create_book(
        self, name: str, author_name: str, department: str, price: str
    ) -> None:

        details = BookCreate(
            name=name, author=author_name, department=department, price=float(price)
        )
        try:
            with get_session() as db:
                status = book_crud.create(body=details, db=db)
            print(status)
        except Exception as e:
            print("something went wrong!", e)

    def read_book(self, id: int) -> list[Any] | Book:
        try:
            with get_session() as db:
                status = book_crud.read(db=db, id=id)
            print(status)
            return status if status else []
        except Exception as e:
            print("something went wrong!", e)
            return []

    def read_all_books(self) -> list[Any] | list[Book]:
        try:
            with get_session() as db:
                all_entires = book_crud.read_all(db=db)
            return all_entires if all_entires else []
            print(all_entires)
            return all_entires
        except Exception as e:
            print("something went wrong!", e)
            return []

    def update_book(self) -> None:
        raise NotImplementedError

    def search_with_key(self, key: str, value: str) -> Any:
        try:
            with get_session() as db:
                result = db.query(Book).filter(getattr(Book, key) == value).first()
            return result
        except Exception as e:
            print("something went wrong!", e)

    def delete_book(self, id: int) -> Book | None:
        try:
            with get_session() as db:
                entry = book_crud.delete(db=db, id=id)
            return entry
        except Exception as e:
            print("Error occurred ", e)


book_service = BookServices()
