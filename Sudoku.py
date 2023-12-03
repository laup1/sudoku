from agent.Agent import Agent
from environment.AgentState import AgentState
from environment.Environment import Environment, create_sudoku_board
import time


class Sudoku:

    @staticmethod
    def main():
        list_agents = []
        for game in range(1000):
            environment = Environment(17, create_sudoku_board())
            environment.initiate_board()

            start = time.time()
            print("Sudoku # ", game)
            agent_state = Sudoku.solve_sudoku(environment)
            end = time.time()
            total_temps = end - start
            agent_state.time = total_temps
            print("Total time ", total_temps)
            list_agents.append(agent_state)

        with open('mi_archivo.txt', 'w') as f:
            for agent in list_agents:
                print(agent.__str__(), file=f)

    @staticmethod
    def solve_sudoku(environment):
        agent = Agent()
        agent_state = AgentState(environment, agent, 0)
        agent_state.solve_sudoku()
        return agent_state


if __name__ == "__main__":
    Sudoku.main()
