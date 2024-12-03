from sqlalchemy.orm import sessionmaker
from models import Library
from dependency import engine


def getAllData() -> list[str]:
    Session = sessionmaker(bind=engine)
    session = Session()
    headers = [
        "Book ID",
        "Book Name",
        "Author Name",
        "Department",
        "Book Price",
        "Added Date",
    ]
    value = session.query(Library).all()
    session.close()
    all_data = [headers] + [each.asList() for each in value]
    return all_data if len(all_data) != 1 else False


if __name__ == "__main__":
    print("not have data" if not getAllData() else getAllData())
