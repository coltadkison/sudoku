__author__ = 'traptInReality'


class SudokuSolver():
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board

    def __check_row(self, row):
        row_squares = [each for each in self.sudoku_board.get_row(row) if each != self.sudoku_board.default_value]
        return len(row_squares) == len(set(row_squares))

    def __check_col(self, col):
        col_squares = [each for each in self.sudoku_board.get_col(col) if each != self.sudoku_board.default_value]
        return len(col_squares) == len(set(col_squares))

    def __check_square(self, row, col):
        square_squares = [each for each in self.sudoku_board.get_sudoku_square(row, col) if each != self.sudoku_board.default_value]
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

    def recursive_solver(self, row, col):
        if row == self.sudoku_board.num_rows:
            return True
        elif col == self.sudoku_board.num_cols:
            return self.recursive_solver(row+1, 0)
        elif self.sudoku_board.get_square(row, col) != 0:
            return self.recursive_solver(row, col+1)
        else:
            all_values = set([each for each in range(1, 10)])
            possible_values = all_values.difference(self.sudoku_board.get_row(row),
                                                    self.sudoku_board.get_col(col),
                                                    self.sudoku_board.get_sudoku_square(row, col))
            if not possible_values:
                return False
            for each in possible_values:
                self.sudoku_board.set_square(row, col, each)
                if self.__check_board() and self.recursive_solver(row, col+1):
                    return True
            self.sudoku_board.reset_square(row, col)
            return False


