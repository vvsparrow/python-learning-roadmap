# Задача 2
# Ваш робот написал еще одну программу
#
# n = int(input())
# a = []
# for i in range(n):
#     a = a + [i] * i
# print(a)
#
# Что будет выведено в результате работы программы при вводе числа 3?


n = int(input())
a = []

for i in range(n):
    a = a + [i] * i
    print(a)


print(a)
