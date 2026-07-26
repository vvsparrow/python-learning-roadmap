balance = int(input())
is_active = True

if not is_active:
    print("Account disabled.")
elif balance < 0:
    print("Negative balance. Please pay.")
elif balance == 0:
    print("Zero balance.")
else:
    print("Access granted.")
