class PaymentStrategy:
    def pay(self, amount: float):
        raise NotImplementedError()

class CardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using Card")

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using Cash")
