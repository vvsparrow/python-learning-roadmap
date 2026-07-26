limit = 10
divisor_sums = [0] * (limit + 1)

for divisor in range(1, limit + 1):
    for multiple in range(2 * divisor, limit + 1, divisor):
        divisor_sums[multiple] += divisor
        print(
            f"Делитель: {divisor}, Ячейка: {multiple}, Сумма в ней: {divisor_sums[multiple]}"
        )
