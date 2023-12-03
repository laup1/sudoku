from dataclasses import dataclass

from environment.Environment import is_valid


@dataclass
class Agent:

    def find_solution(self, board):
        row, column, possible_options = self.find_options(board)

        if row == -1 and column == -1:
            return True

        for num in possible_options:
            if is_valid(board, row, column, num):
                board[row][column] = num
                if self.find_solution(board):
                    return True
                board[row][column] = 0

        return False

    def find_options(self, board):
        minimum_candidates = 10
        row = -1
        column = -1
        candidates = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = self.possible_numbers(board, i, j)
                    if len(nums) < minimum_candidates:
                        minimum_candidates = len(nums)
                        row = i
                        column = j
                        candidates = nums

        return row, column, candidates

    @staticmethod
    def possible_numbers(board, row, column):
        nums = set(range(1, 10))

        for i in range(9):
            if board[i][column] in nums:
                nums.remove(board[i][column])
            if board[row][i] in nums:
                nums.remove(board[row][i])

        start_row = row - row % 3
        start_column = column - column % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_column] in nums:
                    nums.remove(board[i + start_row][j + start_column])

        return list(nums)
