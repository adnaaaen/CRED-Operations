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
    password = Column(String)
    user_name = Column(String)
    phone = Column(String)
    last_visit = Column(Date, default=dt.date.today)

    def __init__(self, email, password, user_name, phone):
        self.email = email
        self.password = password
        self.user_name = user_name
        self.phone = phone

    def __repr__(self):
        return f"{self.email}, {self.user_name}, {self.last_visit}\n"

Base.metadata.create_all(bind=engine)
