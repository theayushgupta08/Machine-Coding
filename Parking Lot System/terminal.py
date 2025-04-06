from ticket import Ticket
from payment_strategy import PaymentStrategy

class Terminal:
    def __init__(self, terminal_id: int):
        self.terminal_id = terminal_id

class EntryTerminal(Terminal):
    def issue_ticket(self, spot_id: int, spot_type):
        return Ticket(spot_id, spot_type)

class ExitTerminal(Terminal):
    def process_payment(self, ticket: Ticket, payment_strategy: PaymentStrategy):
        payment_strategy.pay(ticket.calculate_fee())
        ticket.mark_paid()
