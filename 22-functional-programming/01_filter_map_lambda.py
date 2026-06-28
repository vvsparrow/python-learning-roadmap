# Filter and uppercase product names

products = ["apple", "banana", "kiwi", "pineapple", "mango", "watermelon"]

filtered_and_upper = list(
    map(lambda x: x.upper(), filter(lambda x: len(x) > 5, products))
)


print(filtered_and_upper)
