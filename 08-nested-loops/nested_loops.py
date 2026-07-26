for n in range(1000):
    k = 0
    for x in range(n):
        if x % 7 == 0:
            k += 1
    if k % 10 == 0:
        print(n, k)
