__author__ = 'colt'

class BoardSquare(object):
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def get_col(self):
        return self.col

    def set_col(self, col):
        self.col = col