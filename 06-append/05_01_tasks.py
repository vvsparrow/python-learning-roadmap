# Задача 5
#
# Напишите программу, которая запрашивает у пользователя строку текста и
# добавляет каждое слово в список с помощью метода append. Затем программа
# находит самое часто встречающееся слово в списке и выводит его на экран. В
# ответе укажите результат работы программы для строки "cat cat dog cat dog dog
# cat cat dog dog cat" Для решения данного задания можно использовать метод
# split(). Если решите без него, то будет лучше, но при этом сложнее


line_of_text = input("Enter a line of text: ")
a_list_of_words = line_of_text.split()
words_list = []

for word in a_list_of_words:
    words_list.append(word)

max_count = 0
most_frequent_word = ""

for word in words_list:
    current_count = words_list.count(word)
    if current_count > max_count:
        max_count = current_count
        most_frequent_word = word


print(most_frequent_word)
