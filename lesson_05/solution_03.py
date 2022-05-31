"""
Написать функцию, которая используя модуль requests скачивает файл, сохраняет его
на файловой системе, функция имеет два параметра: ссылка на файл и имя на файловой системе.
В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE
"""

import requests


def get_file(url, file_name):
    response = requests.get(url)
    open(file_name, "wb").write(response.content)


get_file("https://github.com/WeronikaJodkowska/lessons/blob/master/LICENSE",
         "/home/weronika/projects/lessons/lesson_05/LICENSE")
