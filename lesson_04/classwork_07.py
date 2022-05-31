""" Пользователь вводит с клавиатуры числа до тех пор, пока не
введет любой строчный символ, из этих чисел составляется первый
список. Далее таким же образом вводятся второй и третий списки.
Вывести на экран список, элементы которого есть в первых двух
списках, но отсутствуют в третьем. """

list_1 = []
list_2 = []
list_3 = []
result = []

# 1. Input lists

print("Enter numbers for the first list (enter any string to stop):")
while True:
    num_1 = input()
    if not num_1.isdigit():
        break
    list_1.append(num_1)

print("Enter numbers for the second list (enter any string to stop):")
while True:
    num_2 = input()
    if not num_2.isdigit():
        break
    list_2.append(num_2)

print("Enter numbers for the third list (enter any string to stop):")
while True:
    num_3 = input()
    if not num_3.isdigit():
        break
    list_3.append(num_3)

# 2. Find elements common in the first two lists

# first solution (for)
"""
for i in list_1:
    for j in list_2:
        if i == j:
            result.append(i)
            break
print(result)
"""

# second solution (list intersection)
result = list(set(list_1) & set(list_2))
print(result)

# 3. Find elements that are in the first two lists but not in third
result = list(set(result) - set(list_3))
print(result)


"""
is_digit = True
while is_digit:
    x = input()
    is_digit = x.isdigit()
"""

"""
for x in my_list_01:
    if x in my_list_02 and x not in my_list_03:
        print(x)
"""