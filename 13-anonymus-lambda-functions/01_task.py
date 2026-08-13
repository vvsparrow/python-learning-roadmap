D = {"Женя": 89, "Вася": 100, "Марк": 71, "Мария": 79}
f = list(filter(lambda x: D[x] > 80, D))
print(f)
