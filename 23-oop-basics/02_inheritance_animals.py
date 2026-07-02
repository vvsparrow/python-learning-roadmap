# Task: Implement inheritance using animal, dog and cat classes.


class Animal:
    def eat(self):
        print("This animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


class Cat(Animal):
    def meow(self):
        print("Meow...")


# Testing inheritance.
my_dog = Dog()
my_dog.eat()
my_dog.bark()

my_cat = Cat()
my_cat.meow()
