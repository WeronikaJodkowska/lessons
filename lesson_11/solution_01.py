"""
1. Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
2. Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию
и вводить необходимые данные.
"""

import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except ConnectionError as e:
        print(e)
    return conn


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
           CREATE TABLE IF NOT EXISTS Products(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR,
           price INTEGER,
           number INTEGER,
           comment VARCHAR
           );
           """,
    )
    conn.commit()


def create_product(conn, name: str = "", price: int = 0, number: int = 0, comment: str = ""):
    cursor = conn.cursor()
    cursor.execute(
        """
           INSERT INTO Products (name, price, number, comment)
           VALUES (?, ?, ?, ?);
           """,
        (name, price, number, comment)
    )
    conn.commit()


def select_all_products(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
           SELECT * FROM Products;
           """,
    )
    conn.commit()
    records = cursor.fetchall()
    for row in records:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Price: ", row[2])
        print("Number: ", row[3])
        print("Comment: ", row[4], "\n")
    cursor.close()


def select_product(conn, name: str):
    cursor = conn.cursor()
    cursor.execute(
        """
           SELECT * FROM Products WHERE name = ?;
           """,
        (name,)
    )
    conn.commit()
    record = cursor.fetchone()
    print("Id: ", record[0])
    print("Name: ", record[1])
    print("Price: ", record[2])
    print("Number: ", record[3])
    print("Comment: ", record[4], "\n")
    cursor.close()


def update_product(conn, p_id: int, name: str = "", price: int = 0, number: int = 0, comment: str = ""):
    cursor = conn.cursor()
    cursor.execute(
        """
           UPDATE Products 
           SET name = ?,
           price = ?,
           number = ?, 
           comment = ?
           WHERE id = ?;
           """,
        (name, price, number, comment, p_id)
    )
    conn.commit()
    cursor.close()


def delete_product(conn, p_id: int):
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM Products WHERE id = ?;
        """,
        (p_id,)
    )
    conn.commit()
    cursor.close()


def menu():
    strs = ("Enter 1 to crete a product.\n"
            "Enter 2 to select all products.\n"
            "Enter 3 to select product by name.\n"
            "Enter 4 to update product by id.\n"
            "Enter 5 to delete product by id.\n"
            "Enter 6 to exit : ")
    choice = input(strs)
    return int(choice)


if __name__ == "__main__":
    db_conn = create_connection(r"my_database.sqlite3")
    with db_conn:
        create_table(db_conn)
        print("Select option: ")
        while True:
            choice = menu()
            if choice == 1:
                print("To create a product enter: ")
                product_name = input("Product name: ")
                product_price = int(input("Product price: "))
                product_number = int(input("Product number: "))
                product_comment = input("Product comment if necessary: ")
                create_product(db_conn, product_name, product_price, product_number, product_comment)
            if choice == 2:
                select_all_products(db_conn)
            if choice == 3:
                product_name = input("Enter the product's name to select it's data: ")
                select_product(db_conn, product_name)
            if choice == 4:
                product_id = int(input("To update product enter it's id: "))
                product_name = input("Product name: ")
                product_price = int(input("Product price: "))
                product_number = int(input("Product number: "))
                product_comment = input("Product comment: ")
                update_product(db_conn, product_id, product_name, product_price, product_number, product_comment)
            if choice == 5:
                product_id = int(input("Enter the product id to delete it: "))
                delete_product(db_conn, product_id)
            if choice == 6:
                break
