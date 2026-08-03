import copy

nested = [30, 40]
L = [10, 20, nested]
M = copy.deepcopy(L)

# Сравниваем адреса вложенных списков в hex
print(f"L nested: {hex(id(L[2]))}")
print(f"M nested: {hex(id(M[2]))}")

# Оператор 'is' вернет False, так как это разные объекты в памяти
print(f"Independent? {L[2] is not M[2]}")
