marks = {}
with open("input.txt", "r") as f:
    for line in f:
        L1 = line.split()
        name, age, mark = L1[0], L1[1], L1[2]
        if mark[0].isdigit():
            marks[name] = {}
            marks[name]["Возраст"] = age
            marks[name]["Оценка"] = mark
print(marks)

