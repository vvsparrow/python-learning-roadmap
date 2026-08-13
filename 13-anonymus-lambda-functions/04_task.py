# Задача 4
# Напишите программу, которая находит факториал числа. Для решения данной задачи
# воспользуйтесь функцией reduce модуля functools и лямбда функцией. В ответе
# напишите результат работы программы для числа 8.

from functools import reduce

n = 8
number_generator = range(1, n + 1)

factorial_of_number = reduce(lambda a, b: a * b, number_generator)

print(factorial_of_number)
