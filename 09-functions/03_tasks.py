# Задача 3 Напишите функцию, которая проверяет, является ли число совершенным
# (совершенное число - это положительное число, которое равно сумме его
# положительных делителей, исключая само число. Первое совершенное число - 6,
# сумма делителей 1 + 2 + 3 = 6) и выводит булевое значение (True - если число
# совершенное, False - если нет). В ответе укажите значение, которое выдает
# функция для числа 8128

# 1. Define a function that takes n
# 2. Check if n is positive
# 3. Create a variable to store the sum
# 4. Loop from 1 to n-1
# 5. If n is divisible by i, add i to sum
# 6. Return True if sum equals n


def perfect_num(n):
    if 0 >= n:
        return False
    count = 0

    for i in range(1, n):
        if n % i == 0:
            count += i
    return count == n


print(perfect_num(8128))
