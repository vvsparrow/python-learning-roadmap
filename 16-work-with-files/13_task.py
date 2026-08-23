# 13. функция, которая принимает на вход сначала имя первого файла, затем имя
#     второго файла, а после записывает во второй файл все строки, которые
#     начинаются с подстроки , а заканчиваются на подстроку . Используйте методы
#     .startswith() и .endswith().


def successful_tests(file_r, file_w, prefix, suffix):
    with open(file_r, "r", encoding="utf-8") as f:
        with open(file_w, "w", encoding="utf-8") as g:
            for line in f:
                clean_line = line.strip()
                if clean_line.startswith(prefix) and clean_line.endswith(suffix):
                    print(line.strip(), file=g)


successful_tests("input_filter.txt", "ok.txt", "[OK]", "!")
