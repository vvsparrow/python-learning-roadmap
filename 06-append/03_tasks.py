# Задача 3
#
# Напишите программу, которая запрашивает у пользователя строку текста,
# разбивает ее на слова и добавляет каждое слово в массив с помощью метода
# append. Затем программа находит самое длинное слово в массиве и выводит его. В
# ответе укажите результата работы программы для строки "Вот Вотяков нетипичный
# учитель"


text_data = input("Enter a line of text: ")
words = text_data.split()
list_of_words = []

for word in words:
    list_of_words.append(word)

max_word = ""
for word in list_of_words:
    if len(word) >= len(max_word):
        max_word = word
print(max_word)
