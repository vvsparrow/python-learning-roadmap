# Задача 2
# Напишите декоратор cache, который кэширует результаты выполнения функции и
# возвращает сохраненное значение при повторном вызове функции с теми же
# аргументами. При вызове функции с новыми аргументами декоратор должен
# пересчитать результат и сохранить его в кэше.


def my_cache(func):
    result = dict()

    def inside_func(*args):
        if args not in result:
            result[args] = func(*args)
        return result[args]

    return inside_func


@my_cache
def f(x):
    if x <= 1:
        return 1
    else:
        return f(x - 1) + f(x - 2)


for n in range(100):
    print(n, f(n))
