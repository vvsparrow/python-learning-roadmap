# Задача 5
# Напишите программу, которая выводит все различные цифры,
# встречающиеся в исходной строке, в порядке возрастания. Если в строке нет
# цифр, то вывести "NO". В ответе запишите результат программы для строки:
# "kn1mb9c7c5cv5cc9cvv7cx9sd8nm4cz2bm4k6hf9d"


s = input()
digits = set()

for char in s:
    if char.isdigit():
        digits.add(int(char))

if digits:
    print(*sorted(digits))
else:
    print("No digits")
