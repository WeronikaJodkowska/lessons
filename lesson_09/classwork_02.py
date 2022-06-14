"""
2. Переопределить магические методы сложения, вычитания, умножения на число.
3. Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
4. Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
5. Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут, вывести на печать результат.
"""

from __future__ import annotations
from classwork_01 import MyTime


class NewTime(MyTime):

    @staticmethod
    def seconds_to_time(seconds: int) -> NewTime:
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60

        return NewTime(hours=hours, minutes=minutes, seconds=seconds)

    def __add__(self, other: NewTime) -> NewTime:
        seconds = self.to_seconds() + other.to_seconds()
        return NewTime.seconds_to_time(seconds)

    def __sub__(self, other: NewTime) -> NewTime:
        seconds = self.to_seconds() - other.to_seconds()
        return NewTime.seconds_to_time(seconds)

    def __mul__(self, other: int) -> NewTime:
        seconds = self.to_seconds() * other
        return NewTime.seconds_to_time(seconds)

    # 3. Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes}:{self.seconds}"


if __name__ == "__main__":
    a = NewTime(hours=3, minutes=30, seconds=30)
    b = NewTime(hours=3, minutes=30, seconds=30)
    print("a + b:", a + b)
    print("a - b:", a - b)
    print("a * 7:", a * 7)

    # 4. Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
    task_4 = NewTime(hours=21, minutes=20, seconds=35)
    print("task_4 * 2: ", task_4 * 2)

    # 5. Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут,
    # вывести на печать результат.
    task_5 = NewTime(hours=7, minutes=14, seconds=21)
    new_task_5 = NewTime(hours=7, minutes=45, seconds=0)
    res_5 = task_4 - task_5
    print("task_5:", res_5 + new_task_5)
