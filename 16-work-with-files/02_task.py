# функция, которая возвращает первую строку из файла;


def read_first_line(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.readline()


print(read_first_line("input.txt"))
