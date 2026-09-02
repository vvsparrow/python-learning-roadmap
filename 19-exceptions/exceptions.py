L1 = [10, 20, 30]
try:
    x = int(input())
    print(1 / x)
    print(L1[x])
except Exception as name_of_exception:
    print(f"Произошло исключение: {name_of_exception}")
