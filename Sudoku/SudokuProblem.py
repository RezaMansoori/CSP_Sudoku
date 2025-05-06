from CSP.Problem import Problem
from CSP.Variable import Variable
from Sudoku.SudokuConstraint import SudokuConstraint


class SudokuProblem(Problem):
    def __init__(self, board=None, name="Sudoku"):
        if board is None:
            board = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        
        variables = []
        constraints = []

        # Implement here
        ...
        
        
        super().__init__(constraints, variables, name)
    
    def print_assignments(self):
        """
        Print the Sudoku board in a readable format.
        """
        print(f"\n{self.name}")
        print("-" * 25)
        for row in range(9):
            row_str = ""
            for col in range(9):
                var = self.variables[row * 9 + col]
                value = var.value if var.has_value else 0
                if col % 3 == 0:
                    row_str += "| "
                row_str += f"{value} "
            row_str += "|"
            print(row_str)
            if (row + 1) % 3 == 0:
                print("-" * 25)
