# На вход с клавиатуры подаются 4 числа. Напишите программу,
# которая находит минимальное из них.
# В ответе запишите результат работы программы для чисел 12, 10, 5 и 21


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())

min_val = number_1

if number_2 < min_val:
    min_val = number_2

if number_3 < min_val:
    min_val = number_3

if number_4 < min_val:
    min_val = number_4


print(min_val)
