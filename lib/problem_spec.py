
from typing import List

from action import Action
from state import State
from state_action import StateAction


class ProblemSpec:
    """Represents the specification of the search problem.
    """
    def successors(self, state: State) -> List[StateAction]:
        """Returns a list of all possible actions that can be taken from the given state."""
        raise NotImplementedError(
            "A ProblemSpec must implement a successors method, but it is not implemented.")

    def step(self, state: State, action: Action) -> State:
        """ Takes a state and applies the given action, returning the resulting state. """
        raise NotImplementedError("A ProblemSpec must implement a 'step' method, but it is not implemented.")