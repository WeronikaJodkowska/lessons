"""
6. Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты: day, month, year. “Исправить” все магические методы для этого класса.
7. Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

from __future__ import annotations
from classwork_02 import NewTime


class MyDateTime(NewTime):

    def __init__(self, year: int, month: int, day: int, hours: int, minutes: int, seconds: int):
        super().__init__(hours, minutes, seconds)
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def seconds_to_time(seconds: int) -> NewTime:
        year = seconds / 60 / 60 / 24 / 365.25
        day = seconds // (60 * 60 * 24)
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60

        return NewTime(hours=hours, minutes=minutes, seconds=seconds)

    def to_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

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
