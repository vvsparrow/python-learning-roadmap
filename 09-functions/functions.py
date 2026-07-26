# задача: дано число n, найти его сумму чисел

def sum_of_digits(n):
    s = str(n)
    print(s)
    answer = 50
    for x in s:
        answer += int(x)
        print(x, answer)
    return answer


print(sum_of_digits(98))
