# функция, которая возвращает все строки из файла, соединённые в одну строку
# через пробел, а не через символ \n;


def read_lines_joined(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return " ".join(f.read().splitlines())


print(read_lines_joined("input.txt"))
