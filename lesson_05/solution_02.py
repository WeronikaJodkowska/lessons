"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки
с именами участников. Затем каждый играющий по очереди вытягивает бумажку с именем того,
кому предстоит вручить презент. Ваша программа должна используя список имен участников выдать
на выходе пары, кто и кому будет дарить, причем сам себе человек не может подарить,
дубликаты тоже не допустимы.
"""


import random


def secret_santa(*names):
    names = list(names)
    pairs = {}
    while names:
        person_1 = random.choice(names)
        names.remove(person_1)
        person_2 = random.choice(names)
        names.remove(person_2)
        pairs[person_1] = person_2
    return pairs


print(secret_santa("Jane", "Alfred", "Sara", "Ann", "John", "Alex"))
