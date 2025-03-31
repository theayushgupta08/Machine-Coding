from vending_machine import VendingMachine 

# Client code

vending_machine = VendingMachine()
vending_machine.press_insert_coin_button()
vending_machine.insert_coin(300)
vending_machine.press_product_selection_button()
vending_machine.select_product(101)
vending_machine.press_dispense_button()
vending_machine.press_refund_button()
