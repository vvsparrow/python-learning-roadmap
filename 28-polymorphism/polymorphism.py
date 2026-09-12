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


class Triangle(Figure):
    def __init__(self, h, base) -> None:
        self.h = h
        self.base = base

    def area(self) -> float:
        return self.h * self.base * 0.5


if __name__ == "__main__":
    figures = [Square(5), Rectangle(3, 7), Triangle(10, 100)]
    for figure in figures:
        print(figure.area())
