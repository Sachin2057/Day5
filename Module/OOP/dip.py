"""
    Module for dependency inversion principle
    """
from abc import ABC, abstractmethod


class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass


class ConcreteEmailSender(EmailSender):
    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")


class NotificationService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)


if __name__ == "__main__":
    email_sender = ConcreteEmailSender()
    notification_service = NotificationService(email_sender)
    notification_service.send_notification(
        "user@example.com", "Hello, this is a notification!")
