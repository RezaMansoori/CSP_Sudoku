from CSP.Constraint import Constraint
from CSP.Variable import Variable

class KillerCageConstraint(Constraint):
    """Ensures that variables in a cage have distinct values and sum to a target."""
    def __init__(self, variables: list[Variable], target_sum: int):
        super().__init__(variables)
        self.target_sum = target_sum

    def is_satisfied(self) -> bool:
        values = [var.value for var in self.variables if var.value is not None]

        if len(set(values)) != len(values):
            return False

        if all(var.value is not None for var in self.variables):
            return sum(values) == self.target_sum

        return sum(values) <= self.target_sum