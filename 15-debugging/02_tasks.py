# Задача 2
# Следующий код должен находить сумму последовательности чисел от 1 до 10 и выводить ее на экран. Есть ли ошибки в этом коде?
# Если есть, укажите тип ошибки и саму ошибку из предложенных вариантов ответа.
# 1. Ошибок нет
# 2. SyntaxError: invalid syntax
# 3. NameError: name ‘summa‘ is not defined
# 4. TypeError: ‘int‘ object is not callable
# Исправьте ошибку, если потребуется.

summa = 0

for i in range(1, 11):
    summa += i
print("The sum is: ", summa)
