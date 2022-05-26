""" Ввести с клавиатуры целое число n. Получить сумму кубов
всех целых чисел от 1 до n (включая n) используя цикл while. """

n = int(input())
x = 1
res = 0

while x <= n:
    res += x ** 3
    x += 1

print(res)

# the best solution
while n > 0:
    res += n ** 3
    n -= 1
