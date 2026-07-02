# Task: Implement polymorphism using a list of different animals.


class Animal:
    def feed(self):
        print("Feeding an unknown animal.")


class Dog(Animal):
    def feed(self):
        print("The dog is eating meat.")


class Cat(Animal):
    def feed(self):
        print("The cat is eating fish.")


# Testing polymorphism.
animals = [Dog(), Cat()]

for animal in animals:
    animal.feed()
