from Sudoku.SudokuProblem import SudokuProblem
from Sudoku.SudokuConstraint import SudokuConstraint

class KnightSudokuProblem(SudokuProblem):
    def __init__(self, board=None, name="Knight Sudoku"):
        super().__init__(board=board, name=name)
        self.add_knight_constraints()

    def add_knight_constraints(self):
        """Add constraints for all pairs of cells a knight's move apart."""
        for row in range(9):
            for col in range(9):
                var = self.variables[row * 9 + col]
                neighbors = self.get_knight_neighbors(row, col)
                for r, c in neighbors:
                    neighbor_var = self.variables[r * 9 + c]
                    self.constraints.append(SudokuConstraint([var, neighbor_var]))

    def get_knight_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        """Return valid knight's move positions from (row, col)."""
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]
        neighbors = []
        for row_move, col_move in moves:
            r = row + row_move
            c = col + col_move
            if 0 <= r < 9 and 0 <= c < 9:
                neighbors.append((r, c))
        return neighbors