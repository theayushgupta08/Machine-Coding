from State import State

class ProductSelectionState(State):
    def select_product(self, vending_machine, product):
        for item in vending_machine.inventory.products:
            if item.product_code == product and item.product_quantity > 0:
                vending_machine.selected_product = product
                print(f"Product {product} selected.")
                print("Click on Dispense Button to buy your product or Click on Refund Button to get your refund.")
                vending_machine.set_state(vending_machine.dispense_state)
                return
        print("Product not avalaible or out of stock!")
        