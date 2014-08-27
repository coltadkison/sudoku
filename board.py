__author__ = 'Colt'


class Board():
        def __init__(self, num_rows, num_cols, default_value):
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.default_value = default_value
            self.board = [None] * num_rows * num_cols
            self.reset_board()

        #Reset all squares in board to default_value
        def reset_board(self):
            self.board = self.default_value * self.num_rows * self.num_cols

        #Print entire board
        def print_board(self):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    print(self.board.get_square(i, j), end=' ')
                print()

        def print_board2(self):
            temp = []
            for i in range(self.num_rows):
                temp.append([each for each in ])

        #Return the value of a single square on the board
        def get_square(self, row, col):
            return self.board[(self.num_rows * row) + col]

        #Set the value of a single square on the board
        def set_square(self, row, col, value):
            self.board[(self.num_rows * row) + col] = value

