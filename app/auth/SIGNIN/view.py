from sqlalchemy.orm import sessionmaker
from models import User, engine

def signin(username: str, password: str) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        value = (
            session.query(User)
            .filter((User.user_name == username.lower()), (User.password == password))
            .all()
        )
    except Exception as e:
        print("Something went wrong", e)
    else:
        # print("Login" if value != [] else "Invalid credentials")
        return True if value != [] else False
    finally:
        session.close()
