""" Получить сумму кубов натуральных чисел от n до m
используя цикл for, числа n и m вводятся с клавиатуры. """

n = int(input())
m = int(input())
res = 0

for i in range(n, m):
    res += i ** 3

print(res)