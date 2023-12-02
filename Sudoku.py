from environment.AgentState import AgentState
from environment.Environment import Environment, create_sudoku_board, print_board
import time


class Sudoku:

    @staticmethod
    def main():
        for game in range(10):
            start = time.time()
            print("Sudoku # ", game)
            Sudoku.solve_sudoku()
            end = time.time()
            total_temps = end - start
            print("Total time ", total_temps)

    @staticmethod
    def solve_sudoku():
        environment = Environment(10, create_sudoku_board())
        environment.add_initial_random_numbers()
        print_board(environment.initial_board)
        agent_state = AgentState(environment, [])
        agent_state.state(environment.initial_board)


if __name__ == "__main__":
    Sudoku.main()
