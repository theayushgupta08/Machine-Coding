from GameObjects.PlayingPiece import PlayingPiece
from GameObjects.PieceType import PieceType


class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)