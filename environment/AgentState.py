from dataclasses import dataclass

from agent.Agent import Agent
from environment.Environment import Environment


@dataclass
class AgentState:
    environment: Environment
    solved = []
    is_solved = False
    agent: Agent
    time: 0

    def solve_sudoku(self):
        board = self.environment.initial_board
        if self.agent.find_solution(board):
            print("Solved Sudoku ")
            self.environment.print_board(board)
            self.is_solved = True
            self.solved = board
        else:
            print("No solution found")
            self.is_solved = False

    def __str__(self):
        return f"""AgentState(Environment={self.environment}), (Agent={self.agent}), (solved={self.solved}),
        (isSolved={self.is_solved}),(Time={self.time})"""
