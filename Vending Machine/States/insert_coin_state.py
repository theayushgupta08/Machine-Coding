from State import State

class InsertCoinState(State):
    def insert_coin(self, vending_machine, amount):
        print(f"Inserted {amount} coins.")
        vending_machine.balance += amount
        print(f"Total Balance: {vending_machine.balance}")

    def press_product_selection_button(self, vending_machine):
        if vending_machine.balance > 0:
            print("Product Selection button clicked! Going to Product Selection.")
            vending_machine.set_state(vending_machine.product_selection_state)
        else:
            print("Please insert coin first")

            