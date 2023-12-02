from environment.Environment import is_valid


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

        # Eliminar números de la misma fila y columna
        for i in range(9):
            if board[i][column] in nums:
                nums.remove(board[i][column])
            if board[row][i] in nums:
                nums.remove(board[row][i])

        # Eliminar números del mismo cuadrado
        inicio_fila = row - row % 3
        inicio_columna = column - column % 3
        for i in range(3):
            for j in range(3):
                if board[i + inicio_fila][j + inicio_columna] in nums:
                    nums.remove(board[i + inicio_fila][j + inicio_columna])

        return list(nums)
