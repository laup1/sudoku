import numpy as np
import matplotlib.pyplot as plt


class Environment:

    @classmethod
    def __init__(initial_numbers):
        self.board = np.zeros((9, 9))
        self.initial_numbers = initial_numbers

    @staticmethod
    def create_sudoku():
        # Create a 9x9 numpy array with zeros
        board = np.zeros((9, 9))

        # Draw the Sudoku board
        fig, ax = plt.subplots()
        ax.imshow(board, cmap='binary')

        # Draw grid lines
        for x in range(9):
            ax.axhline(x, lw=2, color='k', linestyle='-')
            ax.axvline(x, lw=2, color='k', linestyle='-')

        # Draw thicker lines for the 3x3 subgrids
        for x in range(0, 9, 3):
            ax.axhline(x, lw=3, color='k', linestyle='-')
            ax.axvline(x, lw=3, color='k', linestyle='-')

        plt.show()
