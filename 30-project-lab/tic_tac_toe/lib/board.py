class Board:
    """Tic-Tac-Toe game board."""
    shapes = ('X', 'O')  # Allowed shapes

    def __init__(self):
        """Initialize with a clear board."""
        self.board = []
        self.clear()

    def clear(self):
        """Set the game board representation with empty squares (starting position)

        :return: None
        """
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display(self):
        """Printout the bored with the current squares shapes and coordinates.

        :return: None
        """
        print('  ' + '   '.join([str(i) for i in range(len(self.board))]))
        for y in range(len(self.board)):
            print(str(y) + ' ' + ' | '.join(self.board[y]) + ' ')
            if len(self.board) != y + 1:
                print(' ---' + '+---' * (len(self.board[y]) - 1))
        print()

    def move(self, x, y, shape):
        """Make a move on the board - placing given shape in given board coordinates.

        An exception will be raised if no valid shape is given, or if
        the board square at given coordinates isn't empty.

        :param x: int column coordinate.
        :param y: int row coordinate.
        :param shape: str name of the shape to be placed.
        :return: None
        """
        if shape not in Board.shapes:
            raise UserWarning(f"Given shape '{shape}' is not a valid shape.")
        if ' ' != self.board[y][x]:
            raise UserWarning(f'Square {x},{y} is not empty.')
        self.board[y][x] = shape

    def has_more_moves(self):
        """Check if there are any more moves available in the game board.

        :return: True if there are more moves; False if there aren't.
        """
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if ' ' == self.board[y][x]:
                    return True

        return False

    def board_to_list(self):
        """A conversion utility from a 2D matrix (list of lists) to a 1D vector list.

        :return: list representing the board with 9 indexes.
        """
        board_list = []
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                board_list.append(len(board_list) if 'X' != self.board[y][x] and 'O' != self.board[y][x] else self.board[y][x])
        return board_list

    @staticmethod
    def list_index_to_board_coordinates(index):
        """A conversion utility from a 1D board list index to 2D board coordinates.

        :param index: int index of 1D board list.
        :return: int, int representing 2D board coordinates.
        """
        y = int(index / 3)
        x = index - (y * 3)
        return x, y

    def winning(self, shape, b=None):
        """Check if given shape is in winning state at game board.

        A game is won if the shape is places 3 times in a line - horizontal, vertical or diagonal.
        :param shape: str shape name.
        :param b: list [optional] 1D board list. If not given, the current game board will be used.
        :return: True if game has being won by given shape; False othewise.
        """
        if b is None:
            b = self.board_to_list()
        if (b[0] == shape and b[1] == shape and b[2] == shape) or \
                (b[3] == shape and b[4] == shape and b[5] == shape) or \
                (b[6] == shape and b[7] == shape and b[8] == shape) or \
                (b[0] == shape and b[3] == shape and b[6] == shape) or \
                (b[1] == shape and b[4] == shape and b[7] == shape) or \
                (b[2] == shape and b[5] == shape and b[8] == shape) or \
                (b[0] == shape and b[4] == shape and b[8] == shape) or \
                (b[2] == shape and b[4] == shape and b[6] == shape):
            return True
        else:
            return False
