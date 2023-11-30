import numpy as np

from environment.Environment import is_valid


class Agent:
    def __init__(self):
        pass

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i, j] == 0:
                    for num in np.random.permutation(9) + 1:
                        if is_valid(board, i, j, num):
                            board[i, j] = num
                            if self.solve(board):
                                return True
                            board[i, j] = 0
                    return False
        return True
