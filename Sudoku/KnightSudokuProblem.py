from Sudoku.SudokuProblem import SudokuProblem
from Sudoku.SudokuConstraint import SudokuConstraint

class KnightSudokuProblem(SudokuProblem):
    def __init__(self, board=None, name="Knight Sudoku"):
        super().__init__(board=board, name=name)
        self.add_knight_constraints()

    def add_knight_constraints(self):
        """Add constraints for all pairs of cells a knight's move apart."""
        # Implement here
        ...
    def get_knight_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        """Return valid knight's move positions from (row, col)."""
        # Implement here
        moves = ...
        neighbors = []
        for dr, dc in moves:
            r = row + dr
            c = col + dc
            if 0 <= r < 9 and 0 <= c < 9:
                neighbors.append((r, c))
        return neighbors