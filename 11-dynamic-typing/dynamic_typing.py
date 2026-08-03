import copy

# Industrial standard recursive type alias (Python 3.12+, PEP 695)
type SaladItem = str | list["SaladItem"]

recursive_salad: list["SaladItem"] = ["Огурцы", "Помидоры"]
recursive_salad.append(recursive_salad)
b = copy.deepcopy(recursive_salad)
print(b)
recursive_salad[0] = "Перец"
print(b)
print(recursive_salad)
