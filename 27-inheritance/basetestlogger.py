class BaseTestLogger:
    def __init__(self, test_name: str) -> None:
        self.test_name = test_name

    def log(self, message: str) -> None:
        print(f"[TEST: {self.test_name}] {message}")


class DetailedTestLogger(BaseTestLogger):
    def log(self, message: str) -> None:
        super().log(message)
        print("Status: PASSED")


if __name__ == "__main__":
    # Создаем объект дочернего класса, передавая имя теста
    detailed_logger = DetailedTestLogger("test_user_registration")

    # Вызываем метод log
    detailed_logger.log("Checking database connection...")
