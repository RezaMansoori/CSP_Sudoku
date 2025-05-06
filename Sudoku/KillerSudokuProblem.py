from Sudoku.SudokuProblem import SudokuProblem
from CSP.Variable import Variable
from Sudoku.KillerSudokuConstraint import KillerCageConstraint

class KillerSudokuProblem(SudokuProblem):
    def __init__(self, board=None, cages=None, name="Killer Sudoku"):
        super().__init__(board=board, name=name)
        if cages is not None:
            # Implement here
            ...

    def get_variable_by_position(self, row: int, col: int) -> Variable:
        index = row * 9 + col
        return self.variables[index]