# Задача 3
# На вход подается число n, затем последовательность из n чисел.
# Создайте массив, состоящий из чисел этой последовательности.
# В ответ запишите среднее арифметическое всех элементов массива для
# n = 5 и последовательности [2, 3, 1, 5, 10]


n = int(input())
an_array_of_numbers = []

for i in range(n):
    an_array_of_numbers.append(int(input()))
arithmetic_mean = sum(an_array_of_numbers) / n


print(
    f"The arithmetic mean of all elements in the array for {n} "
    f"and the sequence {an_array_of_numbers}: {arithmetic_mean}"
)
