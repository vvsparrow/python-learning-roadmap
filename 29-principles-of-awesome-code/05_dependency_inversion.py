from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send_notification(self, message) -> None:
        pass


class EmailSender(Notification):
    def send_notification(self, message) -> None:
        pass


class SMSNotification(Notification):
    def send_notification(self, message) -> None:
        pass


class User:
    def __init__(self, username, email, phone, notification_service) -> None:
        self.username = username
        self.email = email
        self.phone = phone
        self.notification_service = notification_service

    def send_notification(self, message) -> None:
        self.notification_service.send_notification(message)


if __name__ == "__main__":
    v = User("qwerty", "test@test.ru", "+79239230000", EmailSender())
