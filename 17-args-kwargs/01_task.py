# Задача 1
# Реализуйте функцию sum_numbers, которая принимает любое количество
# аргументов и возвращает их сумму.
# Пример использования:
# print(sum_numbers(1,2, 3))
# print(sum_numbers(10, 20, 30, 40)) # 100


def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 20, 30, 40))
