__author__ = 'traptInReality'


class Board():
        def __init__(self, num_rows, num_cols, default_value):
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.default_value = default_value
            self.board = [None] * num_rows * num_cols
            self.reset_board()

        #Reset all squares in board to default_value
        def reset_board(self):
            self.board = [self.default_value] * self.num_rows * self.num_cols

        def reset_square(self, row, col):
            self.set_square(row, col, self.default_value)

        #Print entire board
        def print_board(self):
            for row in range(self.num_rows):
                print(' '.join(map(str, self.get_row(row))))

        #Return the value of a single square on the board
        def get_square(self, row, col):
            return self.board[(self.num_rows * row) + col]

        #Set the value of a single square on the board
        def set_square(self, row, col, value):
            self.board[(self.num_rows * row) + col] = value

        def get_row(self, row):
            return [self.get_square(row, col) for col in range(self.num_cols)]

        def get_col(self, col):
            return [self.get_square(row, col) for row in range(self.num_rows)]