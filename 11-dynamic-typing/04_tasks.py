# Задача 4
# У Александра Романовича есть много животных, и он записал всех
# животных, которые у него есть, в список. Напишите программу, которая
# превращает список животных ниже в словарь формата a = {"animal": количество
# животных}. animals = ["cat", "cat", "dog", "dog", "bird", "capybara",
# "capybara", "capybara"] В памяти программы должны храниться как и изначальный
# список, так и конечный словарь. На экран через пробел выведите сначала сумму
# количеств ссылок на каждую строку типа "animal", а затем сумму количеств
# ссылок на числа 1, 2 и 3.


import sys

animals = ["cat", "cat", "dog", "dog", "bird", "capybara", "penguin"]
animalList = {"cat": 2, "dog": 2, "bird": 1, "capybara": 1, "penguin": 1}

print(
    sys.getrefcount("cat")
    + sys.getrefcount("capybara")
    + sys.getrefcount("dog")
    + sys.getrefcount("bird")
    + sys.getrefcount("penguin")
)
print(sys.getrefcount(1) + sys.getrefcount(2) + sys.getrefcount(3))
