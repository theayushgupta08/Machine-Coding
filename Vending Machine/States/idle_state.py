from State import State

class IdleState(State):
    def press_insert_coin_button(self, vending_machine):
        print("Insert Coin button clicked. Going to Intert Coin State")
        vending_machine.set_state(vending_machine.insert_coin_state)

    