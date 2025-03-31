from State import State 

class DispenseState(State):
    def press_dispense_button(self, vending_machine):
        product = vending_machine.selected_product
        for item in vending_machine.inventory.products:
            if product and vending_machine.balance >= item.product_price:
                vending_machine.balance -= item.product_price
                item.product_quantity -= 1
                print(f"Dispensing {product}. Remaining balance: {vending_machine.balance}")
                vending_machine.set_state(vending_machine.idle_state)
                return

        print("Insufficient Balance!")

    def press_refund_button(self, vending_machine):
        print(f"Refunding {vending_machine.balance} coins.")
        vending_machine.balance = 0
        vending_machine.set_state(vending_machine.idle_state)