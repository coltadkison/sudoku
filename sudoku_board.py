__author__ = 'colt'

from board import Board


class SudokuBoard(Board):
    def __init__(self, square_size, num_rows, num_cols, default_value):
        self.square_size = square_size
        Board.__init__(self, num_rows, num_cols, default_value)

    #Return one row of a Sudoku board
    def get_row(self, row):
        return [self.get_square(row, col) for col in range(self.num_cols)]

    #Print one row of a Sudoku board
    def print_row(self, row):
        for each in self.get_row(row):
            print(each, end=' ')

    #Return one row of a Sudoku board
    def get_col(self, col):
            return [self.get_square(row, col) for row in range(self.num_rows)]

    #Print one row of a Sudoku board
    def print_col(self, col):
        for each in self.get_col(col):
            print(each)

    #Finds row, col of the upper left corner of a Sudoku square on a Sudoku board based on
    # the row, col value of a board square
    def find_corner_sudoku_square(self, row, col):
        corner_row = int(row / self.square_size) * self.square_size
        corner_col = int(col / self.square_size) * self.square_size
        return corner_row, corner_col

    def get_sudoku_square(self, row, col):
        return [self.get_square(row+i, col+j) for i in range(self.square_size) for j in range(self.square_size)]

    #Print Sudoku square based on the row, col value of the upper left corner of the Sudoku square
    def print_sudoku_square(self, row, col):
        sudoku_square = self.get_sudoku_square(row, col)
        for i in range(self.square_size):
            for j in range(self.square_size):
                print(sudoku_square[(self.square_size *i) + j], end=' ')
            print()