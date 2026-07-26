# Задача 1
#
# Напишите программу которая запрашивает у пользователя два числа n и m и
# добавляет их в список с помощью метода append. Затем программа выводит на
# экран сумму этих чисел. В ответе укажите вывод массива, затем сумму
# добавленных чисел, для n = 12 и m = 34


n = int(input())
m = int(input())
list_of_nubmers = []

list_of_nubmers.append(n)
list_of_nubmers.append(m)

print(list_of_nubmers)
print(sum(list_of_nubmers))
