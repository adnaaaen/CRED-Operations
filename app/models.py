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
