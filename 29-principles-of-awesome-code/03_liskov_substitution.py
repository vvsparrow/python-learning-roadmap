from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self) -> None:
        pass


class Square(Figure):
    def __init__(self, h) -> None:
        self.h = h

    def area(self) -> None:
        return self.h**2


class Rectangle(Figure):
    def __init__(self, h, w) -> None:
        self.h = h
        self.w = w

    def area(self) -> None:
        return self.h * self.w


if __name__ == "__main__":
    figures = [Square(5), Rectangle(3, 7)]

    for x in figures:
        print(x.area())
