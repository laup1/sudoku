from dataclasses import dataclass
import random


@dataclass
class Environment:
    initial_numbers: 0
    initial_board: []

    def add_initial_random_numbers(self):
        initialized_board = self.initial_board
        for i in range(self.initial_numbers):
            location_row = random.randint(0, 8)
            location_column = random.randint(0, 8)
            number_to_add = random.randint(1, 9)
            if is_valid(initialized_board, location_row, location_column, number_to_add):
                initialized_board[location_row][location_column] = number_to_add
        self.initial_board = initialized_board


def create_sudoku_board():
    board = []
    for i in range(9):
        line = []
        for j in range(9):
            line.append(0)
        board.append(line)
    return board


def is_valid(board, row, column, number):
    # verify number in the row
    for x in range(9):
        if board[row][x] == number:
            return False

    # Verify the number in the column
    for x in range(9):
        if board[x][column] == number:
            return False

    # Verify the number in the square
    start_row, start_col = 3 * (row // 3), 3 * (column // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == number:
                return False
    return True


def print_board(board_to_print):
    board = "------+------+------\n"
    for index, row in enumerate(board_to_print):
        for index_row, number in enumerate(row):
            board += str(number) + " "
            if index_row != 0 and (index_row+1) % 3 == 0:
                board += "|"
            if index_row != 0 and (index_row+1) % 9 == 0:
                board += "\n"

        if index != 0 and (index+1) % 3 == 0:
            board += "------+------+------\n"

    print(board)
