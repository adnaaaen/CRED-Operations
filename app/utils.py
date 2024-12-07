from models import Book
from dependency import get_session


def table_data():
    """generate all existing data in database as a CTKTable Format"""

    title = [
        "Book ID",
        "Book Name",
        "Author Name",
        "Department",
        "Book Price",
        "Is Available ?",
        "Added On",
        "Updated On",
    ]
    with get_session() as db:
        value = db.query(Book).all()
    all_data = [title] + [list((each.json()).values()) for each in value]
    return all_data


if __name__ == "__main__":
    res = table_data()
    for each in res:
        print("ha")
        print(each)
