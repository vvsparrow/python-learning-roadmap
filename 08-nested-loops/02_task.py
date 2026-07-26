# Задача 2
# Напишите программу, которая находит все «пифагоровы тройки» в заданном
# диапазоне чисел – натуральные решения уравнения x 2 + y 2 = k 2 , где x, y и k
# лежат в интервале от l до r включительно. В ответе напишите количество троек,
# удовлетворяющих условию, для l = 10, r = 50

start_range = int(input("Enter the start: "))
end_range = int(input("Enter the end: "))

count = 0
for x in range(start_range, end_range + 1):
    for y in range(start_range, end_range + 1):
        # Calculate the hypotenuse using the 0.5
        k = (x**2 + y**2) ** 0.5

        # Checking:
        # 1. k is an integer (the remainder when divided by 1 is 0)
        # 2. k is within our range
        if k % 1 == 0 and k <= end_range:
            count += 1

print(count)
