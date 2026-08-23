# 11. функция, которая записывает в файл все строки из списка, который подаётся
#     в качестве аргумента;


def write_all(file_name, lines):
    with open(file_name, "w", encoding="utf-8") as f:
        return f.write("\n".join(lines))


write_all(
    "test_write_all.txt",
    [
        "One line",
        "Two line",
        "Tree line",
    ],
)
