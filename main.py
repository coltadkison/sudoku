__author__ = 'Colt'

from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver

#Websudoku Evil Puzzle 9,631,808,478
TEST_BOARD = [
    0,0,0,6,2,0,1,0,0,
    0,0,9,0,0,3,0,7,0,
    4,0,0,0,7,0,0,0,0,
    0,2,0,0,0,0,9,6,0,
    0,8,1,0,0,0,7,5,0,
    0,4,6,0,0,0,0,3,0,
    0,0,0,0,3,0,0,0,9,
    0,6,0,5,0,0,4,0,0,
    0,0,8,0,1,6,0,0,0
]
if __name__ == "__main__":
    square_size = 3
    num_rows = 9
    num_cols = 9
    default_num = 0
    my_board = SudokuBoard(3, num_rows, num_cols, 0)
    for i in range(my_board.num_rows):
        for j in range(my_board.num_cols):
            my_board.set_square(i, j, TEST_BOARD[(my_board.num_rows * i) + j])
    # my_board.print_board()
    my_solver = SudokuSolver(my_board)
    my_solver.recursive_solver(0, 0)
    my_board.print_board()