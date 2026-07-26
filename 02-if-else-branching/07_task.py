# Задача 7
# На вход с клавиатуры подаются 4 числа: a, b, c и d.
# Даны два отрезка на числовой прямой [a, b] и [c, d],
# соответственно a ≤ b и c ≤ d. Напишите программу,
# которая считает количество целых точек,
# являющихся пересечением этих отрезков с учётом границ.
# В ответе запишите результат работы программы для
# a = 3, b = 13, c = 7 и d = 17


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))


# Находим границы пересечения
# start = max(a, c)
# end = min(b, d)

if a > c:
    start = a
else:
    start = b

if b < d:
    end = b
else:
    end = d

if start > end:
    print(end - start + 1)
else:
    print(0)
