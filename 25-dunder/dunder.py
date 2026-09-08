class Dog:
    element = None

    def __new__(cls, *args, **kwargs):
        if not cls.element:
            cls.element = object.__new__(cls)
            cls.element.initialized = False
            print("Выполнение ужасной страшной работы")
        return cls.element

    def __init__(self, name) -> None:
        if not self.initialized:
            self.name = name
            self.initialized = True


d = Dog("Жучка")
p = Dog("Джек")
print(d)
print(p)
print(d.name)
print(p.name)

# SINGLETON
