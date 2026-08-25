# Задача 3
# Создайте функцию filter_by_length, которая будет принимать список строк и
# дополнительный аргумент min_length. Функция должна использовать kwargs для
# передачи списка строк переменной длины и args для передачи значения
# min_length. Функция должна вернуть новый список, содержащий только те строки,
# длина которых больше или равна min_length
# Пример использования:
# strings = ["hello", "world", "how", "are", "you"]
# print(filter_by_length(4, *strings))
# [’hello’, ’world’] print(filter_by_length(3, *strings))
# [’hello’, ’world’, ’you’]


def filter_by_length(min_length, *args):
    return [s for s in args if len(s) >= min_length]


# def filter_by_length(min_length, *args):
#     result = []
#     for s in args:
#         if len(s) >= min_length:
#             result.append(s)
#     return result


strings = ["hello", "world", "how", "are", "you"]

print(filter_by_length(4, *strings))
