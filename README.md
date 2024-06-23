# CRUD operations using SQLAlchemy

A GUI CRUD operation python application using custometkinter and SQLAlchemy

## Installation

```bash
  git clone https://github.com/adnaaaen/CRUD-Operations.git
  cd CRUD-Operations
```

```bash
  pip install -r requirement.txt
```

```bash
  python app
```

## Environment Variables

- `DATABASE_URL`

create a `.env` file at the root of the `app` folder and add the following:

Below are examples of how to set up the `DATABASE_URL` for different types of local databases:

- For `PostgreSQL`
  `DATABASE_URL=postgresql://your_username@localhost:5432/your_database_name`

- For `MySQL`
  `DATABASE_URL=mysql://your_username@localhost:3306/your_database_name`

## Documentation

- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- [CustomTkinter](https://customtkinter.tomschimansky.com/documentation/)
