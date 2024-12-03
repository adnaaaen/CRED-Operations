from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from .config import DB_URL


engine = create_engine(DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
