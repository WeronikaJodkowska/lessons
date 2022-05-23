# 2. Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Рассчитать сумму на счету пользователя по окончании вклада и вывести на печать, если в конце каждого года ему начисляется бонус в размере 120 рублей.

# First (simple) solution

deposit = 2130
percent = 0.1
bonus = 120

year_1 = deposit + deposit * percent + bonus
year_2 = year_1 + year_1 * percent + bonus
year_3 = year_2 + year_2 * percent + bonus
year_4 = year_3 + year_3 * percent + bonus
year_5 = year_4 + year_4 * percent + bonus

print("Amount at the end of the deposit:", year_5)

# Second solution (with range)

for i in range(5):
    deposit += deposit * percent + bonus

print("Amount at the end of the deposit:", deposit)
