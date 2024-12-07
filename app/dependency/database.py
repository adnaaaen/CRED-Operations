from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from .config import DB_URL
from contextlib import contextmanager

engine = create_engine(DB_URL)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
