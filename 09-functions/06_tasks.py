# Задача 6 На вход с клавиатуры подается положительное число N. Напишите
# программу, которая находит число Фибоначчи с индексом N (числа Фибоначчи
# считаются по формуле: F(n) = F(n-1) + F(n-2), F(1) = 0, F(2) = 1, F(3) = 1).
# Ответ укажите для N = 10


N = int(input())


def get_fibonacci_by_index(n):
    if n == 1:
        return 0
    if n in (2, 3):
        return 1
    a, b = 1, 1
    for _ in range(4, n + 1):
        a, b = b, a + b
    return b


print(get_fibonacci_by_index(N))
