# 12. функция, которая принимает на вход сначала имя первого файла, затем имя
#     второго файла, а после записывает содержимое из первого файла во второй
#     файл с помощью функции print().


def copy_file(file_r, file_w):
    with open(file_r, "r", encoding="utf-8") as f:
        with open(file_w, "w", encoding="utf-8") as g:
            for line in f:
                print(line.strip(), file=g)


copy_file("test_write_all.txt", "new_file.txt")
