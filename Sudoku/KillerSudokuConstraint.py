from CSP.Constraint import Constraint
from CSP.Variable import Variable

class KillerCageConstraint(Constraint):
    """Ensures that variables in a cage have distinct values and sum to a target."""
    def __init__(self, variables: list[Variable], target_sum: int):
        super().__init__(variables)
        self.target_sum = target_sum

    def is_satisfied(self) -> bool:
        # Implement here
        ...

        return True