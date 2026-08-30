# Задача 1
# Напишите декоратор timer, который измеряет время выполнения функции и
# выводит результат на экран. Протестируйте декоратор на нескольких функциях
# разной сложности.
import time


def timer(func):
    def inside_func(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        fin = time.time()
        print(f"Функция {func.__name__} поработала {fin - st} сек.")
        return result

    return inside_func


@timer
def f(x):
    k = 0
    for i in range(x):
        for j in range(x):
            if (i + j) % 100_000 == 0:
                k += 1


f(1000)


@timer
def addition_of_numbers(a, b):
    return a + b


print(addition_of_numbers(10, 20))
