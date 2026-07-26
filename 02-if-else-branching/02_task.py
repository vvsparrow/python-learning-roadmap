# Задача 2
# Вы создаёте сайт с авторизацией и Вам нужно, чтобы у пользователя были логин и пароль.
# Для безопасности Вы запрашиваете ввод пароля два раза. Напишите программу,
# которая будет проверять пароль и его подтверждение на совпадение.
# Если всё в порядке - вывести ’True’, если нет - ’False’.
# В ответе запишите результат работы для пароля:
# 8b66bBT67-NVbds8_23dlsa-02EcxjKseQ и его подтверждения:
# 8b66bBT67-NVbds8_23dIsa-02EcxjKseQ


password = "8b66bBT67-NVbds8_23dlsa-02EcxjKseQ"
password_verification = "8b66bBT67-NVbds8_23dIsa-02EcxjKseQ"

result = "True" if password == password_verification else "False"


print(result)
