# Задача 2
# Напишите функцию, которая проверяет, находится ли число в заданном диапазоне.
# В ответе запишите результат работы функции для числа 7 в диапазоне [1, 9]


# def in_range(num, start, end):
#     return start <= num <= end
#
#
# print(in_range(7, 1, 9))


n = int(input())


def check_the_number(n):
    return n >= 0 and n % 2 == 0


print(check_the_number(n))
