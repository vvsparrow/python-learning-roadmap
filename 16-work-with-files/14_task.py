# 14. функция, которая создаёт из информации в файле, организованной следующим образом:
# Имя Питомец Возраст_питомца
# Петя Кошка 5
# Ваня Черепашка 50
# Саша Капибара 1
# словарь и возвращает его. Словарь должен быть организован так:
# ["Петя": ("Кошка", 5), "Ваня": ("Черепашка", 50), "Саша": ("Капибара", 1)]


def pet_owners(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        result = {}
        for line in f:
            parts = line.split()
            if parts[2].isdigit():
                result[parts[0]] = (parts[1], int(parts[2]))
        return result


print(pet_owners("pets.txt"))
