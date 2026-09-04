class My_Date:
    total_number_of_dates = 0

    def __init__(self, S1="01.01.1900") -> None:
        day, month, year = S1.split(".")
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.increase_total()

    @classmethod
    def increase_total(cls):
        cls.total_number_of_dates += 1

    def is_AR_birthday(self):
        if self.day == 12 and self.month == 8 and self.year == 1993:
            return True
        else:
            return False

    def set_data(self, S1="01.01.1900") -> None:
        day, month, year = S1.split(".")
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    @staticmethod
    def DashToDot(str1):
        return str1.replace("-", ".")

    @staticmethod
    def is_valid(str1):
        day, month, year = str1.split(".")
        if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
            return True
        else:
            return False

    @classmethod
    def show_numbers_of_dates(cls):
        return cls.total_number_of_dates


obj1 = My_Date()
obj2 = My_Date()
obj3 = My_Date()
print(obj1.show_numbers_of_dates())
print(obj2.show_numbers_of_dates())
print(obj3.show_numbers_of_dates())
