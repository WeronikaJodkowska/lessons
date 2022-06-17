"""
3. Создать генератор простой геометрической прогрессии.
"""


class GeoIterator:
    def __init__(self, power, limit):
        self.power = power
        self.limit = limit
        self.current_value = 0

    def __next__(self):
        previous_value = self.current_value
        if self.current_value <= self.limit:
            self.current_value *= self.power
            return previous_value
        else:
            raise StopIteration

    def __iter__(self):
        self.current_value = 1
        return self


if __name__ == "__main__":
    my_geo = GeoIterator(power=2, limit=16)
    for item in my_geo:
        print(item)
    # while True:
    #     try:
    #         print(next(my_geo))
    #     except StopIteration:
    #         break
