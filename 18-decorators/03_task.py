# Задача 3
# Реализуйте декоратор logging, который будет записывать вызовы функции с
# аргументами в лог-файл.


def my_logging(func):
    def inside_func(*args, **kwargs):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(
                f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}\n"
            )
        return func(*args, **kwargs)

    return inside_func


@my_logging
def summation(x, y):
    return x + y


result = summation(12, 36)
print(result)
