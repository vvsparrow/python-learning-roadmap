# Задача 5

# Напишите программу, которая запрашивает у пользователя строку текста и
# добавляет каждое слово в список с помощью метода append. Затем программа
# находит самое часто встречающееся слово в списке и выводит его на экран. В
# ответе укажите результат работы программы для строки "cat cat dog cat dog dog
# cat cat dog dog cat" Для решения данного задания можно использовать метод
# split(). Если решите без него, то будет лучше, но при этом сложнее


text = input()
words = text.split()
max_word = ""
max_word_counter = 0
unique_words = list(set(words))
print(unique_words)

for unique_word in unique_words:
    n = 0
    for word in words:
        if word == unique_word:
            n += 1
    if n >= max_word_counter:
        max_word_counter = n
        max_word = unique_word


print(max_word)
