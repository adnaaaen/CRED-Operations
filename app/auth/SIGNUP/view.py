from sqlalchemy.orm import sessionmaker
from models import User, engine

def signup(username: str, password: str, email: str, phone_number: str) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        if username and password and email and phone_number != "":
            new_user = User(user_name=username, password=password, email=email, phone=phone_number)
            session.add(new_user)
            print("Data added")
        else:
            print("Please fill-up all entry!")
    except Exception as e:
        print("something went wrong!", e)
    else:
        session.commit()
    finally:
        session.close()
    
