class Cat:
    def __init__(
        self, name: str = "Васька", age: int = 0, hours: int = 0, salary: int = 0
    ) -> None:
        self.name = name
        self.age = age
        self._hours = hours
        self._salary = salary

    def work(self, hours: int = 1) -> None:
        self._hours += hours

    @property
    def salary(self) -> int:
        print("The getter has been triggered")
        return self._salary * self._hours

    @salary.setter
    def salary(self, hourly_rate: int) -> None:
        print("The setter has been triggered")
        if self._check_salary_value(hourly_rate):
            self._salary = hourly_rate
        else:
            raise ValueError("Incorrect salary value")

    @staticmethod
    def _check_salary_value(salary: int) -> bool:
        return isinstance(salary, int)


if __name__ == "__main__":
    v = Cat("Петя", 18, 0, 0)
    v.work()
    v.work()
    v.work(5)
    v.salary = 500
    print(v.salary)
    v.work()
    v.work()
    print(v.salary)
