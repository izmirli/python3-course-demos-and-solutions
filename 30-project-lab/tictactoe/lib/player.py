from board import Board


class Player:
    """A Tic-Tac-Toe player.

    A player will have its shape and number of wins.
    """
    def __init__(self, shape):
        if shape not in Board.shapes:
            raise UserWarning(f'Invalid shape given ({shape})')
        self.shape = shape
        self.wins = 0
