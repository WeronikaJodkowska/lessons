"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), Triangle (атрибуты:
три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и
периметра). При потребности создавать все необходимые методы не описанные в задании.
"""

from __future__ import annotations
from math import pi, sqrt


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, center: Point = Point(0, 0), radius: int = 0) -> None:
        self.center = center
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self) -> float:
        return pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a: Point = Point(0, 0), b: Point = Point(0, 0), c: Point = Point(0, 0)) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        pass

    def get_area(self) -> float:
        pass


if __name__ == "__main__":
    figures = [Circle(center=Point(1, 1), radius=7)]
    for i in figures:
        print(i.get_area())
