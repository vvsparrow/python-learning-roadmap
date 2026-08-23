# функция, которая возвращает всё содержимое файла в виде строки;


def file_contents(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


print(file_contents("input.txt"))
