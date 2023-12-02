from dataclasses import dataclass

import numpy as np

from agent.Agent import Agent
from environment.Environment import Environment, is_valid, print_board


@dataclass
class AgentState:
    environment: Environment
    solved: []


    def state(self, board):
        if self.solve(board):
            print("Solved Sudoku ")
            print_board(board)
            return True
        else:
            print_board("No solution found")
            return False


    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in np.random.permutation(9) + 1:
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = 0
                    return False
        self.solved = board
        return True
