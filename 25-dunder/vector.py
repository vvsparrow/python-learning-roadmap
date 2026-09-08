import math
from typing import Any, Self


class MyVector:
    def __init__(self, name: str, *args: int | float) -> None:
        self.name = name
        self.coords = args

    def __len__(self) -> int:
        squared_sum = sum(map(lambda x: x**2, self.coords))
        return int(math.sqrt(squared_sum))

    def __abs__(self) -> tuple[int | float, ...]:
        return tuple(map(abs, self.coords))

    def __add__(self, other: "MyVector") -> Self:
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors of different lengths")

        new_coords = []
        for i in range(len(self.coords)):
            new_coords.append(self.coords[i] + other.coords[i])
        new_name = f"{self.name}+{other.name}"
        return self.__class__(new_name, *new_coords)

    def __mul__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise ValueError("I can only multiply by whole numbers")
        new_coords = list(map(lambda x: x * other, self.coords))
        return self.__class__(self.name, *new_coords)

    def __imul__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise ValueError("I can only multiply by whole numbers")
        new_coords = tuple(map(lambda x: x * other, self.coords))
        self.coords = new_coords
        return self

    def __getattribute__(self, item: str) -> Any:
        print(f"__getattribute__ called on {item}")
        if item == "name":
            print("Access to this name is prohibited!")
            return None
        return object.__getattribute__(self, item)

    def __getattr__(self, item: str) -> Any:
        print(f"Sorry, this object {item} has no attributes")
        return None

    def __setattr__(self, key: str, value: Any) -> None:
        print(f"__setattr__ called on {key}: {value}")
        object.__setattr__(self, key, value)


if __name__ == "__main__":
    p = MyVector("Вася", 10, 20, -30)
