"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости (
скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задний ход (
изменение знака скорости).
"""


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5
        print(f"Car speed increased by 5.")

    def decrease_speed(self):
        self.speed -= 5
        print(f"Car speed decreased by 5.")

    def stop_speed(self):
        self.speed = 0
        print(f"Car speed reset to 0.")

    def get_speed(self):
        print(f"Car speed: {self.speed}")

    def back_speed(self):
        self.speed = -self.speed
        print(f"Car reverse.")


if __name__ == "__main__":
    car = Car(brand="Volkswagen", model="Golf", year=1999)
    car.get_speed()
    car.increase_speed()
    car.increase_speed()
    car.get_speed()
    car.decrease_speed()
    car.get_speed()
    car.back_speed()
    car.get_speed()
    car.stop_speed()
    car.get_speed()
