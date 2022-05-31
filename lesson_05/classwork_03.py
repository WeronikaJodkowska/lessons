"""
Написать функцию принимающая на вход неопределенным количеством
аргументов и именованный аргумент func_type. В зависимости от
func_type вернуть минимальное либо максимальное значение.
Написать программу в виде трех функций.
"""


def my_max(*args):
    args_sum = 0
    max_item = args[0]
    for value in args:
        args_sum += value
        if value > max_item:
            max_item = value
    return args_sum, max_item


def my_min(*args):
    args_sum = 0
    min_item = args[0]
    for value in args:
        args_sum += value
        if value < min_item:
            min_item = value
    return args_sum, min_item


def min_or_max(func_type, *args):
    if func_type == "min":
        result = my_min(*args)
    else:
        result = my_max(*args)
    return result


my_list = [1, 2, 3, 4, 5]
print(min_or_max("min", *my_list))
print(min_or_max("max", *my_list))
