# 1. Найти значение выражений:
x_1 = 17 / 2 * 3 + 2
x_2 = 2 + 17 / 2 * 3
x_3 = 19 % 4 + 15 / 2 * 3
x_4 = (15 + 6) - 10 * 4
x_5 = 17 / 2 % 2 * 3

print(x_1, x_2, x_3, x_4, x_5)

# 2. Расставить скобки так, чтобы значение выражений поменялось.

x_1 = 17 / 2 * (3 + 2)
x_2 = (2 + 17) / 2 * 3
x_3 = 19 % (4 + 15) / 2 * 3
x_4 = ((15 + 6) - 10) * 4
x_5 = 17 / 2 % (2 * 3)

print(x_1, x_2, x_3, x_4, x_5)

# 3. Создать три переменные, содержащие возраст трех ваших друзей, в качестве имен переменных использовать имена друзей, найти сумму и вывести ее на экран.

alex_age = 29
jade_age = 18
ivan_age = 25
age_overall = alex_age + jade_age + ivan_age

print(age_overall)

# 4. Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.

average = age_overall / 3

print(average)

# 5. Найти в списке ниже количество не уникальных элементов: my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]'

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
my_set = set(my_list)
print(len(my_list) - len(my_set))

# 6. Взять список из предыдущей задачи, извлечь элементы со 2-го по 4-й включительно и вывести их в обратном порядке.

print(my_list[2:5][::1])

# 7. Создать переменную содержащую сторону квадрата, создать новый список, в котором будут периметр квадрата, площадь квадрата и диагональ квадрата.

length = 5
square_list = [length * 4, length ** 2, (2 * length ** 2) ** (0.5)]
print(square_list)

