import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Column, TIMESTAMP, Integer, Double
from sqlalchemy.orm import declarative_base
from datetime import datetime as dt

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()


# library model
class Library(Base):
    __tablename__ = "library"
    book_id = Column(Integer, autoincrement=True, primary_key=True)
    book_name = Column(String)
    author_name = Column(String)
    department = Column(String)
    book_price = Column(Double)
    added_date = Column(TIMESTAMP, default=dt.now())

    def asList(self):
          return [
            self.book_id, 
            self.book_name, 
            self.author_name, 
            self.department, 
            self.book_price, 
            self.added_date
        ]
          
    def __repr__(self):
        return f"{self.book_id}, {self.book_name}, {self.author_name}, \
            {self.department}, {self.book_price}, {self.added_date}\n"


Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)
    session = Session()
    value1 = Library(book_name="Introduction to Python", author_name="John Doe", department="Computer Science", book_price=50.0)
    value2 = Library(book_name="Data Science Essentials", author_name="Jane Smith", department="Data Science", book_price=65.0, )
    value3 = Library(book_name="Machine Learning Mastery", author_name="Alice Johnson", department="Engineering", book_price=75.0)
    value4 = Library(book_name="Web Development with Django", author_name="Bob Brown", department="Computer Science", book_price=55.0)
    value5 = Library(book_name="Algorithms and Data Structures", author_name="Emily Davis", department="Mathematics", book_price=60.0)
    value6 = Library(book_name="Artificial Intelligence Basics", author_name="Michael Lee", department="Computer Science", book_price=70.0)
    value7 = Library(book_name="History of Science", author_name="Sarah Thompson", department="History", book_price=45.0)
    value8 = Library(book_name="Physics for Engineers", author_name="David Wilson", department="Engineering", book_price=80.0)
    value9 = Library(book_name="Literature Classics", author_name="Emma Johnson", department="Literature", book_price=55.0)
    value10 = Library(book_name="Environmental Studies", author_name="Robert Green", department="Environmental Science", book_price=65.0)
    
    session.add_all([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10])
    session.commit()

    session.close()
