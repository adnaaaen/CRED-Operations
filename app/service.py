from crud import book_crud
from dependency.database import get_session
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

    def read_book(self) -> None:
        raise NotImplementedError

    def read_books(self) -> None:
        raise NotImplementedError

    def update_book(self) -> None:
        raise NotImplementedError

    def delete_book(self, id: int) -> Book | None:
        try:
            with get_session() as db:
                entry = book_crud.delete(db=db, id=id)
            return entry
        except Exception as e:
            print("Error occurred ", e)


book_service = BookServices()
