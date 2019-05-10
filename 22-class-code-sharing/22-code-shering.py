def scan_board(board, code_to_run_for_each_item, code_to_run_for_each_row):
    for i in range(len(board)):
        for j in range(len(board[i])):
            code_to_run_for_each_item(i, j)

        code_to_run_for_each_row()

class HumanPlayer:
    def next_move(self, board):
        self.print_board(board)
        next_move = input("What's your next move? type the square position as (row, column)")
        return next_move

    def print_board(self, board):
        scan_board(
            board,
            lambda i, j: print(f"{board[i][j]:3}", end=""),
            lambda: print()
        )


class AIPlayer:
    _next_move = None

    def next_move(self, board):
        def foreach_cell(i, j):
            if AIPlayer._next_move is not None:
                return None
            if board[i][j] == '.':
                AIPlayer._next_move = f"({j}, {i})"
                return f"({j}, {i})"

        AIPlayer._next_move = None
        scan_board(
            board,
            foreach_cell,
            lambda: None,
        )
        return AIPlayer._next_move


h = HumanPlayer()
a = AIPlayer()
board = [['x', '.', '.'], ['o', '.', '.'], ['.', '.', '.']]
h.next_move(board)

res = a.next_move(board)
print(res)
