"""
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное, в идеале не использовать библиотечные функции.
"""


import re


# def often_and_len(text):
#     wordList = re.sub("[^\w]", " ", text).split()
#     print(wordList)
#     return max(wordList, key=len)


def longest_word(text):
    word_list = re.sub("[^\w]", " ", text).split()
    longest = 0
    word = word_list[0]
    for i in range(len(word_list)):
        if len(word_list[i]) > longest:
            longest = len(word_list[i])
            word = word_list[i]
    return word


def most_common_word(text):
    word_list = re.sub("[^\w]", " ", text.lower()).split()
    counter = 0
    most_common = word_list[0]
    for word in word_list:
        current_frequency = word_list.count(word)
        if current_frequency > counter:
            counter = current_frequency
            most_common = word
    return most_common


my_text = "Always dream and shoot higher than you know you can do. Do not bother just to be better than your " \
          "contemporaries or predecessors. Try to be better than yourself. "

print(longest_word(my_text))
print(most_common_word(my_text))
