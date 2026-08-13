# Задача 1
# Ваш робот написал очередную программу:
a = [2, 4, 6, 8]
b = [1, 3, 5, 7]
a_itera = iter(a)
b_iterb = iter(b)
next(iter(a_itera))
print(next(iter(a_itera)), next(iter(b_iterb)))
next(iter(b_iterb))
print(next(iter(b_iterb)), next(iter(a_itera)))
# В ответе запишите результат работы программы
