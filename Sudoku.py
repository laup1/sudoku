from agent.Agent import Agent
from environment.Environment import Environment, create_sudoku_board


class Sudoku:

    @staticmethod
    def main():
        environment = Environment(10, create_sudoku_board())
        environment.add_initial_random_numbers()
        agent = Agent()



if __name__ == "__main__":
    Sudoku.main()
