from dataclasses import dataclass
from datetime import datetime
from models import Book


@dataclass
class BookCreate:
    name: str
    author: str
    department: str
    price: float


@dataclass
class BookUpdate:
    name: str | None = None
    author: str | None = None
    department: str | None = None
    price: float | None = None
    is_available: bool | None = None
    updated_at: datetime = datetime.now()
