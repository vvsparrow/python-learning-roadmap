# функция, которая возвращает список всех строк из файла (без символов переноса
# строки);


def read_stripped_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


print(read_stripped_lines("input.txt"))
