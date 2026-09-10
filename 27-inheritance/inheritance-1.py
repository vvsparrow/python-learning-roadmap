class Animal:
    _name = "Вася"


class Dog(Animal):
    def show_name(self) -> None:
        print(self._name)


if __name__ == "__main__":
    v = Dog()
    v.show_name()
