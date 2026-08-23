# функция, которая построчно выводит все строки в файле, итерируя по самому
# файлу (строки должны быть разделены одним символом \n);


def print_all_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


print_all_lines("input.txt")
