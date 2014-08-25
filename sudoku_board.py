__author__ = 'colt'

from board import Board


class SudokuBoard(Board):
    def get_row(self, row):
        return [self.get_square(row, col) for col in range(self.num_cols)]

    def print_row(self, row):
        for each in self.get_row(row):
            print(each, end=' ')

    def get_col(self, col):
            return [self.get_square(row, col) for row in range(self.num_rows)]

    def print_col(self, col):
        for each in self.get_col(col):
            print(each)
