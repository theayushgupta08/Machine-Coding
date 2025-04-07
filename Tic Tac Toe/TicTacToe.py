from collections import deque
from typing import Tuple
from GameObjects.Board import Board
from GameObjects.PlayingPieceX import PlayingPieceX
from GameObjects.PlayingPieceO import PlayingPieceO
from GameObjects.Player import Player
from GameObjects.PieceType import PieceType


class TicTacToe:
    def __init__(self):
        self.players = deque()
        self.game_board: Board = None

    def initialize_game(self):
        # Creating 2 Players
        crossPiece = PlayingPieceX()
        player1 = Player("Player1", crossPiece)

        noughtsPiece = PlayingPieceO()
        player2 = Player("Player2", noughtsPiece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize Board
        self.game_board = Board(3)

    def start_game(self) -> str:
        noWinner = True

        while noWinner:
            playerTurn = self.players.popleft()

            # Show the board
            self.game_board.print_board()
            freeSpaces = self.game_board.get_free_cells()
            if not freeSpaces:
                noWinner = False
                continue

            # Read input
            print(f"Player: {playerTurn.name} Enter row,column: ", end="")
            try:
                s = input()
                row, col = map(int, s.strip().split(","))
            except ValueError:
                print("Invalid input format. Try again.")
                self.players.appendleft(playerTurn)
                continue

            # Add piece to the board
            if not self.game_board.add_piece(row, col, playerTurn.playingPiece):
                print("Incorrect position chosen, try again")
                self.players.appendleft(playerTurn)
                continue

            self.players.append(playerTurn)

            # Check winner
            if self.is_there_winner(row, col, playerTurn.playingPiece.pieceType):
                return playerTurn.name

        return "tie"

    def is_there_winner(self, row: int, column: int, pieceType: PieceType) -> bool:
        size = self.game_board.size
        board = self.game_board.board

        rowMatch = all(board[row][i] is not None and board[row][i].pieceType == pieceType for i in range(size))
        colMatch = all(board[i][column] is not None and board[i][column].pieceType == pieceType for i in range(size))
        diagMatch = all(board[i][i] is not None and board[i][i].pieceType == pieceType for i in range(size))
        antiDiagMatch = all(board[i][size - 1 - i] is not None and board[i][size - 1 - i].pieceType == pieceType for i in range(size))

        return rowMatch or colMatch or diagMatch or antiDiagMatch
