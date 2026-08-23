# функция, которая возвращает список всех строк из файла (включая символы
# переноса строки);


def read_all_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.readlines()


print(read_all_lines("input.txt"))
