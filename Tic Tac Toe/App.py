from TicTacToe import TicTacToe

def main():
    game = TicTacToe()
    game.initialize_game()
    winner = game.start_game()
    print(f"Game winner is: {winner}")

if __name__ == "__main__":
    main()
