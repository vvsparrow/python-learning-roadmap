# Задача 3
# На вход с клавиатуры подаются два положительных числа К и N (К < N).
# Напишите программу, которая выводит сумму нечетных чисел от
# К до N включительно с помощью цикла while.
# В ответе запишите результат работы программы для чисел:
# K = 12345 N = 56789

the_sum_of_odd_num = 0
K = int(input())
N = int(input())

while the_sum_of_odd_num >= K and the_sum_of_odd_num <= N:
    if the_sum_of_odd_num % 2 != 0:
        the_sum_of_odd_num += 1


print(the_sum_of_odd_num)
