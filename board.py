__author__ = 'Colt'


class Board():
        def __init__(self, rows, cols, default_value):
            self.num_rows = rows
            self.num_cols = cols
            self.default_value = default_value
            self.board = [None] * rows * cols
            self.reset_board()

        #Reset all squares in board to default_value
        def reset_board(self):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self.set_square(i, j, self.default_value)

        #Print entire board
        def print_board(self):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    print(self.board[(self.num_rows * i) + j], end=' ')
                print()

        #Return the value of a single square on the board
        def get_square(self, row, col):
            return self.board[(self.num_rows * row) + col]

        #Set the value of a single square on the board
        def set_square(self, row, col, value):
            self.board[(self.num_rows * row) + col] = value

