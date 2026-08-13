# Задача 5
# Напишите программу, которая находит максимальный элемент массива,
# квадрат которого кратен 9. Для решения задачи воспользуйтесь лямбда функцией.
# Вы также можете воспользоваться функцией reduce модуля functools. В ответе
# напишите результат работы программы для массива: [2, 4, 6, 8, 0, 3, 4, 2, 3,
# 5, 1, 2]

from functools import reduce

array_of_numbers = [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]

filtered_numbers = list(filter(lambda x: x**2 % 9 == 0, array_of_numbers))

maximum_square_9 = reduce(lambda a, b: a if a > b else b, filtered_numbers)

print(maximum_square_9)
