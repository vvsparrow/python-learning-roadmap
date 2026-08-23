# 9. функция, которая записывает в файл строку, которая подаётся в качестве аргумента;


def write_to_file(file_name, text):
    with open(file_name, "w", encoding="utf-8") as f:
        return f.write(text)


write_to_file("test_write.txt", "Привет текстовый файл на запись!")
