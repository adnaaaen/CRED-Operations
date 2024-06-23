from sqlalchemy.orm import sessionmaker
from models import Library, engine

def addNewBook(bookName: str, authorName: str, department: str, price: str) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        if bookName and authorName and department and price != "":
            new_user = Library(book_name=bookName, author_name=authorName, department=department, book_price=price)
            session.add(new_user)
            print("Book added")
        else:
            print("Please fill-up all entry!")
    except Exception as e:
        print("something went wrong!", e)
    else:
        session.commit()
    finally:
        session.close()
