n = int(input())

for i in range(10 ** (n - 1), 10**n):
    sum_dig = sum(int(dig) ** n for dig in str(i))
    if i == sum_dig:
        print(i, end=" ")
