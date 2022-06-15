"""
1. Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), Triangle (атрибуты:
три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и
периметра). При потребности создавать все необходимые методы не описанные в задании.
2. Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

from __future__ import annotations
from math import pi, sqrt, pow


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Figure:
    def get_perimeter(self):
        raise NotImplementedError(
            'Определите get_perimeter в %s.' % self.__class__.__name__)

    def get_area(self):
        raise NotImplementedError(
            'Определите get_area в %s.' % self.__class__.__name__)


class Circle(Figure):
    def __init__(self, center: Point = Point(0, 0), radius: int = 0):
        self.center = center
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * pow(self.radius, 2)


class Triangle(Figure):
    def __init__(self, a: Point = Point(0, 0), b: Point = Point(0, 0), c: Point = Point(0, 0)):
        self.a = a
        self.b = b
        self.c = c
        self.ab = sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2))
        self.ac = sqrt(pow(c.x - a.x, 2) + pow(c.y - a.y, 2))
        self.bc = sqrt(pow(c.x - b.x, 2) + pow(c.y - b.y, 2))

    def get_perimeter(self):
        return self.ab + self.ac + self.bc

    def get_area(self):
        p_half = (self.ab + self.ac + self.bc) / 2
        return sqrt(p_half * (p_half - self.ab) * (p_half - self.ac) * (p_half - self.bc))


class Square(Figure):
    def __init__(self, point_1: Point = Point(0, 0), point_2: Point = Point(0, 0)):
        self.point_1 = point_1
        self.point_2 = point_2
        self.d = sqrt(point_2.x - point_1.x) + sqrt(point_2.y - point_1.y)

    def get_perimeter(self):
        return self.d * 2 * sqrt(2)

    def get_area(self):
        return pow(self.d, 2) / 2


# 2. Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
if __name__ == "__main__":
    figures = [Circle(center=Point(1, 1), radius=7),
               Triangle(a=Point(-1, -3), b=Point(3, 4), c=Point(5, -5)),
               Square(point_1=Point(4, 3), point_2=Point(10, 9))]
    for figure in figures:
        print(f"Area of the {figure.__class__.__name__}: {figure.get_area()}")
