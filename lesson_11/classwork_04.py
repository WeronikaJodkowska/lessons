"""
7. Создать программу, позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры.
"""

import sqlite3


def select_user(firstname="", age=0):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
           SELECT *
           FROM user
           WHERE user.firstname = ? or age = ?;
           """,
            (firstname, age)
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":
    name_1 = input("Enter name: ")
    age_1 = int(input("Enter age: "))
    print(select_user(name_1, age_1))
