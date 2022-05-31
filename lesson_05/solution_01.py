"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных, но
только если они не равны None. Получим, например, следующее сообщение:
Переданы аргументы: var1 = 2, var3 = 10.
"""


def three_args(var1=None, var2=None, var3=None):
    result = ""
    for key, value in locals().items():
        if value:
            result += f"{key} = {value} "
    print(f"Переданы аргументы: {result}")


three_args(var1=7)
three_args(var2=9, var3="Python")
three_args(var3='Python', var2=12, var1=4)
