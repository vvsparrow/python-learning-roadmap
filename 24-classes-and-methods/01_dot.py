class Dot:
    """Класс  для предоставления точек на координатной плоскости"""

    shape = "square"
    color = "green"

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def change_coords(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def view_coords(self) -> tuple[float, float]:
        return (self.x, self.y)

    def __del__(self) -> None:
        print("Вызов __del__, удалили объект", str(self))


if __name__ == "__main__":
    p = Dot(8.4, 2.1)
    q = Dot(8.4, 2.1)
    print("hello world")
