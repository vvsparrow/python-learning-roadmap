# Задача 5
# Напишите функцию custom_print, которая будет принимать произвольное количество
#     аргументов args и kwargs и выводить их на экран в формате значение (args или
#     ключ=значение (kwargs), разделяя аргументы разделителем. Если передан
#         аргумент sep, он должен использоваться в качестве разделителя между
#         аргументами. Если передан аргумент end, он должен использоваться в
#         качестве символа окончания строки.
# Пример использования:
# custom_print(1, 2, 3, a=4, b=5, sep=’-’, end=’!’)
# # 1-2-3-a=4-b=5!
# custom_print(’Hello’, ’World’, sep=’ ’)
# # Hello World
# custom_print(’apple’, ’banana’, ’cherry’, sep=’, ’)
# # apple, banana, cherry
# custom_print(a=1, b=2, end=’...’)
# # a=1 b=2...


def custom_print(*args, **kwargs):
    sep = kwargs.pop("sep", " ")
    end = kwargs.pop("end", "\n")
    items = [str(x) for x in args] + [f"{k}={v}" for k, v in kwargs.items()]
    print(*items, sep=sep, end=end)


custom_print(1, 2, 3, a=4, b=5, sep="-", end="!")
