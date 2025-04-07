from GameObjects.PlayingPiece import PlayingPiece
from GameObjects.PieceType import PieceType


class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)