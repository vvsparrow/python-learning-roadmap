# 8. функция, которая убирает все знаки «!», «?», «.» из конца строки;


def read_file_rstrip(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip().rstrip("!?."))


read_file_rstrip("input.txt")
