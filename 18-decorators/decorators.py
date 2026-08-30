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
            if (i + j) % 100 == 0:
                k += 1

    return k


p = f(1000)
print(p)
