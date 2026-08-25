# Задача 2
# Реализуйте функцию print_kwargs, которая принимает произвольное количество
# именованных аргументов и выводит их на экран в формате «ключ: значение».
# Пример использования:
# print_kwargs(name=’Alice’, age=25, country=’USA’)
# name: Alice
# age: 25 #
# country: USA


def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


print_kwargs(name="Alice", age=25, country="USA")
