"""
Создать функцию, которая принимает на вход неопределенное
количество аргументов и возвращает их сумму и максимальное из них.
"""


def my_max(*args):
    args_sum = 0
    max_item = args[0]
    for value in args:
        args_sum += value
        if value > max_item:
            max_item = value
    return args_sum, max_item


print(my_max(1, 2, 3, 4, 5))

my_list = [1, 2, 3, 4, 5]
print(my_max(*my_list))
