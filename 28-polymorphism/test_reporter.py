from abc import ABC, abstractmethod


class BaseReporter(ABC):
    @abstractmethod
    def report(self, test_name: str, status: str) -> None:
        pass


class ConsoleReporter(BaseReporter):
    def report(self, test_name: str, status: str) -> None:
        print(f"[Console] {test_name} -> {status.upper()}")


class AllureReporter(BaseReporter):
    def report(self, test_name: str, status: str) -> None:
        print(f"[Allure] Test '{test_name}' finished with status: {status}")


def notify_all(reporters: list[BaseReporter], test_name: str, status: str) -> None:
    for reporter in reporters:
        reporter.report(test_name, status)


if __name__ == "__main__":
    reporters_list = [ConsoleReporter(), AllureReporter()]
    notify_all(reporters_list, "test_user_can_login", "passed")
