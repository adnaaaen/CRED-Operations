from sqlalchemy.orm import sessionmaker
from models import User, engine

def signup(username: str, password: str, email: str, phone_number: str) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        new_user = User(user_name=username, password=password, email=email, phone=phone_number)
        session.add(new_user)
    except Exception as e:
        print("something went wrong!", e)
    else:
        session.commit()
        print("Data added")
    finally:
        session.close()
    
