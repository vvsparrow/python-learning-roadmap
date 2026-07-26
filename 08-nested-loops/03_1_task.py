# Задача 3
# Два различных натуральных числа называются дружественными, если
# первое из них равно сумме делителей второго числа, за исключением самого
# второго числа, а второе равно сумме делителей первого числа, за исключением
# самого первого числа. Напишите программу, которая находит все пары натуральных
# дружественных чисел (не равных друг другу). Оба числа пары должны быть меньше,
# чем введенное с клавиатуры число N. В ответе запишите результат работы для N =
# 300.
# Замечание: перестановка не считать разными парами. Например, 18 13 и 13 18 -
# одна и та же пара


limit = int(input("Enter a number N: "))

# 1. Calculate the sum of divisors for all numbers at once (an efficient method)
# Create a list of zeros of size N + 1
divisor_sums = [0] * (limit + 1)

for divisor in range(1, limit + 1):
    for multiple in range(2 * divisor, limit + 1, divisor):
        divisor_sums[multiple] += divisor

# 2. Looking for pairs
for x in range(1, limit + 1):
    y = divisor_sums[x]

    # Conditions for friendship:
    # 1. The sum of y's divisors must equal x
    # 2. x is not equal to y (by definition)
    # 3. y must be within our range (<= limit)
    # 4. x < y (to avoid printing the same pair twice: 220-284 and 284-220)
    if x < y <= limit and divisor_sums[y] == x:
        print(f"A friendly pair: {x} {y}")
