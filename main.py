from CSP.Solver import Solver
from States.StatesProblem import StatesProblem
from Sudoku.SudokuProblem import SudokuProblem

if __name__ == '__main__':

    print("\nTesting States solver...")
    states = StatesProblem()
    s = Solver(states)
    s.solve()
    states.print_assignments()

    # print("\nTesting Sudoku solver...")
    # sudoku = SudokuProblem()
    # s = Solver(sudoku)
    # s.solve()
    # sudoku.print_assignments()
