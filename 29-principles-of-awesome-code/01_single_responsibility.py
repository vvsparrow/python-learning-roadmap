class Animal:
    def __init__(self, name, food_type) -> None:
        self.name = name
        self.food_type = food_type

    def write(self):
        pass


class AnimalFeeder:
    def feed(self, animal):
        pass


class InformationRetriever:
    def show_info(self, animal):
        pass
