a = [-20, -30, 25, 40, 9, 28, -40, -17, -25]
maximum = -1000000000000000000000

for x in a:
    if x % 3 == 0:
        if x > maximum:
            maximum = x

print(maximum)
