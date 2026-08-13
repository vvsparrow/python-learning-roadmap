# Задача 6

# Напишите настоящий генератор, который возводит в квадрат целые числа от 1 до 5
# включительно. # Выведите элементы с индексами 0, 2 и 4, не используя циклы
# программы. В ответе укажите эти значения через пробел.

generator_numbers = (x**2 for x in range(1, 6))
val_0 = next(generator_numbers)
(next(generator_numbers))
val_2 = next(generator_numbers)
(next(generator_numbers))
val_4 = next(generator_numbers)

print(val_0, val_2, val_4)
