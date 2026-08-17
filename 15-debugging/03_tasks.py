# Задача 3
# Следующий код должен проверять, является ли число четным, и выводить на экран соответствующее сообщение. Есть ли ошибки в этом коде?
# Если есть, укажите тип ошибки и саму ошибку из предложенных вариантов ответа.
# 1. Ошибок нет
# 2. NameError: name ‘n‘ is not defined
# 3. TypeError: not all arguments converted during string formatting
# 4. IndentationError: unexpected indent
# Исправьте ошибку, если потребуется. 

def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
is_even('4')
