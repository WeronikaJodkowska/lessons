from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists


def create_user(
        session: Session, email: str, password: str, phone: str, age: int, city: str, address: str
) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)

    session.add_all([user, profile, address])
    session.commit()

    return user


def update_or_create_address(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address.city = city
        current_address.address = address
    else:
        current_address = Address(user=user, city=city, address=address)

    session.add(current_address)
    session.commit()

    return current_address


# homework

def create_product(session: Session, name: str, price: int, number: int, comment: str) -> Product:
    product = Product(name=name, price=price, number=number, comment=comment)

    session.add(product)
    session.commit()

    return product


def select_all_products(session: Session):
    print(session.query(Product.id, Product.name, Product.price, Product.number, Product.comment).all())


def update_product(session: Session, id: int, name: str, price: int, number: int, comment: str) -> Product:
    session.query(Product).filter_by(id=id).update({"name": name})
    session.query(Product).filter_by(id=id).update({"price": price})
    session.query(Product).filter_by(id=id).update({"number": number})
    session.query(Product).filter_by(id=id).update({"comment": comment})

    session.commit()


def delete_product(session: Session, id: int):
    session.query(Product).filter_by(id=id).delete()
    session.commit()


def purchase_product(session: Session, number: int, user_id: int, product_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    product = session.query(Product).filter_by(id=product_id).first()
    purchase = Purchase(number=number, user=user, product=product)
    session.add(purchase)
    session.commit()


def select_purchases_by_id(session: Session, user_id: int):
    purchases = session.query(Purchase.product_id).filter_by(user_id=user_id).all()
    for i in purchases:
        print(session.query(Product.name, Product.price, Product.number).filter_by(id=i[0]).all())


def menu():
    strs = ("Enter 1 to crete a product.\n"
            "Enter 2 to select all products.\n"
            "Enter 3 to update product by id.\n"
            "Enter 4 to delete product by id.\n"
            "Enter 5 to buy product.\n"
            "Enter 6 to select all purchases.\n"
            "Enter 7 to exit : ")
    choice = input(strs)
    return int(choice)


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    # new_user = create_user(
    #     session=current_session,
    #     email="test@test.com",
    #     password="password",
    #     phone="+375292992929",
    #     age=20,
    #     city="City",
    #     address="Address 123",
    # )

    user = current_session.query(User).filter_by(email="test@test.com").first()
    update_or_create_address(
        session=current_session,
        user=user,
        city="Old City",
        address="Old Address 123"
    )

    while True:
        choice = menu()
        if choice == 1:
            print("To create a product enter: ")
            product_name = input("Product name: ")
            product_price = int(input("Product price: "))
            product_number = int(input("Product number: "))
            product_comment = input("Product comment if necessary: ")
            create_product(session=current_session, name=product_name, price=product_price,
                           number=product_number, comment=product_comment)
        if choice == 2:
            select_all_products(session=current_session)
        if choice == 3:
            product_id = int(input("To update product enter it's id: "))
            product_name = input("Product name: ")
            product_price = int(input("Product price: "))
            product_number = int(input("Product number: "))
            product_comment = input("Product comment: ")
            update_product(session=current_session, id=product_id, name=product_name,
                           price=product_price, number=product_number, comment=product_comment)
        if choice == 4:
            product_id = int(input("Enter the product id to delete it: "))
            delete_product(current_session, product_id)
        if choice == 5:
            user_id = int(input("To buy product enter user's id: "))
            product_id = int(input("Product id: "))
            product_number = int(input("Product number: "))
            purchase_product(session=current_session, number=product_number, user_id=user_id, product_id=product_id)
        if choice == 6:
            user_id = int(input("To select all purchases enter user's id: "))
            select_purchases_by_id(session=current_session, user_id=user_id)
        if choice == 7:
            break
