__author__ = 'traptInReality'

from collections import OrderedDict


class SudokuSolver():
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.solutions = []
        self.num_solutions = 0
        self.num_real_solutions = 0

    def __check_row(self, row):
        row_squares = [each for each in self.sudoku_board.get_row(row) if each != self.sudoku_board.default_value]
        return len(row_squares) == len(set(row_squares))

    def __check_col(self, col):
        col_squares = [each for each in self.sudoku_board.get_col(col) if each != self.sudoku_board.default_value]
        return len(col_squares) == len(set(col_squares))

    def __check_square(self, row, col):
        square_squares = [each for each in self.sudoku_board.get_sudoku_square(row, col)
                          if each != self.sudoku_board.default_value]
        return len(square_squares) == len(set(square_squares))

    def __check_board(self):
        for i in range(self.sudoku_board.num_rows):
            if not self.__check_row(i):
                return False
        for i in range(self.sudoku_board.num_cols):
            if not self.__check_col(i):
                return False
        for i in range(0, self.sudoku_board.num_rows, self.sudoku_board.square_size):
            for j in range(0, self.sudoku_board.num_cols, self.sudoku_board.square_size):
                if not self.__check_square(i, j):
                    return False
        return True

    def get_possible_values(self, row, col):
        all_values = set(range(1, 10))
        return all_values.difference(self.sudoku_board.get_row(row),
                                     self.sudoku_board.get_col(col),
                                     self.sudoku_board.get_sudoku_square(row, col))

    def recursive_solver(self, row, col):
        if row == self.sudoku_board.num_rows:
            return True
        elif col == self.sudoku_board.num_cols:
            return self.recursive_solver(row + 1, 0)
        elif self.sudoku_board.get_square(row, col) != 0:
            return self.recursive_solver(row, col + 1)
        else:
            possible_values = self.get_possible_values(row, col)
            for each in possible_values:
                self.sudoku_board.set_square(row, col, each)
                if self.__check_board() and self.recursive_solver(row, col + 1):
                    return True
            self.sudoku_board.reset_square(row, col)
            return False

    def best_choices(self, choices):
        sorted_choices = sorted(choices.items(), key=lambda t: len(t[1]))
        fewest = len(sorted_choices[0][1])
        best=[each for each in sorted_choices if len(each[1]) == fewest]
        return best

    def logical_solver(self):
        unsolved_squares = self.sudoku_board.get_unsolved_squares()
        all_possible_values = {(row, col): self.get_possible_values(row, col) for (row, col) in unsolved_squares}
        if not all_possible_values:
            self.num_solutions += 1
            if self.sudoku_board.board not in self.solutions:
                self.solutions.append(list(self.sudoku_board.board))
                self.num_real_solutions += 1
            print(self.num_real_solutions, self.num_solutions)
            return
        for (row, col), values in self.best_choices(all_possible_values):
            for value in values:
                self.sudoku_board.set_square(row, col, value)
                if self.__check_board():
                    self.logical_solver()
            self.sudoku_board.reset_square(row, col)

            #Does this work with a board with multiple solutions?

