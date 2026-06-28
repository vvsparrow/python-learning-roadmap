# Calculate factorial using recursion


def get_factorial(n):
    if n == 1:
        return 1
    return n * get_factorial(n - 1)


print(get_factorial(5))
