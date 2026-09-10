class Animal:
    name = "Вася"

    def __init__(self, name: str) -> None:
        print("__init__ from animals")
        self.name = name

    def pet(self) -> None:
        print(f"Petting an animal {self.name}...")


class Goods:
    price = 100
    name = "Orphan"

    def __init__(self, price: int) -> None:
        print("__init__ from goods")
        self.price = price

    def sell(self):
        print(f"Steps to follow when selling goods {self.name}")


class Fish(Animal, Goods):
    def __init__(self, name: str, price: int) -> None:
        Animal.__init__(self, name)
        Goods.__init__(self, price)
        print("The inits from the Animal and Goods classes have been processed")

    def pet(self) -> None:
        print(f"Petting a fish {self.name}...")
        print("Standard procedures for any fish...")


if __name__ == "__main__":
    v = Fish("Jack", 100)
    print(v.__dict__)
