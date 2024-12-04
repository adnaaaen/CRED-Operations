from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass(frozen=True)
class BookCreate:
    name: str
    author: str
    department: str
    price: float


@dataclass(frozen=True)
class Book(BookCreate):
    id: int
    is_available: bool
    created_at: datetime


@dataclass(frozen=True)
class BookUpdate:
    name: str | None = None
    author: str | None = None
    department: str | None = None
    price: float | None = None
    is_available: bool | None = None
    updated_at: datetime = datetime.now()


if __name__ == "__main__":
    values = {
        "name": "Data Science",
        "author": "Adnan",
        "department": "Computer Science",
        "price": 999,
    }
    new_book = BookCreate(values)
    # print(asdict(new_book))
    print(new_book)
