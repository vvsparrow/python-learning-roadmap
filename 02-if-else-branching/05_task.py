# Задача 5
# На вход с клавиатуры подаются 3 числа. Напишите программу,
# которая определяет, что треугольник с такими сторонами существует.
# Если такой треугольник существует - вывести ’True’,
# если нет - ’False’. Ответ запишите для чисел: 13, 19 и 15


side_a = int(input())
side_b = int(input())
side_c = int(input())

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("True")
else:
    print("False")
