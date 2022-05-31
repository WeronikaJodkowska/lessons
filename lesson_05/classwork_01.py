"""
Написать функцию, которая получает на вход имя и выводит строку
вида: f"Hello, {name}". Создать список из 5 имен. Вызвать функцию
для каждого элемента списка в цикле.
"""


def my_function(name):
    print(f"Hello, {name}")


names = ["Weronika", "Alex", "Jessi", "James", "Anna"]

for i in names:
    my_function(i)
