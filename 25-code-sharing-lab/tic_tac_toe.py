"""A Tic-Tac-Toe game.

Two players, one human and the other an AI, will take terns adding
their shape to squares in the board. Their goal is to win by placing
3 in a line - horizontal, vertical or diagonal.
After a game ends, with one of the players winning or with a tie, a
new game will start.
Overall scoreboard will be displayed at the end of each game.
"""

import random
from collections import deque
from time import sleep


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

    def scan_board(self, cell_callback, default_return_val=None):
        """A utility for scanning the squares in the board.

        :param cell_callback: function to be called for each square in the board.
        :param default_return_val: [optional] the value to be returned if nothing was returned earlier.
        :return: None or what was defined at cell_callback/default_return_val.
        """
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                callback_res = cell_callback(self.board[y][x], x, y)
                if callback_res is not None:
                    return callback_res
        return default_return_val

    def has_more_moves(self):
        """Check if there are any more moves available in the game board.

        :return: True if there are more moves; False if there aren't.
        """
        return self.scan_board(lambda cell, *_: True if ' ' == cell else None, False)

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


class Player:
    """A Tic-Tac-Toe player.

    A player will have its shape and number of wins.
    """

    def __init__(self, shape):
        if shape not in Board.shapes:
            raise UserWarning(f'Invalid shape given ({shape})')
        self.shape = shape
        self.wins = 0


class HumanPlayer(Player):
    """A Tic-Tac-Toe human player."""

    def __init__(self, name='Jon', shape='X'):
        super().__init__(shape)
        self.name = name

    def next_move(self):
        """Ask human player for its next move coordinates.

        :return: int, int representing 2D board coordinates.
        """
        next_move = input()
        x, y = next_move.split(',')
        return x, y


class AIPlayer(Player):
    """A Tic-Tac-Toe computer AI (Artificial intelligence) player."""
    def __init__(self, shape='O'):
        super().__init__(shape)
        self.name = "Bot"

    def next_move(self):
        """Compute next move coordinates using minimax algorithm.

        :return: int, int representing 2D board coordinates.
        """
        original_board = bord.board_to_list()
        shapes_map = {'AI': 'X', 'HUM': 'O'} if 'X' == self.shape else {'AI': 'O', 'HUM': 'X'}
        best_move = self.minmax(original_board, 'AI', shapes_map)
        return Board.list_index_to_board_coordinates(best_move['index'])

    def minmax(self, new_board, player, shapes_map):
        """Minimax algorithm to find best next move recursively.

        Go over each possible move and score it, returning highest score move.
        Stop condition is one of the players winning or no more moves.

        :param new_board: list 1D game board representation.
        :param player: str player representation (AI or HUM).
        :param shapes_map: dict mapping players to their shapes.
        :return: dict with keys: 'index' representing next move; 'score' for the move.
        """
        avil_moves = [i for i in new_board if 'X' != i and 'O' != i]
        if bord.winning(shapes_map['HUM'], new_board):
            return {'score': -10}
        elif bord.winning(shapes_map['AI'], new_board):
            return {'score': 10}
        elif len(avil_moves) == 0:  # TIE
            return {'score': 0}

        moves = []
        for move_index in avil_moves:
            move = {'index': move_index}
            move_board = new_board.copy()
            move_board[move_index] = shapes_map[player]
            minmax_res = self.minmax(move_board, 'AI' if 'AI' != player else 'HUM', shapes_map)
            move['score'] = minmax_res['score']
            moves.append(move)

        best_move = None
        best_score = -100 if 'AI' == player else 100
        for move in moves:
            if ('AI' == player and move['score'] > best_score) or ('HUM' == player and move['score'] < best_score):
                best_score = move['score']
                best_move = move

        return best_move


def make_players_and_insert_to_queue():
    """Make human and AI Playeres, and insert them to the global players_queue.

    Prompt human player for its name and use it in its object creation.

    :return: None
    """
    human_player_name = input('What is your name human player? ')
    players_queue.append(HumanPlayer(human_player_name))
    players_queue.append(AIPlayer())


def randomly_order_players():
    """Players are randomly ordered in the global players_queue (a deque).

    1st player in queue will be the X shape and will start the game.
    2nd player will get the O shape and play next.

    :return: None
    """
    if random.random() > 0.5:  # 50% to change existing order.
        players_queue.append(players_queue.popleft())
    players_queue[0].shape = Board.shapes[0]
    players_queue[1].shape = Board.shapes[1]


def get_and_make_player_next_move(player):
    """Get next move of given player, and make in on the game board.

    Ready to handle some exceptions by giving an error message and
    asking again for player next move.

    :param player: a Player object (with next_move function)
    :return: None
    """
    while True:
        print(f"{player.name}, what's your next move?")
        try:
            x, y = player.next_move()
        except ValueError:
            print('Invalid move format. Use: column,row (0,0 is top left; 2,2 is bottom right).')
            continue
        try:
            bord.move(int(x), int(y), player.shape)
        except UserWarning as e:
            print(f'Invalid move: {e}')
            continue
        except IndexError:
            print(f'Invalid move: {x},{y} is out of range. Valid coordinate range is 0-2.')
            continue
        except ValueError:
            print('Invalid move format. Use numbers only for column and row.')
            continue
        return None


def display_scoreboard():
    """Printout the scores of the players."""

    print('Scoreboard - ', end='')
    for player in sorted(players_queue, key=lambda p: p.wins, reverse=True):
        print(f'{player.name}: {player.wins};', end=' ')
    print()


def play_single_game():
    """A single Tic-Tac-Toe game.

    Using the global bord and players_queue.

    :return: None
    """
    while True:
        next_player = players_queue.popleft()
        get_and_make_player_next_move(next_player)
        players_queue.append(next_player)
        bord.display()
        if bord.winning(next_player.shape):
            next_player.wins += 1
            print(f'{next_player.name} wins the game.')
            return None
        if not bord.has_more_moves():
            print(f'No more moves. Game ended with no winner.')
            return None
        sleep(1)


""" pre-games setup """
bord = Board()
players_queue = deque()
make_players_and_insert_to_queue()

""" Games main loop """
games_count = 0
while True:
    games_count += 1
    randomly_order_players()
    bord.clear()

    # pre-game instructions and [empty] board display
    print(f"""
Game number: {games_count}
{players_queue[0].name} will start, playing '{players_queue[0].shape}'.
{players_queue[1].name} will play next with '{players_queue[1].shape}'.
Each turn type the square position for your next move as: column,row (0,0 is top left; 2,2 is bottom right)
""")
    bord.display()
    sleep(2)

    play_single_game()
    display_scoreboard()
    sleep(4)
