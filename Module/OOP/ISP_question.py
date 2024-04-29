from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class RefundInterface(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass


class OnlinePaymentProcessor(PaymentInterface, RefundInterface):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")
