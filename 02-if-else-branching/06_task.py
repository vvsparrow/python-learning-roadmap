# Задача 6
# На вход с клавиатуры подаются 3 числа. Напишите программу,
# которая определяет вид треугольника (разносторонний,
# равносторонний или вырожденный) с такими сторонами.
# В ответе укажите вид треугольника для чисел 10, 13 и 23


side_a = int(input())
side_b = int(input())
side_c = int(input())


if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
    print("This triangle doesn't exist.")

elif (
    side_a + side_b == side_c or side_a + side_c == side_b or side_b + side_c == side_a
):
    print("This triangle is degenerate.")

elif side_a == side_b == side_c:
    print("This triangle is equilateral.")

elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("This triangle is isosceles.")

else:
    print("This triangle is scalene.")
