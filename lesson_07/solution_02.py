"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих
странах. Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы,
которая считывает название города и выводит на печать страну.
"""


def get_country_by_city(city):
    list_of_countries = {
        "Belarus": ["Minsk", "Brest", "Grodno"],
        "Great Britain": ["London", "Cardiff", "Belfast"],
        "USA": ["New York", "Boston", "Chicago"]
    }
    for key, value in list_of_countries.items():
        if city in value:
            print(key)


def main():

    city = input("Enter a city: ")
    get_country_by_city(city)


if __name__ == "__main__":
    main()
