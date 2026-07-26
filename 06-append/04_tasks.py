# Задача 4
#
# Напишите программу, которая запрашивает у пользователя число n и добавляет в
# список все числа от 1 до n включительно, которые делятся на 3 или на 5, с
# помощью метода append. Затем программа находит сумму всех чисел в списке и
# выводит ее на экран. В ответе укажите результат работы программы для n = 1000.


the_number_n = int(input("Enter the number n: "))
list_of_numbers = []

for number in range(1, the_number_n + 1):
    if number % 3 == 0 or number % 5 == 0:
        list_of_numbers.append(number)


print(sum(list_of_numbers))
