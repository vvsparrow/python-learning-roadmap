# 10. функция, которая записывает в файл строку, которая подаётся в качестве
#     аргумента, и дополнительный символ переноса на следующую строку;


def write_line(file_name, text):
    with open(file_name, "w", encoding="utf-8") as f:
        return f.write(f"{text}\n")


write_line(
    "test_write_plus.txt",
    "Сколько было негритят? 12",
)
