__author__ = 'Colt'

from sudoku_board import SudokuBoard

if __name__ == "__main__":
    square_size = 3
    rows = 9
    cols = 9
    my_board = SudokuBoard(3, rows, cols, '-')
    row,col = my_board.find_corner_sudoku_square(4,5)
    my_board.print_sudoku_square(row,col)