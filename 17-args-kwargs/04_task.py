# Задача 4
# Реализуйте функцию calculate_total_price, которая принимает на вход стоимость
# товара и произвольное количество ключевых аргументов, где каждый ключ
# представляет собой тип скидки, а значение — размер скидки в процентах. Функция
# должна вернуть общую стоимость товара после применения скидок.
# Пример использования:
# print(calculate_total_price(100, student=10, coupon=20)) # 70.0
# print(calculate_total_price(200, holiday=25)) # 150.0
# print(calculate_total_price(500)) # 500.0


def calculate_total_price(cost, **kwargs):
    discounts = sum(kwargs.values())
    return cost * (1 - discounts / 100)


print(calculate_total_price(100, student=10, coupon=20))
print(calculate_total_price(200, holiday=25))
print(calculate_total_price(500))
