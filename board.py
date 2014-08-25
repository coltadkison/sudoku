__author__ = 'Colt'


class Board():
        def __init__(self, rows, cols, default_value):
            self.num_rows = rows
            self.num_cols = cols
            self.default_value = default_value
            self.board = [None] * rows * cols
            self.reset_board()

        def reset_board(self):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self.set_square(i, j, i)

        def print_board(self):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    print(self.board[(self.num_rows * i) + j], end=' ')
                print()

        def get_square(self, row, col):
            return self.board[(self.num_rows * row) + col]

        def set_square(self, row, col, value):
            self.board[(self.num_rows * row) + col] = value

