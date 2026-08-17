# Задача 5
# Программа должна проверять, является ли строка палиндромом, но она
# возвращает неправильный результат или выдает ошибку. Необходимо найти и
# исправить ошибку в функции, используя отладчик debugger, чтобы она правильно
# проверяла, является ли строка палиндромом.


def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


print(is_palindrome("sator arepo tenet opera rotas"))
