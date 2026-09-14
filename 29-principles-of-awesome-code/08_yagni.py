class BadTestUser:
    def __init__(
        self,
        username: str,
        email: str,
        passport_id: str,
        crypto_wallet: str,
        is_vip: str,
        discount_percent: int,
    ) -> None:
        self.username = username
        self.email = email
        self.passport_id = passport_id
        self.crypto_wallet = crypto_wallet
        self.is_vip = is_vip
        self.discount_percent = discount_percent

    def pay_with_bitcoin(self, amount: float) -> float:
        self.amount = amount

    def calculate_vip_discount(self):
        pass


class YagniTestUser:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def get_login_data(self) -> dict:
        return {"username": self.username, "email": self.email}


if __name__ == "__main__":
    user = YagniTestUser("Ivan Ivanov", "ivan@mail.ru")
    login_data = user.get_login_data()
    print(login_data)
