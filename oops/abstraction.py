from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using credit card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using UPI.")

upi = UpiPayment()
upi.pay(500)