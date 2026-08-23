# 7. функция, которая возвращает строку без лишних пробелов, символов \n или \t
#    в конце;


def read_file_rstrip(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read().rstrip()


print(read_file_rstrip("input.txt"))
