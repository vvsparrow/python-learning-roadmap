# Filter positive numbers and calculate factorials


def get_factorial(n):
    if n <= 1:  # Пофиксили базу, чтобы 0 и 1 возвращали 1
        return 1
    return n * get_factorial(n - 1)


nums = [3, -2, 5, 0, -1, 4]

results = list(map(get_factorial, filter(lambda x: x >= 0, nums)))


print(results)
