from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Figure):
    def __init__(self, h: float) -> None:
        self.h = h

    def area(self) -> float:
        return self.h**2


class Rectangle(Figure):
    def __init__(self, h: float, w: float) -> None:
        self.h = h
        self.w = w

    def area(self) -> float:
        return self.h * self.w


class AreaCalculator:
    def calculate_area(self, shape) -> None:
        return shape.area()


if __name__ == "__main__":
    figures = [Square(5), Rectangle(3, 7)]
    v = AreaCalculator()
    for figure in figures:
        print(v.calculate_area(figure))
