from environment.Environment import Environment


class Sudoku:

    @staticmethod
    def main():
        environment = Environment()
        environment.create_sudoku()


if __name__ == "__main__":
    Sudoku.main()
