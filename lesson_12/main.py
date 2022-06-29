from sqlalchemy.orm import sessionmaker

from models import Base, User, Profile, Address
from utils import setup_db_engine, create_database_if_not_exists


def create_user(session, email: str, password: str, phone: str, age: int, city: str, address: str) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)
    session.add(user, address, profile)
    session.commit()


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test@test.com", password="password")
    session.add(user)
    session.commit()
    create_user()