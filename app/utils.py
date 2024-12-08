from service import book_service


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
    value = book_service.read_all_books()
    all_data = [title] + [list((each.json()).values()) for each in value]
    return all_data


if __name__ == "__main__":
    res = table_data()
    for each in res:
        print("ha")
        print(each)
