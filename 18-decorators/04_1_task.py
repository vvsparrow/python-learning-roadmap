# Задача 4
# Создайте декоратор retry, который позволяет повторить выполнение функции, если
# она вернула None. Декоратор должен автоматически повторить выполнение
# указанное количество раз с задержкой между попытками.

import time


def retry(func):
    def inside_func(*args, **kwargs):
        for _ in range(3):
            result = func(*args, **kwargs)
            if result is not None:
                return result
            time.sleep(3)

    return inside_func


attempts = 0


@retry
def get_data():
    global attempts
    attempts += 1
    print(f"Attempt number: {attempts}")

    if attempts < 3:
        print("Communication error; returned None...")
        return None

    return "Success! Data received."


result = get_data()
print(result)
