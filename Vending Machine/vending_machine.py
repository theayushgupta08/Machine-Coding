from States.idle_state import IdleState 
from States.insert_coin_state  import InsertCoinState
from States.product_selection_state import ProductSelectionState 
from States.dispense_state import DispenseState
from manage_inventory import ManageProducts


class VendingMachine(ManageProducts):
    def __init__(self):
        self.balance = 0
        self.selected_product = None
        self.inventory = ManageProducts()

        # Adding Products

        self.inventory.add_products(101, "Pepsi", 130, 10)
        self.inventory.add_products(102, "Coke", 130, 10)
        self.inventory.add_products(103, "Soda", 130, 10)


        # Initialising all states

        self.idle_state = IdleState()
        self.insert_coin_state = InsertCoinState()
        self.product_selection_state = ProductSelectionState()
        self.dispense_state = DispenseState()

        # Initialising current state 
        self.current_state = self.idle_state

    def set_state(self, state):
        self.current_state = state 

    def press_insert_coin_button(self):
        self.current_state.press_insert_coin_button(self)

    def insert_coin(self, amount):
        self.current_state.insert_coin(self, amount)

    def select_product(self, product):
        self.current_state.select_product(self, product)

    def press_product_selection_button(self):
        self.current_state.press_product_selection_button(self)

    def press_dispense_button(self):
        self.current_state.press_dispense_button(self)

    def press_refund_button(self):
        self.current_state.press_refund_button(self)


