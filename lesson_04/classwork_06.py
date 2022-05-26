""" Вывести в порядке возрастания все простые числа, расположенные
между n и m (включая сами числа n и m), а также количество x этих чисел. """

n = int(input())
m = int(input())
# number of prime numbers
x = 0

for i in range(n, m + 1):
    # prime numbers are greater than 1
    if i > 1:
        # so we start with 2 and up to the number itself, not including it
        for n in range(2, i):
            # is divisible by anything other than 1 and itself
            if i % n == 0:
                # else not executed (number is not printed)
                break
        # cycle passed without break
        else:
            print(i, "is a prime number!")
            # increase the number of prime numbers
            x += 1

print("Number of primes:", x)
