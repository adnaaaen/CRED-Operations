from sqlalchemy import String, Column, INTEGER, FLOAT, DATETIME, BOOLEAN
from datetime import datetime
from dependency import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(String, index=True, nullable=False)
    author = Column(String, index=True)
    department = Column(String, index=True)
    price = Column(FLOAT)
    is_available = Column(BOOLEAN, default=True)
    created_at = Column(DATETIME, default=datetime.now())
    updated_at = Column(DATETIME, default=datetime.now())

    def __repr__(self) -> str:
        return f"<{self.id} : {self.name} , {self.author} , {self.department}>"

    def json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "department": self.department,
            "price": self.price,
            "is_available": self.is_available,
            "created_at": self.created_at.date(),
            "updated_at": self.updated_at.date(),
        }
