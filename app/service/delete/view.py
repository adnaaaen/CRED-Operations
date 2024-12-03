from sqlalchemy.orm import sessionmaker
from models import Library
from dependency import engine


def deleteBook(book_id: int) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        book_to_delete = (
            session.query(Library).where(Library.book_id == int(book_id)).first()
        )
    except Exception as e:
        print("Please ", e)
    else:
        if book_to_delete is None:
            print("no data")
            return
        else:
            session.delete(book_to_delete)
            session.commit()
            return
    finally:
        session.close()
