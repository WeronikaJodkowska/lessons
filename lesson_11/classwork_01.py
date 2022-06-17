"""
3. Создать python функцию, которая создает таблицу user, для примера использовать слайд №12. Запустить функцию и
проверить, что создался файл базы данных.
"""

import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


if __name__ == "__main__":
    create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
    create_user("Weronika", "Jodkowska", "w.j@gmail.com", "TestPass1", 23)
    create_user("Jane", "Doe", "jane.doe@gmail.com", "TestPass2", 27)
    create_user("John", "Doe", "john.doe@gmail.com", "TestPass3", 30)
    create_user("Sam", "Smith", "sam.smith@gmail.com", "TestPass4", 21)
