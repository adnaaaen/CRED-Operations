from sqlalchemy import String, Column, TIMESTAMP, Integer, Double
from datetime import datetime
from dependency import Base

class Library(Base):
    __tablename__ = "library"
    book_id = Column(Integer, autoincrement=True, primary_key=True)
    book_name = Column(String)
    author_name = Column(String)
    department = Column(String)
    book_price = Column(Double)
    added_date = Column(TIMESTAMP, default=datetime.now())



