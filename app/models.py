import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Column, Boolean, Date, Integer
from sqlalchemy.orm import declarative_base
import datetime as dt

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = "cred_user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    user_name = Column(String)
    password = Column(String)
    phone = Column(String)
    last_visit = Column(Date, default=dt.date.today)

    def __repr__(self):
        return (
            f"{self.user_id}, {self.email}, {self.password}, {self.user_name}, {self.phone}, {self.last_visit}"
        )

Base.metadata.create_all(bind=engine)
