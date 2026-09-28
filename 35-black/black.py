def func(
    first_long_argument=1000,
    second_long_argument=100,
    third_long_argument=10,
    fourth_long_argument=100,
):
    s = 0
    for x, y in zip(
        range(first_long_argument, third_long_argument),
        range(
            second_long_argument if isinstance(second_long_argument, int) else 0,
            fourth_long_argument,
        ),
        strict=True,
    ):
        s += x * y
    return s


print(
    func(
        first_long_argument=1,
        third_long_argument=5,
        second_long_argument=10,
        fourth_long_argument=14,
    )
)
